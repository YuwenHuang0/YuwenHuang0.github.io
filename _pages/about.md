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

/* ── Sections ── */
.s { width: 100%; padding: clamp(1.5rem, 3vh, 2.5rem) clamp(1.2rem, 4vw, 5rem); }
.s-in { max-width: 1100px; width: 100%; margin: 0 auto; }

/* ── HERO ── */
.hero { background: #0d0d0d; color: #f5f5f7; text-align: center; position: relative; overflow: hidden; }
.hero::before { content: ""; position: absolute; inset: 0; background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(255,255,255,.03) 0%, transparent 60%); pointer-events: none; }
.hero .s-in { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; }

.hero-id-row { display: flex; align-items: center; gap: .8rem; margin-bottom: .8rem; }
.hero-photo { width: 64px; height: 64px; border-radius: 50%; object-fit: cover; border: 2px solid rgba(255,255,255,.1); flex-shrink: 0; }
.hero-id { text-align: left; }
.hero-name { font-size: 1.2rem; font-weight: 600; color: #f5f5f7; line-height: 1.2; letter-spacing: -.02em; }
.hero-aff { font-size: .88rem; color: rgba(255,255,255,.5); line-height: 1.3; margin-top: .1rem; }
.hero-aff a { color: rgba(255,255,255,.6); font-weight: 500; }
.hero-aff a:hover { color: #fff; }
.hero-news { font-size: .82rem; color: rgba(255,255,255,.35); margin-top: .15rem; }
.hero-news strong { color: #f0c8a0; font-weight: 600; }
.hero-news a { color: rgba(255,255,255,.5); font-weight: 500; }
.hero-news a:hover { color: #fff; }

.hero-intro { font-size: clamp(1rem, 1.5vw, 1.2rem); font-weight: 400; line-height: 1.5; color: rgba(255,255,255,.65); max-width: 520px; text-align: center; }

.hero-cta { display: flex; flex-wrap: wrap; gap: .5rem; justify-content: center; margin-top: 1rem; }
.btn { display: inline-flex; align-items: center; justify-content: center; height: 2.4rem; padding: 0 1.3rem; border-radius: 980px; font-size: .88rem; font-weight: 600; cursor: pointer; text-decoration: none !important; transition: all .25s ease; letter-spacing: -.01em; }
.btn-light { background: #f5f5f7; color: #0d0d0d !important; }
.splash .page__content .btn-light, .splash .page__content .btn-light:hover { color: #0d0d0d !important; text-decoration: none !important; }
.btn-light:hover { background: #fff; box-shadow: 0 2px 12px rgba(255,255,255,.12); }
.btn-ghost { background: transparent; border: 1.5px solid rgba(255,255,255,.2); color: rgba(255,255,255,.7) !important; }
.splash .page__content .btn-ghost, .splash .page__content .btn-ghost:hover { color: rgba(255,255,255,.7) !important; text-decoration: none !important; }
.btn-ghost:hover { border-color: rgba(255,255,255,.4); background: rgba(255,255,255,.04); }

/* ── Section headers ── */
.sh { font-size: .7rem; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: #6e6e73; margin-bottom: .25rem; }
.sh2 { font-size: clamp(1.3rem, 2.5vw, 1.8rem); font-weight: 700; line-height: 1.1; letter-spacing: -.025em; color: #1d1d1f; }
.sh-sub { margin-top: .3rem; font-size: .9rem; line-height: 1.45; color: #6e6e73; }

/* ── RESEARCH ── */
.research { background: #fff; }
.research-areas { display: grid; gap: 1rem; margin-top: 1rem; }
@media (min-width: 800px) { .research-areas { grid-template-columns: repeat(3, 1fr); gap: 2rem; } }
.ra-name { font-size: 1.05rem; font-weight: 700; color: #1d1d1f; letter-spacing: -.01em; line-height: 1.15; }
.ra-desc { margin-top: .2rem; font-size: .85rem; line-height: 1.45; color: #6e6e73; }
.ra-topics { margin-top: .25rem; font-size: .78rem; color: #86868b; line-height: 1.3; }

/* ── SELECTED WORK ── */
.work { background: #0d0d0d; color: #f5f5f7; }
.work .sh { color: rgba(255,255,255,.35); }
.work .sh2 { color: #fff; }

.wf { margin-top: .8rem; padding-bottom: .8rem; border-bottom: 1px solid rgba(255,255,255,.07); }
.wf-title { font-size: clamp(1.05rem, 1.6vw, 1.3rem); font-weight: 700; color: #fff; letter-spacing: -.015em; line-height: 1.15; }
.wf-desc { margin-top: .25rem; font-size: .88rem; line-height: 1.45; color: rgba(255,255,255,.45); max-width: 600px; }
.wc { display: flex; flex-wrap: wrap; gap: .25rem; margin-top: .4rem; }
.cite { display: inline-flex; align-items: center; padding: .2rem .5rem; border-radius: 980px; background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.08); color: rgba(255,255,255,.65) !important; font-size: .72rem; font-weight: 500; text-decoration: none !important; transition: all .2s; }
.cite:hover { background: rgba(255,255,255,.14); color: #fff !important; }

.work-areas { display: grid; gap: .8rem; margin-top: .8rem; }
@media (min-width: 800px) { .work-areas { grid-template-columns: repeat(3, 1fr); } }
.wa-name { font-size: .92rem; font-weight: 600; color: rgba(255,255,255,.8); }
.wa-desc { margin-top: .1rem; font-size: .8rem; line-height: 1.4; color: rgba(255,255,255,.35); }
.wa .wc { margin-top: .3rem; }

.work-more { margin-top: 1rem; text-align: center; }
.work-more a { font-size: .88rem; font-weight: 500; color: rgba(255,255,255,.4) !important; text-decoration: none !important; transition: color .2s; }
.work-more a:hover { color: #fff !important; }
.work-more a::after { content: " →"; }

/* ── UPDATES ── */
.updates { background: #f5f5f7; }
.ul { margin-top: .6rem; }
.ui { display: flex; gap: clamp(.8rem, 2vw, 1.5rem); padding: .45rem 0; border-bottom: 1px solid rgba(0,0,0,.05); align-items: baseline; }
.ui:first-child { border-top: 1px solid rgba(0,0,0,.05); }
.ud { font-size: .78rem; font-weight: 600; color: #86868b; min-width: 75px; flex-shrink: 0; }
.ut { font-size: .88rem; font-weight: 600; color: #1d1d1f; line-height: 1.25; }
.ut a { color: #1d1d1f !important; text-decoration: none !important; }
.ut a:hover { color: #06c !important; }
.uv { font-size: .78rem; color: #86868b; margin-top: .05rem; }
.ub { display: inline-flex; padding: .1rem .4rem; border-radius: 980px; font-size: .6rem; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; margin-left: .3rem; vertical-align: middle; background: rgba(0,0,0,.06); color: #6e6e73; }

/* ── JOIN ── */
.join { background: #1d1d1f; color: #f5f5f7; }
.join .s-in { display: flex; flex-direction: column; align-items: center; text-align: center; }
.join-h { font-size: clamp(1.4rem, 3vw, 2.2rem); font-weight: 700; line-height: 1.1; letter-spacing: -.03em; color: #fff; }
.join-desc { margin-top: .4rem; font-size: .9rem; line-height: 1.45; color: rgba(255,255,255,.5); max-width: 480px; }

.join-perks { display: grid; gap: .3rem; margin-top: .8rem; text-align: left; max-width: 440px; width: 100%; }
.join-perk { display: flex; align-items: baseline; gap: .4rem; font-size: .85rem; line-height: 1.35; color: rgba(255,255,255,.65); }
.join-perk::before { content: "→"; color: #f0c8a0; font-weight: 600; flex-shrink: 0; }

.join-roles { display: flex; flex-wrap: wrap; gap: .3rem; justify-content: center; margin-top: .8rem; }
.join-role { padding: .25rem .8rem; border-radius: 980px; border: 1px solid rgba(255,255,255,.12); font-size: .8rem; font-weight: 500; color: rgba(255,255,255,.6); background: rgba(255,255,255,.04); }

.join-cta { margin-top: 1rem; }
.btn-accent { background: #f0c8a0; color: #1d1d1f !important; font-weight: 700; }
.splash .page__content .btn-accent, .splash .page__content .btn-accent:hover { color: #1d1d1f !important; text-decoration: none !important; }
.btn-accent:hover { background: #f5d5b3; box-shadow: 0 3px 16px rgba(240,200,160,.25); }

.join-links { display: flex; justify-content: center; flex-wrap: wrap; gap: .2rem .8rem; margin-top: .6rem; }
.join-links a { font-size: .78rem; font-weight: 500; color: rgba(255,255,255,.35) !important; text-decoration: none !important; transition: color .2s; }
.join-links a:hover { color: rgba(255,255,255,.7) !important; }

/* ── Mobile ── */
@media (max-width: 767px) {
  .s { padding: 1.2rem 1rem; }
  .hero-id-row { flex-direction: column; text-align: center; }
  .hero-id { text-align: center; }
  .ui { flex-direction: column; gap: .05rem; }
  .ud { min-width: auto; }
}
@media (min-width: 768px) and (max-width: 1023px) {
  .research-areas { grid-template-columns: repeat(2, 1fr); }
}

/* Skip nav */
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
  <p class="sh-sub">From mathematical structure to scalable computation.</p>
  <div class="research-areas">
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
  <div class="work-areas">
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
  <div class="ul">
    <div class="ui">
      <div class="ud">May 2026</div>
      <div><div class="ut">Joining HKUST (Guangzhou) as Assistant Professor <span class="ub">Starting</span></div><div class="uv">DSA Thrust, Information Hub</div></div>
    </div>
    <div class="ui">
      <div class="ud">Mar 2026</div>
      <div><div class="ut"><a href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">Scalable Distributed Quantum Optimization</a></div><div class="uv">Submitted to Quantum</div></div>
    </div>
    <div class="ui">
      <div class="ud">Jul 2025</div>
      <div><div class="ut"><a href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">Graph-Cover-based Characterization of the Bethe Partition Function</a></div><div class="uv">Submitted to IEEE Trans. Inf. Theory</div></div>
    </div>
    <div class="ui">
      <div class="ud">2024</div>
      <div><div class="ut"><a href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">Degree-M Bethe &amp; Sinkhorn Permanent</a></div><div class="uv">Published in IEEE Trans. Inf. Theory</div></div>
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
