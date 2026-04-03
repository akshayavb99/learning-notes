const fs = require("fs");
const path = require("path");

const docsDir = path.resolve(__dirname, "../"); // points to 'docs'
const outputPath = path.resolve(__dirname, "slug-map.json");

const slugMap = {};

function generateKey(filePath) {
  const parts = filePath.split(path.sep);
  const fileName = parts.pop();
  if (!fileName) return null;
  const baseName = fileName.replace(/\.md$/, "");
  return [...parts, baseName]
    .map((s) => s.replace(/[^a-zA-Z0-9]/g, ""))
    .join("");
}

function walk(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      walk(fullPath);
    } else if (file.endsWith(".md")) {
      const relativePath = path.relative(docsDir, fullPath).replace(/\\/g, "/");
      const slug = "/" + relativePath.replace(/\.md$/, "");
      const key = generateKey(relativePath);
      if (key) slugMap[key] = slug;
    }
  }
}

walk(docsDir);

fs.writeFileSync(outputPath, JSON.stringify(slugMap, null, 2));
console.log("Slug map generated at docs/.vitepress/slug-map.json");
// console.log(slugMap);
