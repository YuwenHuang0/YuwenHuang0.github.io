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
    margin: 0 0 1rem;
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
    margin-bottom: 1.6rem;
    padding: 1.6rem;
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

  .home-intro-grid {
    display: grid;
    gap: 1.2rem;
    align-items: start;
  }

  .home-eyebrow {
    margin: 0 0 0.8rem;
    color: #16677a;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }

  .home-heading {
    position: relative;
    margin: 0 0 1rem;
    max-width: none;
    color: #17313a;
    font-size: clamp(1.38rem, 3vw, 1.95rem);
    font-weight: 800;
    line-height: 1.12;
  }

  .home-lead {
    position: relative;
    margin: 0;
    max-width: 56rem;
    color: #304d57;
    font-size: 1.05rem;
    line-height: 1.82;
  }

  .home-lead + .home-lead {
    margin-top: 0.85rem;
  }

  .home-summary-grid {
    display: grid;
    gap: 1rem;
    margin-top: 1.35rem;
  }

  .home-summary-card {
    position: relative;
    padding: 1rem 1.05rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.82);
  }

  .home-summary-card.accent {
    background: linear-gradient(135deg, rgba(255, 248, 232, 0.95) 0%, rgba(255, 255, 255, 0.9) 100%);
    border-color: rgba(216, 155, 43, 0.2);
  }

  .home-summary-card h3 {
    margin: 0 0 0.45rem;
    color: #1b4754;
    font-size: 1rem;
  }

  .home-summary-card p {
    margin: 0;
    color: #4c6871;
    line-height: 1.72;
  }

  .hero-visual {
    padding: 0.95rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.78);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.72);
  }

  .hero-visual-note {
    margin: 0 0 0.65rem;
    color: #214d5a;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .research-framework {
    margin-bottom: 1.7rem;
    padding: 1.4rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 24px;
    background: #ffffff;
    box-shadow: 0 14px 32px rgba(18, 54, 64, 0.05);
  }

  .framework-intro {
    margin: 0 0 1rem;
    color: #48626b;
    line-height: 1.7;
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
    margin-top: 1rem;
    padding: 1rem 1.05rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #184554 0%, #1e6170 100%);
    color: #ffffff;
  }

  .framework-goal span {
    display: block;
    margin-bottom: 0.35rem;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    opacity: 0.88;
  }

  .framework-goal strong {
    display: block;
    font-size: 1.05rem;
    line-height: 1.6;
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
    .home-intro-grid {
      grid-template-columns: minmax(0, 1.22fr) minmax(280px, 0.88fr);
    }

    .home-summary-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .application-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .interest-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }
</style>

<section class="home-intro">
  <div class="home-intro-grid">
    <div>
      <p class="home-eyebrow">Information Theory · Optimization · Quantum Information</p>
      <h1 class="home-heading">Structured inference and optimization<br>with rigorous guarantees</h1>

      <p class="home-lead">
        I am a postdoctoral researcher working at the intersection of information theory, machine learning, optimization, and quantum information. My research develops provable and scalable methods for inference, counting, and optimization by combining probabilistic graphical models, combinatorics, Bethe and graph-cover techniques, tensor-network representations, and distributed quantum computation.
      </p>
      <p class="home-lead">
        A central theme of my work is to use structural insight to design algorithms that are both mathematically rigorous and computationally practical. I am also interested in how these ideas can lead to future applications in machine learning.
      </p>

      <div class="home-summary-grid">
        <article class="home-summary-card">
          <h3>Current focus</h3>
          <p>Graphical-model methods, counting and inference problems, optimization with guarantees, tensor-network methods, and distributed quantum systems.</p>
        </article>
        <article class="home-summary-card accent">
          <h3>Future direction</h3>
          <p>Bringing these structure-aware tools into machine learning, especially where uncertainty, efficiency, and provable behavior all matter.</p>
        </article>
      </div>
    </div>

    <aside class="hero-visual">
      <p class="hero-visual-note">Theory to Impact</p>
      <svg class="figure-svg" viewBox="0 0 360 360" role="img" aria-label="Diagram showing theory, algorithms, and systems feeding into practical impact">
        <defs>
          <linearGradient id="heroStack" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1d6677" />
            <stop offset="100%" stop-color="#184856" />
          </linearGradient>
        </defs>

        <rect x="102" y="20" width="156" height="68" rx="20" fill="#eaf7fb" stroke="#77b8c8" stroke-width="2" />
        <text x="180" y="48" text-anchor="middle" fill="#1b5665" font-size="18" font-weight="700">Theory</text>
        <text x="180" y="70" text-anchor="middle" fill="#476871" font-size="14">information theory</text>

        <line x1="180" y1="88" x2="180" y2="120" stroke="#8fbfcc" stroke-width="5" stroke-linecap="round" />

        <rect x="60" y="120" width="240" height="84" rx="22" fill="url(#heroStack)" />
        <text x="180" y="152" text-anchor="middle" fill="#ffffff" font-size="21" font-weight="700">Algorithms</text>
        <text x="180" y="176" text-anchor="middle" fill="#dff3f7" font-size="14">inference · counting</text>
        <text x="180" y="196" text-anchor="middle" fill="#dff3f7" font-size="14">optimization</text>

        <line x1="180" y1="204" x2="180" y2="236" stroke="#8fbfcc" stroke-width="5" stroke-linecap="round" />

        <rect x="32" y="236" width="130" height="84" rx="20" fill="#fff7e5" stroke="#ddb24d" stroke-width="2" />
        <text x="97" y="267" text-anchor="middle" fill="#7a5614" font-size="17" font-weight="700">Systems</text>
        <text x="97" y="289" text-anchor="middle" fill="#6d5d38" font-size="13">quantum networks</text>
        <text x="97" y="307" text-anchor="middle" fill="#6d5d38" font-size="13">large-scale analytics</text>

        <rect x="198" y="236" width="130" height="84" rx="20" fill="#eef8f1" stroke="#7fb08b" stroke-width="2" />
        <text x="263" y="267" text-anchor="middle" fill="#376548" font-size="17" font-weight="700">Impact</text>
        <text x="263" y="289" text-anchor="middle" fill="#586f60" font-size="13">ML applications</text>
        <text x="263" y="307" text-anchor="middle" fill="#586f60" font-size="13">efficient computation</text>

        <line x1="180" y1="246" x2="110" y2="236" stroke="#cfc7a5" stroke-width="4" stroke-linecap="round" />
        <line x1="180" y1="246" x2="250" y2="236" stroke="#a8c8b0" stroke-width="4" stroke-linecap="round" />
      </svg>
    </aside>
  </div>
</section>

<section class="research-framework">
  <h2 class="home-section-title">Research Framework</h2>
  <p class="framework-intro">
    My work brings together four technical directions. The common objective is to develop scalable methods for structured inference, counting, and optimization with firm theoretical guarantees.
  </p>

  <div class="figure-card">
    <p class="figure-title">Main Research Directions</p>
    <svg class="figure-svg" viewBox="0 0 920 360" role="img" aria-label="Diagram showing the main research directions connected to the central goal of provable and scalable inference and optimization">
      <defs>
        <linearGradient id="coreNode" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#1d6677" />
          <stop offset="100%" stop-color="#184856" />
        </linearGradient>
      </defs>

      <line x1="460" y1="180" x2="200" y2="90" stroke="#98c8d4" stroke-width="6" stroke-linecap="round" />
      <line x1="460" y1="180" x2="720" y2="90" stroke="#e9c36a" stroke-width="6" stroke-linecap="round" />
      <line x1="460" y1="180" x2="200" y2="270" stroke="#e1a194" stroke-width="6" stroke-linecap="round" />
      <line x1="460" y1="180" x2="720" y2="270" stroke="#9bc4a8" stroke-width="6" stroke-linecap="round" />

      <rect x="312" y="115" width="296" height="130" rx="28" fill="url(#coreNode)" />
      <text x="460" y="156" text-anchor="middle" fill="#ffffff" font-size="24" font-weight="700">Provable and Scalable</text>
      <text x="460" y="188" text-anchor="middle" fill="#ffffff" font-size="24" font-weight="700">Inference, Counting,</text>
      <text x="460" y="220" text-anchor="middle" fill="#ffffff" font-size="24" font-weight="700">and Optimization</text>

      <rect x="36" y="28" width="244" height="108" rx="22" fill="#ebf8fb" stroke="#77b8c8" stroke-width="2" />
      <circle cx="84" cy="70" r="9" fill="#2f7f93" />
      <circle cx="116" cy="52" r="9" fill="#2f7f93" />
      <circle cx="122" cy="92" r="9" fill="#2f7f93" />
      <rect x="146" y="58" width="18" height="18" rx="4" fill="#8ec6d3" />
      <line x1="84" y1="70" x2="116" y2="52" stroke="#78b8c7" stroke-width="3" />
      <line x1="84" y1="70" x2="122" y2="92" stroke="#78b8c7" stroke-width="3" />
      <line x1="116" y1="52" x2="155" y2="67" stroke="#78b8c7" stroke-width="3" />
      <line x1="122" y1="92" x2="155" y2="67" stroke="#78b8c7" stroke-width="3" />
      <text x="196" y="65" text-anchor="middle" fill="#1b5665" font-size="20" font-weight="700">Graphical Models</text>
      <text x="196" y="92" text-anchor="middle" fill="#476871" font-size="17">Bethe methods · Graph covers</text>
      <text x="196" y="115" text-anchor="middle" fill="#476871" font-size="17">Inference and counting</text>

      <rect x="640" y="28" width="244" height="108" rx="22" fill="#fff7e5" stroke="#ddb24d" stroke-width="2" />
      <path d="M686 102 C702 76, 712 60, 730 58 C745 56, 753 74, 768 74 C782 74, 788 62, 806 44" fill="none" stroke="#d9b14f" stroke-width="4" stroke-linecap="round" />
      <path d="M794 38 L808 44 L798 57" fill="none" stroke="#7a5614" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
      <circle cx="706" cy="70" r="4" fill="#7a5614" />
      <circle cx="754" cy="74" r="4" fill="#7a5614" />
      <text x="760" y="65" text-anchor="middle" fill="#7a5614" font-size="20" font-weight="700">Optimization</text>
      <text x="760" y="92" text-anchor="middle" fill="#6d5d38" font-size="17">Structure-exploiting algorithms</text>
      <text x="760" y="115" text-anchor="middle" fill="#6d5d38" font-size="17">Convex and nonconvex settings</text>

      <rect x="36" y="224" width="244" height="108" rx="22" fill="#fff1ed" stroke="#d88d7e" stroke-width="2" />
      <rect x="66" y="248" width="24" height="24" rx="6" fill="#efb2a7" />
      <rect x="98" y="248" width="24" height="24" rx="6" fill="#efb2a7" />
      <rect x="82" y="282" width="24" height="24" rx="6" fill="#efb2a7" />
      <line x1="90" y1="260" x2="98" y2="260" stroke="#cb6651" stroke-width="3" />
      <line x1="78" y1="272" x2="94" y2="282" stroke="#cb6651" stroke-width="3" />
      <line x1="110" y1="272" x2="94" y2="282" stroke="#cb6651" stroke-width="3" />
      <text x="196" y="261" text-anchor="middle" fill="#8b4539" font-size="20" font-weight="700">Tensor Networks</text>
      <text x="196" y="288" text-anchor="middle" fill="#725f59" font-size="17">High-dimensional representations</text>
      <text x="196" y="311" text-anchor="middle" fill="#725f59" font-size="17">Quantum-inspired computation</text>

      <rect x="640" y="224" width="244" height="108" rx="22" fill="#eef8f1" stroke="#7fb08b" stroke-width="2" />
      <rect x="688" y="248" width="18" height="18" rx="5" fill="#4f8b62" />
      <rect x="728" y="236" width="18" height="18" rx="5" fill="#4f8b62" />
      <rect x="760" y="270" width="18" height="18" rx="5" fill="#4f8b62" />
      <rect x="802" y="248" width="18" height="18" rx="5" fill="#4f8b62" />
      <line x1="697" y1="257" x2="737" y2="245" stroke="#86b894" stroke-width="3" />
      <line x1="737" y1="245" x2="769" y2="279" stroke="#86b894" stroke-width="3" />
      <line x1="769" y1="279" x2="811" y2="257" stroke="#86b894" stroke-width="3" />
      <line x1="697" y1="257" x2="769" y2="279" stroke="#86b894" stroke-width="3" />
      <text x="760" y="261" text-anchor="middle" fill="#376548" font-size="20" font-weight="700">Quantum Systems</text>
      <text x="760" y="288" text-anchor="middle" fill="#586f60" font-size="17">Distributed quantum computing</text>
      <text x="760" y="311" text-anchor="middle" fill="#586f60" font-size="17">Quantum networks</text>
    </svg>
  </div>

  <div class="framework-goal">
    <span>Shared Goal</span>
    <strong>Provable and scalable methods for inference, counting, and optimization in modern structured systems.</strong>
  </div>
</section>

<section class="applications-showcase">
  <h2 class="home-section-title">Potential Applications</h2>
  <p class="framework-intro">
    These methods are motivated by core theoretical questions, but they also point toward practical applications in machine learning, large-scale analytics, and emerging quantum platforms.
  </p>

  <div class="application-grid">
    <article class="application-card teal">
      <div class="application-visual">
        <svg class="figure-svg" viewBox="0 0 360 160" role="img" aria-label="Illustration of structured machine learning using a graph">
          <line x1="80" y1="42" x2="176" y2="30" stroke="#78b8c7" stroke-width="4" />
          <line x1="80" y1="42" x2="116" y2="116" stroke="#78b8c7" stroke-width="4" />
          <line x1="176" y1="30" x2="264" y2="64" stroke="#78b8c7" stroke-width="4" />
          <line x1="116" y1="116" x2="220" y2="120" stroke="#78b8c7" stroke-width="4" />
          <line x1="220" y1="120" x2="264" y2="64" stroke="#78b8c7" stroke-width="4" />
          <circle cx="80" cy="42" r="15" fill="#2f7f93" />
          <circle cx="176" cy="30" r="15" fill="#2f7f93" />
          <circle cx="264" cy="64" r="15" fill="#2f7f93" />
          <circle cx="116" cy="116" r="15" fill="#2f7f93" />
          <circle cx="220" cy="120" r="15" fill="#2f7f93" />
          <rect x="286" y="32" width="52" height="18" rx="9" fill="#dff0f5" />
          <rect x="286" y="58" width="44" height="18" rx="9" fill="#dff0f5" />
          <rect x="286" y="84" width="60" height="18" rx="9" fill="#dff0f5" />
          <text x="180" y="152" text-anchor="middle" fill="#476871" font-size="16">latent structure · dependencies · constraints</text>
        </svg>
      </div>
      <h3>Structured machine learning</h3>
      <p>Methods based on graphical models and combinatorial structure can support learning problems where dependencies, constraints, and latent structure should be modeled explicitly rather than ignored.</p>
      <p class="application-note">Potential role: more structured and interpretable ML pipelines.</p>
    </article>

    <article class="application-card gold">
      <div class="application-visual">
        <svg class="figure-svg" viewBox="0 0 360 160" role="img" aria-label="Illustration of uncertainty quantification with intervals and distributions">
          <line x1="42" y1="120" x2="318" y2="120" stroke="#d9b14f" stroke-width="4" stroke-linecap="round" />
          <line x1="88" y1="58" x2="88" y2="120" stroke="#d9b14f" stroke-width="6" stroke-linecap="round" />
          <line x1="180" y1="42" x2="180" y2="120" stroke="#d9b14f" stroke-width="6" stroke-linecap="round" />
          <line x1="270" y1="72" x2="270" y2="120" stroke="#d9b14f" stroke-width="6" stroke-linecap="round" />
          <path d="M52 112 C88 92, 102 54, 132 54 C166 54, 178 102, 210 102 C242 102, 252 72, 300 64" fill="none" stroke="#7a5614" stroke-width="5" stroke-linecap="round" />
          <circle cx="88" cy="58" r="8" fill="#7a5614" />
          <circle cx="180" cy="42" r="8" fill="#7a5614" />
          <circle cx="270" cy="72" r="8" fill="#7a5614" />
          <text x="180" y="152" text-anchor="middle" fill="#6d5d38" font-size="16">approximation quality · confidence · decision support</text>
        </svg>
      </div>
      <h3>Uncertainty quantification and reliable analytics</h3>
      <p>Scalable approximate inference can be useful when decisions must be made under uncertainty and exact probabilistic computation is too expensive.</p>
      <p class="application-note">Potential role: reliable uncertainty estimates in complex systems.</p>
    </article>

    <article class="application-card coral">
      <div class="application-visual">
        <svg class="figure-svg" viewBox="0 0 360 160" role="img" aria-label="Illustration of model compression using tensor-style blocks">
          <rect x="42" y="38" width="54" height="54" rx="8" fill="#efb2a7" />
          <rect x="102" y="38" width="54" height="54" rx="8" fill="#efb2a7" />
          <rect x="42" y="98" width="54" height="22" rx="8" fill="#efb2a7" />
          <rect x="102" y="98" width="54" height="22" rx="8" fill="#efb2a7" />
          <path d="M176 78 L228 78" stroke="#cb6651" stroke-width="6" stroke-linecap="round" />
          <path d="M216 62 L240 78 L216 94" fill="none" stroke="#cb6651" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" />
          <rect x="248" y="52" width="22" height="52" rx="7" fill="#cb6651" />
          <rect x="278" y="52" width="22" height="52" rx="7" fill="#cb6651" />
          <rect x="308" y="52" width="22" height="52" rx="7" fill="#cb6651" />
          <text x="180" y="152" text-anchor="middle" fill="#725f59" font-size="16">compact representations · efficient computation</text>
        </svg>
      </div>
      <h3>Model compression and high-dimensional computation</h3>
      <p>Tensor-network and quantum-inspired ideas may provide principled ways to represent large models or high-dimensional objects more compactly.</p>
      <p class="application-note">Potential role: efficient representations for large-scale ML models.</p>
    </article>

    <article class="application-card green">
      <div class="application-visual">
        <svg class="figure-svg" viewBox="0 0 360 160" role="img" aria-label="Illustration of distributed quantum optimization over a network">
          <line x1="72" y1="52" x2="180" y2="40" stroke="#86b894" stroke-width="4" />
          <line x1="72" y1="52" x2="104" y2="118" stroke="#86b894" stroke-width="4" />
          <line x1="180" y1="40" x2="282" y2="70" stroke="#86b894" stroke-width="4" />
          <line x1="104" y1="118" x2="212" y2="122" stroke="#86b894" stroke-width="4" />
          <line x1="212" y1="122" x2="282" y2="70" stroke="#86b894" stroke-width="4" />
          <rect x="54" y="34" width="36" height="36" rx="10" fill="#4f8b62" />
          <rect x="162" y="22" width="36" height="36" rx="10" fill="#4f8b62" />
          <rect x="264" y="52" width="36" height="36" rx="10" fill="#4f8b62" />
          <rect x="86" y="100" width="36" height="36" rx="10" fill="#4f8b62" />
          <rect x="194" y="104" width="36" height="36" rx="10" fill="#4f8b62" />
          <text x="180" y="152" text-anchor="middle" fill="#586f60" font-size="16">networked processors · coordination · scalability</text>
        </svg>
      </div>
      <h3>Distributed quantum optimization</h3>
      <p>Distributed quantum systems and quantum networks suggest new computational settings where structure-aware decomposition may be essential for scalability.</p>
      <p class="application-note">Potential role: scalable optimization on emerging quantum platforms.</p>
    </article>
  </div>
</section>

<section>
  <h2 class="home-section-title">Research Interests</h2>

  <div class="interest-grid">
    <article class="interest-card teal">
      <span class="interest-accent"></span>
      <div class="interest-visual">
        <svg class="figure-svg" viewBox="0 0 320 120" role="img" aria-label="Factor graph style illustration">
          <circle cx="54" cy="42" r="13" fill="#2f7f93" />
          <circle cx="112" cy="26" r="13" fill="#2f7f93" />
          <circle cx="112" cy="88" r="13" fill="#2f7f93" />
          <rect x="176" y="42" width="24" height="24" rx="6" fill="#8ec6d3" />
          <rect x="238" y="42" width="24" height="24" rx="6" fill="#8ec6d3" />
          <line x1="67" y1="42" x2="99" y2="26" stroke="#78b8c7" stroke-width="4" />
          <line x1="67" y1="42" x2="99" y2="88" stroke="#78b8c7" stroke-width="4" />
          <line x1="125" y1="26" x2="188" y2="54" stroke="#78b8c7" stroke-width="4" />
          <line x1="125" y1="88" x2="188" y2="54" stroke="#78b8c7" stroke-width="4" />
          <line x1="200" y1="54" x2="238" y2="54" stroke="#78b8c7" stroke-width="4" />
        </svg>
      </div>
      <h3>Probabilistic graphical models and combinatorial inference</h3>
      <p>Scalable approximate inference, uncertainty quantification, and counting problems arising in structured learning and data analysis.</p>
    </article>

    <article class="interest-card gold">
      <span class="interest-accent"></span>
      <div class="interest-visual">
        <svg class="figure-svg" viewBox="0 0 320 120" role="img" aria-label="Optimization landscape illustration">
          <path d="M34 90 C70 58, 102 28, 142 28 C188 28, 198 92, 236 92 C262 92, 276 72, 292 42" fill="none" stroke="#d9b14f" stroke-width="5" stroke-linecap="round" />
          <circle cx="142" cy="28" r="7" fill="#7a5614" />
          <circle cx="236" cy="92" r="7" fill="#7a5614" />
          <path d="M270 38 L292 42 L278 58" fill="none" stroke="#7a5614" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
          <line x1="64" y1="98" x2="256" y2="98" stroke="#ead28d" stroke-width="3" stroke-linecap="round" />
        </svg>
      </div>
      <h3>Optimization for learning and sequential decision-making</h3>
      <p>Structure-exploiting algorithms for machine learning and decision problems, with emphasis on rigorous guarantees.</p>
    </article>

    <article class="interest-card coral">
      <span class="interest-accent"></span>
      <div class="interest-visual">
        <svg class="figure-svg" viewBox="0 0 320 120" role="img" aria-label="Tensor network style illustration">
          <rect x="38" y="34" width="38" height="38" rx="8" fill="#efb2a7" />
          <rect x="96" y="34" width="38" height="38" rx="8" fill="#efb2a7" />
          <rect x="154" y="34" width="38" height="38" rx="8" fill="#efb2a7" />
          <rect x="212" y="34" width="38" height="38" rx="8" fill="#efb2a7" />
          <line x1="76" y1="53" x2="96" y2="53" stroke="#cb6651" stroke-width="4" />
          <line x1="134" y1="53" x2="154" y2="53" stroke="#cb6651" stroke-width="4" />
          <line x1="192" y1="53" x2="212" y2="53" stroke="#cb6651" stroke-width="4" />
          <path d="M248 53 L286 53" stroke="#cb6651" stroke-width="5" stroke-linecap="round" />
          <path d="M274 38 L290 53 L274 68" fill="none" stroke="#cb6651" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </div>
      <h3>Tensor-network, quantum-inspired, and quantum-enabled methods</h3>
      <p>Methods for high-dimensional inference, compact representations, and efficient computation in large structured systems.</p>
    </article>

    <article class="interest-card green">
      <span class="interest-accent"></span>
      <div class="interest-visual">
        <svg class="figure-svg" viewBox="0 0 320 120" role="img" aria-label="Distributed quantum network illustration">
          <rect x="44" y="34" width="26" height="26" rx="7" fill="#4f8b62" />
          <rect x="120" y="20" width="26" height="26" rx="7" fill="#4f8b62" />
          <rect x="118" y="74" width="26" height="26" rx="7" fill="#4f8b62" />
          <rect x="202" y="34" width="26" height="26" rx="7" fill="#4f8b62" />
          <rect x="258" y="62" width="26" height="26" rx="7" fill="#4f8b62" />
          <line x1="57" y1="47" x2="133" y2="33" stroke="#86b894" stroke-width="4" />
          <line x1="57" y1="47" x2="131" y2="87" stroke="#86b894" stroke-width="4" />
          <line x1="133" y1="33" x2="215" y2="47" stroke="#86b894" stroke-width="4" />
          <line x1="131" y1="87" x2="215" y2="47" stroke="#86b894" stroke-width="4" />
          <line x1="215" y1="47" x2="271" y2="75" stroke="#86b894" stroke-width="4" />
        </svg>
      </div>
      <h3>Distributed quantum computing and quantum networks</h3>
      <p>Emerging computational platforms for scalable optimization, inference, and data-intensive analytics.</p>
    </article>
  </div>
</section>
