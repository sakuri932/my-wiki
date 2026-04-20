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
    card_re = re.compile(
        r'class="video-card"\s+id="([^"]+)".*?class="video-title">([^<]+)<',
        re.DOTALL
    )
    for m in card_re.finditer(added):
        vid_id = m.group(1)
        title = m.group(2).strip()
        results.append((vid_id, title))
    return results


def _get_local_changes(docs_dir, repo_root):
    """
    返回本地已修改/新增但未 commit 的 md 文件（用于本地预览同步）。
    同时检测：
      - git diff HEAD（已跟踪文件的修改）
      - git ls-files --others（新建的 untracked 文件）
    """
    import datetime
    today = datetime.date.today().isoformat()
    results = []
    lines = []
    try:
        # 已跟踪但修改/staged 的文件
        diff_out = subprocess.check_output(
            ['git', 'diff', '--name-only', 'HEAD'],
            cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=5
        )
        lines.extend(diff_out.splitlines())
    except Exception:
        pass
    try:
        # 新建的 untracked 文件（git add 之前也能捕捉到）
        untracked_out = subprocess.check_output(
            ['git', 'ls-files', '--others', '--exclude-standard'],
            cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=5
        )
        lines.extend(untracked_out.splitlines())
    except Exception:
        pass

    for line in lines:
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

    # ── 本地未提交改动（含新建文件），仅在本地预览时有效 ──────────────
    local_changes = _get_local_changes(docs_dir, repo_root)
    results = []
    seen = set()
    for date, rel, abs_path in local_changes:
        if rel in EXCLUDE_ALWAYS or any(rel.startswith(p) for p in EXCLUDE_PREFIXES):
            continue
        if _is_section_index(rel, docs_dir):
            continue
        seen.add(rel)
        results.append((date, rel, _get_title(abs_path)))

    # ── git log：用 "COMMIT <date>" 作分隔符，解析更稳健 ─────────────
    # --diff-filter=ACM 只看新增/修改，过滤删除/重命名噪音
    # --max-count=60 防止仓库极大时超时
    try:
        out = subprocess.check_output(
            ['git', 'log',
             '--diff-filter=ACM',
             '--pretty=format:COMMIT %ad',
             '--date=short',
             '--name-only',
             '--max-count=60'],
            cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=15
        )
    except Exception:
        return results

    current_date = None
    current_hash_for_video = None

    # 同时拿一份带 hash 的 log，仅用于视频区 diff 查询
    try:
        hash_out = subprocess.check_output(
            ['git', 'log', '--diff-filter=ACM',
             '--pretty=format:HASH %H %ad', '--date=short',
             '--name-only', '--max-count=60'],
            cwd=repo_root, stderr=subprocess.DEVNULL, text=True, timeout=15
        )
    except Exception:
        hash_out = ''

    # 建立 date → hash 的快查表（取每个日期最新的 hash）
    date_to_hash = {}
    _cur_h = None
    for hl in hash_out.splitlines():
        hl = hl.strip()
        if hl.startswith('HASH '):
            parts = hl.split()          # ['HASH', '<hash>', '<date>']
            if len(parts) >= 3:
                _cur_h = parts[1]
                _cur_d = parts[2]
                date_to_hash.setdefault(_cur_d, _cur_h)

    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith('COMMIT '):
            current_date = line[7:].strip()   # '2026-04-20'
            current_hash_for_video = date_to_hash.get(current_date)
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

        # 视频区特殊处理
        if rel == VIDEO_INDEX and current_hash_for_video:
            try:
                diff = subprocess.check_output(
                    ['git', 'show', '--unified=0', current_hash_for_video,
                     '--', f'docs/{VIDEO_INDEX}'],
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
                continue

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
