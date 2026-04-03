// docs/.vitepress/generate-tag-map.js
const fs = require("fs");
const path = require("path");
const { buildTagMap } = require("./extract-tags.js");

const tagMap = buildTagMap();
const outPath = path.resolve(process.cwd(), "docs/.vitepress/tag-map.json");

fs.writeFileSync(outPath, JSON.stringify(tagMap, null, 2), "utf-8");
console.log("Tag map generated at", outPath);
