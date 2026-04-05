---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ═══════════════════════════════════════════════
   FOUNDATIONS
   ═══════════════════════════════════════════════ */
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

/* ═══════════════════════════════════════════════
   FULL-VIEWPORT SECTIONS
   ═══════════════════════════════════════════════ */
.vp {
  width: 100%;
  min-height: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(2.5rem, 4vh, 4rem) clamp(1.5rem, 5vw, 6rem);
  position: relative;
  overflow: hidden;
}

.vp-in {
  max-width: 1100px;
  width: 100%;
  margin: 0 auto;
}

/* Hero stays tall on desktop */
@media (min-width: 1024px) {
  .hero { min-height: 85vh; }
}

/* ═══════════════════════════════════════════════
   HERO — dark, full viewport
   ═══════════════════════════════════════════════ */
.hero {
  background: #0d0d0d;
  color: #f5f5f7;
  text-align: center;
  flex-direction: column;
}
.hero::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(255,255,255,.03) 0%, transparent 60%);
  pointer-events: none;
}
.hero .vp-in {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

/* Identity */
.hero-identity {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.2rem;
}
.hero-photo {
  width: 76px; height: 76px;
  border-radius: 50%; object-fit: cover;
  border: 2px solid rgba(255,255,255,.12);
  flex-shrink: 0;
}
.hero-id { text-align: left; }
.hero-name {
  font-size: 1.4rem; font-weight: 600; color: #f5f5f7;
  line-height: 1.2; letter-spacing: -.02em;
}
.hero-aff {
  font-size: 1rem; color: rgba(255,255,255,.55);
  line-height: 1.4; margin-top: .15rem;
}
.hero-aff a { color: rgba(255,255,255,.65); font-weight: 500; }
.hero-aff a:hover { color: #fff; }
.hero-news {
  font-size: .9rem; color: rgba(255,255,255,.4);
  margin-top: .25rem;
}
.hero-news strong { color: #f0c8a0; font-weight: 600; }
.hero-news a { color: rgba(255,255,255,.55); font-weight: 500; }
.hero-news a:hover { color: #fff; }

/* Headline */
.hero-headline {
  font-size: clamp(2.4rem, 5vw, 4rem);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -.04em;
  color: #fff;
  max-width: 860px;
  text-align: center;
}

/* Subtitle */
.hero-sub {
  margin-top: .8rem;
  font-size: clamp(1rem, 1.4vw, 1.15rem);
  line-height: 1.5;
  color: rgba(255,255,255,.45);
  max-width: 600px;
  text-align: center;
  font-weight: 400;
}

/* CTA */
.hero-cta {
  display: flex; flex-wrap: wrap; gap: .8rem;
  justify-content: center;
  margin-top: 1.5rem;
}
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  height: 2.8rem; padding: 0 1.6rem;
  border-radius: 980px;
  font-size: 1rem; font-weight: 600;
  cursor: pointer;
  text-decoration: none !important;
  transition: all .3s cubic-bezier(.4,0,.2,1);
  letter-spacing: -.01em;
}
.btn-light {
  background: #f5f5f7; color: #0d0d0d !important;
}
.splash .page__content .btn-light,
.splash .page__content .btn-light:hover {
  color: #0d0d0d !important;
  text-decoration: none !important;
}
.btn-light:hover { background: #fff; box-shadow: 0 4px 20px rgba(255,255,255,.15); transform: translateY(-1px); }
.btn-ghost {
  background: transparent;
  border: 1.5px solid rgba(255,255,255,.25);
  color: rgba(255,255,255,.8) !important;
}
.splash .page__content .btn-ghost,
.splash .page__content .btn-ghost:hover {
  color: rgba(255,255,255,.8) !important;
  text-decoration: none !important;
}
.btn-ghost:hover { border-color: rgba(255,255,255,.5); background: rgba(255,255,255,.05); }

/* ═══════════════════════════════════════════════
   RESEARCH — light, full viewport
   ═══════════════════════════════════════════════ */
.research {
  background: #fff;
}

.sec-label {
  font-size: .75rem; font-weight: 600;
  letter-spacing: .1em; text-transform: uppercase;
  color: #6e6e73;
  margin-bottom: .4rem;
}
.sec-heading {
  font-size: clamp(1.6rem, 3vw, 2.4rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -.03em;
  color: #1d1d1f;
}
.sec-desc {
  margin-top: .5rem;
  font-size: clamp(.95rem, 1.3vw, 1.05rem);
  line-height: 1.5;
  color: #6e6e73;
  max-width: 560px;
}

.research-areas {
  display: grid;
  gap: 1.5rem;
  margin-top: clamp(1.5rem, 3vh, 2.5rem);
}
@media (min-width: 800px) {
  .research-areas { grid-template-columns: repeat(3, 1fr); gap: 2.5rem; }
}

.ra {}
.ra-name {
  font-size: clamp(1.1rem, 1.6vw, 1.3rem);
  font-weight: 700;
  color: #1d1d1f;
  letter-spacing: -.015em;
  line-height: 1.15;
}
.ra-desc {
  margin-top: .35rem;
  font-size: .92rem;
  line-height: 1.5;
  color: #6e6e73;
}
.ra-topics {
  margin-top: .4rem;
  font-size: .82rem;
  color: #86868b;
  line-height: 1.4;
}

/* ═══════════════════════════════════════════════
   SELECTED WORK — dark, full viewport
   ═══════════════════════════════════════════════ */
.work {
  background: #0d0d0d;
  color: #f5f5f7;
}
.work .sec-label { color: rgba(255,255,255,.4); }
.work .sec-heading { color: #fff; }
.work .sec-desc { color: rgba(255,255,255,.45); }

.work-featured {
  margin-top: clamp(1.2rem, 2.5vh, 2rem);
  padding-bottom: 1.2rem;
  border-bottom: 1px solid rgba(255,255,255,.08);
}
.work-featured-title {
  font-size: clamp(1.2rem, 2vw, 1.6rem);
  font-weight: 700;
  color: #fff;
  letter-spacing: -.02em;
  line-height: 1.15;
}
.work-featured-desc {
  margin-top: .4rem;
  font-size: clamp(.9rem, 1.2vw, 1rem);
  line-height: 1.5;
  color: rgba(255,255,255,.5);
  max-width: 640px;
}
.work-cites {
  display: flex; flex-wrap: wrap; gap: .35rem;
  margin-top: .6rem;
}
.cite {
  display: inline-flex; align-items: center;
  padding: .25rem .55rem;
  border-radius: 980px;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.1);
  color: rgba(255,255,255,.7) !important;
  font-size: .75rem; font-weight: 500;
  text-decoration: none !important;
  transition: all .2s;
  letter-spacing: -.005em;
}
.cite:hover { background: rgba(255,255,255,.15); color: #fff !important; }

/* Sub-areas */
.work-areas {
  display: grid;
  gap: 1.2rem;
  margin-top: 1.2rem;
}
@media (min-width: 800px) {
  .work-areas { grid-template-columns: repeat(3, 1fr); }
}
.wa {}
.wa-name {
  font-size: 1rem; font-weight: 600;
  color: rgba(255,255,255,.85);
  letter-spacing: -.01em;
}
.wa-desc {
  margin-top: .2rem;
  font-size: .85rem; line-height: 1.45;
  color: rgba(255,255,255,.4);
}
.wa .work-cites { margin-top: .4rem; }

.work-more {
  margin-top: 1.5rem;
  text-align: center;
}
.work-more a {
  font-size: 1rem; font-weight: 500;
  color: rgba(255,255,255,.5) !important;
  text-decoration: none !important;
  transition: color .2s;
}
.work-more a:hover { color: #fff !important; }
.work-more a::after { content: " →"; }

/* ═══════════════════════════════════════════════
   UPDATES — light, full viewport
   ═══════════════════════════════════════════════ */
.updates {
  background: #f5f5f7;
}

.update-list {
  margin-top: clamp(1rem, 2vh, 1.5rem);
  display: flex;
  flex-direction: column;
  gap: 0;
}
.update-item {
  display: flex;
  gap: clamp(1rem, 2vw, 2rem);
  padding: .7rem 0;
  border-bottom: 1px solid rgba(0,0,0,.06);
  align-items: baseline;
}
.update-item:first-child { border-top: 1px solid rgba(0,0,0,.06); }
.update-date {
  font-size: .82rem; font-weight: 600;
  color: #86868b;
  min-width: 85px;
  flex-shrink: 0;
  letter-spacing: -.005em;
}
.update-content {
  flex: 1;
}
.update-title {
  font-size: .95rem; font-weight: 600;
  color: #1d1d1f;
  line-height: 1.3;
  letter-spacing: -.01em;
}
.update-title a { color: #1d1d1f !important; text-decoration: none !important; }
.update-title a:hover { color: #06c !important; }
.update-venue {
  font-size: .82rem; color: #86868b;
  margin-top: .1rem;
}
.update-badge {
  display: inline-flex; padding: .15rem .5rem;
  border-radius: 980px; font-size: .65rem; font-weight: 700;
  letter-spacing: .04em; text-transform: uppercase;
  margin-left: .4rem; vertical-align: middle;
  background: rgba(0,0,0,.06); color: #6e6e73;
}

/* ═══════════════════════════════════════════════
   JOIN — dark, full viewport
   ═══════════════════════════════════════════════ */
.join {
  background: #0d0d0d;
  color: #f5f5f7;
  text-align: center;
}
.join .vp-in {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.join .sec-label { color: rgba(255,255,255,.4); }

.join-heading {
  font-size: clamp(1.8rem, 4vw, 3rem);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -.035em;
  color: #fff;
}
.join-desc {
  margin-top: .6rem;
  font-size: clamp(.92rem, 1.2vw, 1.05rem);
  line-height: 1.5;
  color: rgba(255,255,255,.45);
  max-width: 520px;
}

.join-roles {
  display: flex; flex-wrap: wrap;
  gap: .4rem;
  justify-content: center;
  margin-top: 1.2rem;
}
.join-role {
  padding: .35rem 1rem;
  border-radius: 980px;
  border: 1px solid rgba(255,255,255,.12);
  font-size: .88rem; font-weight: 500;
  color: rgba(255,255,255,.6);
}

.join-cta {
  margin-top: 1.5rem;
}
.btn-white {
  background: #fff; color: #0d0d0d !important;
}
.splash .page__content .btn-white,
.splash .page__content .btn-white:hover {
  color: #0d0d0d !important;
  text-decoration: none !important;
}
.btn-white:hover { box-shadow: 0 4px 24px rgba(255,255,255,.2); transform: translateY(-1px); }

.join-links {
  display: flex; justify-content: center; flex-wrap: wrap;
  gap: .3rem 1rem;
  margin-top: 1rem;
}
.join-links a {
  font-size: .9rem; font-weight: 500;
  color: rgba(255,255,255,.4) !important;
  text-decoration: none !important;
  transition: color .2s;
}
.join-links a:hover { color: rgba(255,255,255,.8) !important; }

/* ═══════════════════════════════════════════════
   MOBILE — natural flow, no snap
   ═══════════════════════════════════════════════ */
@media (max-width: 767px) {
  .vp { padding: 2rem 1.2rem; }
  .hero { min-height: 80vh; }
  .hero-headline { font-size: clamp(1.8rem, 7vw, 2.6rem); }
  .hero-identity { flex-direction: column; text-align: center; }
  .hero-id { text-align: center; }
  .update-item { flex-direction: column; gap: .1rem; }
  .update-date { min-width: auto; }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .vp { padding: 2.5rem clamp(2rem, 4vw, 3rem); }
  .hero { min-height: 70vh; }
  .research-areas { grid-template-columns: repeat(2, 1fr); }
}

/* Skip nav */
.skip-nav {
  position: absolute; top: -100%;
  left: 50%; transform: translateX(-50%);
  padding: .6rem 1.5rem; border-radius: 980px;
  background: #06c; color: #fff !important;
  font-size: .9rem; font-weight: 600;
  text-decoration: none !important;
  z-index: 9999;
}
.skip-nav:focus { top: 1rem; }
</style>

<a class="skip-nav" href="#research">Skip to research</a>

<!-- ═══════════ 1. HERO ═══════════ -->
<section class="vp hero" aria-label="Introduction">
<div class="vp-in">

  <div class="hero-identity">
    <img class="hero-photo" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div class="hero-id">
      <div class="hero-name">Yuwen Huang</div>
      <div class="hero-aff">Postdoctoral Researcher, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></div>
      <div class="hero-news"><strong>May 2026</strong> — Joining <a href="https://www.hkust-gz.edu.cn/">HKUST (Guangzhou)</a> as Assistant Professor</div>
    </div>
  </div>

  <h1 class="hero-headline">Provable methods for structured inference and optimization</h1>

  <p class="hero-sub">Graphical models · Combinatorics · Tensor networks · Quantum systems · Machine learning</p>

  <div class="hero-cta">
    <a class="btn btn-light" href="#positions">Open positions</a>
    <a class="btn btn-ghost" href="#research">Selected research</a>
  </div>

</div>
</section>

<!-- ═══════════ 2. RESEARCH ═══════════ -->
<section class="vp research" aria-label="Research areas">
<div class="vp-in">

  <div class="sec-label">Research</div>
  <h2 class="sec-heading">Three core areas</h2>
  <p class="sec-desc">From mathematical structure to scalable computation.</p>

  <div class="research-areas">

    <div class="ra">
      <div class="ra-name">Structured inference</div>
      <div class="ra-desc">Message passing, Bethe methods, and graph covers for inference and counting on graphical models.</div>
      <div class="ra-topics">Uncertainty · Counting · Graph covers</div>
    </div>

    <div class="ra">
      <div class="ra-name">Provable optimization</div>
      <div class="ra-desc">Permanent bounds and algorithmic guarantees for hard combinatorial problems.</div>
      <div class="ra-topics">Convex / nonconvex · Permanent bounds · Decisions</div>
    </div>

    <div class="ra">
      <div class="ra-name">Quantum &amp; tensors</div>
      <div class="ra-desc">Tensor networks and distributed quantum systems for scalable high-dimensional computation.</div>
      <div class="ra-topics">Tensor networks · Quantum systems · Scalability</div>
    </div>

  </div>

</div>
</section>

<!-- ═══════════ 3. SELECTED WORK ═══════════ -->
<section class="vp work" id="research" aria-label="Selected research">
<div class="vp-in">

  <div class="sec-label">Selected work</div>
  <h2 class="sec-heading">Representative papers</h2>

  <div class="work-featured">
    <div class="work-featured-title">Graphical models and Bethe methods</div>
    <div class="work-featured-desc">Graph covers, message passing, and Bethe approximation for inference and counting on structured graphical models — our longest-running research thread.</div>
    <div class="work-cites">
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
      <div class="work-cites">
        <a class="cite" href="https://arxiv.org/abs/2107.01816">[ISIT 2021]</a>
        <a class="cite" href="https://arxiv.org/abs/2506.16250">[TIT-sub]</a>
        <a class="cite" href="https://arxiv.org/abs/2508.05712">[ICML 2025]</a>
        <a class="cite" href="https://arxiv.org/abs/2603.07673">[QUANTUM-sub]</a>
      </div>
    </div>
    <div class="wa">
      <div class="wa-name">Optimization</div>
      <div class="wa-desc">Permanent bounds and guarantees for hard problems.</div>
      <div class="work-cites">
        <a class="cite" href="https://arxiv.org/abs/2306.02280">[ISIT 2023]</a>
        <a class="cite" href="https://arxiv.org/abs/2306.02280">[TIT 2024]</a>
        <a class="cite" href="https://arxiv.org/abs/2508.05712">[ICML 2025]</a>
      </div>
    </div>
    <div class="wa">
      <div class="wa-name">Quantum systems</div>
      <div class="wa-desc">Distributed quantum optimization and inference.</div>
      <div class="work-cites">
        <a class="cite" href="https://arxiv.org/abs/2603.07673">[QUANTUM-sub]</a>
      </div>
    </div>
  </div>

  <div class="work-more">
    <a href="{{ '/publications/' | relative_url }}">View all publications</a>
  </div>

</div>
</section>

<!-- ═══════════ 4. UPDATES ═══════════ -->
<section class="vp updates" aria-label="Latest updates">
<div class="vp-in">

  <div class="sec-label">Latest</div>
  <h2 class="sec-heading">What's new</h2>

  <div class="update-list">
    <div class="update-item">
      <div class="update-date">May 2026</div>
      <div class="update-content">
        <div class="update-title">Joining HKUST (Guangzhou) as Assistant Professor <span class="update-badge">Starting</span></div>
        <div class="update-venue">DSA Thrust, Information Hub</div>
      </div>
    </div>
    <div class="update-item">
      <div class="update-date">Mar 2026</div>
      <div class="update-content">
        <div class="update-title"><a href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">Scalable Distributed Quantum Optimization</a></div>
        <div class="update-venue">Submitted to Quantum</div>
      </div>
    </div>
    <div class="update-item">
      <div class="update-date">Jul 2025</div>
      <div class="update-content">
        <div class="update-title"><a href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">Graph-Cover-based Characterization of the Bethe Partition Function</a></div>
        <div class="update-venue">Submitted to IEEE Trans. Inf. Theory</div>
      </div>
    </div>
    <div class="update-item">
      <div class="update-date">2024</div>
      <div class="update-content">
        <div class="update-title"><a href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">Degree-M Bethe &amp; Sinkhorn Permanent</a></div>
        <div class="update-venue">Published in IEEE Trans. Inf. Theory</div>
      </div>
    </div>
  </div>

</div>
</section>

<!-- ═══════════ 5. JOIN ═══════════ -->
<section class="vp join" id="positions" aria-label="Open positions">
<div class="vp-in">

  <div class="sec-label">Open positions</div>
  <h2 class="join-heading">Join the group</h2>
  <p class="join-desc">Recruiting for May 2026 at the DSA Thrust, Information Hub, HKUST (Guangzhou).</p>

  <div class="join-roles">
    <span class="join-role">Research Assistant</span>
    <span class="join-role">MPhil</span>
    <span class="join-role">PhD</span>
    <span class="join-role">Postdoc</span>
  </div>

  <div class="join-cta">
    <a class="btn btn-white" href="mailto:{{ site.author.email }}">Get in touch</a>
  </div>

  <div class="join-links">
    <a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
    <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
  </div>

</div>
</section>
