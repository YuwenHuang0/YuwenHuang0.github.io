---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ══════════════════════════════════════════════════
   RESET — kill all theme defaults in splash
   ══════════════════════════════════════════════════ */
.splash .page__content {
  font-family: -apple-system, "SF Pro Display", "SF Pro Text", "Helvetica Neue", "Inter", "Segoe UI", sans-serif;
  max-width: none !important; padding: 0 !important; margin: 0 !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.splash .page__content p,
.splash .page__content h1,
.splash .page__content h2,
.splash .page__content h3,
.splash .page__content h4 {
  margin: 0 !important; padding: 0 !important; border: none !important;
}
.splash .page__content a { text-decoration: none; }

/* ══════════════════════════════════════════════════
   DESIGN TOKENS — Light theme
   ══════════════════════════════════════════════════ */
:root {
  --bg-white: #ffffff;
  --bg-snow: #f8f8fa;
  --bg-warm: #f2f0ed;
  --text-black: #111111;
  --text-body: #333333;
  --text-muted: #666666;
  --text-light: #999999;
  --accent: #7c3aed;
  --accent-light: #ede9fe;
  --accent-hover: #6d28d9;
  --accent-bg: rgba(124,58,237,.06);
  --border: rgba(0,0,0,.08);
  --border-hover: rgba(0,0,0,.15);
  --radius: 12px;
  --transition: .2s cubic-bezier(.4,0,.2,1);
}

/* ══════════════════════════════════════════════════
   SECTION SYSTEM
   ══════════════════════════════════════════════════ */
.sec {
  width: 100%;
  padding: clamp(2rem, 4vw, 3.5rem) clamp(1.5rem, 5vw, 6rem);
}
.sec-in {
  max-width: 960px;
  width: 100%;
  margin: 0 auto;
}

/* Section backgrounds */
.s-white { background: var(--bg-white); }
.s-snow { background: var(--bg-snow); }
.s-warm { background: var(--bg-warm); }
.s-accent { background: var(--accent); }

/* Force black text everywhere on splash */
.s-white h2, .s-white h3, .s-white p, .s-white div, .s-white span,
.s-snow h2, .s-snow h3, .s-snow p, .s-snow div, .s-snow span,
.s-warm h2, .s-warm h3, .s-warm p, .s-warm div, .s-warm span {
  color: var(--text-black);
}

/* ══════════════════════════════════════════════════
   SECTION HEADERS
   ══════════════════════════════════════════════════ */
.label {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent) !important;
  margin-bottom: .4rem;
}
.heading {
  font-size: clamp(1.5rem, 3vw, 2.2rem) !important;
  font-weight: 700 !important;
  letter-spacing: -.03em;
  line-height: 1.1;
  color: var(--text-black) !important;
}
.subtext {
  margin-top: .4rem;
  font-size: .95rem;
  line-height: 1.5;
  color: var(--text-muted) !important;
}

/* ══════════════════════════════════════════════════
   HERO
   ══════════════════════════════════════════════════ */
.hero {
  padding-top: clamp(2.5rem, 6vw, 5rem);
  padding-bottom: clamp(2rem, 4vw, 3.5rem);
  text-align: center;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: "";
  position: absolute;
  top: -40%; left: 50%; transform: translateX(-50%);
  width: 800px; height: 500px;
  background: radial-gradient(ellipse, rgba(124,58,237,.05) 0%, transparent 70%);
  pointer-events: none;
}
.hero .sec-in {
  position: relative; z-index: 1;
  display: flex; flex-direction: column; align-items: center;
}

.hero-id {
  display: flex; align-items: center; gap: .8rem;
  margin-bottom: 1.5rem;
}
.hero-photo {
  width: 60px; height: 60px;
  border-radius: 50%; object-fit: cover;
  border: 2px solid rgba(0,0,0,.08);
  box-shadow: 0 2px 12px rgba(0,0,0,.08);
}
.hero-meta { text-align: left; }
.hero-name {
  font-size: 1.15rem; font-weight: 700;
  color: var(--text-black) !important;
}
.hero-aff {
  font-size: .85rem;
  color: var(--text-muted) !important;
  margin-top: .05rem;
}
.hero-aff a { color: var(--text-muted) !important; font-weight: 500; transition: color var(--transition); }
.hero-aff a:hover { color: var(--accent) !important; }

.hero-tagline {
  font-size: clamp(1.1rem, 2vw, 1.35rem);
  font-weight: 400;
  line-height: 1.5;
  color: var(--text-body) !important;
  max-width: 560px;
}

.hero-announcement {
  display: inline-flex; align-items: center;
  gap: .4rem;
  margin-top: 1.2rem;
  padding: .4rem 1rem;
  border-radius: 980px;
  background: var(--accent-light);
  border: 1px solid rgba(124,58,237,.15);
  font-size: .82rem;
  color: var(--accent) !important;
  font-weight: 600;
}
.hero-announcement strong { color: var(--accent) !important; }
.hero-announcement a {
  color: var(--accent) !important;
  font-weight: 600;
  text-decoration: underline !important;
  text-underline-offset: 2px;
}

.hero-cta {
  display: flex; gap: .5rem;
  margin-top: 1.5rem;
}

/* Buttons */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  height: 2.5rem; padding: 0 1.4rem;
  border-radius: 980px;
  font-size: .88rem; font-weight: 600;
  cursor: pointer;
  text-decoration: none !important;
  transition: all var(--transition);
}
.btn-primary {
  background: var(--text-black);
  color: #fff !important;
}
.splash .page__content .btn-primary,
.splash .page__content .btn-primary:hover {
  color: #fff !important;
  text-decoration: none !important;
}
.btn-primary:hover {
  background: #000;
  box-shadow: 0 4px 16px rgba(0,0,0,.15);
  transform: translateY(-1px);
}
.btn-secondary {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-body) !important;
}
.splash .page__content .btn-secondary,
.splash .page__content .btn-secondary:hover {
  color: var(--text-body) !important;
  text-decoration: none !important;
}
.btn-secondary:hover {
  border-color: var(--border-hover);
  background: rgba(0,0,0,.02);
}

/* ══════════════════════════════════════════════════
   RESEARCH AREAS — cards
   ══════════════════════════════════════════════════ */
.cards {
  display: grid;
  gap: .8rem;
  margin-top: 1.2rem;
}
@media (min-width: 700px) {
  .cards { grid-template-columns: repeat(3, 1fr); }
}
.card {
  padding: 1.2rem;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  background: #fff;
  transition: border-color var(--transition), box-shadow var(--transition);
}
.card:hover {
  border-color: var(--border-hover);
  box-shadow: 0 4px 16px rgba(0,0,0,.06);
}
.card-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-black) !important;
  letter-spacing: -.01em;
}
.card-desc {
  font-size: .85rem;
  line-height: 1.5;
  color: var(--text-muted) !important;
  margin-top: .25rem;
}
.card-tags {
  margin-top: .5rem;
  font-size: .75rem;
  color: var(--text-light) !important;
}

/* ══════════════════════════════════════════════════
   SELECTED WORK — featured + grid
   ══════════════════════════════════════════════════ */
.featured {
  margin-top: 1rem;
  padding: 1.2rem;
  border-radius: var(--radius);
  background: var(--accent-bg);
  border: 1px solid rgba(124,58,237,.1);
}
.feat-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-black) !important;
}
.feat-desc {
  font-size: .85rem;
  line-height: 1.5;
  color: var(--text-muted) !important;
  margin-top: .2rem;
}
.cites {
  display: flex; flex-wrap: wrap;
  gap: .25rem;
  margin-top: .5rem;
}
.cite {
  display: inline-flex; align-items: center;
  padding: .2rem .5rem;
  border-radius: 6px;
  background: #fff;
  border: 1px solid var(--border);
  color: var(--text-body) !important;
  font-size: .72rem;
  font-weight: 500;
  font-family: "SF Mono", "Fira Code", monospace;
  text-decoration: none !important;
  transition: all var(--transition);
}
.cite:hover {
  background: var(--accent-light);
  border-color: rgba(124,58,237,.2);
  color: var(--accent) !important;
}

.sub-grid {
  display: grid; gap: .8rem;
  margin-top: .8rem;
}
@media (min-width: 700px) {
  .sub-grid { grid-template-columns: repeat(3, 1fr); }
}
.sub-title {
  font-size: .9rem; font-weight: 700;
  color: var(--text-black) !important;
}
.sub-desc {
  font-size: .78rem; line-height: 1.4;
  color: var(--text-light) !important;
  margin-top: .1rem;
}

.view-all {
  margin-top: 1rem; text-align: center;
}
.view-all a {
  font-size: .85rem; font-weight: 500;
  color: var(--accent) !important;
  text-decoration: none !important;
  transition: color var(--transition);
}
.view-all a:hover { color: var(--accent-hover) !important; }
.view-all a::after { content: " →"; }

/* ══════════════════════════════════════════════════
   UPDATES — clean rows
   ══════════════════════════════════════════════════ */
.timeline {
  margin-top: .8rem;
}
.tl-row {
  display: flex;
  gap: 1.2rem;
  padding: .5rem 0;
  border-bottom: 1px solid var(--border);
  align-items: baseline;
}
.tl-row:first-child { border-top: 1px solid var(--border); }
.tl-date {
  font-size: .75rem; font-weight: 600;
  color: var(--text-light);
  min-width: 72px; flex-shrink: 0;
  font-family: "SF Mono", "Fira Code", monospace;
}
.tl-title {
  font-size: .88rem; font-weight: 600;
  color: var(--text-black) !important;
  line-height: 1.3;
}
.tl-title a { color: var(--text-black) !important; text-decoration: none !important; transition: color var(--transition); }
.tl-title a:hover { color: var(--accent) !important; }
.tl-venue {
  font-size: .75rem;
  color: var(--text-muted);
  margin-top: .05rem;
}
.tl-badge {
  display: inline-flex;
  padding: .1rem .4rem;
  border-radius: 4px;
  font-size: .6rem; font-weight: 700;
  letter-spacing: .03em; text-transform: uppercase;
  background: var(--accent-light);
  color: var(--accent);
  margin-left: .3rem; vertical-align: middle;
}

/* ══════════════════════════════════════════════════
   JOIN — accent-highlighted section
   ══════════════════════════════════════════════════ */
.join {
  text-align: center;
  position: relative;
  overflow: hidden;
}
.join .sec-in {
  position: relative; z-index: 1;
  display: flex; flex-direction: column; align-items: center;
}
/* Force white text in accent section */
.s-accent h2, .s-accent p, .s-accent div, .s-accent span {
  color: #fff;
}
.join-heading {
  font-size: clamp(1.8rem, 4vw, 2.8rem) !important;
  font-weight: 700 !important;
  letter-spacing: -.035em;
  color: #fff !important;
  line-height: 1.05;
}
.join-sub {
  margin-top: .5rem;
  font-size: .95rem;
  color: rgba(255,255,255,.85) !important;
  line-height: 1.5;
}

.perks {
  display: grid; gap: .3rem;
  margin-top: 1rem;
  text-align: left;
  max-width: 440px; width: 100%;
}
.perk {
  display: flex; align-items: baseline; gap: .4rem;
  font-size: .86rem; line-height: 1.35;
  color: rgba(255,255,255,.92) !important;
}
.perk::before {
  content: "";
  width: 5px; height: 5px;
  border-radius: 50%;
  background: #fff;
  flex-shrink: 0;
  margin-top: .4em;
}

.roles {
  display: flex; gap: .3rem;
  justify-content: center;
  margin-top: 1rem;
}
.role {
  padding: .25rem .75rem;
  border-radius: 6px;
  background: rgba(255,255,255,.18);
  border: 1px solid rgba(255,255,255,.25);
  font-size: .78rem; font-weight: 600;
  color: #fff !important;
}

.join-cta { margin-top: 1.2rem; }
.btn-accent {
  background: #fff;
  color: var(--accent) !important;
  font-weight: 700;
}
.splash .page__content .btn-accent,
.splash .page__content .btn-accent:hover {
  color: var(--accent) !important;
  text-decoration: none !important;
}
.btn-accent:hover {
  background: #f0f0f0;
  box-shadow: 0 4px 24px rgba(0,0,0,.15);
  transform: translateY(-1px);
}

.join-links {
  display: flex; gap: .8rem;
  margin-top: .8rem;
}
.join-links a {
  font-size: .78rem; font-weight: 500;
  color: rgba(255,255,255,.7) !important;
  text-decoration: none !important;
  transition: color var(--transition);
}
.join-links a:hover { color: #fff !important; }

/* ══════════════════════════════════════════════════
   RESPONSIVE
   ══════════════════════════════════════════════════ */
@media (max-width: 700px) {
  .sec { padding: 1.5rem 1rem; }
  .hero-id { flex-direction: column; text-align: center; }
  .hero-meta { text-align: center; }
  .tl-row { flex-direction: column; gap: .1rem; }
  .tl-date { min-width: auto; }
}

/* Skip nav */
.skip-nav {
  position: absolute; top: -100%;
  left: 50%; transform: translateX(-50%);
  padding: .5rem 1.2rem; border-radius: 980px;
  background: var(--accent); color: #fff !important;
  font-size: .82rem; font-weight: 600;
  text-decoration: none !important; z-index: 9999;
}
.skip-nav:focus { top: .8rem; }
</style>

<a class="skip-nav" href="#research">Skip to research</a>

<!-- ════ HERO ════ -->
<section class="sec s-white hero" aria-label="Introduction">
<div class="sec-in">

  <div class="hero-id">
    <img class="hero-photo" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div class="hero-meta">
      <div class="hero-name">Yuwen Huang</div>
      <div class="hero-aff">Postdoc, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></div>
    </div>
  </div>

  <p class="hero-tagline">Provable algorithms for inference, optimization, and quantum computation.</p>

  <div class="hero-announcement">
    <strong>May 2026</strong> — Joining <a href="https://www.hkust-gz.edu.cn/">HKUST (Guangzhou)</a> as Assistant Professor
  </div>

  <div class="hero-cta">
    <a class="btn btn-primary" href="#positions">Open positions</a>
    <a class="btn btn-secondary" href="#research">Research</a>
  </div>

</div>
</section>

<!-- ════ RESEARCH ════ -->
<section class="sec s-snow" aria-label="Research areas">
<div class="sec-in">
  <div class="label">Research</div>
  <h2 class="heading">Three core areas</h2>
  <div class="cards">
    <div class="card">
      <div class="card-title">Structured inference</div>
      <div class="card-desc">Bethe methods, graph covers, and message passing for counting and inference on graphical models.</div>
      <div class="card-tags">Uncertainty · Counting · Graph covers</div>
    </div>
    <div class="card">
      <div class="card-title">Provable optimization</div>
      <div class="card-desc">Permanent bounds and algorithmic guarantees for hard combinatorial problems.</div>
      <div class="card-tags">Convex / nonconvex · Permanent bounds</div>
    </div>
    <div class="card">
      <div class="card-title">Quantum &amp; tensors</div>
      <div class="card-desc">Tensor networks and distributed quantum systems for scalable computation.</div>
      <div class="card-tags">Tensor networks · Quantum systems</div>
    </div>
  </div>
</div>
</section>

<!-- ════ SELECTED WORK ════ -->
<section class="sec s-white" id="research" aria-label="Selected work">
<div class="sec-in">
  <div class="label">Selected work</div>
  <h2 class="heading">Representative papers</h2>
  <div class="featured">
    <div class="feat-title">Graphical models and Bethe methods</div>
    <div class="feat-desc">Graph covers and Bethe approximation for inference and counting — our longest-running thread.</div>
    <div class="cites">
      <a class="cite" href="https://ieeexplore.ieee.org/document/9174508/">ISIT'20</a>
      <a class="cite" href="https://arxiv.org/abs/2107.01816">ISIT'21</a>
      <a class="cite" href="https://ieeexplore.ieee.org/document/9965874/">ITW'22</a>
      <a class="cite" href="https://arxiv.org/abs/2306.02280">ISIT'23</a>
      <a class="cite" href="https://ieeexplore.ieee.org/document/10619603/">ISIT'24</a>
      <a class="cite" href="https://arxiv.org/abs/2306.02280">TIT'24</a>
      <a class="cite" href="https://arxiv.org/abs/2506.16250">TIT-sub</a>
    </div>
  </div>
  <div class="sub-grid">
    <div>
      <div class="sub-title">Tensor methods</div>
      <div class="sub-desc">Tensor-network methods for high-dimensional computation.</div>
      <div class="cites">
        <a class="cite" href="https://arxiv.org/abs/2107.01816">ISIT'21</a>
        <a class="cite" href="https://arxiv.org/abs/2506.16250">TIT-sub</a>
        <a class="cite" href="https://arxiv.org/abs/2508.05712">ICML'25</a>
        <a class="cite" href="https://arxiv.org/abs/2603.07673">Q-sub</a>
      </div>
    </div>
    <div>
      <div class="sub-title">Optimization</div>
      <div class="sub-desc">Permanent bounds for hard problems.</div>
      <div class="cites">
        <a class="cite" href="https://arxiv.org/abs/2306.02280">ISIT'23</a>
        <a class="cite" href="https://arxiv.org/abs/2306.02280">TIT'24</a>
        <a class="cite" href="https://arxiv.org/abs/2508.05712">ICML'25</a>
      </div>
    </div>
    <div>
      <div class="sub-title">Quantum systems</div>
      <div class="sub-desc">Distributed quantum optimization.</div>
      <div class="cites">
        <a class="cite" href="https://arxiv.org/abs/2603.07673">Q-sub</a>
      </div>
    </div>
  </div>
  <div class="view-all"><a href="{{ '/publications/' | relative_url }}">All publications</a></div>
</div>
</section>

<!-- ════ UPDATES ════ -->
<section class="sec s-snow" aria-label="Latest updates">
<div class="sec-in">
  <div class="label">Latest</div>
  <h2 class="heading">What's new</h2>
  <div class="timeline">
    <div class="tl-row">
      <div class="tl-date">May 2026</div>
      <div><div class="tl-title">Joining HKUST (GZ) as Assistant Professor <span class="tl-badge">Starting</span></div><div class="tl-venue">DSA Thrust, Information Hub</div></div>
    </div>
    <div class="tl-row">
      <div class="tl-date">Mar 2026</div>
      <div><div class="tl-title"><a href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">Scalable Distributed Quantum Optimization</a></div><div class="tl-venue">Submitted to Quantum</div></div>
    </div>
    <div class="tl-row">
      <div class="tl-date">Jul 2025</div>
      <div><div class="tl-title"><a href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">Graph-Cover-based Bethe Partition Function</a></div><div class="tl-venue">Submitted to IEEE TIT</div></div>
    </div>
    <div class="tl-row">
      <div class="tl-date">2024</div>
      <div><div class="tl-title"><a href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">Degree-M Bethe &amp; Sinkhorn Permanent</a></div><div class="tl-venue">Published in IEEE TIT</div></div>
    </div>
  </div>
</div>
</section>

<!-- ════ JOIN ════ -->
<section class="sec s-accent join" id="positions" aria-label="Open positions">
<div class="sec-in">
  <div class="label" style="color: rgba(255,255,255,.7) !important;">Open positions</div>
  <h2 class="join-heading">Join the group</h2>
  <p class="join-sub">Building a team at HKUST (Guangzhou) starting May 2026.</p>

  <div class="perks">
    <div class="perk">Full tuition and competitive stipend</div>
    <div class="perk">Mentorship targeting IEEE TIT, ISIT, ICML</div>
    <div class="perk">Greater Bay Area research ecosystem</div>
    <div class="perk">Small group, close advising</div>
  </div>

  <div class="roles">
    <span class="role">RA</span>
    <span class="role">MPhil</span>
    <span class="role">PhD</span>
    <span class="role">Postdoc</span>
  </div>

  <div class="join-cta">
    <a class="btn btn-accent" href="mailto:{{ site.author.email }}">Get in touch</a>
  </div>

  <div class="join-links">
    <a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Info Hub</a>
    <a href="https://www.hkust-gz.edu.cn/">HKUST GZ</a>
  </div>
</div>
</section>
