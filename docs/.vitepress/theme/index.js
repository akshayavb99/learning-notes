import DefaultTheme from "vitepress/theme";
import { h } from "vue";
import { useData } from "vitepress";

export default {
  extends: DefaultTheme,
  Layout() {
    const { frontmatter } = useData();

    return h(DefaultTheme.Layout, null, {
      "doc-before": () => {
        if (!frontmatter.value || !frontmatter.value.title) return null;

        // We wrap it in .vp-doc but apply .title to the H1
        // This ensures it gets the correct typography and spacing
        return h("div", { class: "vp-doc" }, [
          h(
            "h1",
            {
              id: "top",
              class: "title",
            },
            frontmatter.value.title,
          ),
        ]);
      },
    });
  },
};
