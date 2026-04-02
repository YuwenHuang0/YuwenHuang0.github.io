---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ── Reset & base ───────────────────────────────────── */
.splash .page__content {
  font-family: "SF Pro Display", "Helvetica Neue", "Segoe UI", sans-serif;
  max-width: none;
  padding: 0;
  margin: 0;
}
.splash .page__content p { margin: 0; }
.splash .page__content h1,
.splash .page__content h2,
.splash .page__content h3 { margin: 0; }
.splash .page__content a { text-decoration: none; }

/* ── Section scaffold ───────────────────────────────── */
.ap-section {
  width: 100%;
  padding: clamp(4rem, 10vw, 8rem) clamp(1.5rem, 5vw, 3rem);
}
.ap-inner {
  max-width: 980px;
  margin: 0 auto;
}
.ap-inner.wide { max-width: 1120px; }

/* ── Hero ───────────────────────────────────────────── */
.ap-hero {
  text-align: center;
  padding-top: clamp(5rem, 14vw, 11rem);
  padding-bottom: clamp(4rem, 10vw, 8rem);
  background:
    radial-gradient(ellipse 80% 60% at 50% 0%, rgba(22, 95, 112, 0.06) 0%, transparent 70%),
    #fff;
}
.ap-hero-kicker {
  display: inline-block;
  padding: 0.35rem 1rem;
  border-radius: 999px;
  background: rgba(22, 95, 112, 0.07);
  color: #17677a;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 1.6rem;
}
.ap-hero-title {
  font-size: clamp(2.8rem, 7vw, 5.6rem);
  font-weight: 800;
  line-height: 1.02;
  letter-spacing: -0.04em;
  color: #1d1d1f;
  max-width: 14ch;
  margin: 0 auto;
  text-wrap: balance;
}
.ap-hero-sub {
  margin-top: 1.6rem;
  font-size: clamp(1.05rem, 1.8vw, 1.35rem);
  line-height: 1.6;
  color: #6e6e73;
  max-width: 44rem;
  margin-left: auto;
  margin-right: auto;
}
.ap-hero-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.9rem;
  margin-top: 2.4rem;
}
.ap-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 3rem;
  padding: 0.78rem 1.8rem;
  border-radius: 999px;
  font-size: 1.05rem;
  font-weight: 600;
  text-decoration: none !important;
  transition: all 0.22s ease;
}
.ap-btn-primary {
  background: #17677a;
  color: #fff !important;
  box-shadow: 0 4px 16px rgba(23, 103, 122, 0.2);
}
.ap-btn-primary:hover {
  background: #135a6b;
  box-shadow: 0 6px 24px rgba(23, 103, 122, 0.3);
  transform: translateY(-1px);
}
.ap-btn-link {
  color: #17677a !important;
  background: none;
  padding: 0.78rem 0.4rem;
}
.ap-btn-link:hover { color: #114e5d !important; }
.ap-btn-link::after {
  content: " →";
  transition: transform 0.2s ease;
  display: inline-block;
}
.ap-btn-link:hover::after { transform: translateX(3px); }

/* ── Dark section ───────────────────────────────────── */
.ap-dark {
  background: #1d1d1f;
  color: #f5f5f7;
}
.ap-dark .ap-section-kicker { color: rgba(255,255,255,0.5); }
.ap-dark .ap-section-title { color: #f5f5f7; }
.ap-dark .ap-section-sub { color: rgba(255,255,255,0.6); }

/* ── Light-gray section ─────────────────────────────── */
.ap-gray { background: #f5f5f7; }

/* ── Section headers ────────────────────────────────── */
.ap-section-header {
  text-align: center;
  margin-bottom: clamp(2.5rem, 5vw, 4rem);
}
.ap-section-kicker {
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #17677a;
  margin-bottom: 0.8rem;
}
.ap-section-title {
  font-size: clamp(2rem, 4.5vw, 3.6rem);
  font-weight: 800;
  line-height: 1.06;
  letter-spacing: -0.03em;
  color: #1d1d1f;
  max-width: 18ch;
  margin: 0 auto;
  text-wrap: balance;
}
.ap-section-sub {
  margin-top: 1rem;
  font-size: clamp(1rem, 1.5vw, 1.2rem);
  line-height: 1.6;
  color: #6e6e73;
  max-width: 38rem;
  margin-left: auto;
  margin-right: auto;
}

/* ── Research area cards ────────────────────────────── */
.ap-cards {
  display: grid;
  gap: 1.2rem;
  grid-template-columns: 1fr;
}
@media (min-width: 720px) {
  .ap-cards { grid-template-columns: repeat(3, 1fr); }
}
.ap-card {
  position: relative;
  overflow: hidden;
  border-radius: 24px;
  padding: clamp(2rem, 3vw, 2.8rem);
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.ap-card:hover {
  transform: scale(1.015);
  box-shadow: 0 20px 50px rgba(0,0,0,0.12);
}
.ap-card-teal { background: linear-gradient(165deg, #e8f6fa 0%, #f7fcfd 100%); }
.ap-card-gold { background: linear-gradient(165deg, #fef6e4 0%, #fffcf5 100%); }
.ap-card-coral { background: linear-gradient(165deg, #fef0eb 0%, #fffaf8 100%); }

.ap-card-icon {
  width: 3.2rem;
  height: 3.2rem;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.4rem;
}
.ap-card-icon.teal { background: rgba(23, 103, 122, 0.12); }
.ap-card-icon.gold { background: rgba(216, 155, 43, 0.14); }
.ap-card-icon.coral { background: rgba(203, 102, 81, 0.12); }

.ap-card-label {
  font-size: 0.74rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #17677a;
}
.ap-card-gold .ap-card-label { color: #8b5a10; }
.ap-card-coral .ap-card-label { color: #a14430; }

.ap-card h3 {
  font-size: clamp(1.2rem, 2vw, 1.55rem);
  font-weight: 700;
  line-height: 1.15;
  color: #1d1d1f;
}
.ap-card p {
  font-size: 0.98rem;
  line-height: 1.6;
  color: #6e6e73;
}
.ap-card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  margin-top: auto;
}
.ap-card-tags span {
  padding: 0.25rem 0.65rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.7);
  border: 1px solid rgba(0,0,0,0.06);
  font-size: 0.78rem;
  font-weight: 600;
  color: #1d1d1f;
}

/* ── Pipeline strip ─────────────────────────────────── */
.ap-pipeline {
  display: grid;
  gap: 0;
  grid-template-columns: 1fr;
  counter-reset: stage;
}
@media (min-width: 720px) {
  .ap-pipeline { grid-template-columns: repeat(4, 1fr); }
}
.ap-stage {
  text-align: center;
  padding: clamp(2rem, 3vw, 3rem) 1.5rem;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  position: relative;
}
@media (min-width: 720px) {
  .ap-stage { border-bottom: none; border-right: 1px solid rgba(255,255,255,0.08); }
  .ap-stage:last-child { border-right: none; }
}
.ap-stage-num {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.35);
  margin-bottom: 0.9rem;
}
.ap-stage h3 {
  font-size: 1.2rem;
  font-weight: 700;
  color: #f5f5f7;
  margin-bottom: 0.5rem;
}
.ap-stage p {
  font-size: 0.92rem;
  line-height: 1.55;
  color: rgba(255,255,255,0.55);
  max-width: 22ch;
  margin: 0 auto;
}

/* ── Selected research ──────────────────────────────── */
.ap-research-grid {
  display: grid;
  gap: 1.2rem;
  grid-template-columns: 1fr;
}
@media (min-width: 720px) {
  .ap-research-grid { grid-template-columns: repeat(2, 1fr); }
}
.ap-research-item {
  padding: clamp(1.6rem, 3vw, 2.2rem);
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.06);
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  transition: transform 0.22s ease, box-shadow 0.22s ease;
}
.ap-research-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.08);
}
.ap-research-label {
  display: inline-flex;
  width: fit-content;
  padding: 0.22rem 0.7rem;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.ap-research-label.teal { background: rgba(23,103,122,0.08); color: #17677a; }
.ap-research-label.gold { background: rgba(216,155,43,0.1); color: #8b5a10; }
.ap-research-label.coral { background: rgba(203,102,81,0.08); color: #a14430; }
.ap-research-label.green { background: rgba(79,139,98,0.08); color: #3a7049; }

.ap-research-item h3 {
  font-size: 1.15rem;
  font-weight: 700;
  line-height: 1.2;
  color: #1d1d1f;
}
.ap-research-item p {
  font-size: 0.94rem;
  line-height: 1.55;
  color: #6e6e73;
}
.ap-cite-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  margin-top: auto;
}
.ap-cite {
  display: inline-flex;
  align-items: center;
  padding: 0.28rem 0.68rem;
  border-radius: 999px;
  border: 1px solid rgba(23,103,122,0.14);
  background: rgba(23,103,122,0.04);
  color: #17677a !important;
  font-size: 0.82rem;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.18s ease;
}
.ap-cite:hover {
  background: rgba(23,103,122,0.1);
  border-color: rgba(23,103,122,0.28);
  transform: translateY(-1px);
}

/* ── Recruit banner ─────────────────────────────────── */
.ap-recruit {
  text-align: center;
  background:
    radial-gradient(ellipse 70% 50% at 50% 100%, rgba(216,155,43,0.06) 0%, transparent 70%),
    #fff;
}
.ap-recruit-title {
  font-size: clamp(2rem, 4.5vw, 3.6rem);
  font-weight: 800;
  line-height: 1.06;
  letter-spacing: -0.03em;
  color: #1d1d1f;
  max-width: 18ch;
  margin: 0 auto;
  text-wrap: balance;
}
.ap-recruit-sub {
  margin-top: 1rem;
  font-size: clamp(1rem, 1.5vw, 1.2rem);
  line-height: 1.6;
  color: #6e6e73;
  max-width: 42rem;
  margin-left: auto;
  margin-right: auto;
}
.ap-recruit-meta {
  margin-top: 1.6rem;
  font-size: 1rem;
  font-weight: 600;
  color: #8b5a10;
}
.ap-recruit-roles {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
  margin-top: clamp(2.5rem, 5vw, 3.5rem);
  text-align: left;
}
@media (min-width: 720px) {
  .ap-recruit-roles { grid-template-columns: repeat(4, 1fr); }
}
.ap-role {
  padding: 1.6rem 1.4rem;
  border-radius: 18px;
  background: #f5f5f7;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.ap-role h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: #1d1d1f;
}
.ap-role p {
  font-size: 0.9rem;
  line-height: 1.55;
  color: #6e6e73;
}
.ap-recruit-cta {
  margin-top: clamp(2rem, 4vw, 3rem);
}
.ap-recruit-links {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-top: 1.2rem;
}
.ap-recruit-links a {
  font-size: 0.92rem;
  font-weight: 600;
  color: #17677a !important;
  text-decoration: none !important;
}
.ap-recruit-links a:hover { color: #114e5d !important; }
.ap-recruit-links a::after { content: " ↗"; font-size: 0.8em; }

/* ── Divider line ───────────────────────────────────── */
.ap-divider {
  max-width: 980px;
  margin: 0 auto;
  border: none;
  border-top: 1px solid rgba(0,0,0,0.06);
}
</style>

<!-- ════════ HERO ════════ -->
<section class="ap-section ap-hero">
  <div class="ap-inner">
    <p class="ap-hero-kicker">Yuwen Huang</p>
    <h1 class="ap-hero-title">Provable methods for structured inference.</h1>
    <p class="ap-hero-sub">
      Scalable algorithms with rigorous guarantees — built on graphical models, combinatorics, tensor networks, and distributed quantum systems.
    </p>
    <div class="ap-hero-actions">
      <a class="ap-btn ap-btn-primary" href="#positions">Open positions</a>
      <a class="ap-btn ap-btn-link" href="#research">Selected research</a>
    </div>
  </div>
</section>

<!-- ════════ RESEARCH AREAS ════════ -->
<section class="ap-section ap-gray">
  <div class="ap-inner wide">
    <div class="ap-section-header">
      <p class="ap-section-kicker">Research</p>
      <h2 class="ap-section-title">Three pillars. One pursuit.</h2>
      <p class="ap-section-sub">From structure to algorithms to impact — turning mathematical insight into practical computation.</p>
    </div>
    <div class="ap-cards">
      <article class="ap-card ap-card-teal">
        <div class="ap-card-icon teal">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="5" cy="5" r="3.5" fill="#17677a"/><circle cx="15" cy="5" r="3" fill="#17677a"/><circle cx="10" cy="16" r="3" fill="#17677a"/><line x1="7.5" y1="6" x2="13" y2="6" stroke="#17677a" stroke-width="1.5" stroke-linecap="round"/><line x1="6.5" y1="8" x2="9" y2="14" stroke="#17677a" stroke-width="1.5" stroke-linecap="round"/><line x1="14" y1="8" x2="11.5" y2="14" stroke="#17677a" stroke-width="1.5" stroke-linecap="round"/></svg>
        </div>
        <p class="ap-card-label">Inference</p>
        <h3>Structured graphical-model reasoning</h3>
        <p>Message passing, Bethe methods, and combinatorial structure for reliable inference and counting at scale.</p>
        <div class="ap-card-tags">
          <span>Uncertainty</span><span>Counting</span><span>Graph covers</span>
        </div>
      </article>
      <article class="ap-card ap-card-gold">
        <div class="ap-card-icon gold">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M3 14 C6 12, 8 5, 10 5 C13 5, 14 13, 17 8" stroke="#d89b2b" stroke-width="2" stroke-linecap="round" fill="none"/><circle cx="10" cy="5" r="2.5" fill="#d89b2b"/></svg>
        </div>
        <p class="ap-card-label">Optimization</p>
        <h3>Provable optimization and decision-making</h3>
        <p>Structure-aware objectives, permanent bounds, and algorithmic guarantees for hard optimization problems.</p>
        <div class="ap-card-tags">
          <span>Convex / nonconvex</span><span>Permanent bounds</span><span>Decisions</span>
        </div>
      </article>
      <article class="ap-card ap-card-coral">
        <div class="ap-card-icon coral">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><rect x="2" y="8" width="4.5" height="4.5" rx="1.2" fill="#cb6651"/><rect x="8" y="8" width="4.5" height="4.5" rx="1.2" fill="#cb6651"/><rect x="14" y="8" width="4.5" height="4.5" rx="1.2" fill="#cb6651"/><line x1="6.5" y1="10.2" x2="8" y2="10.2" stroke="#cb6651" stroke-width="1.5" stroke-linecap="round"/><line x1="12.5" y1="10.2" x2="14" y2="10.2" stroke="#cb6651" stroke-width="1.5" stroke-linecap="round"/></svg>
        </div>
        <p class="ap-card-label">Quantum &amp; Tensors</p>
        <h3>High-dimensional quantum computation</h3>
        <p>Tensor-network representations and distributed quantum systems for scalable high-dimensional computation.</p>
        <div class="ap-card-tags">
          <span>Tensor networks</span><span>Quantum systems</span><span>Scalability</span>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ════════ PIPELINE ════════ -->
<section class="ap-section ap-dark">
  <div class="ap-inner wide">
    <div class="ap-section-header">
      <p class="ap-section-kicker">From theory to impact</p>
      <h2 class="ap-section-title">Structure becomes computation.</h2>
    </div>
    <div class="ap-pipeline">
      <div class="ap-stage">
        <p class="ap-stage-num">01 — Theory</p>
        <h3>Information theory &amp; statistical physics</h3>
        <p>Structure, correlation, and entropy.</p>
      </div>
      <div class="ap-stage">
        <p class="ap-stage-num">02 — Algorithms</p>
        <h3>Inference, counting, optimization</h3>
        <p>Bethe methods and graph covers.</p>
      </div>
      <div class="ap-stage">
        <p class="ap-stage-num">03 — Platforms</p>
        <h3>Distributed quantum systems</h3>
        <p>Extending the computational regime.</p>
      </div>
      <div class="ap-stage">
        <p class="ap-stage-num">04 — Impact</p>
        <h3>ML &amp; efficient computation</h3>
        <p>Learning theory and analytics at scale.</p>
      </div>
    </div>
  </div>
</section>

<!-- ════════ SELECTED RESEARCH ════════ -->
<section class="ap-section ap-gray" id="research">
  <div class="ap-inner wide">
    <div class="ap-section-header">
      <p class="ap-section-kicker">Selected research</p>
      <h2 class="ap-section-title">Representative directions.</h2>
    </div>
    <div class="ap-research-grid">
      <article class="ap-research-item">
        <span class="ap-research-label teal">Inference</span>
        <h3>Graphical models and Bethe methods</h3>
        <p>Bethe approximations, graph covers, and message passing for principled inference and counting.</p>
        <div class="ap-cite-row">
          <a class="ap-cite" href="{{ '/publication/characterizing-bethe-partition-factor-graphs' | relative_url }}">[ISIT2020]</a>
          <a class="ap-cite" href="{{ '/publication/bethe-free-energy-global-minimum' | relative_url }}">[ITW2022]</a>
          <a class="ap-cite" href="{{ '/publication/bethe-partition-spa-stable-polynomials' | relative_url }}">[ISIT2024]</a>
          <a class="ap-cite" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-sub]</a>
        </div>
      </article>
      <article class="ap-research-item">
        <span class="ap-research-label gold">Optimization</span>
        <h3>Optimization and combinatorial structure</h3>
        <p>Structure-exploiting optimization and permanent bounds with rigorous guarantees.</p>
        <div class="ap-cite-row">
          <a class="ap-cite" href="{{ '/publication/bounding-permanent-degree-m-bethe' | relative_url }}">[ISIT2023]</a>
          <a class="ap-cite" href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">[TIT2024]</a>
          <a class="ap-cite" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
        </div>
      </article>
      <article class="ap-research-item">
        <span class="ap-research-label coral">Tensor methods</span>
        <h3>Tensor networks and quantum-enabled inference</h3>
        <p>Compact high-dimensional computation via tensor-network representations.</p>
        <div class="ap-cite-row">
          <a class="ap-cite" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT2021]</a>
          <a class="ap-cite" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
        </div>
      </article>
      <article class="ap-research-item">
        <span class="ap-research-label green">Quantum systems</span>
        <h3>Distributed quantum systems</h3>
        <p>Distributed quantum architectures for optimization, inference, and analytics.</p>
        <div class="ap-cite-row">
          <a class="ap-cite" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
          <a class="ap-cite" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ════════ OPEN POSITIONS ════════ -->
<section class="ap-section ap-recruit" id="positions">
  <div class="ap-inner">
    <h2 class="ap-recruit-title">Join the group.</h2>
    <p class="ap-recruit-sub">
      Recruiting RAs, MPhil/PhD students, and one Postdoc for Fall 2026 at HKUST (Guangzhou), Data Science and Analytics Thrust.
    </p>
    <p class="ap-recruit-meta">Tenure-track Assistant Professor · Information Hub · DSA</p>
    <div class="ap-recruit-roles">
      <div class="ap-role">
        <h3>RA</h3>
        <p>Core research training and preparation for graduate study.</p>
      </div>
      <div class="ap-role">
        <h3>MPhil</h3>
        <p>Structured transition into independent research.</p>
      </div>
      <div class="ap-role">
        <h3>PhD</h3>
        <p>Ownership of deeper problems and broad collaboration.</p>
      </div>
      <div class="ap-role">
        <h3>Postdoc</h3>
        <p>Shape an agenda, co-mentor students, prepare for faculty searches.</p>
      </div>
    </div>
    <div class="ap-recruit-cta">
      <a class="ap-btn ap-btn-primary" href="mailto:{{ site.author.email }}">Apply by email</a>
    </div>
    <div class="ap-recruit-links">
      <a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>
      <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
      <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
    </div>
  </div>
</section>
