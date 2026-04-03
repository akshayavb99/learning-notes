// docs/.vitepress/generate-recursive-sidebar.js
import fs from "fs";
import path from "path";
import matter from "gray-matter";

/**
 * Clean fallback text for file/folder names
 */
function formatText(name) {
  return name
    .replace(".md", "")
    .replace(/-/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

/**
 * Read frontmatter title from a markdown file
 */
function getTitle(filePath, fallback) {
  const content = fs.readFileSync(filePath, "utf-8");
  const { data } = matter(content);
  return data.title || fallback;
}

/**
 * Recursively build sidebar items
 * @param {string} dir - folder relative to docs/
 * @param {string} basePath - URL base path
 * @param {number} depth - current depth (used for collapsed)
 * @returns {Array}
 */
export function getSidebar(dir, basePath = "", depth = 0) {
  const docsRoot = path.resolve(process.cwd(), "docs");
  const fullPath = path.resolve(docsRoot, dir);

  if (!fs.existsSync(fullPath)) return [];

  const entries = fs.readdirSync(fullPath).sort();

  const items = entries
    .map((entry) => {
      const entryPath = path.join(fullPath, entry);
      const stat = fs.statSync(entryPath);

      // Folder
      if (stat.isDirectory()) {
        const indexPath = path.join(entryPath, "index.md");
        let title = formatText(entry);
        if (fs.existsSync(indexPath)) {
          title = getTitle(indexPath, title);
        }

        return {
          text: title,
          link: fs.existsSync(indexPath) ? `${basePath}/${entry}/` : undefined,
          collapsible: true,
          collapsed: depth > 0,
          items: getSidebar(
            path.join(dir, entry),
            `${basePath}/${entry}`,
            depth + 1,
          ),
        };
      }

      // Markdown file (ignore index.md)
      if (entry.endsWith(".md") && entry !== "index.md") {
        return {
          text: getTitle(entryPath, formatText(entry)),
          link: `${basePath}/${entry.replace(".md", "")}`,
        };
      }
    })
    .filter(Boolean);

  return items;
}

/**
 * Wrap top-level folder to include itself in the sidebar
 * @param {string} dir - top folder (e.g., "programming")
 * @param {string} basePath - URL base path (e.g., "/programming")
 */
export function getSidebarWithRoot(dir, basePath) {
  const indexPath = path.resolve(process.cwd(), "docs", dir, "index.md");
  const rootTitle = fs.existsSync(indexPath)
    ? getTitle(indexPath, formatText(dir))
    : formatText(dir);

  return [
    {
      text: rootTitle,
      link: fs.existsSync(indexPath) ? `${basePath}/` : undefined,
      collapsible: true,
      collapsed: false, // expand top-level by default
      items: getSidebar(dir, basePath, 1),
    },
  ];
}
