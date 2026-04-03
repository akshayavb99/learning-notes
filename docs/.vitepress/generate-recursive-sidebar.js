// docs/.vitepress/generate-recursive-sidebar.js

import fs from "fs";
import path from "path";
import matter from "gray-matter";

/**
 * Format fallback text for files
 */
function formatText(name) {
  return name
    .replace(".md", "")
    .replace(/[-_]/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

/**
 * Force folder name to ALL CAPS
 */
function formatFolderName(name) {
  return name.replace(/[-_]/g, " ").toUpperCase();
}

/**
 * Read title from frontmatter
 */
function getTitle(filePath, fallback) {
  const content = fs.readFileSync(filePath, "utf-8");
  const { data } = matter(content);
  return data.title || fallback;
}

/**
 * Recursively generate sidebar
 */
export function getSidebar(dir, basePath = "", depth = 0) {
  const docsRoot = path.resolve(process.cwd(), "docs");
  const fullPath = path.resolve(docsRoot, dir);

  if (!fs.existsSync(fullPath)) return [];

  const entries = fs.readdirSync(fullPath).sort();
  const items = [];

  for (const entry of entries) {
    const entryPath = path.join(fullPath, entry);
    const stat = fs.statSync(entryPath);

    // 📂 Folder
    if (stat.isDirectory()) {
      const indexPath = path.join(entryPath, "index.md");

      const folderTitle = formatFolderName(entry); // ✅ ALL CAPS
      const children = [];

      // ✅ index.md as first item
      if (fs.existsSync(indexPath)) {
        const indexTitle = getTitle(indexPath, formatText(entry));

        children.push({
          text: indexTitle,
          link: `${basePath}/${entry}/`,
        });
      }

      // ✅ recursive children
      const nestedItems = getSidebar(
        path.join(dir, entry),
        `${basePath}/${entry}`,
        depth + 1,
      );

      children.push(...nestedItems);

      items.push({
        text: folderTitle,
        collapsible: true,
        collapsed: depth > 0,
        items: children,
      });
    }

    // 📄 Markdown files (excluding index.md)
    else if (entry.endsWith(".md") && entry !== "index.md") {
      items.push({
        text: getTitle(entryPath, formatText(entry)),
        link: `${basePath}/${entry.replace(".md", "")}`,
      });
    }
  }

  return items;
}

/**
 * Wrap top-level folder
 */
export function getSidebarWithRoot(dir, basePath) {
  const indexPath = path.resolve(process.cwd(), "docs", dir, "index.md");

  const rootTitle = formatFolderName(dir); // ✅ ALL CAPS

  const items = [];

  // ✅ root index first
  if (fs.existsSync(indexPath)) {
    const indexTitle = getTitle(indexPath, formatText(dir));

    items.push({
      text: indexTitle,
      link: `${basePath}/`,
    });
  }

  items.push(...getSidebar(dir, basePath, 1));

  return [
    {
      text: rootTitle,
      collapsible: true,
      collapsed: false,
      items,
    },
  ];
}
