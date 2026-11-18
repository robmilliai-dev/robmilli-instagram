#!/usr/bin/env node
// Render every <section class="slide"> in an HTML file to its own PNG, plus an optional PDF.
//   node render.mjs carousel.html --out out --size 1080x1350 --pdf
// Needs once: npm i playwright && npx playwright install chromium
// Or point at an existing Chrome: CHROME_PATH=/path/to/chrome node render.mjs ...
import { chromium } from "playwright";
import { mkdirSync } from "node:fs";
import { resolve, join } from "node:path";
import { pathToFileURL } from "node:url";

const args = process.argv.slice(2);
const valueFlags = ["--out", "--size"];
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const html = args.find((a, i) => !a.startsWith("--") && !valueFlags.includes(args[i - 1]));
if (!html) { console.error("Usage: node render.mjs carousel.html [--out out] [--size 1080x1350] [--pdf]"); process.exit(1); }
const out = opt("--out", "out");
const [w, h] = opt("--size", "1080x1350").toLowerCase().split("x").map(Number);
mkdirSync(out, { recursive: true });

const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(html)).href, { waitUntil: "networkidle" });
await page.evaluate(() => document.fonts.ready);
const slides = await page.$$("section.slide");
if (!slides.length) { console.error('No <section class="slide"> found.'); process.exit(1); }
for (let i = 0; i < slides.length; i++) {
  await slides[i].screenshot({ path: join(out, `slide-${String(i + 1).padStart(2, "0")}.png`) });
}
if (args.includes("--pdf")) {
  await page.pdf({ path: join(out, "carousel.pdf"), width: `${w}px`, height: `${h}px`, printBackground: true });
}
await browser.close();
console.log(`Rendered ${slides.length} slides to ${out}/`);
