const BASE_PROMPT = 'You read one clause from a Terms of Service, privacy policy or subscription terms. Reply with JSON only: {"flags": [...], "plain": "..."}. "flags" lists every category that applies, chosen from: limitation_of_liability, unilateral_termination, unilateral_change, content_removal, contract_by_using, choice_of_law, jurisdiction, arbitration, shares_for_ads, shares_with_providers, keeps_data, can_opt_out, auto_renews, trial_converts_to_paid, hard_to_cancel, no_refund, price_can_increase, early_termination_fee. "plain" is one short sentence that tells the user what they agree to. If the clause has none of these, reply {"flags": [], "plain": ""}.';

const MODEL_FILE = "/Users/hridyaagrawal/honey/fineprint/models/fineprint-v5-Q4_K_M.gguf";

export const MODELS = {
  base: { port: 8080, label: "Base", prompt: BASE_PROMPT, parallel: 8, command: "llama-server -hf LiquidAI/LFM2.5-1.2B-Instruct-GGUF:Q8_0 --port 8080 -np 8 -c 16384 -fa on" },
  tuned: { port: 8081, label: "Fine-tuned", prompt: "Flag this Terms of Service or privacy policy clause as JSON.", stop: ["[]"], parallel: 32, command: `llama-server -m ${MODEL_FILE} --port 8081 -np 32 -c 32768 -b 4096 -ub 2048 -fa on` },
};

export const ALL_SITES = { origins: ["<all_urls>"] };

export const SEVERITIES = ["high", "medium", "low"];

export const CATEGORIES = {
  trial_converts_to_paid: { label: "Free trial turns paid", severity: "high", fallback: "Your free trial becomes a paid plan unless you cancel in time." },
  hard_to_cancel: { label: "Hard to cancel", severity: "high", fallback: "Cancelling takes more than a click." },
  early_termination_fee: { label: "Fee to leave early", severity: "high", fallback: "You pay a fee if you cancel before the minimum term ends." },
  no_refund: { label: "No refunds", severity: "high", fallback: "You do not get money back for unused time." },
  price_can_increase: { label: "Price can go up", severity: "high", fallback: "They can raise the price." },
  arbitration: { label: "You cannot sue them", severity: "high", fallback: "You give up your right to sue in court or join a class action." },
  shares_for_ads: { label: "Your data goes to advertisers", severity: "high", fallback: "They share or sell your data for advertising." },
  auto_renews: { label: "Renews automatically", severity: "medium", fallback: "It renews and charges you automatically until you cancel." },
  shares_with_providers: { label: "Shares data with partners", severity: "medium", fallback: "They share your data with companies that work for them." },
  keeps_data: { label: "Keeps your data", severity: "medium", fallback: "They keep your data for a period they choose." },
  limitation_of_liability: { label: "Liability limit", severity: "medium", fallback: "They limit what they owe you if something goes wrong." },
  unilateral_termination: { label: "Can close your account", severity: "medium", fallback: "They can end your account whenever they choose." },
  unilateral_change: { label: "Can change the terms", severity: "medium", fallback: "They can change these terms without asking you." },
  content_removal: { label: "Can remove your content", severity: "medium", fallback: "They can delete what you post." },
  jurisdiction: { label: "Court location", severity: "medium", fallback: "Disputes go to a court they choose." },
  choice_of_law: { label: "Governing law", severity: "medium", fallback: "A law they choose applies to disputes." },
  contract_by_using: { label: "Agree by using", severity: "medium", fallback: "Using the service means you accept these terms." },
  can_opt_out: { label: "You can opt out", severity: "low", fallback: "You can change this in your settings." },
};

const MAX_CLAUSES = 400;
const MIN_CLAUSE_LENGTH = 40;
const sentences = new Intl.Segmenter("en", { granularity: "sentence" });

export const hostOf = (url) => new URL(url).host || "this file";
export const collapse = (text) => text.replace(/\s+/g, " ").trim();
export const normalize = (clause) => collapse(clause.toLowerCase());

export function splitClauses(text) {
  const clauses = [];
  for (const block of text.split(/\n\s*\n/)) {
    for (const { segment } of sentences.segment(block)) {
      const clause = collapse(segment);
      if (clause.length < MIN_CLAUSE_LENGTH) continue;
      clauses.push(clause);
      if (clauses.length === MAX_CLAUSES) return clauses;
    }
  }
  return clauses;
}

export function parseReply(content) {
  const start = content.indexOf("{");
  const end = content.lastIndexOf("}");
  if (start === -1 || end < start) return null;
  let reply;
  try {
    reply = JSON.parse(content.slice(start, end + 1));
  } catch {
    return null;
  }
  if (!Array.isArray(reply?.flags)) return null;
  const flags = [...new Set(reply.flags)].filter((flag) => Object.hasOwn(CATEGORIES, flag));
  flags.sort((a, b) => rank(a) - rank(b));
  const plain = typeof reply.plain === "string" ? reply.plain.trim() : "";
  return { flags, plain: flags.length ? plain || CATEGORIES[flags[0]].fallback : "" };
}

const rank = (flag) => SEVERITIES.indexOf(CATEGORIES[flag].severity);

export const severityOf = (flags) => CATEGORIES[flags[0]].severity;

export function flagsBySeverity(findings) {
  const flags = [...new Set(findings.flatMap((finding) => finding.flags))];
  return Object.fromEntries(SEVERITIES.map((severity) => [severity, flags.filter((flag) => CATEGORIES[flag].severity === severity)]));
}

export function gradeOf(findings) {
  const { high, medium } = flagsBySeverity(findings);
  if (high.length === 0) return medium.length === 0 ? "A" : "B";
  return "CDE"[Math.min(high.length, 3) - 1];
}

const ENTITIES = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " ", rsquo: "’", lsquo: "‘", rdquo: "”", ldquo: "“", mdash: "—", ndash: "–", hellip: "…" };

export function htmlToText(html) {
  const body = html.match(/<main[\s>][\s\S]*<\/main>/i)?.[0] ?? html.match(/<article[\s>][\s\S]*<\/article>/i)?.[0] ?? html;
  return body
    .replace(/<(script|style|noscript|svg|template|head)[\s>][\s\S]*?<\/\1>/gi, " ")
    .replace(/<br\s*\/?>/gi, "\n")
    .replace(/<\/(p|div|li|h[1-6]|section|tr|blockquote|ul|ol|table|article|header|footer|dd|dt)>/gi, "\n\n")
    .replace(/<[^>]+>/g, "")
    .replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (entity, code) =>
      code[0] !== "#" ? ENTITIES[code.toLowerCase()] ?? entity
      : String.fromCodePoint(code[1].toLowerCase() === "x" ? parseInt(code.slice(2), 16) : Number(code.slice(1))))
    .replace(/[ \t]+/g, " ");
}
