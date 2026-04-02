---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ───────────────────────────────────────────────
   FOUNDATIONS
   ─────────────────────────────────────────────── */
.splash .page__content {
  font-family: -apple-system, "SF Pro Display", "SF Pro Text", "Helvetica Neue", "Inter", "Segoe UI", sans-serif;
  max-width: none; padding: 0; margin: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #1d1d1f;
}
.splash .page__content p,
.splash .page__content h1,
.splash .page__content h2,
.splash .page__content h3 { margin: 0; }
.splash .page__content a { text-decoration: none; }

/* ───────────────────────────────────────────────
   LAYOUT — Apple-scale generous sections
   ─────────────────────────────────────────────── */
.sec {
  width: 100%;
  padding: clamp(3.5rem, 8vw, 6rem) clamp(1.5rem, 5vw, 4rem);
}
.sec-in {
  max-width: 980px;
  margin: 0 auto;
}

/* ───────────────────────────────────────────────
   HERO — bold, centered, Apple-scale
   ─────────────────────────────────────────────── */
.hero-sec {
  padding-top: clamp(3rem, 7vw, 5rem);
  padding-bottom: clamp(2.5rem, 6vw, 4.5rem);
  background: #fbfbfd;
  text-align: center;
}

/* Identity row — centered */
.hero-top {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.2rem;
  margin-bottom: 1.8rem;
}
.hero-photo {
  width: 88px; height: 88px;
  border-radius: 50%; object-fit: cover;
  border: 3px solid #fff;
  box-shadow: 0 4px 20px rgba(0,0,0,.10);
  flex-shrink: 0;
}
.hero-id { text-align: left; }
.hero-name {
  font-size: 1.8rem; font-weight: 700; color: #1d1d1f; line-height: 1.15;
  letter-spacing: -.02em;
}
.hero-aff {
  font-size: 1rem; color: #6e6e73; line-height: 1.4; margin-top: .15rem;
}
.hero-aff a { color: #06c; font-weight: 500; }
.hero-aff a:hover { text-decoration: underline; }

/* Announcement — inline badge */
.hero-news {
  display: inline-flex; align-items: baseline;
  gap: .3rem;
  padding: .5rem 1.1rem;
  border-radius: 980px;
  background: #e8f4f8;
  border: 1px solid #cde7ef;
  font-size: .88rem; line-height: 1.4;
  color: #1d1d1f;
  margin-bottom: 2.2rem;
}
@media (min-width: 860px) {
  .hero-news { white-space: nowrap; }
}
.hero-news strong { color: #17677a; font-weight: 700; }
.hero-news a { color: #06c; font-weight: 600; }
.hero-news a:hover { text-decoration: underline; }

/* Headline — LARGE, Apple-scale */
.hero-h {
  font-size: clamp(2rem, 4.5vw, 3.2rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -.025em;
  color: #1d1d1f;
  max-width: 800px;
  margin: 0 auto;
}

/* Subtitle */
.hero-desc {
  margin-top: 1rem;
  font-size: clamp(1.05rem, 1.6vw, 1.25rem);
  line-height: 1.5;
  color: #6e6e73;
  font-weight: 400;
}

/* Keywords — centered row of pills */
.hero-kw {
  display: flex; flex-wrap: wrap; gap: .5rem;
  justify-content: center;
  margin-top: 1.6rem;
}
.kw {
  padding: .35rem .85rem;
  border-radius: 980px;
  background: #f5f5f7;
  font-size: .88rem; font-weight: 500;
  color: #1d1d1f;
  letter-spacing: -.005em;
}

/* CTA buttons */
.hero-act {
  display: flex; flex-wrap: wrap; gap: .7rem;
  justify-content: center;
  margin-top: 2rem;
}
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  height: 3rem; padding: 0 1.8rem;
  border-radius: 980px;
  font-size: 1.05rem; font-weight: 600;
  cursor: pointer;
  text-decoration: none !important;
  transition: background .2s, box-shadow .2s, transform .15s;
  letter-spacing: -.005em;
}
.btn:hover { transform: scale(1.02); }
.btn-fill {
  background: #06c; color: #fff !important;
  box-shadow: 0 2px 12px rgba(0,102,204,.25);
}
.btn-fill:hover { background: #0055b3; box-shadow: 0 4px 20px rgba(0,102,204,.35); }
.btn-out {
  background: transparent;
  border: 1.5px solid #06c;
  color: #06c !important;
}
.btn-out:hover { background: rgba(0,102,204,.06); }

/* ───────────────────────────────────────────────
   SECTION HEADERS — large, left-aligned
   ─────────────────────────────────────────────── */
.sec-hdr {
  margin-bottom: clamp(1.8rem, 3.5vw, 2.8rem);
}
.sec-label {
  font-size: .82rem; font-weight: 600;
  letter-spacing: .06em; text-transform: uppercase;
  color: #6e6e73;
  margin-bottom: .45rem;
}
.sec-title {
  font-size: clamp(1.8rem, 3.5vw, 2.6rem);
  font-weight: 700; line-height: 1.08;
  letter-spacing: -.02em;
  color: #1d1d1f;
}
.sec-sub {
  margin-top: .5rem;
  font-size: clamp(1rem, 1.4vw, 1.15rem);
  line-height: 1.5;
  color: #6e6e73;
  max-width: 600px;
}

/* ───────────────────────────────────────────────
   RESEARCH AREAS — large cards, visual SVGs
   ─────────────────────────────────────────────── */
.area-bg { background: #fff; }

.areas {
  display: grid; gap: 1rem;
}
@media (min-width: 760px) {
  .areas { grid-template-columns: repeat(3, 1fr); }
}
.area {
  border-radius: 20px;
  overflow: hidden;
  display: flex; flex-direction: column;
  transition: box-shadow .3s ease, transform .3s ease;
  background: #fff;
  border: 1px solid rgba(0,0,0,.04);
}
.area:hover {
  box-shadow: 0 12px 40px rgba(0,0,0,.08);
  transform: translateY(-3px);
}

.area-vis {
  height: 180px;
  display: flex; align-items: center; justify-content: center;
  padding: 1.2rem;
}
.area-vis svg { width: 85%; height: 85%; }
.vis-teal  { background: linear-gradient(135deg, #e8f6fa 0%, #d4eef5 100%); }
.vis-amber { background: linear-gradient(135deg, #fef8ec 0%, #fdf0d5 100%); }
.vis-coral { background: linear-gradient(135deg, #fdf2ee 0%, #f9e4dc 100%); }

.area-body {
  padding: 1.4rem 1.5rem 1.6rem;
  display: flex; flex-direction: column; gap: .45rem; flex: 1;
}
.area-label {
  font-size: .76rem; font-weight: 700;
  letter-spacing: .06em; text-transform: uppercase;
}
.lbl-teal  { color: #17677a; }
.lbl-amber { color: #946b14; }
.lbl-coral { color: #a14430; }
.area h3 {
  font-size: 1.2rem; font-weight: 700; line-height: 1.2; color: #1d1d1f;
  letter-spacing: -.01em;
}
.area p {
  font-size: .95rem; line-height: 1.55; color: #6e6e73;
}
.area-tags {
  display: flex; flex-wrap: wrap; gap: .35rem;
  margin-top: auto; padding-top: .5rem;
}
.area-tags span {
  padding: .22rem .6rem; border-radius: 980px;
  background: #f5f5f7;
  font-size: .8rem; font-weight: 500; color: #424245;
}

/* ───────────────────────────────────────────────
   PIPELINE — dramatic dark section
   ─────────────────────────────────────────────── */
.pipe-bg {
  background: #1d1d1f; color: #f5f5f7;
}
.pipe-bg .sec-label { color: rgba(255,255,255,.35); }
.pipe-bg .sec-title { color: #f5f5f7; }

.pipe {
  display: grid; gap: .8rem;
}
@media (min-width: 760px) {
  .pipe { grid-template-columns: repeat(4, 1fr); }
}
.step {
  padding: 1.4rem 1.3rem;
  border-radius: 16px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.07);
  transition: background .3s ease;
}
.step:hover { background: rgba(255,255,255,.08); }
.step-n {
  font-size: .76rem; font-weight: 700;
  color: rgba(255,255,255,.25);
  margin-bottom: .7rem;
  letter-spacing: .04em;
}
.step h3 {
  font-size: 1.08rem; font-weight: 600;
  color: #f5f5f7; margin-bottom: .35rem;
  letter-spacing: -.005em;
}
.step p {
  font-size: .92rem; line-height: 1.55;
  color: rgba(255,255,255,.45);
}

/* ───────────────────────────────────────────────
   SELECTED PAPERS — clean cards
   ─────────────────────────────────────────────── */
.papers-bg { background: #f5f5f7; }

.papers {
  display: grid; gap: 1rem;
}
@media (min-width: 760px) {
  .papers { grid-template-columns: repeat(2, 1fr); }
}
.paper {
  padding: 1.5rem 1.6rem;
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(0,0,0,.04);
  display: flex; flex-direction: column; gap: .45rem;
  transition: box-shadow .3s ease, transform .3s ease;
}
.paper:hover {
  box-shadow: 0 10px 35px rgba(0,0,0,.07);
  transform: translateY(-2px);
}

.paper-tag {
  display: inline-flex; width: fit-content;
  padding: .2rem .65rem; border-radius: 980px;
  font-size: .74rem; font-weight: 700;
  letter-spacing: .04em; text-transform: uppercase;
}
.pt-teal  { background: #e8f4f8; color: #17677a; }
.pt-amber { background: #fef6e0; color: #946b14; }
.pt-coral { background: #fdf0ec; color: #a14430; }
.pt-green { background: #ecf5ef; color: #3a7049; }

.paper h3 {
  font-size: 1.15rem; font-weight: 700; line-height: 1.22; color: #1d1d1f;
  letter-spacing: -.01em;
}
.paper p {
  font-size: .94rem; line-height: 1.55; color: #6e6e73;
}
.paper-cites {
  display: flex; flex-wrap: wrap; gap: .4rem;
  margin-top: auto; padding-top: .35rem;
}
.cite {
  display: inline-flex; align-items: center;
  padding: .28rem .7rem; border-radius: 980px;
  background: #f5f5f7;
  color: #06c !important;
  font-size: .84rem; font-weight: 600;
  text-decoration: none !important;
  transition: background .2s, color .2s;
  letter-spacing: -.005em;
}
.cite:hover { background: #e2e2e7; }

/* ───────────────────────────────────────────────
   RECRUIT — compelling, centered CTA
   ─────────────────────────────────────────────── */
.recruit-bg {
  background: #fbfbfd;
}

.recruit-center { text-align: center; }
.recruit-center .sec-hdr { margin-bottom: clamp(1.2rem, 2.5vw, 2rem); }
.recruit-center .sec-title {
  max-width: none;
  font-size: clamp(1.8rem, 3.5vw, 2.6rem);
}
.recruit-center .sec-sub {
  max-width: none;
  margin-left: auto; margin-right: auto;
  font-size: clamp(.95rem, 1.3vw, 1.08rem);
}

.roles {
  display: grid; gap: .8rem;
  margin-top: 2.2rem; text-align: left;
}
@media (min-width: 760px) {
  .roles { grid-template-columns: repeat(4, 1fr); }
}
.role {
  padding: 1.4rem 1.3rem; border-radius: 18px;
  background: #fff;
  border: 1px solid rgba(0,0,0,.04);
  display: flex; flex-direction: column; gap: .4rem;
  transition: box-shadow .3s ease, transform .3s ease;
}
.role:hover {
  box-shadow: 0 8px 28px rgba(0,0,0,.06);
  transform: translateY(-2px);
}
.role h3 {
  font-size: 1.1rem; font-weight: 700; color: #1d1d1f;
  letter-spacing: -.01em;
}
.role p {
  font-size: .92rem; line-height: 1.5; color: #6e6e73;
}

.recruit-cta { margin-top: 2rem; }
.recruit-links {
  display: flex; justify-content: center; flex-wrap: wrap;
  gap: .3rem 1.2rem;
  margin-top: .8rem;
}
.recruit-links a {
  font-size: .92rem; font-weight: 500;
  color: #06c !important; text-decoration: none !important;
}
.recruit-links a:hover { text-decoration: underline !important; }
</style>

<!-- ═══════════ HERO ═══════════ -->
<section class="sec hero-sec">
<div class="sec-in">

  <div class="hero-top">
    <img class="hero-photo" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div class="hero-id">
      <div class="hero-name">Yuwen Huang</div>
      <div class="hero-aff">Postdoctoral Researcher, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></div>
    </div>
  </div>

  <div class="hero-news">
    <strong>Fall 2026</strong> — Joining
    <a href="https://www.hkust-gz.edu.cn/">HKUST (Guangzhou)</a>
    as Assistant Professor
    (<a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>,
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>)
  </div>

  <h1 class="hero-h">Provable methods for structured<br>inference and optimization</h1>

  <p class="hero-desc">
    Graphical models · Combinatorics · Tensor networks · Quantum systems · Machine learning
  </p>

  <div class="hero-kw">
    <span class="kw">Bethe methods &amp; graph covers</span>
    <span class="kw">Combinatorial inference</span>
    <span class="kw">Tensor networks</span>
    <span class="kw">Quantum systems</span>
  </div>

  <div class="hero-act">
    <a class="btn btn-fill" href="#positions">Open positions</a>
    <a class="btn btn-out" href="#research">Selected research</a>
  </div>

</div>
</section>

<!-- ═══════════ RESEARCH AREAS ═══════════ -->
<section class="sec area-bg">
<div class="sec-in">
  <div class="sec-hdr">
    <div class="sec-label">Research</div>
    <h2 class="sec-title">Three core areas</h2>
    <p class="sec-sub">From mathematical structure to scalable computation.</p>
  </div>

  <div class="areas">

    <article class="area">
      <div class="area-vis vis-teal">
        <svg viewBox="0 0 280 140" fill="none" aria-label="Graphical model">
          <line x1="58" y1="48" x2="125" y2="34" stroke="#a8d5e0" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="58" y1="48" x2="110" y2="105" stroke="#a8d5e0" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="125" y1="34" x2="195" y2="60" stroke="#a8d5e0" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="110" y1="105" x2="195" y2="60" stroke="#a8d5e0" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="195" y1="60" x2="240" y2="48" stroke="#a8d5e0" stroke-width="3.5" stroke-linecap="round"/>
          <circle cx="58" cy="48" r="16" fill="#2a8a9e"/>
          <circle cx="125" cy="34" r="13" fill="#2a8a9e"/>
          <circle cx="110" cy="105" r="13" fill="#5bb3c5"/>
          <circle cx="195" cy="60" r="15" fill="#2a8a9e"/>
          <circle cx="240" cy="48" r="12" fill="#5bb3c5"/>
          <text x="58" y="53" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">x&#x2081;</text>
          <text x="125" y="39" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">x&#x2082;</text>
          <text x="195" y="65" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">x&#x2083;</text>
        </svg>
      </div>
      <div class="area-body">
        <div class="area-label lbl-teal">Inference</div>
        <h3>Structured graphical-model reasoning</h3>
        <p>Message passing, Bethe methods, and combinatorial structure for reliable inference and counting.</p>
        <div class="area-tags"><span>Uncertainty</span><span>Counting</span><span>Graph covers</span></div>
      </div>
    </article>

    <article class="area">
      <div class="area-vis vis-amber">
        <svg viewBox="0 0 280 140" fill="none" aria-label="Optimization landscape">
          <path d="M28 100 C55 78,75 28,115 28 C155 28,170 92,210 92 C238 92,255 68,268 42" stroke="#d9b14f" stroke-width="4" stroke-linecap="round"/>
          <circle cx="115" cy="28" r="10" fill="#946b14"/>
          <circle cx="210" cy="92" r="10" fill="#946b14"/>
          <line x1="40" y1="120" x2="255" y2="120" stroke="#e8d5a0" stroke-width="2.5" stroke-linecap="round"/>
          <rect x="48" y="12" width="52" height="22" rx="8" fill="#fef6e0" stroke="#e8d5a0" stroke-width="1.5"/>
          <text x="74" y="28" text-anchor="middle" fill="#946b14" font-size="10" font-weight="700">Bounds</text>
          <rect x="200" y="12" width="65" height="22" rx="8" fill="#fef6e0" stroke="#e8d5a0" stroke-width="1.5"/>
          <text x="232" y="28" text-anchor="middle" fill="#946b14" font-size="10" font-weight="700">Algorithms</text>
        </svg>
      </div>
      <div class="area-body">
        <div class="area-label lbl-amber">Optimization</div>
        <h3>Provable optimization and decision-making</h3>
        <p>Structure-aware objectives, permanent bounds, and algorithmic guarantees for hard problems.</p>
        <div class="area-tags"><span>Convex / nonconvex</span><span>Permanent bounds</span><span>Decisions</span></div>
      </div>
    </article>

    <article class="area">
      <div class="area-vis vis-coral">
        <svg viewBox="0 0 280 140" fill="none" aria-label="Tensor network">
          <line x1="68" y1="52" x2="102" y2="52" stroke="#d4836e" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="138" y1="52" x2="172" y2="52" stroke="#d4836e" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="208" y1="52" x2="242" y2="52" stroke="#d4836e" stroke-width="3.5" stroke-linecap="round"/>
          <rect x="32" y="36" width="36" height="32" rx="9" fill="#e49886"/>
          <rect x="102" y="36" width="36" height="32" rx="9" fill="#e49886"/>
          <rect x="172" y="36" width="36" height="32" rx="9" fill="#e49886"/>
          <rect x="242" y="36" width="36" height="32" rx="9" fill="#e49886"/>
          <line x1="50" y1="36" x2="50" y2="18" stroke="#d4836e" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="120" y1="36" x2="120" y2="18" stroke="#d4836e" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="190" y1="36" x2="190" y2="18" stroke="#d4836e" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="260" y1="36" x2="260" y2="18" stroke="#d4836e" stroke-width="2.5" stroke-linecap="round"/>
          <ellipse cx="155" cy="108" rx="55" ry="14" stroke="#86b894" stroke-width="2" stroke-dasharray="5 4" fill="none"/>
          <circle cx="155" cy="108" r="9" fill="#4f8b62"/>
          <circle cx="208" cy="105" r="6" fill="#86b894"/>
          <circle cx="102" cy="105" r="6" fill="#86b894"/>
        </svg>
      </div>
      <div class="area-body">
        <div class="area-label lbl-coral">Quantum &amp; Tensors</div>
        <h3>High-dimensional quantum computation</h3>
        <p>Tensor-network representations and distributed quantum systems for scalable computation.</p>
        <div class="area-tags"><span>Tensor networks</span><span>Quantum systems</span><span>Scalability</span></div>
      </div>
    </article>

  </div>
</div>
</section>

<!-- ═══════════ PIPELINE ═══════════ -->
<section class="sec pipe-bg">
<div class="sec-in">
  <div class="sec-hdr">
    <div class="sec-label">From theory to impact</div>
    <h2 class="sec-title">Structure becomes computation</h2>
  </div>
  <div class="pipe">
    <div class="step"><div class="step-n">01</div><h3>Information theory &amp; statistical physics</h3><p>Structure, correlation, and entropy motivate the underlying questions.</p></div>
    <div class="step"><div class="step-n">02</div><h3>Inference, counting, optimization</h3><p>Bethe methods, graph covers, and structure-aware optimization.</p></div>
    <div class="step"><div class="step-n">03</div><h3>Distributed quantum systems</h3><p>Quantum networks extending the computational regime.</p></div>
    <div class="step"><div class="step-n">04</div><h3>ML &amp; efficient computation</h3><p>Learning theory, analytics, and large-scale decision making.</p></div>
  </div>
</div>
</section>

<!-- ═══════════ SELECTED RESEARCH ═══════════ -->
<section class="sec papers-bg" id="research">
<div class="sec-in">
  <div class="sec-hdr">
    <div class="sec-label">Selected research</div>
    <h2 class="sec-title">Representative papers</h2>
  </div>
  <div class="papers">

    <article class="paper">
      <span class="paper-tag pt-teal">Inference</span>
      <h3>Graphical models and Bethe methods</h3>
      <p>Bethe approximations, graph covers, and message passing for principled inference and counting.</p>
      <div class="paper-cites">
        <a class="cite" href="{{ '/publication/characterizing-bethe-partition-factor-graphs' | relative_url }}">[ISIT 2020]</a>
        <a class="cite" href="{{ '/publication/bethe-free-energy-global-minimum' | relative_url }}">[ITW 2022]</a>
        <a class="cite" href="{{ '/publication/bethe-partition-spa-stable-polynomials' | relative_url }}">[ISIT 2024]</a>
        <a class="cite" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-sub]</a>
      </div>
    </article>

    <article class="paper">
      <span class="paper-tag pt-amber">Optimization</span>
      <h3>Optimization and combinatorial structure</h3>
      <p>Structure-exploiting optimization and permanent bounds with rigorous guarantees.</p>
      <div class="paper-cites">
        <a class="cite" href="{{ '/publication/bounding-permanent-degree-m-bethe' | relative_url }}">[ISIT 2023]</a>
        <a class="cite" href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">[TIT 2024]</a>
        <a class="cite" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML 2025]</a>
      </div>
    </article>

    <article class="paper">
      <span class="paper-tag pt-coral">Tensor methods</span>
      <h3>Tensor networks and quantum-enabled inference</h3>
      <p>Compact high-dimensional computation via tensor-network representations.</p>
      <div class="paper-cites">
        <a class="cite" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT 2021]</a>
        <a class="cite" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
      </div>
    </article>

    <article class="paper">
      <span class="paper-tag pt-green">Quantum systems</span>
      <h3>Distributed quantum systems</h3>
      <p>Distributed quantum architectures for optimization, inference, and analytics.</p>
      <div class="paper-cites">
        <a class="cite" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML 2025]</a>
        <a class="cite" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
      </div>
    </article>

  </div>
</div>
</section>

<!-- ═══════════ OPEN POSITIONS ═══════════ -->
<section class="sec recruit-bg" id="positions">
<div class="sec-in recruit-center">
  <div class="sec-hdr">
    <div class="sec-label">Open positions</div>
    <h2 class="sec-title">Join the group</h2>
    <p class="sec-sub">Recruiting RAs, MPhil/PhD students, and one Postdoc for Fall 2026 at the DSA Thrust, Information Hub, HKUST (Guangzhou).</p>
  </div>
  <div class="roles">
    <div class="role"><h3>RA</h3><p>Core research training and preparation for graduate study or industry roles.</p></div>
    <div class="role"><h3>MPhil</h3><p>Structured transition into independent research with publication-minded training.</p></div>
    <div class="role"><h3>PhD</h3><p>Ownership of deeper problems, broad collaboration, and long-term research support.</p></div>
    <div class="role"><h3>Postdoc</h3><p>Shape an agenda, co-mentor students, and prepare for academic searches.</p></div>
  </div>
  <div class="recruit-cta">
    <a class="btn btn-fill" href="mailto:{{ site.author.email }}">Apply by email</a>
  </div>
  <div class="recruit-links">
    <a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
    <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
  </div>
</div>
</section>
