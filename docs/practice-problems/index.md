---
title: Practice Problems MoC
---

# Map of Contents

Solutions, approaches, and complexity analysis for practice problems like Leetcode DSA problems.

<!-- pd:start -->
<style>
.ni-list { border: 1px solid var(--md-default-fg-color--lightest); border-radius: 8px; overflow: hidden; }
.ni { display: flex; flex-direction: column; gap: 0.45rem; padding: 1rem 1.25rem; border-bottom: 1px solid var(--md-default-fg-color--lightest); transition: background-color 0.15s ease; }
.ni:hover { background-color: var(--md-code-bg-color); }
.ni:last-child { border-bottom: none; }
.ni-header { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; }
.ni-title { font-size: 0.92rem; font-weight: 600; color: var(--md-default-fg-color); text-decoration: none; flex: 1; }
.ni-title:hover { color: var(--md-primary-fg-color); }
.ni-date { font-size: 0.72rem; color: var(--md-default-fg-color--light); white-space: nowrap; flex-shrink: 0; }
.ni-desc { margin: 0; font-size: 0.84rem; color: var(--md-default-fg-color--light); line-height: 1.5; }
.ni-tags { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.ni-tag { display: inline-flex; padding: 0.18rem 0.55rem; background: var(--md-default-bg-color); border: 1px solid var(--md-default-fg-color--lightest); border-radius: 999px; font-size: 0.68rem; color: var(--md-default-fg-color--light); font-weight: 500; text-decoration: none; }
.ni a { text-decoration: none; }
.ni-pagination { display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem 1.25rem; border-top: 1px solid var(--md-default-fg-color--lightest); }
.ni-page-btn { padding: 0.3rem 0.8rem; background: var(--md-default-bg-color); border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px; cursor: pointer; font-size: 0.8rem; color: var(--md-default-fg-color); }
.ni-page-btn:hover:not(:disabled) { border-color: var(--md-primary-fg-color); color: var(--md-primary-fg-color); }
.ni-page-btn:disabled { opacity: 0.35; cursor: default; }
.ni-page-info { font-size: 0.78rem; color: var(--md-default-fg-color--light); }
</style>
<div class="ni-list">
<div class="ni">
  <div class="ni-header">
    <a href="./balanced-binary-tree/" class="ni-title">Leetcode 110 - Balanced Binary Tree</a>
    <span class="ni-date">Jun 15, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">tree</span><span class="ni-tag">dfs</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./lru_cache/" class="ni-title">Leetcode 146 - LRU Cache</a>
    <span class="ni-date">Jun 15, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">linked-list</span><span class="ni-tag">hashmap</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./diameter-of-binary-tree/" class="ni-title">Leetcode 543 - Diameter of Binary Tree</a>
    <span class="ni-date">Jun 15, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">tree</span><span class="ni-tag">dfs</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./add-two-numbers/" class="ni-title">Leetcode 2 - Add Two Numbers</a>
    <span class="ni-date">Jun 10, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">linked-list</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./copy-list-with-random-pointer/" class="ni-title">Leetcode 138 - Copy List with Random Pointer</a>
    <span class="ni-date">Jun 8, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">linked-list</span><span class="ni-tag">hashmap</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./time-based-key-value-store/" class="ni-title">Leetcode 981 - Time Based Key-Value Store</a>
    <span class="ni-date">Jun 3, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">binary-search</span><span class="ni-tag">array</span><span class="ni-tag">hashmap</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./koko-eating-bananas/" class="ni-title">Leetcode 875 - Koko Eating Bananas</a>
    <span class="ni-date">Jun 2, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">binary-search</span><span class="ni-tag">array</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./search-2d-matrix/" class="ni-title">Leetcode 74 - Search a 2D Matrix</a>
    <span class="ni-date">Jun 1, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">binary-search</span><span class="ni-tag">matrix</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span></div>
</div>
</div>

<!-- pd:end -->
