#!/usr/bin/env python3
"""Generate concept-notes stats widget for docs/index.md"""

import re
import sys
from pathlib import Path
from datetime import datetime, date, timedelta
from collections import defaultdict
import subprocess
import frontmatter

# Config
DOCS_DIR = Path(__file__).parent.parent / "docs"
INDEX_FILE = DOCS_DIR / "index.md"
TODAY = date.today()

SECTIONS = [
    {
        'dir': DOCS_DIR / 'concept-notes',
        'glob': '*.md',
        'parent_stem': False,
        'url_prefix': 'concept-notes',
        'label': 'Concept Notes',
        'desc': 'A flat collection of notes spanning AI, system design, programming, version control, and more.',
        'start_marker': '<!-- pd-cn:start -->',
        'end_marker': '<!-- pd-cn:end -->',
        'section_index': {
            'file': DOCS_DIR / 'concept-notes' / 'index.md',
            'start': '<!-- pd:start -->',
            'end': '<!-- pd:end -->',
        },
    },
    {
        'dir': DOCS_DIR / 'indexes',
        'glob': '*.md',
        'parent_stem': False,
        'url_prefix': 'indexes',
        'label': 'Indexes',
        'desc': 'Area-wise indexes for Artificial Intelligence, System Design, Programming, and Version Control.',
        'start_marker': '<!-- pd-idx:start -->',
        'end_marker': '<!-- pd-idx:end -->',
        'section_index': {
            'file': DOCS_DIR / 'indexes' / 'index.md',
            'start': '<!-- pd:start -->',
            'end': '<!-- pd:end -->',
        },
    },
    {
        'dir': DOCS_DIR / 'book-summaries',
        'glob': '*/index.md',
        'parent_stem': True,
        'url_prefix': 'book-summaries',
        'label': 'Book Summaries',
        'desc': "Notes and summaries from books I've read, focusing on key ideas, takeaways, and personal insights.",
        'start_marker': '<!-- pd-bs:start -->',
        'end_marker': '<!-- pd-bs:end -->',
        'section_index': {
            'file': DOCS_DIR / 'book-summaries' / 'index.md',
            'start': '<!-- pd:start -->',
            'end': '<!-- pd:end -->',
        },
    },
]


WIDGET_CSS = """<style>
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
</style>"""


# ----------------------------
# DATE HELPERS
# ----------------------------

def get_iso_week(d):
    iso = d.isocalendar()
    return (iso.year, iso.week)


def get_week_start(year, week_num):
    jan_4 = date(year, 1, 4)
    week_1_monday = jan_4 - timedelta(days=jan_4.weekday())
    return week_1_monday + timedelta(weeks=week_num - 1)


def safe_parse_date(value):
    """Robust date parser for YAML frontmatter values."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except Exception:
            return TODAY
    return TODAY


# ----------------------------
# FRONTMATTER LOADING
# ----------------------------

def parse_frontmatter(md_file):
    """Robust frontmatter parsing using python-frontmatter."""
    post = frontmatter.load(md_file)
    return post.metadata or {}


def load_notes(section_cfg):
    notes = []
    section_dir = section_cfg['dir']

    if not section_dir.exists():
        return notes

    for md_file in sorted(section_dir.glob(section_cfg['glob'])):
        if md_file.name == "index.md" and not section_cfg['parent_stem']:
            continue

        fm = parse_frontmatter(md_file)

        title = fm.get('title', md_file.stem)

        tags = fm.get('tags', [])
        if not isinstance(tags, list):
            tags = [tags] if tags else []

        raw_date = fm.get('updated_date')
        updated_date = safe_parse_date(raw_date) if raw_date is not None else date.fromtimestamp(md_file.stat().st_mtime)

        stem = md_file.parent.name if section_cfg['parent_stem'] else md_file.stem

        notes.append({
            'title': title,
            'tags': tags,
            'updated_date': updated_date,
            'stem': stem,
        })

    return notes


# ----------------------------
# STATS
# ----------------------------

def get_git_sparkline(section_dir, glob, weeks=13):
    """Return list of (week_start, created_count, updated_count) from git log.

    Uses --diff-filter=A for new files (created) and =M for modifications (updated).
    Each file is counted at most once per week per category to avoid commit-frequency noise.
    Falls back to all-zero data if git is unavailable.
    """
    repo_root = DOCS_DIR.parent
    pattern = str(section_dir.relative_to(repo_root) / glob).replace('\\', '/')

    def fetch(diff_filter):
        try:
            r = subprocess.run(
                ['git', 'log', f'--since={weeks + 1} weeks ago',
                 f'--diff-filter={diff_filter}', '--name-only',
                 '--pretty=format:%ci', '--', pattern],
                capture_output=True, text=True, cwd=str(repo_root), timeout=10,
            )
            weekly = defaultdict(set)
            current_date = None
            for line in r.stdout.split('\n'):
                line = line.strip()
                if not line:
                    continue
                if len(line) >= 10 and line[4:5] == '-' and line[7:8] == '-':
                    try:
                        current_date = datetime.strptime(line[:10], '%Y-%m-%d').date()
                        continue
                    except ValueError:
                        pass
                if current_date:
                    weekly[get_week_start(*get_iso_week(current_date))].add(line)
            return weekly
        except Exception:
            return {}

    added = fetch('A')
    modified = fetch('M')

    result = []
    for week_offset in range(weeks - 1, -1, -1):
        ws = get_week_start(*get_iso_week(TODAY - timedelta(weeks=week_offset)))
        result.append((ws, len(added.get(ws, set())), len(modified.get(ws, set()))))
    return result


def compute_stats(notes, section_cfg):
    total = len(notes)

    sparkline_data = get_git_sparkline(section_cfg['dir'], section_cfg['glob'])

    this_week_start = get_week_start(*get_iso_week(TODAY))
    this_week = sum(c + u for ws, c, u in sparkline_data if ws == this_week_start)

    tag_counts = defaultdict(int)
    for note in notes:
        for tag in note['tags']:
            tag_counts[tag] += 1

    recent = sorted(
        notes,
        key=lambda n: (-n['updated_date'].toordinal(), n['title'])
    )[:3]

    max_date = max((n['updated_date'] for n in notes), default=TODAY)

    return {
        'total': total,
        'this_week': this_week,
        'tag_counts': dict(sorted(tag_counts.items(), key=lambda x: -x[1])),
        'recent': recent,
        'sparkline_data': sparkline_data,
        'max_date': max_date,
    }


# ----------------------------
# FORMATTING HELPERS
# ----------------------------

def format_date_label(d):
    return d.strftime('%b %-d, %Y') if sys.platform != 'win32' else d.strftime('%b %#d, %Y')


# ----------------------------
# HTML GENERATION
# ----------------------------

def generate_widget_html(stats, label, section_url, desc):
    tag_counts = stats['tag_counts']
    max_tag_count = max(tag_counts.values()) if tag_counts else 1

    # SVG layout budget: top pad → bar area → week row → month row
    _BAR_H   = 40   # max bar height
    _TOP     = 10   # headroom above tallest bar for count labels
    _AXIS1   = 12   # week-number row height
    _AXIS2   = 10   # month-label row height
    _BASE    = _TOP + _BAR_H          # y of bar bottoms = 50
    _SVG_H   = _TOP + _BAR_H + _AXIS1 + _AXIS2   # total SVG height = 72

    compact_rects = []
    compact_texts = []

    sparkline_list = stats['sparkline_data']
    max_total = max((c + u for _, c, u in sparkline_list), default=1) or 1
    scale = _BAR_H / max_total

    for i, (week_start, created, updated) in enumerate(sparkline_list):
        x = i * 15
        center_x = x + 6
        total = created + updated

        created_h = max(1, int(created * scale)) if created else 0
        updated_h = max(1, int(updated * scale)) if updated else 0

        opacity = 0.2 if total == 0 else 0.3 + (i / 12) * 0.7

        if total == 0:
            compact_rects.append(
                f'<rect x="{x}" y="{_BASE - 2}" width="12" height="2" rx="1" fill="#3b82f6" opacity="0.15"/>'
            )
        else:
            if created_h:
                compact_rects.append(
                    f'<rect x="{x}" y="{_BASE - created_h}" width="12" height="{created_h}" rx="2" fill="#3b82f6" opacity="{opacity:.2f}"/>'
                )
            if updated_h:
                compact_rects.append(
                    f'<rect x="{x}" y="{_BASE - created_h - updated_h}" width="12" height="{updated_h}" rx="2" fill="#a78bfa" opacity="{opacity:.2f}"/>'
                )

        if created_h >= 9:
            compact_texts.append(
                f'<text x="{center_x}" y="{int(_BASE - created_h / 2 + 3)}" text-anchor="middle" font-size="6" fill="white" font-weight="500">{created}</text>'
            )
        if updated_h >= 9:
            compact_texts.append(
                f'<text x="{center_x}" y="{int(_BASE - created_h - updated_h / 2 + 3)}" text-anchor="middle" font-size="6" fill="white" font-weight="500">{updated}</text>'
            )

        _, week_num = get_iso_week(week_start)
        compact_texts.append(
            f'<text x="{center_x}" y="{_BASE + _AXIS1 - 1}" text-anchor="middle" font-size="6" fill="#94a3b8">W{week_num}</text>'
        )

        prev_week_start = sparkline_list[i - 1][0] if i > 0 else None
        if i == 0 or (prev_week_start and week_start.month != prev_week_start.month):
            compact_texts.append(
                f'<text x="{center_x}" y="{_BASE + _AXIS1 + _AXIS2 - 1}" text-anchor="middle" font-size="7" fill="#94a3b8">{week_start.strftime("%b")}</text>'
            )

    recent_items = []
    for note in stats['recent']:
        date_label = format_date_label(note['updated_date'])
        tags_html = ''.join(f'<span class="tag tag-t">{tag}</span>' for tag in note['tags'])
        note_url = f"{section_url}/{note['stem']}/"

        recent_items.append(f"""
        <li class="prob">
          <div class="prob-title-row">
            <a href="{note_url}" class="prob-link">{note['title']}</a>
            <span class="prob-date">{date_label}</span>
          </div>
          <div class="prob-tags">{tags_html}</div>
        </li>
        """)

    top_tags = list(stats['tag_counts'].keys())[:6]
    top_tags_html = ''.join(f'<span class="tag tag-t">{tag}</span>' for tag in top_tags)

    updated_label = format_date_label(stats['max_date'])

    html = WIDGET_CSS + f"""
<div class="pd">
  <div class="pd-header">
    <div>
      <a href="{section_url}/" class="pd-label">{label}</a>
      <div class="pd-updated">updated {updated_label}</div>
    </div>
    <div class="pd-stats">
      <div class="pd-stat">
        <span class="pd-stat-n">{stats['total']}</span>
        <span class="pd-stat-l">total</span>
      </div>
      <div class="pd-stat">
        <span class="pd-stat-n">{stats['this_week']}</span>
        <span class="pd-stat-l">this week</span>
      </div>
    </div>
  </div>

  <div class="pd-desc">{desc}</div>

  <div class="pd-body">
    <div style="display:grid;grid-template-columns:1fr 1fr;">
      <div style="padding:14px 18px;border-right:0.5px solid var(--pd-border)">
        <svg viewBox="0 0 195 {_SVG_H}" style="width:100%;height:auto;display:block;overflow:visible">
          {chr(10).join(compact_rects)}
          {chr(10).join(compact_texts)}
        </svg>
        <div style="display:flex;gap:10px;margin-top:6px;margin-bottom:8px">
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#3b82f6;display:inline-block"></span> created</span>
          <span style="display:inline-flex;align-items:center;gap:3px;font-size:10px;color:var(--pd-muted)"><span style="width:8px;height:8px;border-radius:2px;background:#a78bfa;display:inline-block"></span> updated</span>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:4px">{top_tags_html}</div>
      </div>
      <div style="padding:14px 18px">
        <ul style="list-style:none;margin:0;padding:0">{chr(10).join(recent_items)}</ul>
      </div>
    </div>
  </div>
</div>
"""
    return html


# ----------------------------
# INJECTION
# ----------------------------

def inject_widget(widget_html, target_file, start_marker, end_marker):
    if not target_file.exists():
        return False

    content = target_file.read_text(encoding='utf-8')

    if start_marker not in content or end_marker not in content:
        print(f"  WARNING: markers not found in {target_file.name}")
        return False

    pattern = rf'({re.escape(start_marker)}).*?({re.escape(end_marker)})'
    new_content = re.sub(pattern, rf'\1\n{widget_html}\n\2', content, flags=re.DOTALL)

    target_file.write_text(new_content, encoding='utf-8')
    return True


# ----------------------------
# MAIN
# ----------------------------

def main():
    print("Generating widgets...")

    for section_cfg in SECTIONS:
        print(f"\n{section_cfg['label']}:")

        notes = load_notes(section_cfg)
        stats = compute_stats(notes, section_cfg)

        widget_home = generate_widget_html(
            stats,
            section_cfg['label'],
            section_cfg['url_prefix'],
            section_cfg['desc'],
        )

        inject_widget(
            widget_home,
            INDEX_FILE,
            section_cfg['start_marker'],
            section_cfg['end_marker']
        )

        si = section_cfg['section_index']
        widget_section = generate_widget_html(stats, section_cfg['label'], '.', section_cfg['desc'])
        inject_widget(widget_section, si['file'], si['start'], si['end'])

        print(f"  ✓ Done ({len(notes)} notes)")

    print("\nSUCCESS")
    return 0


if __name__ == "__main__":
    sys.exit(main())