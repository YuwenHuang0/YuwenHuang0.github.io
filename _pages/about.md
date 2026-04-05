---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ── Reset ALL theme defaults inside splash ── */
.splash .page__content { font-family: -apple-system, "SF Pro Display", "Helvetica Neue", "Inter", sans-serif; max-width: none !important; padding: 0 !important; margin: 0 !important; -webkit-font-smoothing: antialiased; color: #1d1d1f; }
.splash .page__content p, .splash .page__content h1, .splash .page__content h2, .splash .page__content h3, .splash .page__content h4 { margin: 0 !important; padding: 0 !important; border: none !important; line-height: 1.2; }
.splash .page__content a { text-decoration: none; }

/* ── Sections ── */
.s { width: 100%; padding: .7rem clamp(1.2rem, 4vw, 5rem); }
.s-in { max-width: 960px; width: 100%; margin: 0 auto; }

/* ── Dark section text — force white ── */
.s-dark { background: #0d0d0d; color: #fff; }
.s-dark h2, .s-dark h3, .s-dark p, .s-dark div, .s-dark span, .s-dark a { color: #fff; }

/* ── HERO ── */
.hero { padding-top: 1.5rem; padding-bottom: 1rem; text-align: center; }
.hero .s-in { display: flex; flex-direction: column; align-items: center; }
.h-row { display: flex; align-items: center; gap: .7rem; margin-bottom: .5rem; }
.h-photo { width: 56px; height: 56px; border-radius: 50%; object-fit: cover; border: 2px solid rgba(255,255,255,.15); }
.h-id { text-align: left; }
.h-name { font-size: 1.1rem; font-weight: 700; }
.h-aff { font-size: .85rem; color: rgba(255,255,255,.7) !important; margin-top: .05rem; }
.h-aff a { color: rgba(255,255,255,.8) !important; font-weight: 500; }
.h-news { font-size: .8rem; color: rgba(255,255,255,.55) !important; margin-top: .1rem; }
.h-news strong { color: #f0c8a0 !important; font-weight: 700; }
.h-news a { color: rgba(255,255,255,.7) !important; }
.h-intro { font-size: 1.05rem; line-height: 1.5; color: rgba(255,255,255,.85) !important; max-width: 480px; text-align: center; }
.h-cta { display: flex; gap: .4rem; margin-top: .6rem; }
.btn { display: inline-flex; align-items: center; height: 2.2rem; padding: 0 1.1rem; border-radius: 980px; font-size: .84rem; font-weight: 600; cursor: pointer; text-decoration: none !important; transition: all .2s; }
.btn-w { background: #fff; color: #000 !important; }
.splash .page__content .btn-w, .splash .page__content .btn-w:hover { color: #000 !important; text-decoration: none !important; }
.btn-o { background: transparent; border: 1.5px solid rgba(255,255,255,.3); color: #fff !important; }
.splash .page__content .btn-o, .splash .page__content .btn-o:hover { color: #fff !important; text-decoration: none !important; }

/* ── Light section ── */
.s-light { background: #fff; }
.s-alt { background: #f5f5f7; }

/* ── Section headers ── */
.sh { font-size: .65rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #86868b; margin-bottom: .15rem; }
.s-dark .sh { color: rgba(255,255,255,.5) !important; }
.sh2 { font-size: 1.3rem; font-weight: 800; letter-spacing: -.02em; color: #000; }
.s-dark .sh2 { color: #fff !important; }

/* ── RESEARCH — 3-col text ── */
.r-grid { display: grid; gap: .5rem; margin-top: .4rem; }
@media (min-width: 700px) { .r-grid { grid-template-columns: repeat(3, 1fr); gap: 1rem; } }
.r-name { font-size: .95rem; font-weight: 700; color: #000; }
.r-desc { font-size: .82rem; line-height: 1.4; color: #424245; margin-top: .1rem; }

/* ── WORK — papers ── */
.wf { margin-top: .3rem; padding-bottom: .3rem; border-bottom: 1px solid rgba(255,255,255,.1); }
.wf-t { font-size: 1rem; font-weight: 700; color: #fff !important; }
.wf-d { font-size: .82rem; line-height: 1.4; color: rgba(255,255,255,.65) !important; margin-top: .1rem; }
.wc { display: flex; flex-wrap: wrap; gap: .2rem; margin-top: .25rem; }
.cite { display: inline-flex; padding: .15rem .4rem; border-radius: 980px; background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.15); color: rgba(255,255,255,.85) !important; font-size: .68rem; font-weight: 600; text-decoration: none !important; transition: all .15s; }
.cite:hover { background: rgba(255,255,255,.2); color: #fff !important; }
.w-grid { display: grid; gap: .4rem; margin-top: .4rem; }
@media (min-width: 700px) { .w-grid { grid-template-columns: repeat(3, 1fr); } }
.wa-n { font-size: .88rem; font-weight: 700; color: #fff !important; }
.wa-d { font-size: .76rem; line-height: 1.3; color: rgba(255,255,255,.55) !important; margin-top: .05rem; }
.w-more { margin-top: .4rem; text-align: center; }
.w-more a { font-size: .82rem; font-weight: 600; color: rgba(255,255,255,.6) !important; text-decoration: none !important; }
.w-more a:hover { color: #fff !important; }
.w-more a::after { content: " →"; }

/* ── UPDATES — minimal rows ── */
.u-list { margin-top: .25rem; }
.u-row { display: flex; gap: 1rem; padding: .2rem 0; border-bottom: 1px solid rgba(0,0,0,.06); align-items: baseline; }
.u-row:first-child { border-top: 1px solid rgba(0,0,0,.06); }
.u-dt { font-size: .74rem; font-weight: 700; color: #6e6e73; min-width: 68px; flex-shrink: 0; }
.u-tt { font-size: .84rem; font-weight: 600; color: #000; line-height: 1.2; }
.u-tt a { color: #000 !important; text-decoration: none !important; }
.u-tt a:hover { color: #06c !important; }
.u-v { font-size: .72rem; color: #6e6e73; }

/* ── JOIN — white on black, large & clear ── */
.join { padding-top: 1.2rem; padding-bottom: 1.2rem; }
.join .s-in { display: flex; flex-direction: column; align-items: center; text-align: center; }
.join-h { font-size: 1.8rem !important; font-weight: 800 !important; color: #fff !important; letter-spacing: -.03em; }
.join-d { font-size: .9rem; line-height: 1.4; color: rgba(255,255,255,.75) !important; max-width: 440px; margin-top: .3rem; }
.join-perks { display: grid; gap: .15rem; margin-top: .5rem; text-align: left; max-width: 420px; width: 100%; }
.join-pk { display: flex; align-items: baseline; gap: .35rem; font-size: .84rem; line-height: 1.3; color: rgba(255,255,255,.9) !important; }
.join-pk::before { content: "→"; color: #f0c8a0; font-weight: 700; }
.join-roles { display: flex; gap: .25rem; justify-content: center; margin-top: .5rem; }
.join-role { padding: .2rem .65rem; border-radius: 980px; border: 1.5px solid rgba(255,255,255,.3); font-size: .78rem; font-weight: 700; color: #fff !important; }
.join-cta { margin-top: .5rem; }
.btn-a { background: #f0c8a0; color: #000 !important; font-weight: 800; font-size: .88rem; height: 2.4rem; padding: 0 1.4rem; }
.splash .page__content .btn-a, .splash .page__content .btn-a:hover { color: #000 !important; text-decoration: none !important; }
.btn-a:hover { background: #f5d5b3; }
.join-links { display: flex; gap: .6rem; margin-top: .3rem; }
.join-links a { font-size: .74rem; font-weight: 600; color: rgba(255,255,255,.5) !important; text-decoration: none !important; }
.join-links a:hover { color: #fff !important; }

/* ── Mobile ── */
@media (max-width: 700px) {
  .s { padding: .5rem .8rem; }
  .h-row { flex-direction: column; text-align: center; }
  .h-id { text-align: center; }
  .u-row { flex-direction: column; gap: 0; }
  .u-dt { min-width: auto; }
}

.skip-nav { position: absolute; top: -100%; left: 50%; transform: translateX(-50%); padding: .4rem 1rem; border-radius: 980px; background: #06c; color: #fff !important; font-size: .8rem; font-weight: 600; text-decoration: none !important; z-index: 9999; }
.skip-nav:focus { top: .6rem; }
</style>

<a class="skip-nav" href="#research">Skip to research</a>

<section class="s s-dark hero">
<div class="s-in">
  <div class="h-row">
    <img class="h-photo" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div class="h-id">
      <div class="h-name">Yuwen Huang</div>
      <div class="h-aff">Postdoc, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></div>
      <div class="h-news"><strong>May 2026</strong> — Joining <a href="https://www.hkust-gz.edu.cn/">HKUST (GZ)</a> as Assistant Professor</div>
    </div>
  </div>
  <p class="h-intro">Provable algorithms for inference, optimization, and quantum computation.</p>
  <div class="h-cta">
    <a class="btn btn-w" href="#positions">Open positions</a>
    <a class="btn btn-o" href="#research">Research</a>
  </div>
</div>
</section>

<section class="s s-light">
<div class="s-in">
  <div class="sh">Research</div>
  <h2 class="sh2">Three core areas</h2>
  <div class="r-grid">
    <div><div class="r-name">Structured inference</div><div class="r-desc">Bethe methods, graph covers, and message passing for counting and inference.</div></div>
    <div><div class="r-name">Provable optimization</div><div class="r-desc">Permanent bounds and guarantees for hard combinatorial problems.</div></div>
    <div><div class="r-name">Quantum &amp; tensors</div><div class="r-desc">Tensor networks and distributed quantum systems for scalable computation.</div></div>
  </div>
</div>
</section>

<section class="s s-dark" id="research">
<div class="s-in">
  <div class="sh">Selected work</div>
  <h2 class="sh2">Representative papers</h2>
  <div class="wf">
    <div class="wf-t">Graphical models and Bethe methods</div>
    <div class="wf-d">Graph covers and Bethe approximation for inference and counting — our longest-running thread.</div>
    <div class="wc">
      <a class="cite" href="https://ieeexplore.ieee.org/document/9174508/">[ISIT'20]</a>
      <a class="cite" href="https://arxiv.org/abs/2107.01816">[ISIT'21]</a>
      <a class="cite" href="https://ieeexplore.ieee.org/document/9965874/">[ITW'22]</a>
      <a class="cite" href="https://arxiv.org/abs/2306.02280">[ISIT'23]</a>
      <a class="cite" href="https://ieeexplore.ieee.org/document/10619603/">[ISIT'24]</a>
      <a class="cite" href="https://arxiv.org/abs/2306.02280">[TIT'24]</a>
      <a class="cite" href="https://arxiv.org/abs/2506.16250">[TIT-sub]</a>
    </div>
  </div>
  <div class="w-grid">
    <div><div class="wa-n">Tensor methods</div><div class="wa-d">High-dimensional computation via tensor networks.</div><div class="wc"><a class="cite" href="https://arxiv.org/abs/2107.01816">[ISIT'21]</a><a class="cite" href="https://arxiv.org/abs/2506.16250">[TIT-sub]</a><a class="cite" href="https://arxiv.org/abs/2508.05712">[ICML'25]</a><a class="cite" href="https://arxiv.org/abs/2603.07673">[Q-sub]</a></div></div>
    <div><div class="wa-n">Optimization</div><div class="wa-d">Permanent bounds for hard problems.</div><div class="wc"><a class="cite" href="https://arxiv.org/abs/2306.02280">[ISIT'23]</a><a class="cite" href="https://arxiv.org/abs/2306.02280">[TIT'24]</a><a class="cite" href="https://arxiv.org/abs/2508.05712">[ICML'25]</a></div></div>
    <div><div class="wa-n">Quantum systems</div><div class="wa-d">Distributed quantum optimization.</div><div class="wc"><a class="cite" href="https://arxiv.org/abs/2603.07673">[Q-sub]</a></div></div>
  </div>
  <div class="w-more"><a href="{{ '/publications/' | relative_url }}">All publications</a></div>
</div>
</section>

<section class="s s-alt">
<div class="s-in">
  <div class="sh">Latest</div>
  <h2 class="sh2">What's new</h2>
  <div class="u-list">
    <div class="u-row"><div class="u-dt">May 2026</div><div><div class="u-tt">Joining HKUST (GZ) as Assistant Professor</div><div class="u-v">DSA Thrust, Information Hub</div></div></div>
    <div class="u-row"><div class="u-dt">Mar 2026</div><div><div class="u-tt"><a href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">Scalable Distributed Quantum Optimization</a></div><div class="u-v">Submitted to Quantum</div></div></div>
    <div class="u-row"><div class="u-dt">Jul 2025</div><div><div class="u-tt"><a href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">Graph-Cover-based Bethe Partition Function</a></div><div class="u-v">Submitted to IEEE TIT</div></div></div>
    <div class="u-row"><div class="u-dt">2024</div><div><div class="u-tt"><a href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">Degree-M Bethe &amp; Sinkhorn Permanent</a></div><div class="u-v">Published in IEEE TIT</div></div></div>
  </div>
</div>
</section>

<section class="s s-dark join" id="positions">
<div class="s-in">
  <h2 class="join-h">Join the group</h2>
  <p class="join-d">Building a team at HKUST (Guangzhou) starting May 2026.</p>
  <div class="join-perks">
    <div class="join-pk">Full tuition and competitive stipend</div>
    <div class="join-pk">Mentorship targeting IEEE TIT, ISIT, ICML</div>
    <div class="join-pk">Greater Bay Area research ecosystem</div>
    <div class="join-pk">Small group, close advising</div>
  </div>
  <div class="join-roles"><span class="join-role">RA</span><span class="join-role">MPhil</span><span class="join-role">PhD</span><span class="join-role">Postdoc</span></div>
  <div class="join-cta"><a class="btn btn-a" href="mailto:{{ site.author.email }}">Get in touch</a></div>
  <div class="join-links"><a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a><a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Info Hub</a><a href="https://www.hkust-gz.edu.cn/">HKUST GZ</a></div>
</div>
</section>
