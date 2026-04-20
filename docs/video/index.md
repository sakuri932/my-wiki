# 🎬 视频区

<style>
.video-page-wrap { margin-top: 1.5em; }

.video-section { margin-bottom: 3em; }
.video-section-title {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 1em;
  padding-bottom: 0.4em;
  border-bottom: 2px solid var(--md-primary-fg-color);
  display: flex;
  align-items: center;
  gap: 0.4em;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

.video-card {
  border-radius: 10px;
  overflow: visible;
  text-decoration: none !important;
  color: inherit !important;
  background: var(--md-default-bg-color);
  box-shadow: 0 2px 8px rgba(0,0,0,0.10);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  display: block;
  cursor: pointer;
  position: relative;
}
.video-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 28px rgba(0,0,0,0.18);
}

/* 圆角裁切单独给 thumb-wrap */
.thumb-wrap {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  overflow: hidden;
  background: #1a1a2e;
  border-radius: 10px 10px 0 0;
}
.thumb-wrap img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.thumb-placeholder {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
  color: rgba(255,255,255,0.7);
  font-size: 2rem;
  gap: 0.3em;
}
.thumb-placeholder span {
  font-size: 0.7rem;
  opacity: 0.5;
  letter-spacing: 0.05em;
}

.play-icon {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.18s;
  background: rgba(0,0,0,0.3);
}
.video-card:hover .play-icon { opacity: 1; }
.play-icon svg {
  width: 48px; height: 48px;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.5));
}

.source-badge {
  position: absolute;
  bottom: 8px;
  right: 8px;
  font-size: 0.62rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  letter-spacing: 0.03em;
}
.badge-youtube { background: #ff0000; color: #fff; }
.badge-bilibili { background: #00a1d6; color: #fff; }
.badge-local { background: #555; color: #fff; }

.video-info {
  padding: 10px 12px 12px;
  border-radius: 0 0 10px 10px;
  background: var(--md-default-bg-color);
}
.video-title {
  font-size: 0.82rem;
  font-weight: 600;
  line-height: 1.45;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  color: var(--md-default-fg-color);
}

/* 悬停时展开全部标题 */
.video-card:hover .video-title {
  -webkit-line-clamp: unset;
  overflow: visible;
  position: absolute;
  left: 0; right: 0;
  background: var(--md-default-bg-color);
  padding: 10px 12px 12px;
  border-radius: 0 0 10px 10px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.15);
  z-index: 10;
}

@media (max-width: 600px) {
  .video-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
}
</style>

<div class="video-page-wrap">

<div class="video-section">
<div class="video-section-title">🧠 深度学习区</div>
<div class="video-grid">

  <a class="video-card" id="attention-efficient" href="https://www.youtube.com/watch?v=Y-o545eYjXM" target="_blank" rel="noopener">
    <div class="thumb-wrap">
      <img src="https://img.youtube.com/vi/Y-o545eYjXM/hqdefault.jpg" alt="How Attention Got So Efficient">
      <div class="play-icon"><svg viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="40" fill="rgba(0,0,0,0.5)"/><polygon points="32,24 60,40 32,56" fill="white"/></svg></div>
      <span class="source-badge badge-youtube">YouTube</span>
    </div>
    <div class="video-info">
      <div class="video-title">How Attention Got So Efficient [GQA/MLA/DSA]</div>
    </div>
  </a>

  <a class="video-card" id="diffusion-policy-intro" href="https://www.youtube.com/watch?v=e4VTrXqo1-Q" target="_blank" rel="noopener">
    <div class="thumb-wrap">
      <img src="https://img.youtube.com/vi/e4VTrXqo1-Q/hqdefault.jpg" alt="最适合入门的diffusion policy">
      <div class="play-icon"><svg viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="40" fill="rgba(0,0,0,0.5)"/><polygon points="32,24 60,40 32,56" fill="white"/></svg></div>
      <span class="source-badge badge-youtube">YouTube</span>
    </div>
    <div class="video-info">
      <div class="video-title">上交IWIN实验室：最适合入门的diffusion policy</div>
    </div>
  </a>

  <a class="video-card" id="diffusion-models-scratch" href="https://www.youtube.com/watch?v=B4oHJpEJBAA" target="_blank" rel="noopener">
    <div class="thumb-wrap">
      <img src="https://img.youtube.com/vi/B4oHJpEJBAA/hqdefault.jpg" alt="Diffusion Models From Scratch">
      <div class="play-icon"><svg viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="40" fill="rgba(0,0,0,0.5)"/><polygon points="32,24 60,40 32,56" fill="white"/></svg></div>
      <span class="source-badge badge-youtube">YouTube</span>
    </div>
    <div class="video-info">
      <div class="video-title">Diffusion Models From Scratch | Score-Based Generative Models Explained</div>
    </div>
  </a>

</div>
</div>

<div class="video-section">
<div class="video-section-title">🌿 日常区</div>
<div class="video-grid">

  <a class="video-card" id="jin-tangli" href="https://www.bilibili.com/video/BV1Lb9GB8ELk/" target="_blank" rel="noopener">
    <div class="thumb-wrap">
      <img src="assets/thumb-金汤力.jpg" alt="如何做一杯好喝的金汤力">
      <div class="play-icon"><svg viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="40" fill="rgba(0,0,0,0.5)"/><polygon points="32,24 60,40 32,56" fill="white"/></svg></div>
      <span class="source-badge badge-bilibili">bilibili</span>
    </div>
    <div class="video-info">
      <div class="video-title">如何做一杯好喝的金汤力</div>
    </div>
  </a>

</div>
</div>

<div class="video-section">
<div class="video-section-title">📦 其他区 <span style="font-size:0.75rem;font-weight:400;opacity:0.5;">（测试）</span></div>
<div class="video-grid">

  <a class="video-card" id="honkai3-mad" href="assets/崩坏3两周年MAD-月光的指引.mp4" target="_blank" rel="noopener">
    <div class="thumb-wrap">
      <img src="assets/thumb-月光的指引.jpg" alt="崩坏3两周年MAD">
      <div class="play-icon"><svg viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="40" fill="rgba(0,0,0,0.5)"/><polygon points="32,24 60,40 32,56" fill="white"/></svg></div>
      <span class="source-badge badge-local">本地收藏</span>
    </div>
    <div class="video-info">
      <div class="video-title">【崩坏3两周年MAD】月光的指引 ツキアカリのミチシルベ</div>
    </div>
  </a>

</div>
</div>

</div>
