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
<div class="ni-paged">
  <div class="ni-list">
    <div class="ni">
  <div class="ni-header">
    <a href="./design-twitter-dsa/" class="ni-title">Leetcode 355 - Design Twitter</a>
    <span class="ni-date">Jul 31, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">heap</span><span class="ni-tag">hashmap</span><span class="ni-tag">design</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./task-scheduler/" class="ni-title">Leetcode 621 - Task Scheduler</a>
    <span class="ni-date">Jul 30, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">heap</span><span class="ni-tag">queue</span><span class="ni-tag">greedy</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./encode-and-decode-strings/" class="ni-title">Leetcode 271 - Encode and Decode Strings</a>
    <span class="ni-date">Jul 29, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">string</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./clone-graph/" class="ni-title">Leetcode 133 - Clone Graph</a>
    <span class="ni-date">Jul 20, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">graph</span><span class="ni-tag">bfs</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./max-area-of-island/" class="ni-title">Leetcode 695 - Max Area of Island</a>
    <span class="ni-date">Jul 20, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">dfs</span><span class="ni-tag">graph</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./matrix-vector-dot-product/" class="ni-title">Deep-ML - Matrix-Vector Dot Product</a>
    <span class="ni-date">Jul 16, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">deep-ml</span><span class="ni-tag">linear-algebra</span><span class="ni-tag">python</span><span class="ni-tag">matrix-operations</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./subsets-ii/" class="ni-title">Leetcode 90 - Subsets II</a>
    <span class="ni-date">Jul 16, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">backtracking</span><span class="ni-tag">recursion</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./combination-sum-2/" class="ni-title">Leetcode 40 - Combination Sum II</a>
    <span class="ni-date">Jul 14, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">backtracking</span><span class="ni-tag">recursion</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./permutations/" class="ni-title">Leetcode 46 - Permutations</a>
    <span class="ni-date">Jul 14, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">backtracking</span><span class="ni-tag">recursion</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./subsets/" class="ni-title">Leetcode 78 - Subsets</a>
    <span class="ni-date">Jul 7, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">backtracking</span><span class="ni-tag">recursion</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./generate-parantheses/" class="ni-title">Leetcode 22 - Generate Parentheses</a>
    <span class="ni-date">Jul 4, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">backtracking</span><span class="ni-tag">recursion</span><span class="ni-tag">None</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./k-closest-points-to-origin/" class="ni-title">Leetcode 973 - K Closest Points to Origin</a>
    <span class="ni-date">Jul 3, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">max-heap</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./arena-ray-tracing/" class="ni-title">ARENA - 0.1 Ray Tracing</a>
    <span class="ni-date">Jul 2, 2026</span>
  </div>
  <p class="ni-desc">My notes and explanation about the exercises for Ray Tracing Exercises in the ARENA curriculum</p>
  <div class="ni-tags"><span class="ni-tag">pytorch</span><span class="ni-tag">numpy</span><span class="ni-tag">linear-algebra</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./last-stone-weight/" class="ni-title">Leetcode 1046 - Last Stone Weight</a>
    <span class="ni-date">Jul 2, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">max-heap</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./kth-largest-element-in-an-array/" class="ni-title">Leetcode 215 - Kth Largest Element in an Array</a>
    <span class="ni-date">Jul 1, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">min-heap</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./kth-largest-element-in-a-stream/" class="ni-title">Leetcode 703 - Kth Largest Element in a Stream</a>
    <span class="ni-date">Jul 1, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">min-heap</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./count-good-nodes-in-binary-tree/" class="ni-title">Leetcode 1448 - Count Good Nodes in Binary Tree</a>
    <span class="ni-date">Jun 30, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">binary-tree</span><span class="ni-tag">dfs</span></div>
</div>
<div class="ni">
  <div class="ni-header">
    <a href="./binary-tree-right-side-view/" class="ni-title">Leetcode 199- Binary Tree Right Side View</a>
    <span class="ni-date">Jun 30, 2026</span>
  </div>
  <div class="ni-tags"><span class="ni-tag">leetcode</span><span class="ni-tag">neetcode-150-list</span><span class="ni-tag">python</span><span class="ni-tag">binary-tree</span><span class="ni-tag">bfs</span><span class="ni-tag">deque</span></div>
</div>
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
    <div class="ni-pagination">
      <button class="ni-page-btn ni-prev">&#8592; Prev</button>
      <span class="ni-page-info"></span>
      <button class="ni-page-btn ni-next">Next &#8594;</button>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.ni-paged').forEach(function(paged) {
    var PAGE_SIZE = 15;
    var items = Array.from(paged.querySelectorAll('.ni-list > .ni'));
    var total = items.length;
    if (total <= PAGE_SIZE) return;
    var pages = Math.ceil(total / PAGE_SIZE);
    var page = 0;
    var prevBtn = paged.querySelector('.ni-prev');
    var nextBtn = paged.querySelector('.ni-next');
    var info = paged.querySelector('.ni-page-info');
    function render() {
      items.forEach(function(item, i) {
        item.style.display = (i >= page * PAGE_SIZE && i < (page + 1) * PAGE_SIZE) ? '' : 'none';
      });
      info.textContent = 'Page ' + (page + 1) + ' of ' + pages;
      prevBtn.disabled = (page === 0);
      nextBtn.disabled = (page === pages - 1);
    }
    prevBtn.addEventListener('click', function() { page--; render(); });
    nextBtn.addEventListener('click', function() { page++; render(); });
    render();
  });
});
</script>

<!-- pd:end -->
