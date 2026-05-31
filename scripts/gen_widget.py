#!/usr/bin/env python3
"""Generate concept-notes stats widget for docs/index.md"""

import re
import sys
from pathlib import Path, PurePosixPath
from datetime import datetime, date, timedelta
from collections import defaultdict
import subprocess
import frontmatter

# Config
DOCS_DIR = Path(__file__).parent.parent / "docs"
INDEX_FILE = DOCS_DIR / "index.md"
TODAY = date.today()
PAGE_SIZE = 15

RECENT_START = '<!-- pd-recent:start -->'
RECENT_END   = '<!-- pd-recent:end -->'

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
    
    {
        'dir': DOCS_DIR / 'paper-summaries',
        'glob': '*.md',
        'parent_stem': False,
        'url_prefix': 'paper-summaries',
        'label': 'Paper Summaries',
        'desc': "Notes and summaries from papers I have read.",
        'start_marker': '<!-- pd-ps:start -->',
        'end_marker': '<!-- pd-ps:end -->',
        'section_index': {
            'file': DOCS_DIR / 'paper-summaries' / 'index.md',
            'start': '<!-- pd:start -->',
            'end': '<!-- pd:end -->',
        },
    },
    {
        'dir': DOCS_DIR / 'course-summaries',
        'glob': '*/index.md',
        'parent_stem': True,
        'url_prefix': 'course-summaries',
        'label': 'Course Summaries',
        'desc': "Notes and summaries from courses I have taken.",
        'start_marker': '<!-- pd-cs:start -->',
        'end_marker': '<!-- pd-cs:end -->',
        'section_index': {
            'file': DOCS_DIR / 'course-summaries' / 'index.md',
            'start': '<!-- pd:start -->',
            'end': '<!-- pd:end -->',
        },
    },
    {
        'dir': DOCS_DIR / 'practice-problems',
        'glob': '*.md',
        'parent_stem': False,
        'url_prefix': 'practice-problems',
        'label': 'Leetcode Solutions',
        'desc': "Solutions, approaches, and complexity analysis for Leetcode problems.",
        'start_marker': '<!-- pd-lc:start -->',
        'end_marker': '<!-- pd-lc:end -->',
        'section_index': {
            'file': DOCS_DIR / 'practice-problems' / 'index.md',
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

SECTION_INDEX_CSS = """<style>
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

        description = fm.get('description', '') or ''
        if not isinstance(description, str):
            description = str(description)

        notes.append({
            'title': title,
            'tags': tags,
            'updated_date': updated_date,
            'stem': stem,
            'description': description.strip(),
        })

    return notes


# ----------------------------
# STATS
# ----------------------------

def is_section_note_path(path, section_cfg, repo_root):
    """Return True when a git path is a real note for the section."""
    section_path = section_cfg['dir'].relative_to(repo_root).as_posix()
    git_path = PurePosixPath(path)

    try:
        rel_path = git_path.relative_to(section_path)
    except ValueError:
        return False

    if not rel_path.match(section_cfg['glob']):
        return False

    if rel_path.name == "index.md" and not section_cfg['parent_stem']:
        return False

    return True


def get_git_sparkline(section_cfg, weeks=13):
    """Return list of (week_start, created_count, updated_count) from git log.

    Uses per-commit name-status data: A means created, M means updated.
    Counts notes per commit, so one commit that updates three notes contributes three
    updates. Generated index pages are excluded using the same section rules as
    load_notes().
    Falls back to all-zero data if git is unavailable.
    """
    repo_root = DOCS_DIR.parent
    section_path = section_cfg['dir'].relative_to(repo_root).as_posix()
    created = defaultdict(int)
    updated = defaultdict(int)

    try:
        r = subprocess.run(
            ['git', 'log', f'--since={weeks + 1} weeks ago',
             '--name-status', '--date=short',
             '--pretty=format:commit:%H%x09%ad', '--', section_path],
            capture_output=True, text=True, cwd=str(repo_root), timeout=10,
        )

        current_week = None
        for line in r.stdout.splitlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith('commit:'):
                parts = line.split('\t')
                if len(parts) >= 2:
                    try:
                        commit_date = datetime.strptime(parts[1], '%Y-%m-%d').date()
                        current_week = get_week_start(*get_iso_week(commit_date))
                    except ValueError:
                        current_week = None
                continue

            if current_week is None:
                continue

            parts = line.split('\t')
            if len(parts) < 2:
                continue

            status = parts[0]
            path = parts[-1]

            if not is_section_note_path(path, section_cfg, repo_root):
                continue

            if status == 'A':
                created[current_week] += 1
            elif status == 'M':
                updated[current_week] += 1
    except Exception:
        pass

    result = []
    for week_offset in range(weeks - 1, -1, -1):
        ws = get_week_start(*get_iso_week(TODAY - timedelta(weeks=week_offset)))
        result.append((ws, created.get(ws, 0), updated.get(ws, 0)))
    return result


def get_git_dates(sections):
    """Return {abs_path: last_commit_date} for all note files across sections."""
    repo_root = DOCS_DIR.parent
    path_set = set()
    for section_cfg in sections:
        for md_file in section_cfg['dir'].glob(section_cfg['glob']):
            if md_file.name == "index.md" and not section_cfg['parent_stem']:
                continue
            path_set.add(md_file.resolve())

    if not path_set:
        return {}

    try:
        r = subprocess.run(
            ['git', 'log', '--pretty=format:COMMIT:%ad', '--date=short', '--name-only'],
            capture_output=True, text=True, cwd=str(repo_root), timeout=15,
        )
    except Exception:
        return {}

    dates = {}
    current_date = None
    for line in r.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('COMMIT:'):
            try:
                current_date = datetime.strptime(line[7:], '%Y-%m-%d').date()
            except ValueError:
                current_date = None
            continue
        if current_date is None:
            continue
        abs_path = (repo_root / line).resolve()
        if abs_path in path_set and abs_path not in dates:
            dates[abs_path] = current_date

    return dates


def compute_stats(notes, section_cfg):
    total = len(notes)

    sparkline_data = get_git_sparkline(section_cfg)

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


def generate_section_index_html(notes, section_url):
    """Generate section index HTML with Material CSS vars, sorted by git date (recent first)."""
    sorted_notes = sorted(notes, key=lambda n: (-n['updated_date'].toordinal(), n['title']))
    rows = []
    for note in sorted_notes:
        date_label = format_date_label(note['updated_date'])
        url = f"{section_url}/{note['stem']}/"
        desc_html = f'  <p class="ni-desc">{note["description"]}</p>\n' if note.get('description') else ''
        tags_html = ''.join(f'<span class="ni-tag">{tag}</span>' for tag in note['tags'])
        rows.append(
            f'<div class="ni">\n'
            f'  <div class="ni-header">\n'
            f'    <a href="{url}" class="ni-title">{note["title"]}</a>\n'
            f'    <span class="ni-date">{date_label}</span>\n'
            f'  </div>\n'
            + desc_html
            + f'  <div class="ni-tags">{tags_html}</div>\n'
            f'</div>'
        )

    notes_html = '\n'.join(rows)

    if len(sorted_notes) > PAGE_SIZE:
        pagination_html = (
            f'    <div class="ni-pagination">\n'
            f'      <button class="ni-page-btn ni-prev">&#8592; Prev</button>\n'
            f'      <span class="ni-page-info"></span>\n'
            f'      <button class="ni-page-btn ni-next">Next &#8594;</button>\n'
            f'    </div>\n'
        )
        pagination_script = '''
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
'''
        return (
            SECTION_INDEX_CSS + '\n'
            f'<div class="ni-paged">\n'
            f'  <div class="ni-list">\n'
            f'    {notes_html}\n'
            f'{pagination_html}'
            f'  </div>\n'
            f'</div>\n'
            f'{pagination_script}'
        )
    else:
        return SECTION_INDEX_CSS + '\n<div class="ni-list">\n' + notes_html + '\n</div>\n'


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
# RECENT NOTES (homepage)
# ----------------------------

def get_git_recent_notes(sections, n=4):
    """Return the n most recently committed note files across all sections."""
    repo_root = DOCS_DIR.parent

    path_to_section = {}
    for section_cfg in sections:
        for md_file in section_cfg['dir'].glob(section_cfg['glob']):
            if md_file.name == "index.md" and not section_cfg['parent_stem']:
                continue
            path_to_section[md_file.resolve()] = section_cfg

    if not path_to_section:
        return []

    try:
        r = subprocess.run(
            ['git', 'log', '--pretty=format:COMMIT:%ad', '--date=short',
             '--diff-filter=AMR', '--name-only'],
            capture_output=True, text=True, cwd=str(repo_root), timeout=15,
        )
    except Exception:
        return []

    seen = {}
    current_date = None
    for line in r.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('COMMIT:'):
            try:
                current_date = datetime.strptime(line[7:], '%Y-%m-%d').date()
            except ValueError:
                current_date = None
            continue
        if current_date is None:
            continue
        abs_path = (repo_root / line).resolve()
        if abs_path in path_to_section and abs_path not in seen:
            seen[abs_path] = current_date

    sorted_paths = sorted(seen.items(), key=lambda x: -x[1].toordinal())[:n]

    notes = []
    for abs_path, commit_date in sorted_paths:
        section_cfg = path_to_section[abs_path]
        fm = parse_frontmatter(abs_path)
        title = fm.get('title', abs_path.stem)
        tags = fm.get('tags', [])
        if not isinstance(tags, list):
            tags = [tags] if tags else []
        stem = abs_path.parent.name if section_cfg['parent_stem'] else abs_path.stem
        notes.append({
            'title': title,
            'tags': tags,
            'updated_date': commit_date,
            'stem': stem,
            'url_prefix': section_cfg['url_prefix'],
        })
    return notes


def generate_recent_html(notes):
    rows = []
    for note in notes:
        date_label = format_date_label(note['updated_date'])
        tags_html = ''.join(f'<span class="rn-tag">{tag}</span>' for tag in note['tags'])
        url = f"{note['url_prefix']}/{note['stem']}/"
        rows.append(
            f'  <div class="recent-note">\n'
            f'    <div class="recent-note-main">\n'
            f'      <a href="{url}" class="recent-note-title">{note["title"]}</a>\n'
            f'      <span class="recent-note-date">{date_label}</span>\n'
            f'    </div>\n'
            f'    <div class="recent-note-tags">{tags_html}</div>\n'
            f'  </div>'
        )
    return '<div class="recent-notes-list">\n' + '\n'.join(rows) + '\n</div>\n'


# ----------------------------
# HOMEPAGE COUNTS
# ----------------------------

def update_homepage_counts(sections):
    """Update category counts and stats in the main index.md."""
    section_counts = {}
    total_notes = 0

    for section_cfg in sections:
        notes = load_notes(section_cfg)
        count = len(notes)
        section_counts[section_cfg['label']] = count
        total_notes += count

    # Map section labels to their marker keys
    section_map = {
        'Concept Notes': ('concept-notes', count_label(section_counts.get('Concept Notes', 0), 'note')),
        'Book Summaries': ('book-summaries', count_label(section_counts.get('Book Summaries', 0), 'book')),
        'Paper Summaries': ('paper-summaries', count_label(section_counts.get('Paper Summaries', 0), 'paper')),
        'Indexes': ('indexes', count_label(section_counts.get('Indexes', 0), 'index')),
        'Course Summaries': ('course-summaries', count_label(section_counts.get('Course Summaries', 0), 'course')),
        'Leetcode Solutions': ('practice-problems', count_label(section_counts.get('Leetcode Solutions', 0), 'solution')),
    }

    content = INDEX_FILE.read_text(encoding='utf-8')

    # Update category counts
    for label, (key, count_text) in section_map.items():
        pattern = rf'(<!-- cat-count:{key} -->).*?(<!-- /cat-count -->)'
        replacement = lambda m: m.group(1) + count_text + m.group(2)
        content = re.sub(pattern, replacement, content)

    # Update stat values
    stat_updates = {
        'total-notes': str(total_notes),
        'sections': '6',
        'concept-notes': str(section_counts.get('Concept Notes', 0)),
        'book-summaries': str(section_counts.get('Book Summaries', 0)),
        'paper-summaries': str(section_counts.get('Paper Summaries', 0)),
        'indexes': str(section_counts.get('Indexes', 0)),
        'course-summaries': str(section_counts.get('Course Summaries', 0)),
        'practice-problems': str(section_counts.get('Leetcode Solutions', 0)),
    }

    for stat_key, value in stat_updates.items():
        pattern = rf'(<!-- stat:{stat_key} -->).*?(<!-- /stat -->)'
        replacement = lambda m, v=value: m.group(1) + v + m.group(2)
        content = re.sub(pattern, replacement, content)

    INDEX_FILE.write_text(content, encoding='utf-8')


def count_label(count, singular):
    """Generate plural label for count."""
    if count == 1:
        return f"1 {singular}"
    else:
        # Handle special cases
        if singular == 'index':
            return f"{count} indexes"
        elif singular.endswith('y'):
            return f"{count} {singular[:-1]}ies"
        else:
            return f"{count} {singular}s"


# ----------------------------
# MAIN
# ----------------------------

def main():
    print("Generating widgets...")

    git_dates = get_git_dates(SECTIONS)

    for section_cfg in SECTIONS:
        print(f"\n{section_cfg['label']}:")
        notes = load_notes(section_cfg)
        for note in notes:
            abs_path = (section_cfg['dir'] / (note['stem'] + '.md')).resolve()
            if section_cfg['parent_stem']:
                abs_path = (section_cfg['dir'] / note['stem'] / 'index.md').resolve()
            if abs_path in git_dates:
                note['updated_date'] = git_dates[abs_path]
        si = section_cfg['section_index']
        section_html = generate_section_index_html(notes, '.')
        inject_widget(section_html, si['file'], si['start'], si['end'])
        print(f"  Done ({len(notes)} notes)")

    print("\nRecent notes (homepage):")
    recent_notes = get_git_recent_notes(SECTIONS, n=5)
    recent_html = generate_recent_html(recent_notes)
    inject_widget(recent_html, INDEX_FILE, RECENT_START, RECENT_END)
    print(f"  Done ({len(recent_notes)} notes shown)")

    print("\nUpdating homepage counts...")
    update_homepage_counts(SECTIONS)
    print("  Done")

    print("\nSUCCESS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
