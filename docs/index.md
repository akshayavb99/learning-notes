---
title: Akshaya's Learning Notes
hide:
  - navigation
  - toc
  - footer
---

<style>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 1.5rem 2rem;
}

/* ── Hero ─────────────────────────────────────────── */
.home-hero {
  padding-bottom: 1.5rem;
}

.home-kicker {
  margin: 0 0 0.75rem;
  color: var(--md-primary-fg-color);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.78rem;
}

.home-title {
  margin: 0;
  color: var(--md-primary-fg-color);
  font-size: clamp(2.6rem, 7vw, 5rem);
  line-height: 1;
  letter-spacing: 0;
}

.home-tagline {
  margin: 1.25rem 0 0;
  max-width: 620px;
  color: var(--md-default-fg-color--light);
  font-size: 1.18rem;
  line-height: 1.65;
}

.home-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 2rem;
}

.home-action {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.65rem;
  padding: 0 1.1rem;
  border-radius: 999px;
  font-weight: 700;
  text-decoration: none;
  border: 1px solid var(--md-default-fg-color--lightest);
}

.home-action.portfolio {
  background: var(--md-primary-fg-color);
  border-color: var(--md-primary-fg-color);
  color: var(--md-primary-bg-color);
}

.home a { text-decoration: none; }

.section-panel {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  padding: 1.25rem;
  background: var(--md-code-bg-color);
}

.section-label {
  margin: 0 0 1rem;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--md-default-fg-color--light);
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

/* ── Stats ────────────────────────────────────────── */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(155px, 1fr));
  gap: 1rem;
}

.stat-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 6px;
  padding: 1.1rem;
  text-align: center;
}

.stat-label {
  font-size: 0.7rem;
  color: var(--md-default-fg-color--light);
  margin-bottom: 0.55rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  font-weight: 600;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--md-default-fg-color);
  line-height: 1;
}

.stat-detail {
  font-size: 0.69rem;
  color: var(--md-default-fg-color--light);
  margin-top: 0.4rem;
}

/* ── Categories ───────────────────────────────────── */
.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 0.75rem;
}

.cat-item {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 6px;
  padding: 1rem 0.75rem;
  text-align: center;
  text-decoration: none;
  color: inherit;
  transition: border-color 0.15s;
  display: block;
}

.cat-item:hover { border-color: var(--md-primary-fg-color); }

.cat-icon { font-size: 1.5rem; margin-bottom: 0.45rem; }

.cat-name {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--md-default-fg-color);
  margin-bottom: 0.3rem;
}

.cat-count {
  font-size: 0.71rem;
  color: var(--md-default-fg-color--light);
}

/* ── Recent notes list ────────────────────────────── */
.recent-notes-list {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  overflow: hidden;
}

.recent-note {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 0.9rem 1.25rem;
  background: var(--md-code-bg-color);
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}

.recent-note:last-child { border-bottom: none; }

.recent-note-main {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
}

.recent-note-title {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--md-default-fg-color);
  flex: 1;
}

.recent-note-title:hover { color: var(--md-primary-fg-color); }

.recent-note-date {
  font-size: 0.73rem;
  color: var(--md-default-fg-color--light);
  white-space: nowrap;
  flex-shrink: 0;
}

.recent-note-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}

.rn-tag {
  display: inline-flex;
  align-items: center;
  padding: 0.18rem 0.55rem;
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 999px;
  font-size: 0.68rem;
  color: var(--md-default-fg-color--light);
  font-weight: 500;
}

/* ── Responsive ───────────────────────────────────── */
@media (max-width: 760px) {
  .home { padding-top: 2.5rem; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>

<div class="home">

  <section class="home-hero">
    <div>
      <h1 class="home-title">Akshaya's Learning Notes</h1>
      <p class="home-tagline">A personal knowledge base for machine learning, data science, systems, programming, books, and papers.</p>
      <div class="home-actions">
        <a class="home-action portfolio" href="https://akshayavb99.github.io/">Portfolio</a>
      </div>
    </div>
  </section>

  <!-- categories -->
  <div class="section-panel" style="margin-bottom:1.5rem;">
    <p class="section-label">Browse by category</p>
    <div class="categories-grid">
      <a href="concept-notes/" class="cat-item">
        <div class="cat-icon">&#128196;</div>
        <div class="cat-name">Concept Notes</div>
        <div class="cat-count"><!-- cat-count:concept-notes -->6 notes<!-- /cat-count --></div>
      </a>
      <a href="book-summaries/" class="cat-item">
        <div class="cat-icon">&#128218;</div>
        <div class="cat-name">Book Summaries</div>
        <div class="cat-count"><!-- cat-count:book-summaries -->1 book<!-- /cat-count --></div>
      </a>
      <a href="paper-summaries/" class="cat-item">
        <div class="cat-icon">&#128203;</div>
        <div class="cat-name">Paper Summaries</div>
        <div class="cat-count"><!-- cat-count:paper-summaries -->2 papers<!-- /cat-count --></div>
      </a>
      <a href="indexes/" class="cat-item">
        <div class="cat-icon">&#128270;</div>
        <div class="cat-name">Indexes</div>
        <div class="cat-count"><!-- cat-count:indexes -->4 indexes<!-- /cat-count --></div>
      </a>
      <a href="course-summaries/" class="cat-item">
        <div class="cat-icon">&#127891;</div>
        <div class="cat-name">Course Summaries</div>
        <div class="cat-count"><!-- cat-count:course-summaries -->1 course<!-- /cat-count --></div>
      </a>
      <a href="practice-problems/" class="cat-item">
        <div class="cat-icon">&#128187;</div>
        <div class="cat-name">Practice Problems</div>
        <div class="cat-count"><!-- cat-count:practice-problems -->8 solutions<!-- /cat-count --></div>
      </a>
    </div>
  </div>

  <!-- stats -->
  <div class="section-panel" style="margin-bottom:1.5rem;">
    <p class="section-label">Knowledge base at a glance</p>
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-label">Total Notes</div>
        <div class="stat-value"><!-- stat:total-notes -->22<!-- /stat --></div>
        <div class="stat-detail">across all sections</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Sections</div>
        <div class="stat-value"><!-- stat:sections -->6<!-- /stat --></div>
        <div class="stat-detail">topic areas</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Concept Notes</div>
        <div class="stat-value"><!-- stat:concept-notes -->6<!-- /stat --></div>
        <div class="stat-detail">quick references</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Book Summaries</div>
        <div class="stat-value"><!-- stat:book-summaries -->1<!-- /stat --></div>
        <div class="stat-detail">deep dives</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Paper Summaries</div>
        <div class="stat-value"><!-- stat:paper-summaries -->2<!-- /stat --></div>
        <div class="stat-detail">research notes</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Indexes</div>
        <div class="stat-value"><!-- stat:indexes -->4<!-- /stat --></div>
        <div class="stat-detail">topic maps</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Course Summaries</div>
        <div class="stat-value"><!-- stat:course-summaries -->1<!-- /stat --></div>
        <div class="stat-detail">courses</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Practice Problems</div>
        <div class="stat-value"><!-- stat:practice-problems -->8<!-- /stat --></div>
        <div class="stat-detail">problems solved</div>
      </div>
    </div>
  </div>

  <!-- recent notes — gen_widget.py injects between markers -->
  <div class="widgets-section">
    <p class="section-label" style="margin-bottom:1rem;">Recently updated</p>
<!-- pd-recent:start -->
<div class="recent-notes-list">
  <div class="recent-note">
    <div class="recent-note-main">
      <a href="course-summaries/llm-zoomcamp-2026/" class="recent-note-title">LLM Zoomcamp 2026</a>
      <span class="recent-note-date">Jun 25, 2026</span>
    </div>
    <div class="recent-note-tags"><span class="rn-tag">artificial-intelligence</span><span class="rn-tag">course-summary</span><span class="rn-tag">git</span><span class="rn-tag">large-language-models</span><span class="rn-tag">agentic-ai</span><span class="rn-tag">kestra</span></div>
  </div>
  <div class="recent-note">
    <div class="recent-note-main">
      <a href="practice-problems/balanced-binary-tree/" class="recent-note-title">Leetcode 110 - Balanced Binary Tree</a>
      <span class="recent-note-date">Jun 15, 2026</span>
    </div>
    <div class="recent-note-tags"><span class="rn-tag">leetcode</span><span class="rn-tag">neetcode-150-list</span><span class="rn-tag">python</span><span class="rn-tag">tree</span><span class="rn-tag">dfs</span></div>
  </div>
  <div class="recent-note">
    <div class="recent-note-main">
      <a href="practice-problems/diameter-of-binary-tree/" class="recent-note-title">Leetcode 543 - Diameter of Binary Tree</a>
      <span class="recent-note-date">Jun 15, 2026</span>
    </div>
    <div class="recent-note-tags"><span class="rn-tag">leetcode</span><span class="rn-tag">neetcode-150-list</span><span class="rn-tag">python</span><span class="rn-tag">tree</span><span class="rn-tag">dfs</span></div>
  </div>
  <div class="recent-note">
    <div class="recent-note-main">
      <a href="practice-problems/lru_cache/" class="recent-note-title">Leetcode 146 - LRU Cache</a>
      <span class="recent-note-date">Jun 15, 2026</span>
    </div>
    <div class="recent-note-tags"><span class="rn-tag">leetcode</span><span class="rn-tag">neetcode-150-list</span><span class="rn-tag">python</span><span class="rn-tag">linked-list</span><span class="rn-tag">hashmap</span></div>
  </div>
  <div class="recent-note">
    <div class="recent-note-main">
      <a href="practice-problems/add-two-numbers/" class="recent-note-title">Leetcode 2 - Add Two Numbers</a>
      <span class="recent-note-date">Jun 10, 2026</span>
    </div>
    <div class="recent-note-tags"><span class="rn-tag">leetcode</span><span class="rn-tag">neetcode-150-list</span><span class="rn-tag">python</span><span class="rn-tag">linked-list</span></div>
  </div>
</div>

<!-- pd-recent:end -->
  </div>

</div>
