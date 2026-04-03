const fs = require("fs");
const path = require("path");

const tagMapPath = path.resolve(process.cwd(), "docs/.vitepress/tag-map.json");
const tagMap = JSON.parse(fs.readFileSync(tagMapPath, "utf-8"));

const tagsIndexPath = path.resolve(process.cwd(), "docs/tags/index.md");

// Helper to get lightweight frontmatter title
function getFrontmatterTitle(filePath, fallback) {
  if (!fs.existsSync(filePath)) return fallback;
  const content = fs.readFileSync(filePath, "utf-8");
  const match = content.match(/^---\s*([\s\S]*?)\s*---/);
  if (!match) return fallback;
  const frontmatter = match[1].split("\n").reduce((acc, line) => {
    const [key, ...rest] = line.split(":");
    if (key && rest.length) acc[key.trim()] = rest.join(":").trim();
    return acc;
  }, {});
  return frontmatter.title || fallback;
}

// Helper to convert slug to markdown path
function getMdPathFromSlug(slug) {
  return path.join(process.cwd(), "docs", slug.replace(/^\//, "") + ".md");
}

// Build the content
let content = `---
title: Tags
---

`;

for (const [tag, slugs] of Object.entries(tagMap)) {
  content += `## ${tag}\n\n`;
  slugs.forEach((slug) => {
    const mdPath = getMdPathFromSlug(slug);
    const title = getFrontmatterTitle(mdPath, slug.split("/").pop());
    content += `- [${title}](${slug})\n`;
  });
  content += "\n";
}

// Ensure tags folder exists
fs.mkdirSync(path.dirname(tagsIndexPath), { recursive: true });

// Write the index page
fs.writeFileSync(tagsIndexPath, content);
console.log("Generated single /tags/index.md page");
