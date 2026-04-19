# 🤔 不务正业

用 AI 写的小玩具，闲着没事可以玩玩。

<style>
.game-page-wrap { margin-top: 1.5em; }

.game-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.game-card {
  border-radius: 12px;
  overflow: visible;
  text-decoration: none !important;
  color: inherit !important;
  background: var(--md-default-bg-color);
  box-shadow: 0 2px 10px rgba(0,0,0,0.12);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  display: block;
  cursor: pointer;
  position: relative;
}
.game-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.2);
}

.game-thumb {
  position: relative;
  width: 100%;
  padding-top: 62%;
  overflow: hidden;
  border-radius: 12px 12px 0 0;
}
.game-cover {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  user-select: none;
}
.cover-icon { font-size: 3rem; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.4)); }
.cover-label {
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}

/* 斗地主封面：绿色牌桌 */
.cover-doudizhu {
  background: radial-gradient(ellipse 120% 100% at 50% 80%, #1d6020, #0a2010);
}
.cover-doudizhu .cover-label { color: #ffd700; }
.cover-doudizhu .suit-row {
  font-size: 1.4rem;
  letter-spacing: 0.15em;
  color: rgba(255,255,255,0.7);
}

/* 打僵尸封面：暗夜 FPS */
.cover-zombie {
  background: radial-gradient(ellipse 120% 100% at 50% 30%, #1a0a0a, #0d0d0d);
}
.cover-zombie .cover-label { color: #ff3333; text-shadow: 0 0 12px rgba(255,50,50,0.7); }
.cover-zombie .cover-sub {
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  color: rgba(255,100,100,0.6);
  text-transform: uppercase;
}

/* 悬停遮罩 */
.play-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.35);
  opacity: 0;
  transition: opacity 0.18s;
  border-radius: 12px 12px 0 0;
}
.game-card:hover .play-overlay { opacity: 1; }
.play-overlay svg { width: 52px; height: 52px; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.5)); }

.game-info {
  padding: 11px 14px 14px;
  background: var(--md-default-bg-color);
  border-radius: 0 0 12px 12px;
}
.game-title {
  font-size: 0.92rem;
  font-weight: 700;
  margin-bottom: 4px;
  color: var(--md-default-fg-color);
}
.game-desc {
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--md-default-fg-color--light);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.game-card:hover .game-desc {
  -webkit-line-clamp: unset;
  overflow: visible;
  position: absolute;
  left: 0; right: 0;
  background: var(--md-default-bg-color);
  padding: 11px 14px 14px;
  border-radius: 0 0 12px 12px;
  box-shadow: 0 12px 24px rgba(0,0,0,0.15);
  z-index: 10;
}

@media (max-width: 600px) {
  .game-grid { grid-template-columns: repeat(2, 1fr); gap: 12px; }
}
</style>

<div class="game-page-wrap">
<div class="game-grid">

  <a class="game-card" id="doudizhu" href="斗地主.html" target="_blank" rel="noopener">
    <div class="game-thumb">
      <div class="game-cover cover-doudizhu">
        <div class="cover-icon">🃏</div>
        <div class="suit-row">♠ ♥ ♣ ♦</div>
        <div class="cover-label">斗地主</div>
      </div>
      <div class="play-overlay"><svg viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="40" fill="rgba(0,0,0,0.5)"/><polygon points="32,24 60,40 32,56" fill="white"/></svg></div>
    </div>
    <div class="game-info">
      <div class="game-title">斗地主</div>
      <div class="game-desc">经典三人纸牌对战游戏。你是农民还是地主？与 AI 斗智斗勇，争夺牌桌霸权。</div>
    </div>
  </a>

  <a class="game-card" id="zombie" href="打僵尸.html" target="_blank" rel="noopener">
    <div class="game-thumb">
      <div class="game-cover cover-zombie">
        <div class="cover-icon">🧟</div>
        <div class="cover-label">Shadow Strike</div>
        <div class="cover-sub">FPS · Survival</div>
      </div>
      <div class="play-overlay"><svg viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="40" fill="rgba(0,0,0,0.5)"/><polygon points="32,24 60,40 32,56" fill="white"/></svg></div>
    </div>
    <div class="game-info">
      <div class="game-title">打僵尸 · Shadow Strike FPS</div>
      <div class="game-desc">第一人称射击生存游戏。僵尸潮水涌来，弹药有限，能撑多久全靠你。</div>
    </div>
  </a>

</div>
</div>
