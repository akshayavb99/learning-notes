---
title: Akshaya's Learning Notes
hide:
  - navigation
  - toc
  - footer
---

# Akshaya's Learning Notes

A collection of my learning notes across ML, data science and systems.

[View Portfolio](https://akshayavb99.github.io/){ .md-button .md-button--primary }

---

## Section Summaries

<div class="browse-grid">

<!-- pd-cn:start -->
<style>
:root {
  --pd-accent: #3b82f6;
  --pd-surface: var(--color-background-secondary);
  --pd-border: var(--color-border-tertiary);
  --pd-text: var(--color-text-primary);
  --pd-muted: var(--color-text-secondary);
  --pd-r: var(--border-radius-md);
}
.browse-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.6rem; align-items: start; }
@media (max-width: 76.1875em) { .browse-grid { grid-template-columns: 1fr; } }
.pd { border: 0.5px solid var(--pd-border); border-radius: var(--border-radius-lg); overflow: hidden; font-size: 14px; transition: box-shadow 0.18s ease; }
.pd:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.10); }
.pd-header { display: flex; justify-content: space-between; align-items: center; padding: 14px 18px; border-bottom: 0.5px solid var(--pd-border); background: var(--pd-surface); }
.pd-label { font-size: 17px; font-weight: 500; color: var(--pd-accent); text-decoration: none; }
.pd-label:hover { text-decoration: underline; }
.pd-updated { font-size: 11px; color: var(--pd-muted); font-family: var(--font-mono); margin-top: 2px; }
.pd-stats { display: flex; align-items: center; gap: 8px; }
.pd-stat { display: flex; flex-direction: column; align-items: center; }
.pd-stat-n { font-size: 25px; font-weight: 500; font-family: var(--font-mono); color: var(--pd-text); line-height: 1; }
.pd-stat-l { font-size: 11px; text-transform: uppercase; letter-spacing: 0.07em; color: var(--pd-muted); }
.pd-div { width: 0.5px; height: 28px; background: var(--pd-border); }
.pd-desc { padding: 9px 18px; font-size: 13px; color: var(--pd-muted); border-bottom: 0.5px solid var(--pd-border); }
.pd-body { display: block; border-top: 0.5px solid var(--pd-border); }
.pd-sec { padding: 14px 18px; }
.pd-sec-title { font-size: 11px; font-weight: 500; letter-spacing: 0.09em; text-transform: uppercase; color: var(--pd-muted); margin: 0 0 8px; }
.prob-list { list-style: none; list-style-type: none; margin: 0; padding: 0; }
.pd ul.prob-list, .pd ul.prob-list li { list-style: none !important; padding-left: 0; margin-left: 0; }
.prob { padding-bottom: 9px; margin-bottom: 9px; border-bottom: 0.5px solid var(--pd-border); }
.prob:last-child { border-bottom: none; padding-bottom: 0; margin-bottom: 0; }
.prob-link { color: var(--pd-text); text-decoration: none; font-weight: 500; flex: 1; min-width: 0; word-wrap: break-word; overflow-wrap: break-word; }
.prob-link:hover { color: var(--pd-accent); }
.prob-title-row { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; margin-bottom: 4px; }
.prob-tags { display: flex; flex-wrap: wrap; gap: 4px; }
.tag { font-size: 10px; font-weight: 500; padding: 1px 5px; border-radius: 3px; text-transform: uppercase; letter-spacing: 0.05em; }
.tag-t { background: var(--pd-surface); color: var(--pd-muted); border: 0.5px solid var(--pd-border); font-weight: 400; text-transform: none; }
.prob-date { font-size: 11px; font-family: var(--font-mono); color: var(--pd-muted); white-space: nowrap; flex-shrink: 0; }
.pd-footer { padding: 10px 18px; border-top: 0.5px solid var(--pd-border); background: var(--pd-surface); text-align: right; }
.pd-footer a { font-size: 11px; color: var(--pd-accent); text-decoration: none; font-weight: 500; letter-spacing: 0.03em; }
.pd-footer a:hover { text-decoration: underline; }
</style>
<div class="pd">
  <div class="pd-header">
    <div>
      <a href="concept-notes/" class="pd-label">Concept Notes</a>
      <div class="pd-updated">updated May 11, 2026</div>
    </div>
    <div class="pd-stats">
      <div class="pd-stat">
        <span class="pd-stat-n">5</span>
        <span class="pd-stat-l">total</span>
      </div>
      <div class="pd-stat">
        <span class="pd-stat-n">0</span>
        <span class="pd-stat-l">this week</span>
      </div>
    </div>
  </div>

  <div class="pd-desc">A flat collection of notes spanning AI, system design, programming, version control, and more.</div>

  <div class="pd-body">
    <div style="display:grid;grid-template-columns:1fr 1fr;">
      <div style="padding:14px 18px;border-right:0.5px solid var(--pd-border)">
        <svg viewBox="0 0 195 72" style="width:100%;height:auto;display:block;overflow:visible">
          <rect x="0" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="15" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="30" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="45" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="60" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="75" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="90" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="105" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="120" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="135" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="150" y="17" width="12" height="33" rx="2" fill="#3b82f6" opacity="0.88"/>
<rect x="150" y="11" width="12" height="6" rx="2" fill="#a78bfa" opacity="0.88"/>
<rect x="165" y="44" width="12" height="6" rx="2" fill="#a78bfa" opacity="0.94"/>
<rect x="180" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
          <text x="6" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W8</text>
<text x="6" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Feb</text>
<text x="21" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W9</text>
<text x="36" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W10</text>
<text x="36" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Mar</text>
<text x="51" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W11</text>
<text x="66" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W12</text>
<text x="81" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W13</text>
<text x="96" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W14</text>
<text x="111" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W15</text>
<text x="111" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Apr</text>
<text x="126" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W16</text>
<text x="141" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W17</text>
<text x="156" y="36" text-anchor="middle" font-size="6" fill="white" font-weight="500">5</text>
<text x="156" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W18</text>
<text x="171" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W19</text>
<text x="171" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">May</text>
<text x="186" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W20</text>
        </svg>
        <div style="display:flex;gap:10px;margin-top:6px;margin-bottom:8px">
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#3b82f6;display:inline-block"></span> created</span>
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#a78bfa;display:inline-block"></span> updated</span>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:4px"><span class="tag tag-t">git</span><span class="tag tag-t">github</span><span class="tag tag-t">dsa</span><span class="tag tag-t">interview-preparation</span><span class="tag tag-t">version-control</span><span class="tag tag-t">best-practices</span></div>
      </div>
      <div style="padding:14px 18px">
        <ul style="list-style:none;margin:0;padding:0">
        <li class="prob">
          <div class="prob-title-row">
            <a href="concept-notes/json-grammar/" class="prob-link">JSON Grammar Rules - McKeenan Form</a>
            <span class="prob-date">May 11, 2026</span>
          </div>
          <div class="prob-tags"><span class="tag tag-t">json</span></div>
        </li>
        

        <li class="prob">
          <div class="prob-title-row">
            <a href="concept-notes/conventional-commits-quick-ref/" class="prob-link">Conventional Commits Quick Reference</a>
            <span class="prob-date">May 1, 2026</span>
          </div>
          <div class="prob-tags"><span class="tag tag-t">git</span><span class="tag tag-t">github</span><span class="tag tag-t">version-control</span><span class="tag tag-t">best-practices</span></div>
        </li>
        

        <li class="prob">
          <div class="prob-title-row">
            <a href="concept-notes/dsa-patterns-revision-sheet/" class="prob-link">DSA Patterns Revision Sheet</a>
            <span class="prob-date">May 1, 2026</span>
          </div>
          <div class="prob-tags"><span class="tag tag-t">dsa</span><span class="tag tag-t">interview-preparation</span></div>
        </li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- pd-cn:end -->

<!-- pd-idx:start -->
<style>
:root {
  --pd-accent: #3b82f6;
  --pd-surface: var(--color-background-secondary);
  --pd-border: var(--color-border-tertiary);
  --pd-text: var(--color-text-primary);
  --pd-muted: var(--color-text-secondary);
  --pd-r: var(--border-radius-md);
}
.browse-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.6rem; align-items: start; }
@media (max-width: 76.1875em) { .browse-grid { grid-template-columns: 1fr; } }
.pd { border: 0.5px solid var(--pd-border); border-radius: var(--border-radius-lg); overflow: hidden; font-size: 14px; transition: box-shadow 0.18s ease; }
.pd:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.10); }
.pd-header { display: flex; justify-content: space-between; align-items: center; padding: 14px 18px; border-bottom: 0.5px solid var(--pd-border); background: var(--pd-surface); }
.pd-label { font-size: 17px; font-weight: 500; color: var(--pd-accent); text-decoration: none; }
.pd-label:hover { text-decoration: underline; }
.pd-updated { font-size: 11px; color: var(--pd-muted); font-family: var(--font-mono); margin-top: 2px; }
.pd-stats { display: flex; align-items: center; gap: 8px; }
.pd-stat { display: flex; flex-direction: column; align-items: center; }
.pd-stat-n { font-size: 25px; font-weight: 500; font-family: var(--font-mono); color: var(--pd-text); line-height: 1; }
.pd-stat-l { font-size: 11px; text-transform: uppercase; letter-spacing: 0.07em; color: var(--pd-muted); }
.pd-div { width: 0.5px; height: 28px; background: var(--pd-border); }
.pd-desc { padding: 9px 18px; font-size: 13px; color: var(--pd-muted); border-bottom: 0.5px solid var(--pd-border); }
.pd-body { display: block; border-top: 0.5px solid var(--pd-border); }
.pd-sec { padding: 14px 18px; }
.pd-sec-title { font-size: 11px; font-weight: 500; letter-spacing: 0.09em; text-transform: uppercase; color: var(--pd-muted); margin: 0 0 8px; }
.prob-list { list-style: none; list-style-type: none; margin: 0; padding: 0; }
.pd ul.prob-list, .pd ul.prob-list li { list-style: none !important; padding-left: 0; margin-left: 0; }
.prob { padding-bottom: 9px; margin-bottom: 9px; border-bottom: 0.5px solid var(--pd-border); }
.prob:last-child { border-bottom: none; padding-bottom: 0; margin-bottom: 0; }
.prob-link { color: var(--pd-text); text-decoration: none; font-weight: 500; flex: 1; min-width: 0; word-wrap: break-word; overflow-wrap: break-word; }
.prob-link:hover { color: var(--pd-accent); }
.prob-title-row { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; margin-bottom: 4px; }
.prob-tags { display: flex; flex-wrap: wrap; gap: 4px; }
.tag { font-size: 10px; font-weight: 500; padding: 1px 5px; border-radius: 3px; text-transform: uppercase; letter-spacing: 0.05em; }
.tag-t { background: var(--pd-surface); color: var(--pd-muted); border: 0.5px solid var(--pd-border); font-weight: 400; text-transform: none; }
.prob-date { font-size: 11px; font-family: var(--font-mono); color: var(--pd-muted); white-space: nowrap; flex-shrink: 0; }
.pd-footer { padding: 10px 18px; border-top: 0.5px solid var(--pd-border); background: var(--pd-surface); text-align: right; }
.pd-footer a { font-size: 11px; color: var(--pd-accent); text-decoration: none; font-weight: 500; letter-spacing: 0.03em; }
.pd-footer a:hover { text-decoration: underline; }
</style>
<div class="pd">
  <div class="pd-header">
    <div>
      <a href="indexes/" class="pd-label">Indexes</a>
      <div class="pd-updated">updated May 1, 2026</div>
    </div>
    <div class="pd-stats">
      <div class="pd-stat">
        <span class="pd-stat-n">4</span>
        <span class="pd-stat-l">total</span>
      </div>
      <div class="pd-stat">
        <span class="pd-stat-n">0</span>
        <span class="pd-stat-l">this week</span>
      </div>
    </div>
  </div>

  <div class="pd-desc">Area-wise indexes for Artificial Intelligence, System Design, Programming, and Version Control.</div>

  <div class="pd-body">
    <div style="display:grid;grid-template-columns:1fr 1fr;">
      <div style="padding:14px 18px;border-right:0.5px solid var(--pd-border)">
        <svg viewBox="0 0 195 72" style="width:100%;height:auto;display:block;overflow:visible">
          <rect x="0" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="15" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="30" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="45" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="60" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="75" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="90" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="105" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="120" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="135" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="150" y="30" width="12" height="20" rx="2" fill="#3b82f6" opacity="0.88"/>
<rect x="150" y="10" width="12" height="20" rx="2" fill="#a78bfa" opacity="0.88"/>
<rect x="165" y="46" width="12" height="4" rx="2" fill="#a78bfa" opacity="0.94"/>
<rect x="180" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
          <text x="6" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W8</text>
<text x="6" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Feb</text>
<text x="21" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W9</text>
<text x="36" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W10</text>
<text x="36" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Mar</text>
<text x="51" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W11</text>
<text x="66" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W12</text>
<text x="81" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W13</text>
<text x="96" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W14</text>
<text x="111" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W15</text>
<text x="111" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Apr</text>
<text x="126" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W16</text>
<text x="141" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W17</text>
<text x="156" y="43" text-anchor="middle" font-size="6" fill="white" font-weight="500">5</text>
<text x="156" y="23" text-anchor="middle" font-size="6" fill="white" font-weight="500">5</text>
<text x="156" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W18</text>
<text x="171" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W19</text>
<text x="171" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">May</text>
<text x="186" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W20</text>
        </svg>
        <div style="display:flex;gap:10px;margin-top:6px;margin-bottom:8px">
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#3b82f6;display:inline-block"></span> created</span>
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#a78bfa;display:inline-block"></span> updated</span>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:4px"><span class="tag tag-t">index</span><span class="tag tag-t">artificial-intelligence</span><span class="tag tag-t">programming</span><span class="tag tag-t">system-design</span><span class="tag tag-t">version-control</span><span class="tag tag-t">git</span></div>
      </div>
      <div style="padding:14px 18px">
        <ul style="list-style:none;margin:0;padding:0">
        <li class="prob">
          <div class="prob-title-row">
            <a href="indexes/artificial-intelligence/" class="prob-link">Artificial Intelligence Index</a>
            <span class="prob-date">May 1, 2026</span>
          </div>
          <div class="prob-tags"><span class="tag tag-t">artificial-intelligence</span><span class="tag tag-t">index</span></div>
        </li>
        

        <li class="prob">
          <div class="prob-title-row">
            <a href="indexes/programming/" class="prob-link">Programming Index</a>
            <span class="prob-date">May 1, 2026</span>
          </div>
          <div class="prob-tags"><span class="tag tag-t">programming</span><span class="tag tag-t">index</span></div>
        </li>
        

        <li class="prob">
          <div class="prob-title-row">
            <a href="indexes/system-design/" class="prob-link">System Design Index</a>
            <span class="prob-date">May 1, 2026</span>
          </div>
          <div class="prob-tags"><span class="tag tag-t">system-design</span><span class="tag tag-t">index</span></div>
        </li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- pd-idx:end -->

<!-- pd-bs:start -->
<style>
:root {
  --pd-accent: #3b82f6;
  --pd-surface: var(--color-background-secondary);
  --pd-border: var(--color-border-tertiary);
  --pd-text: var(--color-text-primary);
  --pd-muted: var(--color-text-secondary);
  --pd-r: var(--border-radius-md);
}
.browse-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.6rem; align-items: start; }
@media (max-width: 76.1875em) { .browse-grid { grid-template-columns: 1fr; } }
.pd { border: 0.5px solid var(--pd-border); border-radius: var(--border-radius-lg); overflow: hidden; font-size: 14px; transition: box-shadow 0.18s ease; }
.pd:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.10); }
.pd-header { display: flex; justify-content: space-between; align-items: center; padding: 14px 18px; border-bottom: 0.5px solid var(--pd-border); background: var(--pd-surface); }
.pd-label { font-size: 17px; font-weight: 500; color: var(--pd-accent); text-decoration: none; }
.pd-label:hover { text-decoration: underline; }
.pd-updated { font-size: 11px; color: var(--pd-muted); font-family: var(--font-mono); margin-top: 2px; }
.pd-stats { display: flex; align-items: center; gap: 8px; }
.pd-stat { display: flex; flex-direction: column; align-items: center; }
.pd-stat-n { font-size: 25px; font-weight: 500; font-family: var(--font-mono); color: var(--pd-text); line-height: 1; }
.pd-stat-l { font-size: 11px; text-transform: uppercase; letter-spacing: 0.07em; color: var(--pd-muted); }
.pd-div { width: 0.5px; height: 28px; background: var(--pd-border); }
.pd-desc { padding: 9px 18px; font-size: 13px; color: var(--pd-muted); border-bottom: 0.5px solid var(--pd-border); }
.pd-body { display: block; border-top: 0.5px solid var(--pd-border); }
.pd-sec { padding: 14px 18px; }
.pd-sec-title { font-size: 11px; font-weight: 500; letter-spacing: 0.09em; text-transform: uppercase; color: var(--pd-muted); margin: 0 0 8px; }
.prob-list { list-style: none; list-style-type: none; margin: 0; padding: 0; }
.pd ul.prob-list, .pd ul.prob-list li { list-style: none !important; padding-left: 0; margin-left: 0; }
.prob { padding-bottom: 9px; margin-bottom: 9px; border-bottom: 0.5px solid var(--pd-border); }
.prob:last-child { border-bottom: none; padding-bottom: 0; margin-bottom: 0; }
.prob-link { color: var(--pd-text); text-decoration: none; font-weight: 500; flex: 1; min-width: 0; word-wrap: break-word; overflow-wrap: break-word; }
.prob-link:hover { color: var(--pd-accent); }
.prob-title-row { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; margin-bottom: 4px; }
.prob-tags { display: flex; flex-wrap: wrap; gap: 4px; }
.tag { font-size: 10px; font-weight: 500; padding: 1px 5px; border-radius: 3px; text-transform: uppercase; letter-spacing: 0.05em; }
.tag-t { background: var(--pd-surface); color: var(--pd-muted); border: 0.5px solid var(--pd-border); font-weight: 400; text-transform: none; }
.prob-date { font-size: 11px; font-family: var(--font-mono); color: var(--pd-muted); white-space: nowrap; flex-shrink: 0; }
.pd-footer { padding: 10px 18px; border-top: 0.5px solid var(--pd-border); background: var(--pd-surface); text-align: right; }
.pd-footer a { font-size: 11px; color: var(--pd-accent); text-decoration: none; font-weight: 500; letter-spacing: 0.03em; }
.pd-footer a:hover { text-decoration: underline; }
</style>
<div class="pd">
  <div class="pd-header">
    <div>
      <a href="book-summaries/" class="pd-label">Book Summaries</a>
      <div class="pd-updated">updated May 9, 2026</div>
    </div>
    <div class="pd-stats">
      <div class="pd-stat">
        <span class="pd-stat-n">1</span>
        <span class="pd-stat-l">total</span>
      </div>
      <div class="pd-stat">
        <span class="pd-stat-n">0</span>
        <span class="pd-stat-l">this week</span>
      </div>
    </div>
  </div>

  <div class="pd-desc">Notes and summaries from books I've read, focusing on key ideas, takeaways, and personal insights.</div>

  <div class="pd-body">
    <div style="display:grid;grid-template-columns:1fr 1fr;">
      <div style="padding:14px 18px;border-right:0.5px solid var(--pd-border)">
        <svg viewBox="0 0 195 72" style="width:100%;height:auto;display:block;overflow:visible">
          <rect x="0" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="15" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="30" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="45" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="60" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="75" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="90" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="105" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
<rect x="120" y="10" width="12" height="40" rx="2" fill="#3b82f6" opacity="0.77"/>
<rect x="135" y="10" width="12" height="40" rx="2" fill="#a78bfa" opacity="0.82"/>
<rect x="150" y="10" width="12" height="40" rx="2" fill="#a78bfa" opacity="0.88"/>
<rect x="165" y="10" width="12" height="40" rx="2" fill="#a78bfa" opacity="0.94"/>
<rect x="180" y="48" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>
          <text x="6" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W8</text>
<text x="6" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Feb</text>
<text x="21" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W9</text>
<text x="36" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W10</text>
<text x="36" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Mar</text>
<text x="51" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W11</text>
<text x="66" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W12</text>
<text x="81" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W13</text>
<text x="96" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W14</text>
<text x="111" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W15</text>
<text x="111" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">Apr</text>
<text x="126" y="33" text-anchor="middle" font-size="6" fill="white" font-weight="500">1</text>
<text x="126" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W16</text>
<text x="141" y="33" text-anchor="middle" font-size="6" fill="white" font-weight="500">1</text>
<text x="141" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W17</text>
<text x="156" y="33" text-anchor="middle" font-size="6" fill="white" font-weight="500">1</text>
<text x="156" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W18</text>
<text x="171" y="33" text-anchor="middle" font-size="6" fill="white" font-weight="500">1</text>
<text x="171" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W19</text>
<text x="171" y="71" text-anchor="middle" font-size="7" fill="#94a3b8">May</text>
<text x="186" y="61" text-anchor="middle" font-size="6" fill="#94a3b8">W20</text>
        </svg>
        <div style="display:flex;gap:10px;margin-top:6px;margin-bottom:8px">
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#3b82f6;display:inline-block"></span> created</span>
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#a78bfa;display:inline-block"></span> updated</span>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:4px"><span class="tag tag-t">book-summary</span><span class="tag tag-t">machine-learning</span><span class="tag tag-t">system-design</span></div>
      </div>
      <div style="padding:14px 18px">
        <ul style="list-style:none;margin:0;padding:0">
        <li class="prob">
          <div class="prob-title-row">
            <a href="book-summaries/designing-ml-systems/" class="prob-link">Designing ML Systems</a>
            <span class="prob-date">May 9, 2026</span>
          </div>
          <div class="prob-tags"><span class="tag tag-t">book-summary</span><span class="tag tag-t">machine-learning</span><span class="tag tag-t">system-design</span></div>
        </li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- pd-bs:end -->

</div>
