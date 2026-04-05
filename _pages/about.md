---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
.splash .page__content {
  font-family: -apple-system, "SF Pro Display", "SF Pro Text", "Helvetica Neue", "Inter", "Segoe UI", sans-serif;
  max-width: none !important; padding: 0 !important; margin: 0 !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #1d1d1f;
}
.splash .page__content p,
.splash .page__content h1,
.splash .page__content h2,
.splash .page__content h3 {
  margin: 0 !important; padding: 0 !important;
  border: none !important;
  color: inherit;
}
.splash .page__content a { text-decoration: none; }
.splash .page__content > *:first-child { margin-top: 0 !important; }
.splash .page__content > *:last-child { margin-bottom: 0 !important; }

/* ── Sections — minimal padding ── */
.s { width: 100%; padding: .8rem clamp(1.2rem, 4vw, 5rem); }
.s-in { max-width: 1000px; width: 100%; margin: 0 auto; }

/* ── HERO ── */
.hero { background: #0d0d0d; color: #fff; text-align: center; padding-top: 1.5rem; padding-bottom: 1.2rem; }
.hero .s-in { display: flex; flex-direction: column; align-items: center; }

.hero-id-row { display: flex; align-items: center; gap: .7rem; margin-bottom: .6rem; }
.hero-photo { width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid rgba(255,255,255,.15); flex-shrink: 0; }
.hero-id { text-align: left; }
.hero-name { font-size: 1.15rem; font-weight: 700; color: #fff; line-height: 1.2; }
.hero-aff { font-size: .88rem; color: rgba(255,255,255,.7); line-height: 1.3; margin-top: .1rem; }
.hero-aff a { color: rgba(255,255,255,.8); font-weight: 500; }
.hero-aff a:hover { color: #fff; }
.hero-news { font-size: .84rem; color: rgba(255,255,255,.6); margin-top: .15rem; }
.hero-news strong { color: #f0c8a0; font-weight: 700; }
.hero-news a { color: rgba(255,255,255,.75); font-weight: 600; }
.hero-news a:hover { color: #fff; }

.hero-intro { font-size: clamp(1rem, 1.5vw, 1.15rem); font-weight: 400; line-height: 1.5; color: rgba(255,255,255,.85); max-width: 520px; text-align: center; }

.hero-cta { display: flex; flex-wrap: wrap; gap: .4rem; justify-content: center; margin-top: .6rem; }
.btn { display: inline-flex; align-items: center; justify-content: center; height: 2.3rem; padding: 0 1.2rem; border-radius: 980px; font-size: .86rem; font-weight: 600; cursor: pointer; text-decoration: none !important; transition: all .2s ease; }
.btn-light { background: #fff; color: #000 !important; }
.splash .page__content .btn-light, .splash .page__content .btn-light:hover { color: #000 !important; text-decoration: none !important; }
.btn-light:hover { box-shadow: 0 2px 10px rgba(255,255,255,.15); }
.btn-ghost { background: transparent; border: 1.5px solid rgba(255,255,255,.35); color: #fff !important; }
.splash .page__content .btn-ghost, .splash .page__content .btn-ghost:hover { color: #fff !important; text-decoration: none !important; }
.btn-ghost:hover { border-color: rgba(255,255,255,.6); background: rgba(255,255,255,.06); }

/* ── Section headers — high contrast ── */
.sh { font-size: .68rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #86868b; margin-bottom: .2rem; }
.sh2 { font-size: clamp(1.25rem, 2.5vw, 1.7rem); font-weight: 800; line-height: 1.1; letter-spacing: -.025em; color: #000; }

/* ── RESEARCH ── */
.research { background: #fff; }
.ra-grid { display: grid; gap: .5rem; margin-top: .5rem; }
@media (min-width: 800px) { .ra-grid { grid-template-columns: repeat(3, 1fr); gap: 1.2rem; } }
.ra-name { font-size: 1rem; font-weight: 700; color: #000; line-height: 1.15; }
.ra-desc { margin-top: .15rem; font-size: .84rem; line-height: 1.4; color: #424245; }
.ra-topics { margin-top: .2rem; font-size: .76rem; color: #86868b; }

/* ── SELECTED WORK ── */
.work { background: #000; color: #fff; }
.work .sh { color: rgba(255,255,255,.5); }
.work .sh2 { color: #fff; }

.wf { margin-top: .4rem; padding-bottom: .4rem; border-bottom: 1px solid rgba(255,255,255,.1); }
.wf-title { font-size: clamp(1rem, 1.5vw, 1.2rem); font-weight: 700; color: #fff; line-height: 1.15; }
.wf-desc { margin-top: .2rem; font-size: .84rem; line-height: 1.4; color: rgba(255,255,255,.65); }
.wc { display: flex; flex-wrap: wrap; gap: .2rem; margin-top: .35rem; }
.cite { display: inline-flex; align-items: center; padding: .18rem .45rem; border-radius: 980px; background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.15); color: rgba(255,255,255,.85) !important; font-size: .7rem; font-weight: 600; text-decoration: none !important; transition: all .15s; }
.cite:hover { background: rgba(255,255,255,.2); color: #fff !important; }

.wa-grid { display: grid; gap: .4rem; margin-top: .4rem; }
@media (min-width: 800px) { .wa-grid { grid-template-columns: repeat(3, 1fr); } }
.wa-name { font-size: .9rem; font-weight: 700; color: #fff; }
.wa-desc { margin-top: .1rem; font-size: .78rem; line-height: 1.35; color: rgba(255,255,255,.55); }
.wa .wc { margin-top: .25rem; }

.work-more { margin-top: .5rem; text-align: center; }
.work-more a { font-size: .84rem; font-weight: 600; color: rgba(255,255,255,.6) !important; text-decoration: none !important; }
.work-more a:hover { color: #fff !important; }
.work-more a::after { content: " →"; }

/* ── UPDATES ── */
.updates { background: #f5f5f7; }
.u-list { margin-top: .3rem; }
.u-item { display: flex; gap: clamp(.6rem, 1.5vw, 1.2rem); padding: .25rem 0; border-bottom: 1px solid rgba(0,0,0,.07); align-items: baseline; }
.u-item:first-child { border-top: 1px solid rgba(0,0,0,.07); }
.u-date { font-size: .76rem; font-weight: 700; color: #6e6e73; min-width: 72px; flex-shrink: 0; }
.u-title { font-size: .86rem; font-weight: 600; color: #000; line-height: 1.25; }
.u-title a { color: #000 !important; text-decoration: none !important; }
.u-title a:hover { color: #06c !important; }
.u-venue { font-size: .74rem; color: #6e6e73; }
.u-badge { display: inline-flex; padding: .08rem .35rem; border-radius: 980px; font-size: .58rem; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; margin-left: .25rem; vertical-align: middle; background: #e8fbe8; color: #1a7a2e; }

/* ── JOIN — high contrast white on dark ── */
.join { background: #0d0d0d; color: #fff; padding-top: 1.2rem; padding-bottom: 1.2rem; }
.join .s-in { display: flex; flex-direction: column; align-items: center; text-align: center; }
.join-h { font-size: clamp(1.6rem, 3.5vw, 2.6rem); font-weight: 800; line-height: 1.05; letter-spacing: -.035em; color: #fff; }
.join-desc { margin-top: .4rem; font-size: .92rem; line-height: 1.4; color: rgba(255,255,255,.75); max-width: 460px; }

.join-perks { display: grid; gap: .15rem; margin-top: .5rem; text-align: left; max-width: 440px; width: 100%; }
.join-perk { display: flex; align-items: baseline; gap: .4rem; font-size: .86rem; line-height: 1.3; color: rgba(255,255,255,.9); }
.join-perk::before { content: "→"; color: #f0c8a0; font-weight: 700; flex-shrink: 0; }

.join-roles { display: flex; flex-wrap: wrap; gap: .25rem; justify-content: center; margin-top: .5rem; }
.join-role { padding: .22rem .7rem; border-radius: 980px; border: 1.5px solid rgba(255,255,255,.3); font-size: .8rem; font-weight: 600; color: #fff; }

.join-cta { margin-top: .5rem; }
.btn-accent { background: #f0c8a0; color: #000 !important; font-weight: 800; font-size: .9rem; height: 2.5rem; padding: 0 1.5rem; }
.splash .page__content .btn-accent, .splash .page__content .btn-accent:hover { color: #000 !important; text-decoration: none !important; }
.btn-accent:hover { background: #f5d5b3; box-shadow: 0 3px 16px rgba(240,200,160,.3); }

.join-links { display: flex; justify-content: center; flex-wrap: wrap; gap: .2rem .7rem; margin-top: .3rem; }
.join-links a { font-size: .76rem; font-weight: 600; color: rgba(255,255,255,.5) !important; text-decoration: none !important; }
.join-links a:hover { color: #fff !important; }

/* ── Mobile ── */
@media (max-width: 767px) {
  .s { padding: .6rem .8rem; }
  .hero { padding-top: 1rem; padding-bottom: .8rem; }
  .join { padding-top: .8rem; padding-bottom: .8rem; }
  .hero-id-row { flex-direction: column; text-align: center; }
  .hero-id { text-align: center; }
  .u-item { flex-direction: column; gap: .02rem; }
  .u-date { min-width: auto; }
}
@media (min-width: 768px) and (max-width: 1023px) {
  .ra-grid { grid-template-columns: repeat(2, 1fr); }
}

.skip-nav { position: absolute; top: -100%; left: 50%; transform: translateX(-50%); padding: .5rem 1.2rem; border-radius: 980px; background: #06c; color: #fff !important; font-size: .85rem; font-weight: 600; text-decoration: none !important; z-index: 9999; }
.skip-nav:focus { top: .8rem; }
</style>

<a class="skip-nav" href="#research">Skip to research</a>

<!-- ═══ HERO ═══ -->
<section class="s hero" aria-label="Introduction">
<div class="s-in">
  <div class="hero-id-row">
    <img class="hero-photo" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div class="hero-id">
      <div class="hero-name">Yuwen Huang</div>
      <div class="hero-aff">Postdoctoral Researcher, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></div>
      <div class="hero-news"><strong>May 2026</strong> — Joining <a href="https://www.hkust-gz.edu.cn/">HKUST (Guangzhou)</a> as Assistant Professor</div>
    </div>
  </div>
  <p class="hero-intro">I develop provable algorithms for inference, optimization, and quantum computation — with tools from graphical models, combinatorics, and tensor networks.</p>
  <div class="hero-cta">
    <a class="btn btn-light" href="#positions">Open positions</a>
    <a class="btn btn-ghost" href="#research">Selected research</a>
  </div>
</div>
</section>

<!-- ═══ RESEARCH ═══ -->
<section class="s research" aria-label="Research areas">
<div class="s-in">
  <div class="sh">Research</div>
  <h2 class="sh2">Three core areas</h2>
  <div class="ra-grid">
    <div>
      <div class="ra-name">Structured inference</div>
      <div class="ra-desc">Message passing, Bethe methods, and graph covers for inference and counting on graphical models.</div>
      <div class="ra-topics">Uncertainty · Counting · Graph covers</div>
    </div>
    <div>
      <div class="ra-name">Provable optimization</div>
      <div class="ra-desc">Permanent bounds and algorithmic guarantees for hard combinatorial problems.</div>
      <div class="ra-topics">Convex / nonconvex · Permanent bounds · Decisions</div>
    </div>
    <div>
      <div class="ra-name">Quantum &amp; tensors</div>
      <div class="ra-desc">Tensor networks and distributed quantum systems for scalable high-dimensional computation.</div>
      <div class="ra-topics">Tensor networks · Quantum systems · Scalability</div>
    </div>
  </div>
</div>
</section>

<!-- ═══ SELECTED WORK ═══ -->
<section class="s work" id="research" aria-label="Selected research">
<div class="s-in">
  <div class="sh">Selected work</div>
  <h2 class="sh2">Representative papers</h2>
  <div class="wf">
    <div class="wf-title">Graphical models and Bethe methods</div>
    <div class="wf-desc">Graph covers, message passing, and Bethe approximation for inference and counting — our longest-running thread.</div>
    <div class="wc">
      <a class="cite" href="https://ieeexplore.ieee.org/document/9174508/">[ISIT 2020]</a>
      <a class="cite" href="https://arxiv.org/abs/2107.01816">[ISIT 2021]</a>
      <a class="cite" href="https://ieeexplore.ieee.org/document/9965874/">[ITW 2022]</a>
      <a class="cite" href="https://arxiv.org/abs/2306.02280">[ISIT 2023]</a>
      <a class="cite" href="https://ieeexplore.ieee.org/document/10619603/">[ISIT 2024]</a>
      <a class="cite" href="https://arxiv.org/abs/2306.02280">[TIT 2024]</a>
      <a class="cite" href="https://arxiv.org/abs/2506.16250">[TIT-sub]</a>
    </div>
  </div>
  <div class="wa-grid">
    <div class="wa">
      <div class="wa-name">Tensor methods</div>
      <div class="wa-desc">Tensor-network methods for high-dimensional computation.</div>
      <div class="wc">
        <a class="cite" href="https://arxiv.org/abs/2107.01816">[ISIT 2021]</a>
        <a class="cite" href="https://arxiv.org/abs/2506.16250">[TIT-sub]</a>
        <a class="cite" href="https://arxiv.org/abs/2508.05712">[ICML 2025]</a>
        <a class="cite" href="https://arxiv.org/abs/2603.07673">[QUANTUM-sub]</a>
      </div>
    </div>
    <div class="wa">
      <div class="wa-name">Optimization</div>
      <div class="wa-desc">Permanent bounds and guarantees for hard problems.</div>
      <div class="wc">
        <a class="cite" href="https://arxiv.org/abs/2306.02280">[ISIT 2023]</a>
        <a class="cite" href="https://arxiv.org/abs/2306.02280">[TIT 2024]</a>
        <a class="cite" href="https://arxiv.org/abs/2508.05712">[ICML 2025]</a>
      </div>
    </div>
    <div class="wa">
      <div class="wa-name">Quantum systems</div>
      <div class="wa-desc">Distributed quantum optimization and inference.</div>
      <div class="wc">
        <a class="cite" href="https://arxiv.org/abs/2603.07673">[QUANTUM-sub]</a>
      </div>
    </div>
  </div>
  <div class="work-more"><a href="{{ '/publications/' | relative_url }}">View all publications</a></div>
</div>
</section>

<!-- ═══ UPDATES ═══ -->
<section class="s updates" aria-label="Latest updates">
<div class="s-in">
  <div class="sh">Latest</div>
  <h2 class="sh2">What's new</h2>
  <div class="u-list">
    <div class="u-item">
      <div class="u-date">May 2026</div>
      <div><div class="u-title">Joining HKUST (Guangzhou) as Assistant Professor <span class="u-badge">Starting</span></div><div class="u-venue">DSA Thrust, Information Hub</div></div>
    </div>
    <div class="u-item">
      <div class="u-date">Mar 2026</div>
      <div><div class="u-title"><a href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">Scalable Distributed Quantum Optimization</a></div><div class="u-venue">Submitted to Quantum</div></div>
    </div>
    <div class="u-item">
      <div class="u-date">Jul 2025</div>
      <div><div class="u-title"><a href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">Graph-Cover-based Characterization of the Bethe Partition Function</a></div><div class="u-venue">Submitted to IEEE Trans. Inf. Theory</div></div>
    </div>
    <div class="u-item">
      <div class="u-date">2024</div>
      <div><div class="u-title"><a href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">Degree-M Bethe &amp; Sinkhorn Permanent</a></div><div class="u-venue">Published in IEEE Trans. Inf. Theory</div></div>
    </div>
  </div>
</div>
</section>

<!-- ═══ JOIN ═══ -->
<section class="s join" id="positions" aria-label="Open positions">
<div class="s-in">
  <h2 class="join-h">Join the group</h2>
  <p class="join-desc">Recruiting for May 2026 at HKUST (Guangzhou), DSA Thrust, Information Hub.</p>
  <div class="join-perks">
    <div class="join-perk">Competitive funding with full tuition and stipend</div>
    <div class="join-perk">Publication-driven mentorship at top venues (IEEE TIT, ISIT, ICML)</div>
    <div class="join-perk">Access to the Greater Bay Area research ecosystem</div>
    <div class="join-perk">Hands-on collaboration — small group, close advising</div>
  </div>
  <div class="join-roles">
    <span class="join-role">Research Assistant</span>
    <span class="join-role">MPhil</span>
    <span class="join-role">PhD</span>
    <span class="join-role">Postdoc</span>
  </div>
  <div class="join-cta"><a class="btn btn-accent" href="mailto:{{ site.author.email }}">Get in touch</a></div>
  <div class="join-links">
    <a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
    <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
  </div>
</div>
</section>
