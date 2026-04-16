"""
MkDocs hook: 自动扫描 PDF 文件夹并生成下载链接列表。

用法：在 Markdown 文件中插入如下占位符（须在独立一行）：
    <!-- PDF_AUTO_LIST: 文件夹名称 -->

文件夹路径相对于该 md 文件所在目录。
每次构建时自动替换为当前文件夹内所有 PDF 的链接列表，按文件名排序。
"""

import os
import re
import urllib.parse


def on_page_markdown(markdown, page, config, **kwargs):
    pattern = re.compile(
        r'<!-- PDF_AUTO_LIST: (.+?) -->'
    )

    def replace(match):
        folder_name = match.group(1).strip()
        # md 文件所在目录
        page_dir = os.path.dirname(
            os.path.join(config['docs_dir'], page.file.src_path)
        )
        pdf_dir = os.path.join(page_dir, folder_name)

        if not os.path.isdir(pdf_dir):
            return f'> ⚠️ 找不到文件夹：`{folder_name}`'

        pdfs = sorted(f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf'))

        if not pdfs:
            return '> 暂无课件。'

        # 生成显示名：去掉日期前缀（如 20260120_）和扩展名，下划线换空格
        def display_name(filename):
            name = filename[:-4]  # 去掉 .pdf
            name = re.sub(r'^\d{8}_', '', name)  # 去掉日期前缀
            return name.replace('_', ' ')

        # URL 编码文件夹名和文件名（处理空格、中文等）
        folder_encoded = urllib.parse.quote(folder_name)
        lines = []
        for pdf in pdfs:
            file_encoded = urllib.parse.quote(pdf)
            lines.append(f'- [{display_name(pdf)}](./{folder_encoded}/{file_encoded})')

        return '\n'.join(lines)

    return pattern.sub(replace, markdown)
