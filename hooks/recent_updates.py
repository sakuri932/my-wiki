"""
MkDocs hook: 自动生成最近更新文章列表。

在 Markdown 文件中插入如下占位符（须在独立一行）：
    <!-- RECENT_UPDATES_AUTO -->

构建时自动替换为最近 git 提交的文章列表（按提交时间降序，最多 5 篇）。

特殊处理 video/index.md：解析 git diff 找出具体新增了哪个视频，
以视频标题 + 锚点链接的形式显示，而不是笼统地显示"视频区"。
"""

import os
import re
import subprocess

PLACEHOLDER = '<!-- RECENT_UPDATES_AUTO -->'
MAX_COUNT = 5
EXCLUDE_ALWAYS = {'最近更新.md'}
EXCLUDE_PREFIXES = ('blog/',)
VIDEO_INDEX = 'video/index.md'


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


def _parse_new_videos(diff_text):
    """从 git diff 中提取新增视频卡片的 (id, title) 列表。"""
    added = '\n'.join(
        line[1:] for line in diff_text.splitlines() if line.startswith('+')
    )
    results = []
    # 找每个新增 video-card 的 id，及其后紧跟的 video-title 文本
    card_re = re.compile(
        r'class="video-card"\s+id="([^"]+)".*?class="video-title">([^<]+)<',
        re.DOTALL
    )
    for m in card_re.finditer(added):
        vid_id = m.group(1)
        title = m.group(2).strip()
        results.append((vid_id, title))
    return results


def _get_uncommitted(docs_dir, repo_root):
    """返回本地已修改但未 commit 的 md 文件（用于本地预览同步）。"""
    import datetime
    today = datetime.date.today().isoformat()
    results = []
    try:
        out = subprocess.check_output(
            ['git', 'diff', '--name-only', 'HEAD'],
            cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=5
        )
    except Exception:
        return results
    for line in out.splitlines():
        line = line.strip()
        if not (line.endswith('.md') and line.startswith('docs/')):
            continue
        rel = line[len('docs/'):]
        abs_path = os.path.join(docs_dir, rel)
        if os.path.exists(abs_path):
            results.append((today, rel, abs_path))
    return results


def _get_recent(docs_dir):
    repo_root = _find_repo_root(docs_dir)
    try:
        out = subprocess.check_output(
            ['git', 'log', '--pretty=format:%ad %H', '--date=short', '--name-only'],
            cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=10
        )
    except Exception:
        return []

    # 先把本地未提交的改动放到最前面（本地预览用）
    uncommitted = _get_uncommitted(docs_dir, repo_root)
    results = []
    seen = set()
    for date, rel, abs_path in uncommitted:
        if rel in EXCLUDE_ALWAYS or any(rel.startswith(p) for p in EXCLUDE_PREFIXES):
            continue
        if _is_section_index(rel, docs_dir):
            continue
        seen.add(rel)
        results.append((date, rel, _get_title(abs_path)))

    current_date = None
    current_hash = None

    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        commit_match = re.match(r'^(\d{4}-\d{2}-\d{2})\s+([0-9a-f]{7,40})$', line)
        if commit_match:
            current_date = commit_match.group(1)
            current_hash = commit_match.group(2)
            continue

        if not (line.endswith('.md') and line.startswith('docs/')):
            continue

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
        if not os.path.exists(abs_path):
            continue

        # 视频区特殊处理：解析 diff 找具体新增的视频
        if rel == VIDEO_INDEX and current_hash:
            try:
                diff = subprocess.check_output(
                    ['git', 'show', '--unified=0', current_hash, '--',
                     f'docs/{VIDEO_INDEX}'],
                    cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=10
                )
                new_videos = _parse_new_videos(diff)
            except Exception:
                new_videos = []

            if new_videos:
                for vid_id, title in new_videos:
                    results.append((current_date, f'{VIDEO_INDEX}#{vid_id}', title))
                    if len(results) >= MAX_COUNT:
                        return results
                continue  # 不再走下面的普通处理

        results.append((current_date, rel, _get_title(abs_path)))
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
        for date, link, title in recent:
            rows.append(f'| [{title}]({link}) | {date} |')
        replacement = '| 文章 | 最后更新 |\n| --- | --- |\n' + '\n'.join(rows)

    return markdown.replace(PLACEHOLDER, replacement)
