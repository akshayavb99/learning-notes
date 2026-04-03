// docs/.vitepress/utils/tags.js
const fs = require("fs");
const path = require("path");
const matter = require("gray-matter");

const docsRoot = path.resolve(process.cwd(), "docs");

// Recursively read all markdown files
function getAllMarkdownFiles(dir) {
  const fullDir = path.join(docsRoot, dir);
  if (!fs.existsSync(fullDir)) return [];

  const entries = fs.readdirSync(fullDir);
  let files = [];

  entries.forEach((entry) => {
    const fullPath = path.join(fullDir, entry);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      files = files.concat(getAllMarkdownFiles(path.join(dir, entry)));
    } else if (entry.endsWith(".md")) {
      files.push(path.join(dir, entry));
    }
  });

  return files;
}

// Build tag map: tag -> list of note links
function buildTagMap() {
  const files = getAllMarkdownFiles(""); // all notes
  const tagMap = {};

  files.forEach((file) => {
    const content = fs.readFileSync(path.join(docsRoot, file), "utf-8");
    const { data } = matter(content);

    if (data.tags) {
      data.tags.forEach((tag) => {
        if (!tagMap[tag]) tagMap[tag] = [];
        tagMap[tag].push("/" + file.replace(/\.md$/, "").replace(/\\/g, "/"));
      });
    }
  });

  return tagMap;
}

module.exports = { buildTagMap };
