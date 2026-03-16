---
permalink: /
title: "Yuwen Huang's homepage"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
  .page__title {
    display: none;
  }

  .page__content .home-section-title {
    margin: 0 0 0.75rem;
    padding: 0;
    border: 0;
    color: #16323c;
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: 0.01em;
  }

  .home-intro {
    position: relative;
    overflow: hidden;
    margin-bottom: 1.05rem;
    padding: 1.25rem;
    border: 1px solid rgba(54, 118, 134, 0.16);
    border-radius: 24px;
    background:
      linear-gradient(135deg, rgba(242, 250, 252, 0.98) 0%, rgba(255, 255, 255, 0.98) 54%, rgba(255, 248, 232, 0.98) 100%);
    box-shadow: 0 14px 34px rgba(18, 54, 64, 0.06);
  }

  .home-intro::after {
    content: "";
    position: absolute;
    top: -56px;
    right: -52px;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(216, 155, 43, 0.18) 0%, rgba(216, 155, 43, 0) 72%);
    pointer-events: none;
  }

  .home-eyebrow {
    margin: 0 0 0.55rem;
    color: #16677a;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }

  .home-heading {
    position: relative;
    margin: 0 0 0.75rem;
    max-width: none;
    color: #17313a;
    font-size: clamp(1.38rem, 3vw, 1.95rem);
    font-weight: 800;
    line-height: 1.12;
  }

  .home-lead {
    position: relative;
    margin: 0;
    max-width: 68rem;
    color: #304d57;
    font-size: 1.05rem;
    line-height: 1.72;
  }

  .home-lead + .home-lead {
    margin-top: 0.85rem;
  }

  .home-top-grid {
    display: grid;
    gap: 0.9rem;
    align-items: start;
  }

  .home-main-copy {
    min-width: 0;
  }

  .home-recruiting {
    position: relative;
    margin: 0;
    padding: 0.95rem 1.05rem 1rem;
    border: 1px solid rgba(216, 155, 43, 0.3);
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(255, 245, 223, 0.98) 0%, rgba(255, 255, 255, 0.98) 100%);
    box-shadow: 0 12px 26px rgba(118, 84, 18, 0.09);
  }

  .home-recruiting::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    border-radius: 20px 20px 0 0;
    background: linear-gradient(90deg, #d89b2b 0%, #1d6677 100%);
  }

  .home-recruiting-label {
    display: inline-block;
    margin: 0 0 0.42rem;
    padding: 0.14rem 0.52rem;
    border-radius: 999px;
    background: rgba(216, 155, 43, 0.14);
    color: #8a5b10;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-recruiting h2 {
    margin: 0 0 0.2rem;
    color: #17313a;
    font-size: 1.12rem;
    line-height: 1.25;
  }

  .home-recruiting-meta {
    margin: 0 0 0.38rem;
    color: #8a5b10;
    font-size: 0.87rem;
    font-weight: 700;
    line-height: 1.35;
  }

  .home-recruiting p {
    margin: 0;
    color: #4d5f67;
    line-height: 1.58;
  }

  .home-summary-grid {
    display: grid;
    gap: 0.8rem;
    margin-top: 0.95rem;
  }

  .home-summary-card {
    position: relative;
    padding: 0.85rem 0.95rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.82);
  }

  .home-summary-card.accent {
    background: linear-gradient(135deg, rgba(255, 248, 232, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%);
    border-color: rgba(216, 155, 43, 0.2);
  }

  .home-summary-card h3 {
    margin: 0 0 0.3rem;
    color: #1b4754;
    font-size: 1rem;
  }

  .home-summary-card p {
    margin: 0;
    color: #4c6871;
    line-height: 1.62;
  }

  .home-citation {
    display: inline-block;
    margin: 0.35rem 0.28rem 0 0;
    padding: 0.12rem 0.48rem;
    border: 1px solid rgba(34, 84, 97, 0.16);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.72);
    color: #1f6070;
    font-size: 0.8rem;
    font-weight: 700;
    line-height: 1.35;
    text-decoration: none !important;
    white-space: nowrap;
  }

  .home-citation:hover {
    background: #edf7fa;
    border-color: rgba(34, 84, 97, 0.28);
  }

  .home-citation-row {
    display: flex;
    flex-wrap: nowrap;
    gap: 0.28rem;
    margin-top: 0.48rem;
    overflow-x: auto;
    scrollbar-width: none;
  }

  .home-citation-row::-webkit-scrollbar {
    display: none;
  }

  .home-citation-row .home-citation {
    margin: 0;
    flex: 0 0 auto;
  }

  .hero-flow {
    margin-top: 0.7rem;
  }

  .hero-flow-note {
    margin: 0 0 0.45rem;
    color: #214d5a;
    font-size: 0.84rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .hero-flow-grid {
    display: grid;
    gap: 0.55rem;
    justify-items: center;
  }

  .hero-node {
    width: 100%;
    max-width: 100%;
    padding: 0.8rem 0.9rem 0.78rem;
    border-radius: 20px;
    border: 2px solid transparent;
    text-align: center;
    box-sizing: border-box;
  }

  .hero-node h3 {
    margin: 0 0 0.22rem;
    font-size: 1.05rem;
    line-height: 1.2;
  }

  .hero-node p {
    margin: 0;
    font-size: 0.98rem;
    line-height: 1.38;
  }

  .hero-node .home-citation {
    margin-top: 0.32rem;
    background: rgba(255, 255, 255, 0.16);
    border-color: rgba(255, 255, 255, 0.24);
    color: inherit;
  }

  .hero-node.theory .home-citation,
  .hero-node.systems .home-citation,
  .hero-node.impact .home-citation {
    background: rgba(255, 255, 255, 0.62);
    border-color: rgba(34, 84, 97, 0.12);
  }

  .hero-node.theory {
    max-width: 220px;
    background: #eaf7fb;
    border-color: #77b8c8;
    color: #1b5665;
  }

  .hero-node.core {
    max-width: 520px;
    background: linear-gradient(135deg, #1d6677 0%, #184856 100%);
    color: #ffffff;
    padding: 0.95rem 1.15rem 0.92rem;
  }

  .hero-node.core h3 {
    font-size: 1.3rem;
  }

  .hero-node.core p {
    color: #dff3f7;
    font-size: 1rem;
    font-weight: 600;
  }

  .hero-node.systems {
    background: #fff7e5;
    border-color: #ddb24d;
    color: #7a5614;
  }

  .hero-node.impact {
    background: #eef8f1;
    border-color: #7fb08b;
    color: #376548;
  }

  .hero-arrow {
    color: #8fbfcc;
    font-size: 1.55rem;
    line-height: 1;
    text-align: center;
    font-weight: 700;
  }

  .hero-side {
    display: grid;
    gap: 0.55rem;
    width: 100%;
  }

  .hero-arrow.down {
    transform: scale(1.05);
  }

  .research-framework {
    margin-bottom: 1.05rem;
    padding: 1.1rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 24px;
    background: #ffffff;
    box-shadow: 0 14px 32px rgba(18, 54, 64, 0.05);
  }

  .framework-intro {
    margin: 0 0 0.75rem;
    color: #48626b;
    line-height: 1.58;
  }

  .figure-card {
    margin-top: 1rem;
    padding: 0.9rem;
    border-radius: 20px;
    border: 1px solid rgba(34, 84, 97, 0.12);
    background: linear-gradient(180deg, #ffffff 0%, #fbfdfe 100%);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.7);
  }

  .figure-title {
    margin: 0 0 0.7rem;
    color: #214d5a;
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .figure-svg {
    width: 100%;
    height: auto;
    display: block;
  }

  .direction-grid {
    display: grid;
    gap: 0.8rem;
    margin-top: 0.75rem;
  }

  .direction-card {
    padding: 0.82rem;
    border: 1px solid rgba(34, 84, 97, 0.1);
    border-radius: 20px;
    background: linear-gradient(180deg, #ffffff 0%, #fbfdfe 100%);
    box-shadow: 0 10px 24px rgba(18, 54, 64, 0.04);
  }

  .direction-card.teal {
    background: linear-gradient(180deg, #eef8fb 0%, #ffffff 100%);
  }

  .direction-card.gold {
    background: linear-gradient(180deg, #fff8e7 0%, #ffffff 100%);
  }

  .direction-card.coral {
    background: linear-gradient(180deg, #fff2ee 0%, #ffffff 100%);
  }

  .direction-card.green {
    background: linear-gradient(180deg, #eef8f1 0%, #ffffff 100%);
  }

  .direction-visual {
    margin-bottom: 0.62rem;
    padding: 0.58rem;
    border-radius: 16px;
    border: 1px solid rgba(34, 84, 97, 0.08);
    background: rgba(255, 255, 255, 0.82);
  }

  .direction-card h3 {
    margin: 0 0 0.26rem;
    color: #183743;
    font-size: 1.05rem;
    line-height: 1.34;
  }

  .direction-card p {
    margin: 0;
    color: #4b666f;
    line-height: 1.58;
  }

  .applications-showcase {
    margin-bottom: 1.7rem;
    padding: 1.4rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 24px;
    background: linear-gradient(135deg, #ffffff 0%, #f9fcfd 100%);
    box-shadow: 0 14px 32px rgba(18, 54, 64, 0.04);
  }

  .application-grid {
    display: grid;
    gap: 1rem;
    margin-top: 1rem;
  }

  .application-card {
    padding: 1rem;
    border: 1px solid rgba(34, 84, 97, 0.1);
    border-radius: 20px;
    background: linear-gradient(180deg, #ffffff 0%, #fbfdfe 100%);
    box-shadow: 0 10px 24px rgba(18, 54, 64, 0.04);
  }

  .application-card.teal {
    background: linear-gradient(180deg, #eef8fb 0%, #ffffff 100%);
  }

  .application-card.gold {
    background: linear-gradient(180deg, #fff8e7 0%, #ffffff 100%);
  }

  .application-card.coral {
    background: linear-gradient(180deg, #fff2ee 0%, #ffffff 100%);
  }

  .application-card.green {
    background: linear-gradient(180deg, #eef8f1 0%, #ffffff 100%);
  }

  .application-visual {
    margin-bottom: 0.85rem;
    padding: 0.7rem;
    border-radius: 16px;
    border: 1px solid rgba(34, 84, 97, 0.08);
    background: rgba(255, 255, 255, 0.78);
  }

  .application-card h3 {
    margin: 0 0 0.45rem;
    color: #183743;
    font-size: 1.04rem;
    line-height: 1.35;
  }

  .application-card p {
    margin: 0;
    color: #4b666f;
    line-height: 1.72;
  }

  .application-note {
    margin-top: 0.6rem;
    color: #2d5966;
    font-size: 0.94rem;
    font-weight: 600;
  }

  .framework-goal {
    margin-top: 0.8rem;
    padding: 0.82rem 0.95rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #184554 0%, #1e6170 100%);
    color: #ffffff;
  }

  .framework-goal span {
    display: block;
    margin-bottom: 0.22rem;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    opacity: 0.88;
  }

  .framework-goal strong {
    display: block;
    font-size: 1.05rem;
    line-height: 1.42;
    font-weight: 700;
  }

  .interest-grid {
    display: grid;
    gap: 1rem;
    margin-bottom: 1.6rem;
  }

  .interest-card {
    padding: 1.05rem 1.05rem 1rem;
    border: 1px solid rgba(34, 84, 97, 0.1);
    border-radius: 20px;
    background: linear-gradient(180deg, #ffffff 0%, #fbfdfe 100%);
    box-shadow: 0 10px 24px rgba(18, 54, 64, 0.04);
  }

  .interest-card h3 {
    margin: 0 0 0.45rem;
    color: #183743;
    font-size: 1.03rem;
    line-height: 1.35;
  }

  .interest-card p {
    margin: 0;
    color: #4b666f;
    line-height: 1.72;
  }

  .interest-visual {
    margin-bottom: 0.9rem;
    padding: 0.65rem;
    border-radius: 16px;
    border: 1px solid rgba(34, 84, 97, 0.08);
    background: rgba(255, 255, 255, 0.85);
  }

  .interest-card .interest-accent {
    display: block;
    width: 52px;
    height: 4px;
    margin-bottom: 0.8rem;
    border-radius: 999px;
  }

  .interest-card.teal .interest-accent {
    background: #2f7f93;
  }

  .interest-card.gold .interest-accent {
    background: #d89b2b;
  }

  .interest-card.coral .interest-accent {
    background: #cb6651;
  }

  .interest-card.green .interest-accent {
    background: #4f8b62;
  }

  @media (min-width: 760px) {
    .home-top-grid {
      grid-template-columns: minmax(0, 1.5fr) minmax(300px, 0.9fr);
    }

    .hero-flow-grid {
      width: 100%;
    }

    .hero-node.theory {
      max-width: 360px;
    }

    .hero-node.theory p {
      white-space: nowrap;
      font-size: 0.92rem;
    }

    .hero-node.core {
      max-width: 700px;
    }

    .hero-node.core p {
      white-space: nowrap;
      font-size: 0.94rem;
    }

    .hero-side {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .home-summary-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .direction-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .application-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .interest-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (min-width: 1100px) {
    .home-heading {
      white-space: nowrap;
    }
  }

</style>

<section class="home-intro">
  <p class="home-eyebrow">Information Theory · Statistical Physics · Optimization · Quantum Information</p>
  <h1 class="home-heading">Structured inference and optimization with rigorous guarantees</h1>
  <div class="home-top-grid">
    <div class="home-main-copy">
      <p class="home-lead">
        I am a postdoctoral researcher at CUHK developing provable and scalable methods for inference, counting, and optimization in structured systems. My research combines probabilistic graphical models, Bethe and graph-cover methods, combinatorics, tensor-network representations, and distributed quantum computation to turn mathematical structure into algorithms with rigorous guarantees.
      </p>
    </div>

    <div class="home-recruiting">
      <span class="home-recruiting-label">Open Positions</span>
      <h2>Recruiting RAs and PhD students</h2>
      <p class="home-recruiting-meta">Faculty appointment at HKUST (Guangzhou) beginning Fall 2026</p>
      <p>I will join the Data Science and Analytic Thrust (DSA), Information Hub, Hong Kong University of Science and Technology (Guangzhou) in Fall 2026. I am actively recruiting prospective RAs and PhD students interested in graphical models, inference, optimization, machine learning, and quantum information, especially students excited by mathematically grounded research with algorithmic impact.</p>
    </div>
  </div>

  <div class="home-summary-grid">
    <article class="home-summary-card">
      <h3>Current work</h3>
      <p>Graphical models, combinatorial inference, structure-aware optimization, and distributed quantum computation.</p>
    </article>
    <article class="home-summary-card accent">
      <h3>Future direction</h3>
      <p>Extending structure-aware inference and optimization into machine learning, learning theory, and quantum information processing.</p>
      <div class="home-citation-row">
        <a class="home-citation" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
        <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[Quantum2026]</a>
      </div>
    </article>
  </div>

  <div class="hero-flow">
    <p class="hero-flow-note">Theory to Impact</p>
    <div class="hero-flow-grid" aria-label="Diagram showing theory flowing into algorithms, systems, and practical impact">
      <div class="hero-node theory">
        <h3>Theory</h3>
        <p>information theory · statistical physics</p>
      </div>

      <div class="hero-arrow down" aria-hidden="true">↓</div>

      <div class="hero-node core">
        <h3>Algorithms</h3>
        <p>Inference, counting, and optimization with structure and guarantees</p>
      </div>

      <div class="hero-arrow down" aria-hidden="true">↓</div>

      <div class="hero-side">
        <div class="hero-node systems">
          <h3>Systems</h3>
          <p>distributed quantum platforms</p>
        </div>
        <div class="hero-node impact">
          <h3>Impact</h3>
          <p>machine learning and efficient computation</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="research-framework">
  <h2 class="home-section-title">Research Directions</h2>
  <p class="framework-intro">
    Selected directions and representative papers:
  </p>

  <div class="direction-grid">
    <article class="direction-card teal">
      <div class="direction-visual">
        <svg class="figure-svg" viewBox="0 0 320 150" role="img" aria-label="Graphical models illustration">
          <circle cx="54" cy="54" r="14" fill="#2f7f93" />
          <circle cx="116" cy="34" r="14" fill="#2f7f93" />
          <circle cx="120" cy="104" r="14" fill="#2f7f93" />
          <rect x="196" y="48" width="26" height="26" rx="6" fill="#8ec6d3" />
          <rect x="252" y="48" width="26" height="26" rx="6" fill="#8ec6d3" />
          <line x1="68" y1="54" x2="102" y2="34" stroke="#78b8c7" stroke-width="4" />
          <line x1="68" y1="54" x2="106" y2="104" stroke="#78b8c7" stroke-width="4" />
          <line x1="130" y1="34" x2="209" y2="61" stroke="#78b8c7" stroke-width="4" />
          <line x1="134" y1="104" x2="209" y2="61" stroke="#78b8c7" stroke-width="4" />
          <line x1="222" y1="61" x2="252" y2="61" stroke="#78b8c7" stroke-width="4" />
        </svg>
      </div>
      <h3>Probabilistic graphical models</h3>
      <p>Bethe approximations, graph covers, and message passing for principled inference and counting.</p>
      <div class="home-citation-row">
        <a class="home-citation" href="{{ '/publication/characterizing-bethe-partition-factor-graphs' | relative_url }}">[ISIT2020]</a>
        <a class="home-citation" href="{{ '/publication/bethe-free-energy-global-minimum' | relative_url }}">[ITW2022]</a>
        <a class="home-citation" href="{{ '/publication/bethe-partition-spa-stable-polynomials' | relative_url }}">[ISIT2024]</a>
        <a class="home-citation" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-Sub]</a>
      </div>
    </article>

    <article class="direction-card gold">
      <div class="direction-visual">
        <svg class="figure-svg" viewBox="0 0 320 150" role="img" aria-label="Optimization illustration">
          <path d="M34 114 C78 82, 104 34, 150 34 C188 34, 210 104, 248 104 C270 104, 286 86, 300 52" fill="none" stroke="#d9b14f" stroke-width="5" stroke-linecap="round" />
          <circle cx="150" cy="34" r="8" fill="#7a5614" />
          <circle cx="248" cy="104" r="8" fill="#7a5614" />
          <path d="M282 46 L300 52 L288 66" fill="none" stroke="#7a5614" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
          <line x1="58" y1="122" x2="276" y2="122" stroke="#ead28d" stroke-width="3" stroke-linecap="round" />
        </svg>
      </div>
      <h3>Optimization and decision-making</h3>
      <p>Structure-exploiting optimization and permanent bounds with provable guarantees.</p>
      <div class="home-citation-row">
        <a class="home-citation" href="{{ '/publication/bounding-permanent-degree-m-bethe' | relative_url }}">[ISIT2023]</a>
        <a class="home-citation" href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">[TIT2024]</a>
        <a class="home-citation" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
      </div>
    </article>

    <article class="direction-card coral">
      <div class="direction-visual">
        <svg class="figure-svg" viewBox="0 0 320 150" role="img" aria-label="Tensor network illustration">
          <rect x="42" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <rect x="96" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <rect x="150" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <rect x="204" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <line x1="76" y1="61" x2="96" y2="61" stroke="#cb6651" stroke-width="4" />
          <line x1="130" y1="61" x2="150" y2="61" stroke="#cb6651" stroke-width="4" />
          <line x1="184" y1="61" x2="204" y2="61" stroke="#cb6651" stroke-width="4" />
          <path d="M238 61 L286 61" stroke="#cb6651" stroke-width="5" stroke-linecap="round" />
          <path d="M272 46 L288 61 L272 76" fill="none" stroke="#cb6651" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </div>
      <h3>Tensor networks and quantum-enabled methods</h3>
      <p>Tensor-network representations and quantum-enabled methods for compact, high-dimensional computation.</p>
      <div class="home-citation-row">
        <a class="home-citation" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT2021]</a>
        <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[Quantum2026]</a>
      </div>
    </article>

    <article class="direction-card green">
      <div class="direction-visual">
        <svg class="figure-svg" viewBox="0 0 320 150" role="img" aria-label="Quantum systems illustration">
          <rect x="46" y="44" width="28" height="28" rx="7" fill="#4f8b62" />
          <rect x="126" y="26" width="28" height="28" rx="7" fill="#4f8b62" />
          <rect x="126" y="90" width="28" height="28" rx="7" fill="#4f8b62" />
          <rect x="210" y="44" width="28" height="28" rx="7" fill="#4f8b62" />
          <rect x="270" y="76" width="28" height="28" rx="7" fill="#4f8b62" />
          <line x1="60" y1="58" x2="140" y2="40" stroke="#86b894" stroke-width="4" />
          <line x1="60" y1="58" x2="140" y2="104" stroke="#86b894" stroke-width="4" />
          <line x1="154" y1="40" x2="224" y2="58" stroke="#86b894" stroke-width="4" />
          <line x1="154" y1="104" x2="224" y2="58" stroke="#86b894" stroke-width="4" />
          <line x1="224" y1="58" x2="284" y2="90" stroke="#86b894" stroke-width="4" />
        </svg>
      </div>
      <h3>Distributed quantum computing and networks</h3>
      <p>Distributed quantum architectures for large-scale optimization, inference, and data-intensive analytics.</p>
      <div class="home-citation-row">
        <a class="home-citation" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
        <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[Quantum2026]</a>
      </div>
    </article>
  </div>

  <div class="framework-goal">
    <span>Shared Goal</span>
    <strong>Turn mathematical structure into scalable algorithms with rigorous guarantees.</strong>
  </div>
</section>
