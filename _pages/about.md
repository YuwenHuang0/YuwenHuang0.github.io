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
  font-family: -apple-system, "SF Pro Text", "Helvetica Neue", "Inter", "Segoe UI", sans-serif;
  max-width: none; padding: 0; margin: 0;
  -webkit-font-smoothing: antialiased;
  color: #1d1d1f;
}
.splash .page__content p,
.splash .page__content h1,
.splash .page__content h2,
.splash .page__content h3 { margin: 0; }
.splash .page__content a { text-decoration: none; }

/* ───────────────────────────────────────────────
   LAYOUT
   ─────────────────────────────────────────────── */
.sec {
  width: 100%;
  padding: clamp(2.4rem, 5vw, 4rem) clamp(1.5rem, 4vw, 3rem);
}
.sec-in {
  max-width: 980px;
  margin: 0 auto;
}

/* ───────────────────────────────────────────────
   HERO — photo, bio, headline, announcement
   ─────────────────────────────────────────────── */
.hero-sec {
  padding-top: clamp(2.4rem, 5vw, 3.6rem);
  padding-bottom: clamp(1.8rem, 4vw, 3rem);
  background: #fbfbfd;
}

/* Row: photo + identity */
.hero-top {
  display: flex;
  align-items: center;
  gap: 1.3rem;
  margin-bottom: 1.5rem;
}
.hero-photo {
  width: 80px; height: 80px;
  border-radius: 50%; object-fit: cover;
  border: 3px solid #fff;
  box-shadow: 0 2px 12px rgba(0,0,0,.08);
  flex-shrink: 0;
}
.hero-name {
  font-size: 1.65rem; font-weight: 700; color: #1d1d1f; line-height: 1.2;
}
.hero-aff {
  font-size: 1.05rem; color: #6e6e73; line-height: 1.4; margin-top: .2rem;
}
.hero-aff a { color: #06c; font-weight: 500; }
.hero-aff a:hover { text-decoration: underline; }

/* Announcement strip */
.hero-news {
  display: inline-flex; align-items: baseline; flex-wrap: wrap;
  gap: .35rem;
  padding: .55rem 1rem;
  border-radius: 10px;
  background: #f0f6f8;
  border: 1px solid #d9e8ed;
  font-size: .96rem; line-height: 1.45;
  color: #1d1d1f;
  margin-bottom: 1.8rem;
}
.hero-news strong { color: #17677a; font-weight: 700; }
.hero-news a { color: #06c; font-weight: 600; }
.hero-news a:hover { text-decoration: underline; }

/* Headline — fits on one line at desktop (980px container) */
.hero-h {
  font-size: clamp(1.28rem, 2.5vw, 1.85rem);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -.01em;
  color: #1d1d1f;
}
@media (min-width: 760px) {
  .hero-h { white-space: nowrap; }
}

/* Description */
.hero-desc {
  margin-top: .8rem;
  font-size: clamp(1.05rem, 1.5vw, 1.18rem);
  line-height: 1.65;
  color: #424245;
  max-width: 640px;
}

/* Keywords */
.hero-kw {
  display: flex; flex-wrap: wrap; gap: .45rem;
  margin-top: 1.1rem;
}
.kw {
  padding: .32rem .78rem;
  border-radius: 8px;
  background: #f5f5f7;
  font-size: .9rem; font-weight: 500;
  color: #1d1d1f;
}

/* Actions */
.hero-act {
  display: flex; flex-wrap: wrap; gap: .7rem;
  margin-top: 1.4rem;
}
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  height: 2.75rem; padding: 0 1.5rem;
  border-radius: 980px;
  font-size: 1rem; font-weight: 600;
  cursor: pointer;
  text-decoration: none !important;
  transition: background .2s, box-shadow .2s;
}
.btn-fill {
  background: #06c; color: #fff !important;
}
.btn-fill:hover { background: #0055b3; }
.btn-out {
  background: transparent;
  border: 1px solid #06c;
  color: #06c !important;
}
.btn-out:hover { background: rgba(0,102,204,.06); }

/* ───────────────────────────────────────────────
   SECTION HEADER — left-aligned, compact
   ─────────────────────────────────────────────── */
.sec-hdr {
  margin-bottom: clamp(1.4rem, 2.5vw, 2rem);
}
.sec-label {
  font-size: .82rem; font-weight: 600;
  letter-spacing: .04em; text-transform: uppercase;
  color: #6e6e73;
  margin-bottom: .3rem;
}
.sec-title {
  font-size: clamp(1.35rem, 2.6vw, 1.85rem);
  font-weight: 700; line-height: 1.12;
  letter-spacing: -.015em;
  color: #1d1d1f;
}
@media (min-width: 760px) {
  .sec-title { white-space: nowrap; }
}
.sec-sub {
  margin-top: .4rem;
  font-size: 1.02rem; line-height: 1.55;
  color: #6e6e73;
  max-width: none;
}
@media (min-width: 760px) {
  .sec-sub { white-space: nowrap; }
}

/* ───────────────────────────────────────────────
   RESEARCH AREA CARDS — full-bleed tinted panels
   ─────────────────────────────────────────────── */
.area-bg { background: #fff; }

.areas {
  display: grid; gap: .8rem;
}
@media (min-width: 760px) {
  .areas { grid-template-columns: repeat(3, 1fr); }
}
.area {
  border-radius: 18px;
  overflow: hidden;
  display: flex; flex-direction: column;
  transition: box-shadow .25s ease;
}
.area:hover { box-shadow: 0 8px 30px rgba(0,0,0,.07); }

/* Static illustration panel */
.area-vis {
  height: 160px;
  display: flex; align-items: center; justify-content: center;
  padding: 1rem;
}
.area-vis svg { width: 80%; height: 80%; }
.vis-teal  { background: #edf7fa; }
.vis-amber { background: #fdf5e6; }
.vis-coral { background: #fdf0ec; }

.area-body {
  padding: 1.2rem 1.3rem 1.4rem;
  display: flex; flex-direction: column; gap: .4rem; flex: 1;
  background: #fff;
  border: 1px solid rgba(0,0,0,.05);
  border-top: none;
  border-radius: 0 0 18px 18px;
}
.area-label {
  font-size: .78rem; font-weight: 700;
  letter-spacing: .05em; text-transform: uppercase;
}
.lbl-teal  { color: #17677a; }
.lbl-amber { color: #946b14; }
.lbl-coral { color: #a14430; }
.area h3 {
  font-size: 1.18rem; font-weight: 600; line-height: 1.22; color: #1d1d1f;
}
.area p {
  font-size: .98rem; line-height: 1.55; color: #6e6e73;
}
.area-tags {
  display: flex; flex-wrap: wrap; gap: .3rem;
  margin-top: auto; padding-top: .35rem;
}
.area-tags span {
  padding: .22rem .58rem; border-radius: 6px;
  background: #f5f5f7;
  font-size: .82rem; font-weight: 500; color: #424245;
}

/* ───────────────────────────────────────────────
   PIPELINE — horizontal timeline
   ─────────────────────────────────────────────── */
.pipe-bg {
  background: #1d1d1f; color: #f5f5f7;
}
.pipe-bg .sec-label { color: rgba(255,255,255,.4); }
.pipe-bg .sec-title { color: #f5f5f7; }

.pipe {
  display: grid; gap: .6rem;
}
@media (min-width: 760px) {
  .pipe { grid-template-columns: repeat(4, 1fr); }
}
.step {
  padding: 1.2rem 1.1rem;
  border-radius: 14px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.06);
}
.step-n {
  font-size: .78rem; font-weight: 700;
  color: rgba(255,255,255,.3);
  margin-bottom: .6rem;
}
.step h3 {
  font-size: 1.05rem; font-weight: 600;
  color: #f5f5f7; margin-bottom: .3rem;
}
.step p {
  font-size: .94rem; line-height: 1.5;
  color: rgba(255,255,255,.5);
}

/* ───────────────────────────────────────────────
   SELECTED PAPERS — clean list with color accent
   ─────────────────────────────────────────────── */
.papers-bg { background: #fbfbfd; }

.papers {
  display: grid; gap: .8rem;
}
@media (min-width: 760px) {
  .papers { grid-template-columns: repeat(2, 1fr); }
}
.paper {
  padding: 1.3rem 1.4rem;
  border-radius: 16px;
  background: #fff;
  border: 1px solid rgba(0,0,0,.06);
  display: flex; flex-direction: column; gap: .4rem;
  transition: box-shadow .25s ease;
}
.paper:hover { box-shadow: 0 6px 24px rgba(0,0,0,.06); }

.paper-tag {
  display: inline-flex; width: fit-content;
  padding: .18rem .6rem; border-radius: 6px;
  font-size: .75rem; font-weight: 700;
  letter-spacing: .04em; text-transform: uppercase;
}
.pt-teal  { background: #edf7fa; color: #17677a; }
.pt-amber { background: #fdf5e6; color: #946b14; }
.pt-coral { background: #fdf0ec; color: #a14430; }
.pt-green { background: #edf5ef; color: #3a7049; }

.paper h3 {
  font-size: 1.1rem; font-weight: 600; line-height: 1.25; color: #1d1d1f;
}
.paper p {
  font-size: .96rem; line-height: 1.55; color: #6e6e73;
}
.paper-cites {
  display: flex; flex-wrap: wrap; gap: .35rem;
  margin-top: auto; padding-top: .25rem;
}
.cite {
  display: inline-flex; align-items: center;
  padding: .26rem .62rem; border-radius: 6px;
  background: #f5f5f7;
  color: #06c !important;
  font-size: .86rem; font-weight: 600;
  text-decoration: none !important;
  transition: background .2s;
}
.cite:hover { background: #e8e8ed; }

/* ───────────────────────────────────────────────
   RECRUIT — clean centered CTA
   ─────────────────────────────────────────────── */
.recruit-bg { background: #fff; }

.recruit-center { text-align: center; }
.recruit-center .sec-title {
  max-width: none;
}
.recruit-center .sec-sub {
  max-width: none; margin-left: auto; margin-right: auto;
}

.recruit-inst {
  display: inline-flex; align-items: center; gap: .4rem;
  margin-top: .8rem;
  font-size: .93rem; font-weight: 600; color: #946b14;
}
@media (min-width: 760px) {
  .recruit-inst { white-space: nowrap; }
}

.roles {
  display: grid; gap: .7rem;
  margin-top: 1.8rem; text-align: left;
}
@media (min-width: 760px) {
  .roles { grid-template-columns: repeat(4, 1fr); }
}
.role {
  padding: 1.2rem 1.1rem; border-radius: 14px;
  background: #f5f5f7;
  display: flex; flex-direction: column; gap: .35rem;
}
.role h3 { font-size: 1.05rem; font-weight: 600; color: #1d1d1f; }
.role p  { font-size: .94rem; line-height: 1.5; color: #6e6e73; }

.recruit-cta { margin-top: 1.6rem; }
.recruit-links {
  display: flex; justify-content: center; flex-wrap: wrap;
  gap: .3rem 1.1rem;
  margin-top: .7rem;
}
.recruit-links a {
  font-size: .94rem; font-weight: 500;
  color: #06c !important; text-decoration: none !important;
}
.recruit-links a:hover { text-decoration: underline !important; }
</style>

<!-- ═══════════ HERO ═══════════ -->
<section class="sec hero-sec">
<div class="sec-in">

  <div class="hero-top">
    <img class="hero-photo" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div>
      <div class="hero-name">Yuwen Huang</div>
      <div class="hero-aff">Postdoctoral Researcher, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></div>
    </div>
  </div>

  <div class="hero-news">
    <strong>Fall 2026</strong> — Joining
    <a href="https://dsa.hkust-gz.edu.cn/">Data Science and Analytics Thrust</a>,
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>,
    <a href="https://www.hkust-gz.edu.cn/">HKUST (Guangzhou)</a>
    as tenure-track Assistant Professor.
  </div>

  <h1 class="hero-h">Provable methods for structured inference and optimization</h1>

  <p class="hero-desc">
    I develop scalable algorithms with rigorous guarantees using graphical models, combinatorics, tensor networks, and distributed quantum systems, with growing directions in machine learning and learning theory.
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
    <p class="sec-sub">Turning mathematical structure into practical, scalable computation.</p>
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
    <h2 class="sec-title">Representative directions and papers</h2>
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
    <p class="sec-sub">Recruiting RAs, MPhil/PhD students, and one Postdoc for Fall 2026 at HKUST (Guangzhou).</p>
    <p class="recruit-inst">Tenure-track Assistant Professor &middot; Information Hub &middot; DSA Thrust</p>
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
