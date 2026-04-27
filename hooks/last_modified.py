"""通过 git log 给每篇文章注入最后修改时间。"""
import subprocess, datetime
from pathlib import Path

def on_page_markdown(markdown, page, config, files):
    src = page.file.abs_src_path
    if not src:
        return markdown
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%ct', '--', src],
            capture_output=True, text=True,
            cwd=str(Path(src).parent)
        )
        ts = result.stdout.strip()
        if not ts:
            return markdown
        dt = datetime.datetime.fromtimestamp(int(ts))
        label = dt.strftime('%Y 年 %m 月 %d 日')
        footer = f'\n\n---\n\n<small>📝 最后更新：{label}</small>\n'
        return markdown + footer
    except Exception:
        return markdown
