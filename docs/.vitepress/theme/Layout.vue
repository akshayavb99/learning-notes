<template>
  <Layout>
    <!-- Inject frontmatter title if it exists -->
    <template #doc-top>
      <h1 v-if="$page.frontmatter.title">{{ $page.frontmatter.title }}</h1>
      <br />
    </template>

    <!-- Render the original page content -->
    <slot />
  </Layout>
</template>

<script setup>
import { Layout } from "vitepress/theme";
</script>
