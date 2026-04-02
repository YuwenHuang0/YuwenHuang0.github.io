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
   LAYOUT — full-bleed, wide inner
   ═══════════════════════════════════════════════ */
.sec {
  width: 100%;
  padding: clamp(3rem, 6vw, 4.5rem) clamp(1.5rem, 5vw, 6rem);
}
.sec-in {
  max-width: 1600px;
  margin: 0 auto;
}

/* ═══════════════════════════════════════════════
   HERO — dark, compact
   ═══════════════════════════════════════════════ */
.hero-sec {
  background: #0d0d0d;
  color: #f5f5f7;
  min-height: auto;
  display: flex;
  align-items: center;
  text-align: center;
  padding-top: clamp(4rem, 8vw, 6rem);
  padding-bottom: clamp(3.5rem, 7vw, 5rem);
  position: relative;
  overflow: hidden;
}
.hero-sec::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(99,102,241,.08) 0%, transparent 60%);
  pointer-events: none;
}
.hero-sec .sec-in {
  width: 100%;
  position: relative;
  z-index: 1;
}

/* Identity row */
.hero-top {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.2rem;
  margin-bottom: 1.8rem;
}
.hero-photo {
  width: 80px; height: 80px;
  border-radius: 50%; object-fit: cover;
  border: 2px solid rgba(255,255,255,.15);
  flex-shrink: 0;
}
.hero-id { text-align: left; }
.hero-name {
  font-size: 1.5rem; font-weight: 600; color: #f5f5f7; line-height: 1.2;
  letter-spacing: -.02em;
}
.hero-aff {
  font-size: 1.1rem; color: rgba(255,255,255,.7); line-height: 1.4; margin-top: .15rem;
}
.hero-aff a { color: rgba(255,255,255,.8); font-weight: 500; }
.hero-aff a:hover { color: #fff; }

/* Announcement pill */
.hero-news {
  display: inline-flex; align-items: baseline;
  gap: .3rem;
  padding: .45rem 1.1rem;
  border-radius: 980px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.18);
  font-size: 1.05rem; line-height: 1.4;
  color: #e5e5e7;
  margin-bottom: 2rem;
}
@media (min-width: 920px) {
  .hero-news { white-space: nowrap; }
}
.hero-news strong { color: #f0c8a0; font-weight: 700; }
.hero-news a { color: #fff; font-weight: 600; }
.hero-news a:hover { text-decoration: underline; }

/* Headline */
.hero-h {
  font-size: clamp(2.2rem, 4.5vw, 3.8rem);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -.035em;
  color: #fff;
}
@media (min-width: 880px) {
  .hero-h { white-space: nowrap; }
}

/* Subtitle */
.hero-desc {
  margin-top: 1rem;
  font-size: clamp(1.15rem, 1.8vw, 1.4rem);
  line-height: 1.5;
  color: rgba(255,255,255,.9);
  font-weight: 500;
  letter-spacing: -.005em;
}

/* Keywords */
.hero-kw {
  display: flex; flex-wrap: wrap; gap: .45rem;
  justify-content: center;
  margin-top: 1.5rem;
}
.kw {
  padding: .4rem 1rem;
  border-radius: 980px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.15);
  font-size: 1rem; font-weight: 500;
  color: rgba(255,255,255,.85);
  letter-spacing: -.005em;
}

/* CTA */
.hero-act {
  display: flex; flex-wrap: wrap; gap: .8rem;
  justify-content: center;
  margin-top: 2rem;
}
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  height: 3rem; padding: 0 1.8rem;
  border-radius: 980px;
  font-size: 1rem; font-weight: 600;
  cursor: pointer;
  text-decoration: none !important;
  transition: background .2s, box-shadow .2s, transform .15s;
  letter-spacing: -.005em;
}
.btn:hover { transform: scale(1.02); }
.btn-fill {
  background: #f5f5f7; color: #0d0d0d !important;
}
.splash .page__content .btn-fill,
.splash .page__content .btn-fill:hover {
  color: #0d0d0d !important;
  text-decoration: none !important;
}
.btn-fill:hover { background: #fff; box-shadow: 0 4px 16px rgba(255,255,255,.15); }
.btn-out {
  background: transparent;
  border: 1.5px solid rgba(255,255,255,.4);
  color: #fff !important;
}
.splash .page__content .btn-out,
.splash .page__content .btn-out:hover {
  color: rgba(255,255,255,.9) !important;
  text-decoration: none !important;
}
.btn-out:hover { background: rgba(255,255,255,.06); border-color: rgba(255,255,255,.4); }

/* ═══════════════════════════════════════════════
   METRICS STRIP — credibility numbers
   ═══════════════════════════════════════════════ */
.metrics-strip {
  width: 100%;
  padding: clamp(1.8rem, 3vw, 2.5rem) clamp(1.5rem, 5vw, 6rem);
  background: #161617;
  border-top: 1px solid rgba(255,255,255,.06);
}
.metrics-in {
  max-width: 1600px; margin: 0 auto;
  display: flex; justify-content: center;
  flex-wrap: wrap;
  gap: clamp(2rem, 5vw, 5rem);
}
.metric { text-align: center; min-width: 110px; }
.metric-num {
  font-size: clamp(2rem, 3.5vw, 3rem);
  font-weight: 800; letter-spacing: -.04em;
  line-height: 1; color: #fff;
}
.metric-label {
  font-size: .78rem; font-weight: 600;
  letter-spacing: .06em; text-transform: uppercase;
  color: rgba(255,255,255,.5); margin-top: .35rem;
}
.metric-detail {
  font-size: .8rem; color: rgba(255,255,255,.5); margin-top: .15rem;
}

/* ═══════════════════════════════════════════════
   INSTITUTION LOGOS — trust bar
   ═══════════════════════════════════════════════ */
.logo-bar {
  width: 100%;
  padding: clamp(1rem, 2vw, 1.5rem) clamp(1.5rem, 5vw, 6rem);
  background: #f5f5f7;
}
.logo-bar-in {
  max-width: 1600px; margin: 0 auto;
  display: flex; align-items: center; justify-content: center;
  flex-wrap: wrap;
  gap: clamp(1.2rem, 3vw, 3rem);
}
.logo-bar-label {
  font-size: .72rem; font-weight: 600;
  letter-spacing: .08em; text-transform: uppercase;
  color: #6e6e73; white-space: nowrap;
}
.logo-item {
  display: flex; align-items: center; gap: .4rem;
  opacity: .6; transition: opacity .3s;
  text-decoration: none !important;
}
.logo-item:hover { opacity: .9; }
.logo-icon {
  width: 26px; height: 26px; border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  font-size: .65rem; font-weight: 800; color: #fff; flex-shrink: 0;
}
.logo-name {
  font-size: .8rem; font-weight: 600;
  color: #424245; letter-spacing: -.005em;
}

/* ═══════════════════════════════════════════════
   LATEST UPDATES — timeline
   ═══════════════════════════════════════════════ */
.timeline { display: grid; gap: 0; }
.tl-item {
  display: grid; grid-template-columns: auto 1fr;
  gap: 1rem; padding: .8rem 0;
  border-bottom: 1px solid rgba(0,0,0,.04);
}
.tl-item:last-child { border-bottom: none; }
.tl-dot-col {
  display: flex; flex-direction: column; align-items: center;
  padding-top: .3rem;
}
.tl-dot {
  width: 9px; height: 9px; border-radius: 50%;
  background: #06c; flex-shrink: 0;
}
.tl-dot.tl-new { background: #30d158; }
.tl-dot.tl-upcoming { background: #ff9f0a; }
.tl-line {
  width: 1.5px; flex: 1;
  background: rgba(0,0,0,.08); margin-top: .3rem;
}
.tl-item:last-child .tl-line { display: none; }
.tl-date {
  font-size: .7rem; font-weight: 600;
  letter-spacing: .06em; text-transform: uppercase;
  color: #6e6e73; margin-bottom: .1rem;
}
.tl-title {
  font-size: .92rem; font-weight: 600;
  color: #1d1d1f; line-height: 1.35;
}
.tl-title a { color: #1d1d1f !important; text-decoration: none !important; }
.tl-title a:hover { color: #06c !important; }
.tl-venue { font-size: .8rem; color: #6e6e73; margin-top: .05rem; }
.tl-badge {
  display: inline-flex; padding: .1rem .45rem;
  border-radius: 980px; font-size: .62rem; font-weight: 700;
  letter-spacing: .04em; text-transform: uppercase;
  margin-left: .3rem; vertical-align: middle;
}
.badge-new { background: #e8fbe8; color: #1a7a2e; }
.badge-upcoming { background: #fff5e0; color: #946b14; }

/* ═══════════════════════════════════════════════
   SECTION TRANSITIONS — accent dividers
   ═══════════════════════════════════════════════ */
.sec-divider {
  width: 100%; height: 1px;
  background: linear-gradient(90deg, transparent 0%, rgba(0,102,204,.12) 20%, rgba(0,102,204,.2) 50%, rgba(0,102,204,.12) 80%, transparent 100%);
}
.sec-divider-dark {
  background: linear-gradient(90deg, transparent 0%, rgba(99,102,241,.1) 20%, rgba(99,102,241,.18) 50%, rgba(99,102,241,.1) 80%, transparent 100%);
}

/* ═══════════════════════════════════════════════
   DOT GRID TEXTURE — subtle depth
   ═══════════════════════════════════════════════ */
.dot-bg { position: relative; }
.dot-bg::after {
  content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  background-image: radial-gradient(circle, rgba(0,0,0,.035) 1px, transparent 1px);
  background-size: 22px 22px; pointer-events: none; z-index: 0;
}
.dot-bg > * { position: relative; z-index: 1; }

/* ═══════════════════════════════════════════════
   SECTION HEADERS — compact
   ═══════════════════════════════════════════════ */
.sec-hdr {
  margin-bottom: clamp(1.5rem, 3vw, 2.5rem);
}
.sec-label {
  font-size: .78rem; font-weight: 600;
  letter-spacing: .1em; text-transform: uppercase;
  color: #6e6e73;
  margin-bottom: .4rem;
}
.sec-title {
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 700; line-height: 1.08;
  letter-spacing: -.03em;
  color: #1d1d1f;
}
.sec-sub {
  margin-top: .5rem;
  font-size: clamp(1rem, 1.4vw, 1.12rem);
  line-height: 1.5;
  color: #6e6e73;
  max-width: 620px;
}

/* ═══════════════════════════════════════════════
   RESEARCH AREAS — compact cards
   ═══════════════════════════════════════════════ */
.area-bg { background: #f5f5f7; }

.areas {
  display: grid; gap: 1.2rem;
}
@media (min-width: 800px) {
  .areas { grid-template-columns: repeat(3, 1fr); }
}
.area {
  border-radius: 20px;
  overflow: hidden;
  display: flex; flex-direction: column;
  transition: box-shadow .3s ease, transform .3s ease;
  background: #fff;
  border: 1px solid rgba(0,0,0,.05);
}
.area:hover {
  box-shadow: 0 12px 40px rgba(0,0,0,.08);
  transform: translateY(-4px);
}

.area-vis {
  height: 180px;
  display: flex; align-items: center; justify-content: center;
  padding: 1.2rem;
}
.area-vis svg { width: 80%; height: 80%; }
.vis-teal  { background: linear-gradient(160deg, #e8f6fa 0%, #c3e6ef 100%); }
.vis-amber { background: linear-gradient(160deg, #fef8ec 0%, #fcefd0 100%); }
.vis-coral { background: linear-gradient(160deg, #fdf2ee 0%, #f8ddd2 100%); }

.area-body {
  padding: 1.4rem 1.6rem 1.6rem;
  display: flex; flex-direction: column; gap: .4rem; flex: 1;
}
.area-label {
  font-size: .72rem; font-weight: 700;
  letter-spacing: .08em; text-transform: uppercase;
}
.lbl-teal  { color: #17677a; }
.lbl-amber { color: #946b14; }
.lbl-coral { color: #a14430; }
.area h3 {
  font-size: 1.15rem; font-weight: 700; line-height: 1.2; color: #1d1d1f;
  letter-spacing: -.01em;
}
.area p {
  font-size: .92rem; line-height: 1.55; color: #6e6e73;
}
.area-tags {
  display: flex; flex-wrap: wrap; gap: .35rem;
  margin-top: auto; padding-top: .4rem;
}
.area-tags span {
  padding: .2rem .6rem; border-radius: 980px;
  background: #f5f5f7;
  font-size: .78rem; font-weight: 500; color: #424245;
}

/* ═══════════════════════════════════════════════
   PIPELINE — dark section, compact
   ═══════════════════════════════════════════════ */
.pipe-bg {
  background: #1d1d1f; color: #f5f5f7;
}
.pipe-bg .sec-label { color: rgba(255,255,255,.6); }
.pipe-bg .sec-title { color: #fff; }

.pipe {
  display: grid; gap: 1rem;
}
@media (min-width: 800px) {
  .pipe { grid-template-columns: repeat(4, 1fr); }
}
.step {
  padding: 1.5rem 1.4rem;
  border-radius: 18px;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.12);
  transition: background .3s ease;
}
.step:hover { background: rgba(255,255,255,.12); }
.step-n {
  font-size: .72rem; font-weight: 700;
  color: rgba(255,255,255,.55);
  margin-bottom: .7rem;
  letter-spacing: .06em;
}
.step h3 {
  font-size: 1.05rem; font-weight: 600;
  color: #fff; margin-bottom: .3rem;
  letter-spacing: -.005em;
}
.step p {
  font-size: .9rem; line-height: 1.55;
  color: rgba(255,255,255,.75);
}

/* ═══════════════════════════════════════════════
   SELECTED PAPERS — bento grid
   ═══════════════════════════════════════════════ */
.papers-bg { background: #fff; }

.papers {
  display: grid; gap: 1rem;
  grid-template-columns: 1fr;
}
@media (min-width: 800px) {
  .papers {
    grid-template-columns: repeat(3, 1fr);
  }
  .paper-featured {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: center;
  }
  .paper-featured .paper-featured-left { display: flex; flex-direction: column; gap: .4rem; }
  .paper-featured .paper-featured-right { display: flex; flex-direction: column; gap: .5rem; }
}
.paper {
  padding: 1.5rem;
  border-radius: 18px;
  background: #f5f5f7;
  border: 1px solid rgba(0,0,0,.04);
  display: flex; flex-direction: column; gap: .4rem;
  transition: box-shadow .3s ease, transform .3s ease;
}
.paper:hover {
  box-shadow: 0 12px 36px rgba(0,0,0,.07);
  transform: translateY(-3px);
}
/* Featured card — full-width dark banner */
.paper-featured {
  background: #1d1d1f;
  border: 1px solid rgba(255,255,255,.08);
  padding: clamp(1.8rem, 3vw, 2.5rem);
}
.paper-featured .paper-tag { background: rgba(255,255,255,.12); color: rgba(255,255,255,.8); }
.paper-featured h3 {
  font-size: clamp(1.15rem, 2vw, 1.45rem) !important;
  color: #fff !important;
}
.paper-featured p { color: rgba(255,255,255,.65) !important; font-size: .88rem; line-height: 1.5; }
.paper-featured .cite {
  background: rgba(255,255,255,.1);
  border-color: rgba(255,255,255,.15);
  color: rgba(255,255,255,.85) !important;
}
.paper-featured .cite:hover { background: rgba(255,255,255,.18); }
.paper-featured:hover { box-shadow: 0 16px 48px rgba(0,0,0,.3); }
/* Featured stats highlight */
.paper-featured-stats {
  display: flex; gap: 1.5rem; flex-wrap: wrap;
}
.pf-stat { text-align: center; }
.pf-stat-num {
  font-size: 1.6rem; font-weight: 800;
  color: #fff; letter-spacing: -.03em; line-height: 1;
}
.pf-stat-label {
  font-size: .68rem; font-weight: 600;
  color: rgba(255,255,255,.5); text-transform: uppercase;
  letter-spacing: .05em; margin-top: .2rem;
}

.paper-tag {
  display: inline-flex; width: fit-content;
  padding: .18rem .6rem; border-radius: 980px;
  font-size: .7rem; font-weight: 700;
  letter-spacing: .05em; text-transform: uppercase;
}
.pt-teal  { background: #ddf0f5; color: #17677a; }
.pt-amber { background: #fef6e0; color: #946b14; }
.pt-coral { background: #fdf0ec; color: #a14430; }
.pt-green { background: #e9f3ec; color: #3a7049; }

.paper h3 {
  font-size: 1.02rem; font-weight: 700; line-height: 1.22; color: #1d1d1f;
  letter-spacing: -.01em;
}
.paper p {
  font-size: .88rem; line-height: 1.5; color: #6e6e73;
}
.paper-cites {
  display: flex; flex-wrap: wrap; gap: .35rem;
  margin-top: auto; padding-top: .4rem;
}
.cite {
  display: inline-flex; align-items: center;
  padding: .4rem .7rem; border-radius: 980px;
  min-height: 2.2rem;
  background: #fff;
  color: #06c !important;
  font-size: .78rem; font-weight: 600;
  text-decoration: none !important;
  transition: background .2s;
  letter-spacing: -.005em;
  border: 1px solid rgba(0,0,0,.06);
}
.cite:hover { background: #e8e8ed; }

/* ═══════════════════════════════════════════════
   RECRUIT — compact, centered
   ═══════════════════════════════════════════════ */
.recruit-bg {
  background: #f5f5f7;
}

.recruit-center { text-align: center; }
.recruit-center .sec-hdr { margin-bottom: clamp(1rem, 2.5vw, 2rem); }
.recruit-center .sec-title { max-width: none; }
.recruit-center .sec-sub {
  max-width: none;
  margin-left: auto; margin-right: auto;
  font-size: clamp(.95rem, 1.3vw, 1.08rem);
}

.roles {
  display: grid; gap: 1rem;
  margin-top: 2rem; text-align: left;
}
@media (min-width: 800px) {
  .roles { grid-template-columns: repeat(4, 1fr); }
}
.role {
  padding: 1.5rem 1.4rem; border-radius: 18px;
  background: #fff;
  border: 1px solid rgba(0,0,0,.05);
  display: flex; flex-direction: column; gap: .35rem;
  transition: box-shadow .3s ease, transform .3s ease;
}
.role:hover {
  box-shadow: 0 8px 28px rgba(0,0,0,.06);
  transform: translateY(-3px);
}
.role h3 {
  font-size: 1.1rem; font-weight: 700; color: #1d1d1f;
  letter-spacing: -.01em;
}
.role p {
  font-size: .9rem; line-height: 1.55; color: #6e6e73;
}

.recruit-cta { margin-top: 2rem; }
.recruit-cta .btn-fill {
  background: #1d1d1f; color: #fff !important;
}
.splash .page__content .recruit-cta .btn-fill,
.splash .page__content .recruit-cta .btn-fill:hover {
  color: #fff !important;
  text-decoration: none !important;
}
.recruit-cta .btn-fill:hover { background: #000; box-shadow: 0 4px 16px rgba(0,0,0,.2); }
.recruit-links {
  display: flex; justify-content: center; flex-wrap: wrap;
  gap: .3rem 1.1rem;
  margin-top: 1rem;
}
.recruit-links a {
  font-size: .9rem; font-weight: 500;
  color: #06c !important; text-decoration: none !important;
}
.recruit-links a:hover { text-decoration: underline !important; }

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
.skip-nav:focus {
  top: 1rem;
}
</style>

<a class="skip-nav" href="#research">Skip to research</a>

<!-- ═══════════ HERO ═══════════ -->
<section class="sec hero-sec" aria-label="Introduction">
<div class="sec-in">

  <div class="hero-top">
    <img class="hero-photo" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div class="hero-id">
      <div class="hero-name">Yuwen Huang</div>
      <div class="hero-aff">Postdoctoral Researcher, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></div>
    </div>
  </div>

  <div class="hero-news">
    <strong>May 2026</strong> — Joining
    <a href="https://www.hkust-gz.edu.cn/">HKUST (Guangzhou)</a>
    as Assistant Professor
    (<a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>,
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>)
  </div>

  <h1 class="hero-h">Provable methods for structured inference and optimization</h1>

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

<!-- ═══════════ METRICS STRIP ═══════════ -->
<div class="metrics-strip">
<div class="metrics-in">
  <div class="metric">
    <div class="metric-num">14+</div>
    <div class="metric-label">Publications</div>
    <div class="metric-detail">Journal &amp; Conference</div>
  </div>
  <div class="metric">
    <div class="metric-num">3</div>
    <div class="metric-label">Research Areas</div>
    <div class="metric-detail">Inference · Optimization · Quantum</div>
  </div>
  <div class="metric">
    <div class="metric-num">5+</div>
    <div class="metric-label">Top Venues</div>
    <div class="metric-detail">IEEE TIT · ISIT · ICML</div>
  </div>
  <div class="metric">
    <div class="metric-num">6</div>
    <div class="metric-label">Invited Talks</div>
    <div class="metric-detail">International &amp; Domestic</div>
  </div>
</div>
</div>

<!-- ═══════════ INSTITUTION LOGOS ═══════════ -->
<div class="logo-bar">
<div class="logo-bar-in">
  <span class="logo-bar-label">Affiliations &amp; Venues</span>
  <a class="logo-item" href="https://www.cuhk.edu.hk/" style="text-decoration:none !important">
    <span class="logo-icon" style="background:#6b2fa0;">CU</span>
    <span class="logo-name">CUHK</span>
  </a>
  <a class="logo-item" href="https://www.hkust-gz.edu.cn/" style="text-decoration:none !important">
    <span class="logo-icon" style="background:#003d7c;">HK</span>
    <span class="logo-name">HKUST (GZ)</span>
  </a>
  <a class="logo-item" href="https://www.scut.edu.cn/" style="text-decoration:none !important">
    <span class="logo-icon" style="background:#8b1a1a;">SC</span>
    <span class="logo-name">SCUT</span>
  </a>
  <span class="logo-item">
    <span class="logo-icon" style="background:#00629b;">IE</span>
    <span class="logo-name">IEEE</span>
  </span>
  <span class="logo-item">
    <span class="logo-icon" style="background:#b31b1b;">IC</span>
    <span class="logo-name">ICML</span>
  </span>
</div>
</div>

<!-- ═══════════ LATEST UPDATES ═══════════ -->
<section class="sec" style="background:#fff;" aria-label="Latest updates">
<div class="sec-in">
  <div class="sec-hdr">
    <div class="sec-label">Latest updates</div>
    <h2 class="sec-title">What's new</h2>
  </div>
  <div class="timeline">
    <div class="tl-item">
      <div class="tl-dot-col"><div class="tl-dot tl-new"></div><div class="tl-line"></div></div>
      <div class="tl-content">
        <div class="tl-date">May 2026</div>
        <div class="tl-title">Joining HKUST (Guangzhou) as Assistant Professor <span class="tl-badge badge-upcoming">Starting</span></div>
        <div class="tl-venue">DSA Thrust, Information Hub</div>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot-col"><div class="tl-dot"></div><div class="tl-line"></div></div>
      <div class="tl-content">
        <div class="tl-date">Mar 2026</div>
        <div class="tl-title"><a href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">Scalable Distributed Quantum Optimization</a></div>
        <div class="tl-venue">Submitted to Quantum</div>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot-col"><div class="tl-dot"></div><div class="tl-line"></div></div>
      <div class="tl-content">
        <div class="tl-date">Jul 2025</div>
        <div class="tl-title"><a href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">Graph-Cover-based Characterization of the Bethe Partition Function</a></div>
        <div class="tl-venue">Submitted to IEEE Trans. Inf. Theory</div>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot-col"><div class="tl-dot"></div><div class="tl-line"></div></div>
      <div class="tl-content">
        <div class="tl-date">2024</div>
        <div class="tl-title"><a href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">Degree-M Bethe &amp; Sinkhorn Permanent</a></div>
        <div class="tl-venue">Published in IEEE Trans. Inf. Theory, 2024</div>
      </div>
    </div>
  </div>
</div>
</section>

<!-- ═══════════ RESEARCH AREAS ═══════════ -->
<section class="sec area-bg" aria-label="Research areas">
<div class="sec-in">
  <div class="sec-hdr">
    <div class="sec-label">Research</div>
    <h2 class="sec-title">Three core areas</h2>
    <p class="sec-sub">From mathematical structure to scalable computation.</p>
  </div>

  <div class="areas">

    <article class="area">
      <div class="area-vis vis-teal">
        <svg viewBox="0 0 280 140" fill="none" aria-label="Graphical model illustration">
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
        <p>Message passing, Bethe methods, and graph covers for inference and counting.</p>
        <div class="area-tags"><span>Uncertainty</span><span>Counting</span><span>Graph covers</span></div>
      </div>
    </article>

    <article class="area">
      <div class="area-vis vis-amber">
        <svg viewBox="0 0 280 140" fill="none" aria-label="Optimization landscape illustration">
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
        <p>Permanent bounds and algorithmic guarantees for hard combinatorial problems.</p>
        <div class="area-tags"><span>Convex / nonconvex</span><span>Permanent bounds</span><span>Decisions</span></div>
      </div>
    </article>

    <article class="area">
      <div class="area-vis vis-coral">
        <svg viewBox="0 0 280 140" fill="none" aria-label="Tensor network illustration">
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
        <p>Tensor networks and distributed quantum systems for scalable computation.</p>
        <div class="area-tags"><span>Tensor networks</span><span>Quantum systems</span><span>Scalability</span></div>
      </div>
    </article>

  </div>
</div>
</section>

<!-- ═══════════ PIPELINE ═══════════ -->
<section class="sec pipe-bg" aria-label="Research pipeline">
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

<!-- ═══════════ SELECTED RESEARCH — bento grid ═══════════ -->
<section class="sec papers-bg" id="research">
<div class="sec-in">
  <div class="sec-hdr">
    <div class="sec-label">Selected research</div>
    <h2 class="sec-title">Representative papers</h2>
  </div>
  <div class="papers">

    <article class="paper paper-featured">
      <div class="paper-featured-left">
        <span class="paper-tag pt-teal">Inference — Core Theme</span>
        <h3>Graphical models and Bethe methods</h3>
        <p>Graph covers, message passing, and Bethe approximation for inference and counting on structured graphical models — our longest-running research thread.</p>
        <div class="paper-cites">
          <a class="cite" href="{{ '/publication/characterizing-bethe-partition-factor-graphs' | relative_url }}">[ISIT 2020]</a>
          <a class="cite" href="{{ '/publication/bethe-free-energy-global-minimum' | relative_url }}">[ITW 2022]</a>
          <a class="cite" href="{{ '/publication/bethe-partition-spa-stable-polynomials' | relative_url }}">[ISIT 2024]</a>
          <a class="cite" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-sub]</a>
        </div>
      </div>
      <div class="paper-featured-right">
        <div class="paper-featured-stats">
          <div class="pf-stat"><div class="pf-stat-num">4</div><div class="pf-stat-label">Papers</div></div>
          <div class="pf-stat"><div class="pf-stat-num">2020–25</div><div class="pf-stat-label">Span</div></div>
          <div class="pf-stat"><div class="pf-stat-num">3</div><div class="pf-stat-label">Venues</div></div>
        </div>
      </div>
    </article>

    <article class="paper">
      <span class="paper-tag pt-amber">Optimization</span>
      <h3>Optimization and combinatorial structure</h3>
      <p>Permanent bounds and guarantees for hard problems.</p>
      <div class="paper-cites">
        <a class="cite" href="{{ '/publication/bounding-permanent-degree-m-bethe' | relative_url }}">[ISIT 2023]</a>
        <a class="cite" href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">[TIT 2024]</a>
        <a class="cite" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML 2025]</a>
      </div>
    </article>

    <article class="paper">
      <span class="paper-tag pt-coral">Tensor methods</span>
      <h3>Tensor networks and quantum-enabled inference</h3>
      <p>Tensor-network methods for high-dimensional computation.</p>
      <div class="paper-cites">
        <a class="cite" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT 2021]</a>
        <a class="cite" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
      </div>
    </article>

    <article class="paper">
      <span class="paper-tag pt-green">Quantum systems</span>
      <h3>Distributed quantum systems</h3>
      <p>Distributed quantum optimization and inference.</p>
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
    <p class="sec-sub">Recruiting RAs, MPhil/PhD students, and one Postdoc for May 2026 at the DSA Thrust, Information Hub, HKUST (Guangzhou).</p>
  </div>
  <div class="roles">
    <div class="role"><h3>RA</h3><p>Research training for graduate study or industry.</p></div>
    <div class="role"><h3>MPhil</h3><p>Independent research with publication-focused training.</p></div>
    <div class="role"><h3>PhD</h3><p>Deep problems, broad collaboration, long-term support.</p></div>
    <div class="role"><h3>Postdoc</h3><p>Shape an agenda, co-mentor, prepare for faculty searches.</p></div>
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
