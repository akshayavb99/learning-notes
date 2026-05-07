#!/usr/bin/env python3
"""Generate concept-notes stats widget for docs/index.md"""

import re
import sys
from pathlib import Path
from datetime import datetime, date, timedelta
from collections import defaultdict

# Config
DOCS_DIR = Path(__file__).parent.parent / "docs"
INDEX_FILE = DOCS_DIR / "index.md"
TODAY = date.today()

# Color palette (from prep_dashboard_preview): cycles through the color scheme
TAG_COLORS = ["#3b82f6", "#4ade80", "#facc15", "#f87171", "#a78bfa", "#34d399"]

# Section configurations
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


def get_iso_week(d):
    """Return (year, week_num) for ISO week; Monday is day 0"""
    iso = d.isocalendar()
    return (iso.year, iso.week)


def get_week_start(year, week_num):
    """Return the Monday of the given ISO week"""
    jan_4 = date(year, 1, 4)
    week_1_monday = jan_4 - timedelta(days=jan_4.weekday())
    return week_1_monday + timedelta(weeks=week_num - 1)


def parse_frontmatter(md_file):
    """Parse YAML frontmatter from a markdown file.

    Returns: dict of frontmatter, or None if no frontmatter
    Uses simple manual parsing (no PyYAML dependency).
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return None

    # Find closing delimiter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None

    fm_text = parts[1].strip()
    fm = {}

    # Simple line-by-line YAML parser for our specific use case
    lines = fm_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.startswith('#'):
            i += 1
            continue

        # Parse key: value pairs
        if ':' in line and not line.startswith(' '):
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()

            # Handle inline lists: tags: [item1, item2]
            if val.startswith('[') and val.endswith(']'):
                items = val[1:-1].split(',')
                fm[key] = [item.strip() for item in items]
            # Handle empty value (multiline list below)
            elif not val:
                # Check if next lines are list items (indented with -)
                items = []
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    if next_line.startswith('  -'):
                        item = next_line.strip('- ').strip()
                        items.append(item)
                        i += 1
                    elif not next_line.strip():
                        i += 1
                        continue
                    else:
                        break
                if items:
                    fm[key] = items
                    i -= 1  # Back up since we'll i+=1 at end
            # Handle block scalar (> or |)
            elif val.startswith('>') or val.startswith('|'):
                # Skip for now; we don't use description
                i += 1
                continue
            else:
                fm[key] = val

        i += 1

    return fm if fm else None


def load_notes(section_cfg):
    """Load notes from a section and extract metadata.

    Returns: list of dicts with {title, tags, updated_date, stem}
    """
    notes = []
    section_dir = section_cfg['dir']

    if not section_dir.exists():
        return notes

    for md_file in sorted(section_dir.glob(section_cfg['glob'])):
        if md_file.name == "index.md" and not section_cfg['parent_stem']:
            continue

        fm = parse_frontmatter(md_file)
        if not fm:
            continue

        title = fm.get('title', md_file.stem)
        tags = fm.get('tags', [])
        if not isinstance(tags, list):
            tags = [tags] if tags else []

        updated_date_str = fm.get('updated_date')
        if updated_date_str:
            try:
                updated_date = datetime.strptime(updated_date_str, '%Y-%m-%d').date()
            except Exception:
                updated_date = TODAY
        else:
            updated_date = TODAY

        stem = md_file.parent.name if section_cfg['parent_stem'] else md_file.stem
        notes.append({
            'title': title,
            'tags': tags,
            'updated_date': updated_date,
            'stem': stem,
        })

    return notes


def compute_stats(notes):
    """Compute widget stats from notes.

    Returns: dict with keys: total, this_week, tag_counts, recent, sparkline_data, max_date
    """
    total = len(notes)

    # This week: ISO week of today
    this_week_year, this_week_num = get_iso_week(TODAY)
    this_week = sum(1 for n in notes if get_iso_week(n['updated_date']) == (this_week_year, this_week_num))

    # Tag counts: each note contributes to count of each tag
    tag_counts = defaultdict(int)
    for note in notes:
        for tag in note['tags']:
            tag_counts[tag] += 1

    # Recent: 3 most recent by date (ties broken by title)
    recent = sorted(notes, key=lambda n: (-n['updated_date'].toordinal(), n['title']))[:3]

    # Sparkline: last 13 weeks (~3 months)
    sparkline_data = {}
    for week_offset in range(12, -1, -1):
        target_date = TODAY - timedelta(weeks=week_offset)
        target_year, target_week = get_iso_week(target_date)
        count = sum(1 for n in notes if get_iso_week(n['updated_date']) == (target_year, target_week))
        week_start = get_week_start(target_year, target_week)
        sparkline_data[week_start] = count

    # Max date for "updated" field
    max_date = max((n['updated_date'] for n in notes), default=TODAY)

    return {
        'total': total,
        'this_week': this_week,
        'tag_counts': dict(sorted(tag_counts.items(), key=lambda x: -x[1])),
        'recent': recent,
        'sparkline_data': sparkline_data,
        'max_date': max_date,
    }


def format_date_label(d):
    """Format date as 'Mon D, YYYY' for display (e.g., 'May 7, 2026')"""
    return d.strftime('%b %-d, %Y') if sys.platform != 'win32' else d.strftime('%b %#d, %Y')

def format_week_date(d):
    """Format date as 'Mon DD' for sparkline labels (e.g., 'Feb 17')"""
    return d.strftime('%b %-d') if sys.platform != 'win32' else d.strftime('%b %#d')


def generate_widget_html(stats, label, section_url, desc):
    """Generate the HTML widget with style and structure."""

    tag_counts = stats['tag_counts']
    max_tag_count = max(tag_counts.values()) if tag_counts else 1

    # Bar widths proportional to count
    def bar_width(count):
        if max_tag_count == 0:
            return 6
        return max(6, round(count / max_tag_count * 120))

    # Compact sparkline: 13 weeks for left column (narrower SVG)
    compact_rects = []
    compact_texts = []
    sparkline_data = stats['sparkline_data']
    sparkline_list = list(sparkline_data.items())
    max_sparkline_count = max(sparkline_data.values()) if sparkline_data else 1

    for i, (week_start, count) in enumerate(sparkline_list):
        x = i * 15
        bar_w = 12
        center_x = x + 6

        if max_sparkline_count == 0:
            height = 5 if count > 0 else 2
        else:
            height = int((count / max_sparkline_count) * 40) if count > 0 else 2

        opacity = 0.2 if count == 0 else 0.3 + (i / 12) * 0.7

        compact_rects.append(
            f'<rect x="{x}" y="{40 - height}" width="{bar_w}" height="{height}" rx="2" fill="#3b82f6" opacity="{opacity:.2f}"/>'
        )

        # Count label above bar for non-zero counts
        if count > 0:
            compact_texts.append(
                f'<text x="{center_x}" y="{40 - height - 3}" text-anchor="middle" font-size="7" font-weight="500" fill="#3b82f6" font-family="monospace">{count}</text>'
            )

        # Month label at boundaries only
        prev_week_start = sparkline_list[i - 1][0] if i > 0 else None
        if i == 0 or (prev_week_start and week_start.month != prev_week_start.month):
            month_str = week_start.strftime('%b')
            compact_texts.append(
                f'<text x="{center_x}" y="54" text-anchor="middle" font-size="7" style="fill: var(--pd-muted);" font-family="monospace">{month_str}</text>'
            )


    # Recent items (max 3) — titles are links to the note page
    recent_items = []
    for note in stats['recent']:
        date_label = format_date_label(note['updated_date'])
        # Show all tags as chips
        tags_html = ''.join(f'<span class="tag tag-t">{tag}</span>' for tag in note['tags'])
        note_url = f"{section_url}/{note['stem']}/"
        recent_items.append(f'''          <li class="prob">
            <div class="prob-title-row">
              <a href="{note_url}" class="prob-link">{note['title']}</a>
              <span class="prob-date">{date_label}</span>
            </div>
            <div class="prob-tags">{tags_html}</div>
          </li>''')

    # Top tags for left column
    top_tags = list(stats['tag_counts'].keys())[:6]
    top_tags_html = ''.join(f'<span class="tag tag-t">{tag}</span>' for tag in top_tags)

    # Updated date label
    updated_label = format_date_label(stats['max_date'])

    html = f'''<style>
:root {{
  --pd-accent: #3b82f6;
  --pd-surface: var(--color-background-secondary);
  --pd-border: var(--color-border-tertiary);
  --pd-text: var(--color-text-primary);
  --pd-muted: var(--color-text-secondary);
  --pd-r: var(--border-radius-md);
}}
.browse-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.6rem; align-items: start; }}
@media (max-width: 76.1875em) {{ .browse-grid {{ grid-template-columns: 1fr; }} }}
.pd {{ border: 0.5px solid var(--pd-border); border-radius: var(--border-radius-lg); overflow: hidden; font-size: 14px; transition: box-shadow 0.18s ease; }}
.pd:hover {{ box-shadow: 0 4px 20px rgba(0,0,0,0.10); }}
.pd-header {{ display: flex; justify-content: space-between; align-items: center; padding: 14px 18px; border-bottom: 0.5px solid var(--pd-border); background: var(--pd-surface); }}
.pd-label {{ font-size: 17px; font-weight: 500; color: var(--pd-accent); }}
.pd-updated {{ font-size: 11px; color: var(--pd-muted); font-family: var(--font-mono); margin-top: 2px; }}
.pd-stats {{ display: flex; align-items: center; gap: 8px; }}
.pd-stat {{ display: flex; flex-direction: column; align-items: center; }}
.pd-stat-n {{ font-size: 25px; font-weight: 500; font-family: var(--font-mono); color: var(--pd-text); line-height: 1; }}
.pd-stat-l {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.07em; color: var(--pd-muted); }}
.pd-div {{ width: 0.5px; height: 28px; background: var(--pd-border); }}
.pd-desc {{ padding: 9px 18px; font-size: 13px; color: var(--pd-muted); border-bottom: 0.5px solid var(--pd-border); }}
.pd-body {{ display: block; }}
.pd-sec {{ padding: 14px 18px; }}
.pd-sec-title {{ font-size: 11px; font-weight: 500; letter-spacing: 0.09em; text-transform: uppercase; color: var(--pd-muted); margin: 0 0 8px; }}
.prob-list {{ list-style: none; list-style-type: none; margin: 0; padding: 0; }}
.pd ul.prob-list, .pd ul.prob-list li {{ list-style: none !important; padding-left: 0; margin-left: 0; }}
.prob {{ padding-bottom: 9px; margin-bottom: 9px; border-bottom: 0.5px solid var(--pd-border); }}
.prob:last-child {{ border-bottom: none; padding-bottom: 0; margin-bottom: 0; }}
.prob-link {{ color: var(--pd-text); text-decoration: none; font-weight: 500; flex: 1; min-width: 0; word-wrap: break-word; overflow-wrap: break-word; }}
.prob-link:hover {{ color: var(--pd-accent); }}
.prob-title-row {{ display: flex; justify-content: space-between; align-items: baseline; gap: 8px; margin-bottom: 4px; }}
.prob-tags {{ display: flex; flex-wrap: wrap; gap: 4px; }}
.tag {{ font-size: 10px; font-weight: 500; padding: 1px 5px; border-radius: 3px; text-transform: uppercase; letter-spacing: 0.05em; }}
.tag-t {{ background: var(--pd-surface); color: var(--pd-muted); border: 0.5px solid var(--pd-border); font-weight: 400; text-transform: none; }}
.prob-date {{ font-size: 11px; font-family: var(--font-mono); color: var(--pd-muted); white-space: nowrap; flex-shrink: 0; }}
.pd-footer {{ padding: 10px 18px; border-top: 0.5px solid var(--pd-border); background: var(--pd-surface); text-align: right; }}
.pd-footer a {{ font-size: 11px; color: var(--pd-accent); text-decoration: none; font-weight: 500; letter-spacing: 0.03em; }}
.pd-footer a:hover {{ text-decoration: underline; }}
</style>

<div class="pd">
  <div class="pd-header">
    <div>
      <div class="pd-label">{label}</div>
      <div class="pd-updated">updated {updated_label}</div>
    </div>
    <div class="pd-stats">
      <div class="pd-stat">
        <span class="pd-stat-n">{stats['total']}</span>
        <span class="pd-stat-l">total</span>
      </div>
      <div class="pd-div"></div>
      <div class="pd-stat">
        <span class="pd-stat-n">{stats['this_week']}</span>
        <span class="pd-stat-l">this week</span>
      </div>
    </div>
  </div>

  <div class="pd-desc">{desc}</div>

  <div class="pd-body">
    <div style="display:grid;grid-template-columns:1fr 1fr;border-bottom:0.5px solid var(--pd-border)">
      <div style="padding:14px 18px;border-right:0.5px solid var(--pd-border)">
        <div class="pd-sec-title">Activity (13 weeks)</div>
        <svg viewBox="0 -12 200 75" xmlns="http://www.w3.org/2000/svg"
             style="width:100%;height:auto;display:block;margin-bottom:12px">
          {chr(10).join(compact_rects)}
          {chr(10).join(compact_texts)}
        </svg>
        <div class="pd-sec-title" style="margin-bottom:6px">Top tags</div>
        <div style="display:flex;flex-wrap:wrap;gap:4px">{top_tags_html}</div>
      </div>
      <div style="padding:14px 18px">
        <div class="pd-sec-title">Recent</div>
        <ul class="prob-list">
          {chr(10).join(recent_items)}
        </ul>
      </div>
    </div>
  </div>

  <div class="pd-footer">
    <a href="{section_url}/">View All →</a>
  </div>
</div>'''

    return html


def inject_widget(widget_html, target_file, start_marker, end_marker):
    """Replace widget content between markers in a target markdown file"""

    if not target_file.exists():
        print(f"  ERROR: {target_file} not found")
        return False

    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if markers exist
    if start_marker not in content or end_marker not in content:
        print(f"  ERROR: Markers {start_marker} / {end_marker} not found in {target_file.name}")
        return False

    # Replace content between markers
    pattern = rf'({re.escape(start_marker)}).*?({re.escape(end_marker)})'
    new_content = re.sub(pattern, rf'\1\n{widget_html}\n\2', content, flags=re.DOTALL)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    print("Generating widgets for all sections...")

    for section_cfg in SECTIONS:
        section_name = section_cfg['label']
        print(f"\n{section_name}:")

        notes = load_notes(section_cfg)
        print(f"  Loaded {len(notes)} items")

        if not notes:
            print(f"  WARNING: No items found")
            continue

        stats = compute_stats(notes)
        print(f"  Total: {stats['total']}, This week: {stats['this_week']}, Tags: {len(stats['tag_counts'])}")

        # Home page: links use full prefix (e.g. "concept-notes/note-slug/")
        widget_html_home = generate_widget_html(
            stats,
            section_cfg['label'],
            section_cfg['url_prefix'],
            section_cfg['desc'],
        )
        ok1 = inject_widget(widget_html_home, INDEX_FILE, section_cfg['start_marker'], section_cfg['end_marker'])
        if not ok1:
            print(f"  ERROR: Failed to inject into home page")
            return 1

        # Section index: links use "." so they resolve as "./note-slug/" (correct from that page's depth)
        widget_html_section = generate_widget_html(
            stats,
            section_cfg['label'],
            '.',
            section_cfg['desc'],
        )
        si = section_cfg['section_index']
        ok2 = inject_widget(widget_html_section, si['file'], si['start'], si['end'])
        if not ok2:
            print(f"  ERROR: Failed to inject into section index page")
            return 1

        print(f"  ✓ Injected (home page + section index)")

    print("\nSUCCESS: All widgets generated and injected")
    return 0


if __name__ == '__main__':
    sys.exit(main())
    
'''
claude --resume 0ecab798-eb82-4465-81d4-44d596df2d46
'''
