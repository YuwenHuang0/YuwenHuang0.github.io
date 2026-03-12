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
    max-width: 14ch;
    color: #17313a;
    font-size: clamp(2.1rem, 5vw, 3.2rem);
    font-weight: 800;
    line-height: 1.02;
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

  .home-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    margin-top: 1.1rem;
  }

  .home-link {
    padding: 0.45rem 0.85rem;
    border: 1px solid rgba(54, 118, 134, 0.16);
    border-radius: 999px;
    background: #ffffff;
    color: #1e5767;
    font-size: 0.95rem;
    font-weight: 600;
    text-decoration: none;
    box-shadow: 0 8px 20px rgba(18, 54, 64, 0.04);
  }

  .home-link:hover {
    text-decoration: none;
    transform: translateY(-1px);
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

  .framework-grid {
    display: grid;
    gap: 0.95rem;
  }

  .framework-card {
    padding: 1rem 1rem 0.95rem;
    border-radius: 18px;
    border: 1px solid rgba(34, 84, 97, 0.1);
    background: #fbfdfe;
  }

  .framework-card.teal {
    background: #edf7fa;
    border-color: rgba(47, 127, 147, 0.22);
  }

  .framework-card.gold {
    background: #fff7e5;
    border-color: rgba(216, 155, 43, 0.24);
  }

  .framework-card.coral {
    background: #fff1ed;
    border-color: rgba(203, 102, 81, 0.22);
  }

  .framework-card.green {
    background: #eef8f1;
    border-color: rgba(79, 139, 98, 0.24);
  }

  .framework-label {
    display: inline-block;
    margin: 0 0 0.5rem;
    padding: 0.22rem 0.5rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.7);
    color: #2d5864;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .framework-card h3 {
    margin: 0 0 0.45rem;
    color: #193641;
    font-size: 1.04rem;
    line-height: 1.3;
  }

  .framework-card p {
    margin: 0;
    color: #4b666f;
    line-height: 1.68;
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

  .phd-callout {
    padding: 1.2rem 1.25rem;
    border: 1px solid rgba(54, 118, 134, 0.16);
    border-radius: 22px;
    background: linear-gradient(135deg, #f5fbfc 0%, #ffffff 100%);
  }

  .phd-callout h2 {
    margin: 0 0 0.5rem;
    padding: 0;
    border: 0;
    color: #17313a;
    font-size: 1.2rem;
  }

  .phd-callout p {
    margin: 0;
    color: #48626b;
    line-height: 1.76;
  }

  @media (min-width: 760px) {
    .home-summary-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .framework-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .interest-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }
</style>

<section class="home-intro">
  <p class="home-eyebrow">Information Theory · Optimization · Quantum Information</p>
  <h1 class="home-heading">Structured inference and optimization with rigorous guarantees</h1>

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

  <div class="home-links">
    <a class="home-link" href="mailto:yuwen.huang@link.cuhk.edu.hk">Email</a>
    <a class="home-link" href="https://scholar.google.com/citations?user=9A1utW0AAAAJ">Google Scholar</a>
    <a class="home-link" href="https://orcid.org/0000-0003-1189-5690">ORCID</a>
  </div>
</section>

<section class="research-framework">
  <h2 class="home-section-title">Research Framework</h2>
  <p class="framework-intro">
    My work brings together four technical directions. The common objective is to develop scalable methods for structured inference, counting, and optimization with firm theoretical guarantees.
  </p>

  <div class="framework-grid">
    <article class="framework-card teal">
      <span class="framework-label">Area 1</span>
      <h3>Probabilistic Graphical Models</h3>
      <p>Bethe methods, graph covers, message passing, and structure-aware approximations for inference and counting.</p>
    </article>

    <article class="framework-card gold">
      <span class="framework-label">Area 2</span>
      <h3>Optimization and Decision-Making</h3>
      <p>Convex and nonconvex optimization methods that exploit structure and provide rigorous guarantees.</p>
    </article>

    <article class="framework-card coral">
      <span class="framework-label">Area 3</span>
      <h3>Tensor Networks and Quantum-Enabled Methods</h3>
      <p>High-dimensional representations and quantum-inspired tools for efficient inference and compact computation.</p>
    </article>

    <article class="framework-card green">
      <span class="framework-label">Area 4</span>
      <h3>Distributed Quantum Computing and Networks</h3>
      <p>Structure-aware quantum architectures for large-scale optimization, inference, and data-intensive analytics.</p>
    </article>
  </div>

  <div class="framework-goal">
    <span>Shared Goal</span>
    <strong>Provable and scalable methods for inference, counting, and optimization in modern structured systems.</strong>
  </div>
</section>

<section>
  <h2 class="home-section-title">Research Interests</h2>

  <div class="interest-grid">
    <article class="interest-card teal">
      <span class="interest-accent"></span>
      <h3>Probabilistic graphical models and combinatorial inference</h3>
      <p>Scalable approximate inference, uncertainty quantification, and counting problems arising in structured learning and data analysis.</p>
    </article>

    <article class="interest-card gold">
      <span class="interest-accent"></span>
      <h3>Optimization for learning and sequential decision-making</h3>
      <p>Structure-exploiting algorithms for machine learning and decision problems, with emphasis on rigorous guarantees.</p>
    </article>

    <article class="interest-card coral">
      <span class="interest-accent"></span>
      <h3>Tensor-network, quantum-inspired, and quantum-enabled methods</h3>
      <p>Methods for high-dimensional inference, compact representations, and efficient computation in large structured systems.</p>
    </article>

    <article class="interest-card green">
      <span class="interest-accent"></span>
      <h3>Distributed quantum computing and quantum networks</h3>
      <p>Emerging computational platforms for scalable optimization, inference, and data-intensive analytics.</p>
    </article>
  </div>
</section>

<section class="phd-callout">
  <h2>For Prospective PhD Students</h2>
  <p>
    I am interested in working with students who want to build mathematically grounded methods at the interface of information theory, optimization, graphical models, and quantum information, especially when theory and algorithms need to reinforce each other.
  </p>
</section>
