"""
MkDocs hook: 自动生成最近更新文章列表。

在 Markdown 文件中插入如下占位符（须在独立一行）：
    <!-- RECENT_UPDATES_AUTO -->

构建时自动替换为最近 git 提交的文章列表（按提交时间降序，最多 5 篇）。
排除"栏目导航页"性质的 index.md（即同目录下还有其他 md 文件的情况）、
blog/ 目录以及本页自身。
如果某目录的 index.md 是唯一的 md 文件（如视频区），则视为内容页保留。
"""

import os
import re
import subprocess

PLACEHOLDER = '<!-- RECENT_UPDATES_AUTO -->'
MAX_COUNT = 5
EXCLUDE_ALWAYS = {'最近更新.md'}
EXCLUDE_PREFIXES = ('blog/',)


def _find_repo_root(start):
    path = start
    for _ in range(15):
        if os.path.isdir(os.path.join(path, '.git')):
            return path
        parent = os.path.dirname(path)
        if parent == path:
            break
        path = parent
    return start


def _get_title(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith('# '):
                    return stripped[2:].strip()
    except Exception:
        pass
    return os.path.splitext(os.path.basename(filepath))[0]


def _is_section_index(rel, docs_dir):
    """index.md 且同目录下还有其他 md 文件 → 栏目导航页，应排除。"""
    if os.path.basename(rel) != 'index.md':
        return False
    dir_path = os.path.join(docs_dir, os.path.dirname(rel))
    try:
        siblings = [f for f in os.listdir(dir_path) if f.endswith('.md') and f != 'index.md']
    except OSError:
        return False
    return len(siblings) > 0


def _get_recent(docs_dir):
    repo_root = _find_repo_root(docs_dir)
    try:
        out = subprocess.check_output(
            ['git', 'log', '--pretty=format:%ad', '--date=short', '--name-only'],
            cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=10
        )
    except Exception:
        return []

    results = []
    seen = set()
    current_date = None

    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d{4}-\d{2}-\d{2}$', line):
            current_date = line
        elif line.endswith('.md') and line.startswith('docs/'):
            rel = line[len('docs/'):]
            if rel in EXCLUDE_ALWAYS:
                continue
            if any(rel.startswith(p) for p in EXCLUDE_PREFIXES):
                continue
            if _is_section_index(rel, docs_dir):
                continue
            if rel in seen:
                continue
            seen.add(rel)
            abs_path = os.path.join(docs_dir, rel)
            if os.path.exists(abs_path):
                results.append((current_date, rel, abs_path))
            if len(results) >= MAX_COUNT:
                break

    return results


def on_page_markdown(markdown, page, config, **kwargs):
    if PLACEHOLDER not in markdown:
        return markdown

    recent = _get_recent(config['docs_dir'])

    if not recent:
        replacement = '> 暂无更新记录。'
    else:
        rows = []
        for date, rel_path, abs_path in recent:
            title = _get_title(abs_path)
            rows.append(f'| [{title}]({rel_path}) | {date} |')
        replacement = '| 文章 | 最后更新 |\n| --- | --- |\n' + '\n'.join(rows)

    return markdown.replace(PLACEHOLDER, replacement)
