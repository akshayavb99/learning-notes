import { defineConfig } from "vitepress";
import { withMermaid } from "vitepress-plugin-mermaid";
import { tabsMarkdownPlugin } from "vitepress-plugin-tabs";
import fs from "fs";
import path from "path";
import { getSidebarWithRoot } from "./generate-recursive-sidebar.js";

const slugMapPath = path.resolve(__dirname, "slug-map.json");
export const slugMap = JSON.parse(fs.readFileSync(slugMapPath, "utf-8"));

const tagMap = JSON.parse(
  fs.readFileSync(path.resolve(__dirname, "tag-map.json"), "utf-8"),
);

const baseValue = "/learning-notes/";

export default withMermaid(
  defineConfig({
    title: "Akshaya's Learning Notes",
    description: "A VitePress site to hold my learning notes",
    base: baseValue,

    lastUpdated: true,

    head: [["script", { type: "module", src: "/.vitepress/tag-page.js" }]],

    markdown: {
      config(md) {
        md.use(tabsMarkdownPlugin);

        const defaultTextRule = md.renderer.rules.text;
        md.renderer.rules.text = (tokens, idx, options, env, self) => {
          let text = tokens[idx].content;
          Object.entries(slugMap).forEach(([key, slug]) => {
            text = text.replaceAll(`@${key}`, slug);
          });
          return text;
        };

        // Render tags at the bottom of each note
        md.core.ruler.push("inject_tags_bottom", (state) => {
          const { frontmatter } = state.env;
          if (!frontmatter || !frontmatter.tags) return;

          const Token = state.Token;
          const tagsHtml =
            `<div class="note-tags" style="margin-top:2rem;">` +
            frontmatter.tags
              .map(
                (tag) =>
                  `<a class="tag-chip" href="${baseValue}tags/#${tag
                    .toLowerCase()
                    .replace(
                      /\s+/g,
                      "-",
                    )}" style="margin-right:0.5rem; padding:0.2rem 0.5rem; background:#eee; border-radius:4px; text-decoration:none;">${tag}</a>`,
              )
              .join("") +
            `</div>`;

          const htmlToken = new Token("html_block", "", 0);
          htmlToken.content = tagsHtml;
          state.tokens.push(htmlToken);
        });
      },
      math: true,
      image: { lazyLoading: true },
    },

    themeConfig: {
      nav: [
        { text: "Home", link: "/" },
        { text: "Machine Learning", link: "/ml/index" },
        { text: "Systems", link: "/systems/index" },
        { text: "Programming", link: "/programming/index" },
        { text: "Tags", link: "/tags/index" },
        { text: "Miscellaneous", link: "/miscellaneous/index" },
      ],

      sidebar: {
        "/": getSidebarWithRoot("Home", "/"),
        "/ml/": getSidebarWithRoot("ml", "/ml"),
        "/systems/": getSidebarWithRoot("systems", "/systems"),
        "/programming/": getSidebarWithRoot("programming", "/programming"),
        "/tags/": getSidebarWithRoot("tags", "/tags"),
        "/miscellaneous/": getSidebarWithRoot(
          "miscellaneous",
          "/miscellaneous",
        ),
      },

      footer: {
        message:
          'Website built with <a href="https://vitepress.vuejs.org/" target="_blank" rel="noopener noreferrer">VitePress</a>',
        copyright: `© 2026 Akshaya Balaji. Last Updated: ${new Intl.DateTimeFormat("en-US", { month: "long", day: "2-digit", year: "numeric" }).format(new Date())}`,
      },

      search: {
        provider: "local",
        options: {
          // Include frontmatter title in the search index
          searchExtra: (page) => {
            console.log("Page title for searchExtra:", page.frontmatter.title);
            return page.frontmatter.title || "";
          },
        },
      },
    },

    mermaid: {
      theme: "default",
    },
  }),
);

// https://vitepress.dev/reference/site-config

// socialLinks: [
//   { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
// ]
