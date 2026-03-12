---
permalink: /
title: "Yuwen Huang's homepage"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
  .home-hero {
    position: relative;
    overflow: hidden;
    margin: 0 0 2rem;
    padding: 1.75rem;
    border: 1px solid rgba(47, 127, 147, 0.18);
    border-radius: 24px;
    background:
      radial-gradient(circle at top right, rgba(233, 182, 77, 0.24), transparent 28%),
      linear-gradient(135deg, #f4fbfd 0%, #ffffff 48%, #eef7f9 100%);
    box-shadow: 0 18px 48px rgba(24, 62, 74, 0.08);
  }

  .home-hero-grid {
    display: grid;
    gap: 1.5rem;
    align-items: center;
  }

  .home-kicker {
    margin: 0 0 0.75rem;
    color: #0f6a7a;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-headline {
    margin: 0 0 0.85rem;
    color: #17313a;
    font-size: clamp(1.9rem, 3.2vw, 2.8rem);
    line-height: 1.08;
  }

  .home-summary {
    margin: 0 0 1rem;
    color: #314b54;
    font-size: 1.04rem;
    line-height: 1.75;
  }

  .home-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin: 1rem 0 0;
  }

  .home-tag {
    padding: 0.42rem 0.8rem;
    border-radius: 999px;
    background: #ffffff;
    border: 1px solid rgba(47, 127, 147, 0.18);
    color: #215160;
    font-size: 0.92rem;
    font-weight: 600;
    box-shadow: 0 8px 18px rgba(24, 62, 74, 0.05);
  }

  .home-contact {
    margin-top: 1.15rem;
    color: #43626c;
    font-size: 0.98rem;
  }

  .home-contact a {
    font-weight: 600;
  }

  .research-map-card {
    padding: 1rem;
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(47, 127, 147, 0.16);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.75);
  }

  .research-map-title {
    margin: 0 0 0.75rem;
    color: #20515f;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .research-map-svg {
    width: 100%;
    height: auto;
    display: block;
  }

  .section-title {
    margin: 2.2rem 0 1rem;
    color: #17313a;
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: 0.01em;
  }

  .interest-grid {
    display: grid;
    gap: 1rem;
    margin: 0 0 2rem;
  }

  .interest-card {
    padding: 1.2rem 1.15rem;
    border-radius: 20px;
    border: 1px solid rgba(32, 81, 95, 0.12);
    background: linear-gradient(180deg, #ffffff 0%, #fbfdfe 100%);
    box-shadow: 0 12px 28px rgba(24, 62, 74, 0.05);
  }

  .interest-card.teal {
    border-top: 4px solid #2f7f93;
  }

  .interest-card.gold {
    border-top: 4px solid #d89b2b;
  }

  .interest-card.red {
    border-top: 4px solid #cb6651;
  }

  .interest-card.green {
    border-top: 4px solid #4f8b62;
  }

  .interest-card h3 {
    margin: 0 0 0.55rem;
    color: #193541;
    font-size: 1.03rem;
  }

  .interest-card p {
    margin: 0;
    color: #466069;
    line-height: 1.7;
  }

  .future-callout {
    margin: 2rem 0 1.5rem;
    padding: 1.3rem 1.25rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #fff8e8 0%, #fffdf7 100%);
    border: 1px solid rgba(216, 155, 43, 0.22);
  }

  .future-callout h3 {
    margin: 0 0 0.45rem;
    color: #7c5513;
    font-size: 1.05rem;
  }

  .future-callout p {
    margin: 0;
    color: #6b5a34;
    line-height: 1.7;
  }

  @media (min-width: 900px) {
    .home-hero-grid {
      grid-template-columns: minmax(0, 1.25fr) minmax(320px, 0.95fr);
    }

    .interest-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }
</style>

<section class="home-hero">
  <div class="home-hero-grid">
    <div>
      <p class="home-kicker">Information Theory • Optimization • Quantum Information</p>
      <h1 class="home-headline">Provable methods for inference, counting, and optimization in structured systems</h1>
      <p class="home-summary">
        I am a postdoctoral researcher working at the intersection of information theory, machine learning, optimization, and quantum information. My research develops provable and scalable methods for inference, counting, and optimization by combining probabilistic graphical models, combinatorics, Bethe and graph-cover techniques, tensor-network representations, and distributed quantum computation, with potential applications in machine learning (ML).
      </p>
      <p class="home-summary">
        A recurring goal in my work is to turn structural insight into practical algorithms with rigorous performance guarantees. Exploring these applications to ML is one of my future research directions. I am particularly interested in working with PhD students who want to build mathematically grounded methods with impact on modern data-intensive systems.
      </p>
      <div class="home-tags">
        <span class="home-tag">Graphical Models</span>
        <span class="home-tag">Combinatorial Inference</span>
        <span class="home-tag">Optimization Theory</span>
        <span class="home-tag">Tensor Networks</span>
        <span class="home-tag">Distributed Quantum Computing</span>
      </div>
      <p class="home-contact">
        Contact: <a href="mailto:yuwen.huang@link.cuhk.edu.hk">yuwen.huang@link.cuhk.edu.hk</a> ·
        <a href="https://scholar.google.com/citations?user=9A1utW0AAAAJ">Google Scholar</a> ·
        <a href="https://orcid.org/0000-0003-1189-5690">ORCID</a>
      </p>
    </div>

    <div class="research-map-card">
      <p class="research-map-title">Research Map</p>
      <svg class="research-map-svg" viewBox="0 0 560 360" role="img" aria-label="Research map showing the connections between graphical models, optimization, tensor networks, and distributed quantum systems">
        <defs>
          <linearGradient id="heroCenter" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#2f7f93" />
            <stop offset="100%" stop-color="#1b5a69" />
          </linearGradient>
        </defs>

        <line x1="280" y1="178" x2="120" y2="82" stroke="#9ec9d4" stroke-width="4" />
        <line x1="280" y1="178" x2="445" y2="82" stroke="#ecc879" stroke-width="4" />
        <line x1="280" y1="178" x2="120" y2="282" stroke="#e1a59a" stroke-width="4" />
        <line x1="280" y1="178" x2="445" y2="282" stroke="#a7cfb2" stroke-width="4" />

        <rect x="176" y="117" width="208" height="122" rx="26" fill="url(#heroCenter)" />
        <text x="280" y="157" text-anchor="middle" fill="#ffffff" font-size="19" font-weight="700">Provable, Scalable</text>
        <text x="280" y="186" text-anchor="middle" fill="#ffffff" font-size="19" font-weight="700">Inference and</text>
        <text x="280" y="215" text-anchor="middle" fill="#ffffff" font-size="19" font-weight="700">Optimization</text>

        <rect x="22" y="28" width="188" height="92" rx="22" fill="#eaf7fb" stroke="#7bb6c6" />
        <text x="116" y="61" text-anchor="middle" fill="#1d5564" font-size="17" font-weight="700">Graphical Models</text>
        <text x="116" y="87" text-anchor="middle" fill="#40626c" font-size="14">Bethe approximation</text>
        <text x="116" y="107" text-anchor="middle" fill="#40626c" font-size="14">Graph covers</text>

        <rect x="350" y="28" width="188" height="92" rx="22" fill="#fff4d8" stroke="#d8ab43" />
        <text x="444" y="61" text-anchor="middle" fill="#7d5615" font-size="17" font-weight="700">Optimization</text>
        <text x="444" y="87" text-anchor="middle" fill="#72603a" font-size="14">Learning and decisions</text>
        <text x="444" y="107" text-anchor="middle" fill="#72603a" font-size="14">Guarantees and structure</text>

        <rect x="22" y="240" width="188" height="92" rx="22" fill="#fff0ec" stroke="#d28c7d" />
        <text x="116" y="273" text-anchor="middle" fill="#8b4438" font-size="17" font-weight="700">Tensor Networks</text>
        <text x="116" y="299" text-anchor="middle" fill="#7a5f58" font-size="14">High-dimensional inference</text>
        <text x="116" y="319" text-anchor="middle" fill="#7a5f58" font-size="14">Compact representations</text>

        <rect x="350" y="240" width="188" height="92" rx="22" fill="#eef8f1" stroke="#7bb28b" />
        <text x="444" y="273" text-anchor="middle" fill="#346245" font-size="17" font-weight="700">Quantum Systems</text>
        <text x="444" y="299" text-anchor="middle" fill="#516b59" font-size="14">Distributed computation</text>
        <text x="444" y="319" text-anchor="middle" fill="#516b59" font-size="14">Networks and scalability</text>
      </svg>
    </div>
  </div>
</section>

<h2 class="section-title">Research Interests</h2>

<section class="interest-grid">
  <article class="interest-card teal">
    <h3>Probabilistic Graphical Models and Counting</h3>
    <p>Probabilistic graphical models, approximate inference, and combinatorial counting for scalable learning, uncertainty quantification, and structured machine learning.</p>
  </article>

  <article class="interest-card gold">
    <h3>Optimization for Learning and Decision-Making</h3>
    <p>Optimization for machine learning and sequential decision-making, with emphasis on structure-exploiting algorithms and provable guarantees in both convex and nonconvex settings.</p>
  </article>

  <article class="interest-card red">
    <h3>Tensor-Network and Quantum-Enabled Inference</h3>
    <p>Tensor-network, quantum-inspired, and quantum-enabled methods for high-dimensional inference, compact model representations, and efficient computation.</p>
  </article>

  <article class="interest-card green">
    <h3>Distributed Quantum Computing and Networks</h3>
    <p>Distributed quantum computing and quantum networks for large-scale optimization, inference, and data-intensive analytics.</p>
  </article>
</section>

<section class="future-callout">
  <h3>Future Direction</h3>
  <p>
    One of my future research directions is to bring these mathematically grounded tools more directly into machine learning, especially in settings where structure, uncertainty, and computational efficiency matter simultaneously.
  </p>
</section>
