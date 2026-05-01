document.addEventListener('DOMContentLoaded', () => {

  /* ── 1. 阅读进度条 ── */
  const bar = document.createElement('div');
  bar.className = 'reading-progress';
  document.body.appendChild(bar);
  const updateBar = () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = total > 0 ? (window.scrollY / total * 100) + '%' : '0%';
  };
  window.addEventListener('scroll', updateBar, { passive: true });
  updateBar();

  /* ── 2. 长代码块折叠 ── */
  const COLLAPSE_LINES = 25;
  document.querySelectorAll('.highlight').forEach(block => {
    const code = block.querySelector('code');
    if (!code) return;
    const lines = code.textContent.trimEnd().split('\n').length;
    if (lines <= COLLAPSE_LINES) return;

    const wrap = document.createElement('div');
    wrap.className = 'code-wrap code-collapsed';
    block.parentNode.insertBefore(wrap, block);
    wrap.appendChild(block);

    const btn = document.createElement('button');
    btn.className = 'code-expand-btn';
    btn.textContent = `展开完整代码（共 ${lines} 行）▾`;
    wrap.appendChild(btn);

    btn.addEventListener('click', () => {
      const collapsed = wrap.classList.toggle('code-collapsed');
      btn.textContent = collapsed
        ? `展开完整代码（共 ${lines} 行）▾`
        : '收起 ▴';
      if (collapsed) wrap.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
  });

  /* ── 3. 字数 & 阅读时长 ── */
  const article = document.querySelector('.md-content__inner');
  if (article) {
    const text = article.innerText || '';
    const chars = text.replace(/\s/g, '').length;
    if (chars > 150) {
      const mins = Math.ceil(chars / 400); // 中文技术文约 400 字/分钟
      const meta = document.createElement('div');
      meta.className = 'article-meta';
      meta.innerHTML =
        `<span>📖 约 ${chars.toLocaleString()} 字</span>` +
        `<span>⏱ 预计阅读 ${mins} 分钟</span>`;
      const h1 = article.querySelector('h1');
      if (h1) h1.insertAdjacentElement('afterend', meta);
    }
  }

});
