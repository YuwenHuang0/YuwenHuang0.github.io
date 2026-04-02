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

  .page__content {
    font-family: "Avenir Next", "Segoe UI", "Helvetica Neue", sans-serif;
  }

  .page__content .home-shell {
    display: grid;
    gap: 1.4rem;
  }

  .page__content .home-panel {
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(34, 90, 106, 0.12);
    border-radius: 34px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 251, 252, 0.98) 100%);
    box-shadow: 0 22px 48px rgba(17, 45, 54, 0.09);
  }

  .home-hero {
    padding: clamp(1.4rem, 2vw, 2.5rem);
    background:
      radial-gradient(circle at top right, rgba(216, 155, 43, 0.18) 0%, rgba(216, 155, 43, 0) 22%),
      radial-gradient(circle at bottom left, rgba(29, 102, 119, 0.12) 0%, rgba(29, 102, 119, 0) 26%),
      linear-gradient(135deg, rgba(241, 249, 251, 0.98) 0%, rgba(255, 255, 255, 0.99) 52%, rgba(255, 248, 233, 0.98) 100%);
  }

  .home-hero::before {
    content: "";
    position: absolute;
    inset: auto auto -7rem -7rem;
    width: 15rem;
    height: 15rem;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(29, 102, 119, 0.14) 0%, rgba(29, 102, 119, 0) 72%);
    pointer-events: none;
  }

  .home-hero-grid {
    position: relative;
    z-index: 1;
    display: grid;
    gap: 1.2rem;
    align-items: center;
  }

  .home-copy {
    display: grid;
    gap: 1rem;
  }

  .home-kicker {
    margin: 0;
    color: #17677a;
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .home-title {
    margin: 0;
    max-width: 12ch;
    color: #17313a;
    font-size: clamp(2.45rem, 5.7vw, 4.95rem);
    font-weight: 800;
    line-height: 0.96;
    letter-spacing: -0.05em;
    text-wrap: balance;
  }

  .home-subtitle {
    margin: 0;
    max-width: 38rem;
    color: #35505a;
    font-size: clamp(1.02rem, 1.5vw, 1.18rem);
    line-height: 1.75;
  }

  .home-chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
  }

  .home-chip {
    display: inline-flex;
    align-items: center;
    padding: 0.45rem 0.85rem;
    border: 1px solid rgba(23, 103, 122, 0.12);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.72);
    color: #1a5d6c;
    font-size: 0.88rem;
    font-weight: 700;
    line-height: 1.2;
  }

  .home-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .home-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 2.8rem;
    padding: 0.72rem 1.2rem;
    border-radius: 999px;
    font-size: 0.95rem;
    font-weight: 800;
    text-decoration: none !important;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  }

  .home-button:hover {
    transform: translateY(-1px);
  }

  .home-button.primary {
    border: 1px solid #135c6d;
    background: linear-gradient(180deg, #1b7286 0%, #145b6c 100%);
    color: #fff !important;
    box-shadow: 0 12px 24px rgba(20, 91, 108, 0.18);
  }

  .home-button.secondary {
    border: 1px solid rgba(23, 103, 122, 0.16);
    background: rgba(255, 255, 255, 0.78);
    color: #175f70 !important;
  }

  .home-hero-note {
    display: grid;
    gap: 0.45rem;
    width: min(100%, 28rem);
    padding: 0.9rem 1rem;
    border: 1px solid rgba(23, 103, 122, 0.1);
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.72);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.84);
  }

  .home-hero-note strong {
    color: #17313a;
    font-size: 0.98rem;
    line-height: 1.2;
  }

  .home-hero-note p {
    margin: 0;
    color: #53666f;
    font-size: 0.92rem;
    line-height: 1.55;
  }

  .home-visual {
    position: relative;
    min-height: 24rem;
    border: 1px solid rgba(23, 103, 122, 0.12);
    border-radius: 30px;
    background:
      radial-gradient(circle at 50% 50%, rgba(29, 102, 119, 0.16) 0%, rgba(29, 102, 119, 0.03) 26%, rgba(29, 102, 119, 0) 54%),
      linear-gradient(180deg, rgba(255, 255, 255, 0.92) 0%, rgba(244, 250, 251, 0.95) 100%);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.72);
  }

  .home-visual svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    display: block;
  }

  .home-visual-core,
  .home-visual-pill {
    position: absolute;
    border: 1px solid rgba(23, 103, 122, 0.14);
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: 0 18px 26px rgba(22, 69, 81, 0.08);
    backdrop-filter: blur(10px);
  }

  .home-visual-core {
    top: 50%;
    left: 50%;
    width: min(82%, 18rem);
    padding: 1rem 1.15rem;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .home-visual-core strong {
    display: block;
    color: #17313a;
    font-size: 1.05rem;
    line-height: 1.15;
  }

  .home-visual-core span {
    display: block;
    margin-top: 0.35rem;
    color: #56707a;
    font-size: 0.86rem;
    font-weight: 700;
    line-height: 1.35;
  }

  .home-visual-pill {
    padding: 0.55rem 0.8rem;
    color: #184f5d;
    font-size: 0.84rem;
    font-weight: 800;
    line-height: 1.25;
  }

  .home-visual-pill.models {
    top: 1rem;
    left: 1rem;
  }

  .home-visual-pill.optimization {
    top: 1.2rem;
    right: 1rem;
  }

  .home-visual-pill.tensor {
    left: 1.2rem;
    bottom: 1.2rem;
  }

  .home-visual-pill.quantum {
    right: 1rem;
    bottom: 1.4rem;
  }

  .home-recruit {
    position: relative;
    z-index: 1;
    margin-top: 1.25rem;
    padding: 1.1rem;
    border: 1px solid rgba(216, 155, 43, 0.22);
    border-radius: 28px;
    background:
      linear-gradient(135deg, rgba(255, 245, 224, 0.96) 0%, rgba(255, 255, 255, 0.98) 42%, rgba(243, 249, 251, 0.98) 100%);
    box-shadow: 0 18px 32px rgba(84, 67, 26, 0.08);
  }

  .home-recruit::before {
    content: "";
    position: absolute;
    inset: 0 auto auto 0;
    width: 100%;
    height: 4px;
    border-radius: 28px 28px 0 0;
    background: linear-gradient(90deg, #d89b2b 0%, #17677a 58%, #4f8b62 100%);
  }

  .home-recruit-grid {
    display: grid;
    gap: 0.95rem;
    align-items: start;
  }

  .home-badge {
    display: inline-flex;
    align-items: center;
    width: fit-content;
    padding: 0.2rem 0.68rem;
    border-radius: 999px;
    background: rgba(216, 155, 43, 0.14);
    color: #8b5a10;
    font-size: 0.76rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-recruit-copy {
    display: grid;
    gap: 0.7rem;
  }

  .home-recruit-copy h2 {
    margin: 0;
    color: #17313a;
    font-size: clamp(1.35rem, 2.2vw, 1.9rem);
    line-height: 1.08;
  }

  .home-recruit-meta {
    margin: 0;
    color: #8b5a10;
    font-size: 0.98rem;
    font-weight: 800;
    line-height: 1.45;
  }

  .home-recruit-copy p {
    margin: 0;
    color: #435962;
    font-size: 0.98rem;
    line-height: 1.6;
  }

  .home-link-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .home-link-pills a {
    display: inline-flex;
    align-items: center;
    padding: 0.3rem 0.72rem;
    border: 1px solid rgba(23, 103, 122, 0.14);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.86);
    color: #17677a;
    font-size: 0.84rem;
    font-weight: 800;
    text-decoration: none !important;
  }

  .home-link-pills a:hover {
    color: #114e5d;
    border-color: rgba(17, 78, 93, 0.24);
  }

  .home-apply-card {
    display: grid;
    gap: 0.7rem;
    padding: 1rem;
    border: 1px solid rgba(23, 103, 122, 0.1);
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.76);
  }

  .home-apply-card h3,
  .home-role-strip-title {
    margin: 0;
    color: #17313a;
    font-size: 1rem;
    line-height: 1.2;
  }

  .home-apply-card p {
    margin: 0;
    color: #536870;
    font-size: 0.94rem;
    line-height: 1.55;
  }

  .home-apply-block {
    display: grid;
    gap: 0.4rem;
    padding: 0.8rem 0.9rem;
    border: 1px solid rgba(23, 103, 122, 0.1);
    border-radius: 18px;
    background: linear-gradient(180deg, rgba(235, 247, 250, 0.96) 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-apply-block strong {
    color: #17677a;
    font-size: 0.76rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-apply-block code {
    color: #1e3c46;
    font-size: 0.88rem;
    font-weight: 800;
    overflow-wrap: anywhere;
    white-space: normal;
  }

  .home-apply-rule {
    padding: 0.75rem 0.9rem;
    border-radius: 18px;
    background: rgba(255, 247, 233, 0.7);
    color: #51656d;
    font-size: 0.92rem;
    line-height: 1.5;
  }

  .home-apply-rule strong {
    color: #17313a;
  }

  .home-apply-cta {
    justify-self: start;
  }

  .home-support-strip {
    display: grid;
    gap: 0.75rem;
    margin-top: 0.95rem;
    padding-top: 0.95rem;
    border-top: 1px solid rgba(23, 103, 122, 0.12);
  }

  .home-support-grid {
    display: grid;
    gap: 0.7rem;
  }

  .home-support-card {
    padding: 0.9rem 0.95rem;
    border: 1px solid rgba(23, 103, 122, 0.1);
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.76);
  }

  .home-support-card span {
    display: block;
    margin-bottom: 0.28rem;
    color: #17313a;
    font-size: 0.98rem;
    font-weight: 800;
  }

  .home-support-card p {
    margin: 0;
    color: #556a72;
    font-size: 0.9rem;
    line-height: 1.55;
  }

  .home-gallery-grid {
    display: grid;
    gap: 0.9rem;
  }

  .home-gallery-card {
    position: relative;
    overflow: hidden;
    display: grid;
    gap: 0.9rem;
    padding: 1rem;
    border: 1px solid rgba(23, 103, 122, 0.1);
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.84);
    box-shadow: 0 16px 30px rgba(17, 45, 54, 0.06);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .home-gallery-card:hover,
  .home-stage-card:hover,
  .home-direction-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 22px 36px rgba(17, 45, 54, 0.1);
  }

  .home-gallery-card.teal {
    background: linear-gradient(180deg, #ebf8fb 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-gallery-card.gold {
    background: linear-gradient(180deg, #fff8e6 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-gallery-card.coral {
    background: linear-gradient(180deg, #fff2ed 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-gallery-art {
    height: 14rem;
    border: 1px solid rgba(23, 103, 122, 0.08);
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.78);
  }

  .home-gallery-art svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .home-gallery-kicker {
    margin: 0;
    color: #17677a;
    font-size: 0.74rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-gallery-card h3 {
    margin: 0;
    color: #17313a;
    font-size: clamp(1.12rem, 1.9vw, 1.5rem);
    line-height: 1.15;
  }

  .home-gallery-card p {
    margin: 0;
    color: #566971;
    font-size: 0.96rem;
    line-height: 1.6;
  }

  .home-gallery-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
  }

  .home-gallery-tags span {
    display: inline-flex;
    align-items: center;
    min-height: 1.8rem;
    padding: 0.26rem 0.68rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.84);
    border: 1px solid rgba(23, 103, 122, 0.12);
    color: #175d6d;
    font-size: 0.78rem;
    font-weight: 800;
    line-height: 1.2;
  }

  .home-section {
    padding: clamp(1.2rem, 1.8vw, 2rem);
  }

  .home-section-header {
    display: grid;
    gap: 0.45rem;
    margin-bottom: 1rem;
  }

  .home-section-kicker {
    margin: 0;
    color: #17677a;
    font-size: 0.76rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-section-title {
    margin: 0;
    color: #17313a;
    font-size: clamp(1.6rem, 2.5vw, 2.35rem);
    line-height: 1.06;
    letter-spacing: -0.03em;
    text-wrap: balance;
  }

  .home-section-copy {
    margin: 0;
    max-width: 44rem;
    color: #53666f;
    font-size: 0.98rem;
    line-height: 1.6;
  }

  .home-stage-grid {
    display: grid;
    gap: 0.8rem;
  }

  .home-stage-card {
    position: relative;
    overflow: hidden;
    padding: 1rem;
    border: 1px solid rgba(23, 103, 122, 0.1);
    border-radius: 28px;
    background: rgba(255, 255, 255, 0.82);
    min-height: 14rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .home-stage-card.theory {
    background: linear-gradient(180deg, #eef8fb 0%, rgba(255, 255, 255, 0.94) 100%);
  }

  .home-stage-card.algorithms {
    background: linear-gradient(180deg, #f2f9fb 0%, rgba(255, 255, 255, 0.94) 100%);
  }

  .home-stage-card.platforms {
    background: linear-gradient(180deg, #eef7f0 0%, rgba(255, 255, 255, 0.94) 100%);
  }

  .home-stage-card.impact {
    background: linear-gradient(180deg, #fff6e6 0%, rgba(255, 255, 255, 0.94) 100%);
  }

  .home-stage-art {
    width: 100%;
    height: 6rem;
    margin-bottom: 0.9rem;
  }

  .home-stage-art svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .home-stage-index {
    display: inline-flex;
    align-items: center;
    margin-bottom: 0.45rem;
    color: #7b949b;
    font-size: 0.76rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-stage-card h3 {
    margin: 0 0 0.3rem;
    color: #17313a;
    font-size: 1.08rem;
    line-height: 1.18;
  }

  .home-stage-card p {
    margin: 0;
    color: #556a72;
    font-size: 0.94rem;
    line-height: 1.58;
  }

  .home-directions-grid {
    display: grid;
    gap: 0.9rem;
  }

  .home-direction-card {
    position: relative;
    overflow: hidden;
    display: grid;
    gap: 0.9rem;
    padding: 1rem;
    border: 1px solid rgba(23, 103, 122, 0.1);
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: 0 14px 28px rgba(17, 45, 54, 0.06);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .home-direction-card.teal {
    background: linear-gradient(180deg, #edf8fb 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-direction-card.gold {
    background: linear-gradient(180deg, #fff8e8 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-direction-card.coral {
    background: linear-gradient(180deg, #fff1ed 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-direction-card.green {
    background: linear-gradient(180deg, #eef8f1 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-direction-media {
    height: 10.5rem;
    border: 1px solid rgba(23, 103, 122, 0.08);
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.78);
  }

  .home-direction-media svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .home-direction-card h3 {
    margin: 0;
    color: #17313a;
    font-size: clamp(1.1rem, 1.9vw, 1.45rem);
    line-height: 1.14;
  }

  .home-direction-card p {
    margin: 0;
    color: #52666f;
    font-size: 0.98rem;
    line-height: 1.6;
  }

  .home-direction-label {
    display: inline-flex;
    align-items: center;
    width: fit-content;
    min-height: 1.85rem;
    padding: 0.28rem 0.72rem;
    border-radius: 999px;
    border: 1px solid rgba(23, 103, 122, 0.12);
    background: rgba(255, 255, 255, 0.84);
    color: #17677a;
    font-size: 0.78rem;
    font-weight: 900;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .home-citation-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
  }

  .home-citation {
    display: inline-flex;
    align-items: center;
    min-height: 2rem;
    padding: 0.34rem 0.75rem;
    border: 1px solid rgba(23, 103, 122, 0.16);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.8);
    color: #165f71 !important;
    font-size: 0.84rem;
    font-weight: 900;
    letter-spacing: 0.01em;
    text-decoration: none !important;
    transition: border-color 0.18s ease, transform 0.18s ease;
  }

  .home-citation:hover {
    transform: translateY(-1px);
    border-color: rgba(23, 103, 122, 0.28);
  }

  @media (min-width: 760px) {
    .home-hero-grid {
      grid-template-columns: minmax(0, 1.12fr) minmax(20rem, 0.88fr);
    }

    .home-recruit-grid {
      grid-template-columns: minmax(0, 1.2fr) minmax(18rem, 0.9fr);
    }

    .home-support-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .home-gallery-grid {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .home-stage-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .home-directions-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (min-width: 1080px) {
    .home-support-grid {
      grid-template-columns: repeat(4, minmax(0, 1fr));
    }

    .home-stage-grid {
      grid-template-columns: repeat(4, minmax(0, 1fr));
    }
  }

  @media (max-width: 759px) {
    .home-title {
      max-width: none;
    }

    .home-visual {
      min-height: 20rem;
    }

    .home-visual-pill {
      font-size: 0.78rem;
    }

    .home-visual-pill.models,
    .home-visual-pill.tensor {
      left: 0.8rem;
    }

    .home-visual-pill.optimization,
    .home-visual-pill.quantum {
      right: 0.8rem;
    }

    .home-visual-pill.models {
      top: 0.85rem;
    }

    .home-visual-pill.optimization {
      top: 1rem;
    }

    .home-visual-pill.tensor,
    .home-visual-pill.quantum {
      bottom: 1rem;
    }
  }
</style>

<div class="home-shell">
  <section class="home-panel home-hero">
    <div class="home-hero-grid">
      <div class="home-copy">
        <p class="home-kicker">Information theory / statistical physics / optimization / quantum information</p>
        <h1 class="home-title">Provable methods for structured inference and optimization</h1>
        <p class="home-subtitle">
          I develop scalable algorithms with rigorous guarantees using graphical models, combinatorics, tensor networks, and distributed quantum systems, with growing directions in machine learning and learning theory.
        </p>
        <div class="home-hero-note">
          <strong>Current focus</strong>
          <p>Inference, counting, optimization, and distributed quantum computation grounded in information theory and statistical physics.</p>
        </div>
        <div class="home-chip-row">
          <span class="home-chip">Bethe methods and graph covers</span>
          <span class="home-chip">Combinatorial inference and counting</span>
          <span class="home-chip">Tensor networks</span>
          <span class="home-chip">Distributed quantum systems</span>
        </div>
        <div class="home-actions">
          <a class="home-button primary" href="#open-positions">Open positions</a>
          <a class="home-button secondary" href="#selected-research">Selected research</a>
        </div>
      </div>

      <div class="home-visual" aria-hidden="true">
        <svg viewBox="0 0 680 520" role="presentation">
          <defs>
            <linearGradient id="hero-line" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#8ec6d3" />
              <stop offset="100%" stop-color="#e4c36f" />
            </linearGradient>
            <radialGradient id="hero-core" cx="50%" cy="50%" r="60%">
              <stop offset="0%" stop-color="#1d6677" stop-opacity="0.36" />
              <stop offset="100%" stop-color="#1d6677" stop-opacity="0" />
            </radialGradient>
          </defs>
          <circle cx="340" cy="260" r="160" fill="url(#hero-core)" />
          <path d="M136 132 C220 114, 248 164, 340 260" fill="none" stroke="url(#hero-line)" stroke-width="6" stroke-linecap="round" />
          <path d="M544 152 C460 146, 428 184, 340 260" fill="none" stroke="url(#hero-line)" stroke-width="6" stroke-linecap="round" />
          <path d="M170 394 C252 360, 276 334, 340 260" fill="none" stroke="url(#hero-line)" stroke-width="6" stroke-linecap="round" />
          <path d="M536 378 C444 346, 420 326, 340 260" fill="none" stroke="url(#hero-line)" stroke-width="6" stroke-linecap="round" />
          <circle cx="168" cy="136" r="14" fill="#2f7f93" />
          <circle cx="518" cy="152" r="14" fill="#d9b14f" />
          <circle cx="188" cy="386" r="14" fill="#cb6651" />
          <circle cx="510" cy="364" r="14" fill="#4f8b62" />
          <circle cx="340" cy="260" r="20" fill="#17313a" />
        </svg>
        <div class="home-visual-pill models">Graphical models</div>
        <div class="home-visual-pill optimization">Optimization</div>
        <div class="home-visual-pill tensor">Tensor networks</div>
        <div class="home-visual-pill quantum">Quantum systems</div>
        <div class="home-visual-core">
          <strong>Structure-aware algorithms</strong>
          <span>Inference / counting / optimization</span>
        </div>
      </div>
    </div>

    <div class="home-recruit" id="open-positions">
      <div class="home-recruit-grid">
        <div class="home-recruit-copy">
          <span class="home-badge">Open positions</span>
          <h2>Recruiting RAs, MPhil/PhD students, and one Postdoc</h2>
          <p class="home-recruit-meta">I will join HKUST (Guangzhou) as a tenure-track assistant professor in Fall 2026 in the Data Science and Analytics Thrust (DSA), Information Hub.</p>
          <p>I am building a research group on graphical models, inference, optimization, machine learning, and quantum information, centered on mathematically rigorous ideas that lead to scalable algorithms.</p>
          <div class="home-link-pills">
            <a href="https://dsa.hkust-gz.edu.cn/">DSA</a>
            <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
            <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
          </div>
        </div>

        <div class="home-apply-card">
          <h3>How to apply</h3>
          <p>Send a concise email describing your background and research interests.</p>
          <div class="home-apply-block">
            <strong>Email title</strong>
            <code>[RA Application] Your Name - Current Institution</code>
            <code>[MPhil Inquiry] Your Name - Current Institution</code>
            <code>[PhD Inquiry] Your Name - Current Institution</code>
            <code>[Postdoc Application] Your Name - Current Institution</code>
          </div>
          <div class="home-apply-rule">
            <strong>RA / MPhil / PhD:</strong> include a short motivation note in the email body, plus your CV and transcript.
          </div>
          <div class="home-apply-rule">
            <strong>Postdoc:</strong> include your CV and a short research statement describing your interests and future agenda.
          </div>
          <a class="home-button primary home-apply-cta" href="mailto:{{ site.author.email }}">Apply by email</a>
        </div>
      </div>

      <div class="home-support-strip">
        <h3 class="home-role-strip-title">What I provide</h3>
        <div class="home-support-grid">
          <article class="home-support-card">
            <span>RA</span>
            <p>Close mentoring, core research training, and preparation for graduate study or algorithm-focused industry roles.</p>
          </article>
          <article class="home-support-card">
            <span>MPhil</span>
            <p>A structured transition into independent research with theory, applications, and publication-minded training.</p>
          </article>
          <article class="home-support-card">
            <span>PhD</span>
            <p>Ownership of deeper problems, broad collaboration, and support for long-term research careers.</p>
          </article>
          <article class="home-support-card">
            <span>Postdoc</span>
            <p>One opening with room to shape an agenda, co-mentor students, and prepare for academic searches.</p>
          </article>
        </div>
      </div>
    </div>
  </section>

  <section class="home-panel home-section">
    <div class="home-section-header">
      <p class="home-section-kicker">Research gallery</p>
      <h2 class="home-section-title">Example views of the problems and systems behind the research.</h2>
      <p class="home-section-copy">A more visual snapshot of the kinds of structures, algorithms, and platforms that drive the work.</p>
    </div>

    <div class="home-gallery-grid">
      <article class="home-gallery-card teal">
        <div class="home-gallery-art">
          <svg viewBox="0 0 360 220" role="img" aria-label="Structured inference illustration">
            <circle cx="62" cy="62" r="18" fill="#2f7f93" />
            <circle cx="138" cy="46" r="16" fill="#2f7f93" />
            <circle cx="144" cy="132" r="16" fill="#2f7f93" />
            <rect x="240" y="52" width="34" height="34" rx="9" fill="#9bd0dc" />
            <rect x="294" y="52" width="34" height="34" rx="9" fill="#9bd0dc" />
            <rect x="236" y="116" width="98" height="46" rx="14" fill="#e9f7fa" stroke="#78b8c7" stroke-width="3" />
            <line x1="80" y1="62" x2="122" y2="46" stroke="#78b8c7" stroke-width="6" stroke-linecap="round" />
            <line x1="80" y1="62" x2="128" y2="132" stroke="#78b8c7" stroke-width="6" stroke-linecap="round" />
            <line x1="154" y1="46" x2="257" y2="69" stroke="#78b8c7" stroke-width="6" stroke-linecap="round" />
            <line x1="160" y1="132" x2="257" y2="69" stroke="#78b8c7" stroke-width="6" stroke-linecap="round" />
            <line x1="274" y1="69" x2="294" y2="69" stroke="#78b8c7" stroke-width="6" stroke-linecap="round" />
            <rect x="252" y="129" width="10" height="20" rx="4" fill="#2f7f93" />
            <rect x="270" y="120" width="10" height="29" rx="4" fill="#78b8c7" />
            <rect x="288" y="111" width="10" height="38" rx="4" fill="#2f7f93" />
            <rect x="306" y="124" width="10" height="25" rx="4" fill="#78b8c7" />
          </svg>
        </div>
        <p class="home-gallery-kicker">Inference</p>
        <h3>Structured graphical-model reasoning</h3>
        <p>Graphical models, message passing, and combinatorial structure for reliable inference and counting at scale.</p>
        <div class="home-gallery-tags">
          <span>Uncertainty</span>
          <span>Counting</span>
          <span>Graph covers</span>
        </div>
      </article>

      <article class="home-gallery-card gold">
        <div class="home-gallery-art">
          <svg viewBox="0 0 360 220" role="img" aria-label="Optimization illustration">
            <defs>
              <marker id="gallery-opt-arrow" viewBox="0 0 12 12" markerWidth="9" markerHeight="9" refX="10.5" refY="6" orient="auto" markerUnits="userSpaceOnUse">
                <path d="M1 1 L11 6 L1 11" fill="none" stroke="#d9b14f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
              </marker>
            </defs>
            <path d="M42 154 C92 122, 114 54, 166 54 C214 54, 230 148, 274 148 C300 148, 320 130, 332 86" fill="none" stroke="#d9b14f" stroke-width="8" stroke-linecap="round" marker-end="url(#gallery-opt-arrow)" />
            <circle cx="166" cy="54" r="13" fill="#7a5614" />
            <circle cx="274" cy="148" r="13" fill="#7a5614" />
            <line x1="60" y1="176" x2="304" y2="176" stroke="#ead28d" stroke-width="5" stroke-linecap="round" />
            <rect x="56" y="26" width="76" height="36" rx="14" fill="#fff6de" stroke="#ead28d" stroke-width="3" />
            <rect x="240" y="28" width="76" height="36" rx="14" fill="#fff6de" stroke="#ead28d" stroke-width="3" />
            <text x="94" y="49" text-anchor="middle" fill="#8a5b10" font-size="14" font-weight="800">Bounds</text>
            <text x="278" y="51" text-anchor="middle" fill="#8a5b10" font-size="14" font-weight="800">Algorithms</text>
          </svg>
        </div>
        <p class="home-gallery-kicker">Optimization</p>
        <h3>Provable optimization and decision-making</h3>
        <p>Structure-aware objectives, permanent bounds, and algorithmic guarantees for hard optimization problems.</p>
        <div class="home-gallery-tags">
          <span>Convex / nonconvex</span>
          <span>Permanent bounds</span>
          <span>Decisions</span>
        </div>
      </article>

      <article class="home-gallery-card coral">
        <div class="home-gallery-art">
          <svg viewBox="0 0 360 220" role="img" aria-label="Quantum and tensor illustration">
            <defs>
              <marker id="gallery-tensor-arrow" viewBox="0 0 12 12" markerWidth="9" markerHeight="9" refX="10.5" refY="6" orient="auto" markerUnits="userSpaceOnUse">
                <path d="M1 1 L11 6 L1 11" fill="none" stroke="#cb6651" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
              </marker>
            </defs>
            <rect x="48" y="82" width="34" height="34" rx="9" fill="#efb2a7" />
            <rect x="106" y="82" width="34" height="34" rx="9" fill="#efb2a7" />
            <rect x="164" y="82" width="34" height="34" rx="9" fill="#efb2a7" />
            <rect x="222" y="82" width="34" height="34" rx="9" fill="#efb2a7" />
            <line x1="82" y1="99" x2="106" y2="99" stroke="#cb6651" stroke-width="6" stroke-linecap="round" />
            <line x1="140" y1="99" x2="164" y2="99" stroke="#cb6651" stroke-width="6" stroke-linecap="round" />
            <line x1="198" y1="99" x2="222" y2="99" stroke="#cb6651" stroke-width="6" stroke-linecap="round" />
            <path d="M256 99 L318 99" fill="none" stroke="#cb6651" stroke-width="7" stroke-linecap="round" marker-end="url(#gallery-tensor-arrow)" />
            <circle cx="110" cy="44" r="10" fill="#4f8b62" />
            <circle cx="180" cy="34" r="10" fill="#4f8b62" />
            <circle cx="252" cy="50" r="10" fill="#4f8b62" />
            <line x1="120" y1="44" x2="170" y2="34" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="190" y1="34" x2="242" y2="50" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <circle cx="110" cy="164" r="10" fill="#4f8b62" />
            <circle cx="180" cy="178" r="10" fill="#4f8b62" />
            <circle cx="250" cy="164" r="10" fill="#4f8b62" />
            <line x1="120" y1="164" x2="170" y2="178" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="190" y1="178" x2="240" y2="164" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
          </svg>
        </div>
        <p class="home-gallery-kicker">Quantum and tensors</p>
        <h3>High-dimensional and distributed quantum computation</h3>
        <p>Tensor-network representations and distributed quantum systems for scalable high-dimensional computation.</p>
        <div class="home-gallery-tags">
          <span>Tensor networks</span>
          <span>Quantum systems</span>
          <span>Scalability</span>
        </div>
      </article>
    </div>
  </section>

  <section class="home-panel home-section">
    <div class="home-section-header">
      <p class="home-section-kicker">From theory to impact</p>
      <h2 class="home-section-title">Research built from structure, algorithms, and scalable systems.</h2>
      <p class="home-section-copy">The common thread is to turn mathematical structure into practical computation, from graphical-model inference to quantum-enabled platforms.</p>
    </div>

    <div class="home-stage-grid">
      <article class="home-stage-card theory">
        <div class="home-stage-art" aria-hidden="true">
          <svg viewBox="0 0 220 100" role="presentation">
            <circle cx="48" cy="52" r="12" fill="#2f7f93" />
            <circle cx="110" cy="30" r="10" fill="#8ec6d3" />
            <circle cx="164" cy="68" r="10" fill="#8ec6d3" />
            <line x1="60" y1="52" x2="100" y2="32" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
            <line x1="120" y1="36" x2="154" y2="62" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
          </svg>
        </div>
        <span class="home-stage-index">01 / Theory</span>
        <h3>Information theory and statistical physics</h3>
        <p>Structure, correlation, and entropy motivate the underlying questions and bounds.</p>
      </article>

      <article class="home-stage-card algorithms">
        <div class="home-stage-art" aria-hidden="true">
          <svg viewBox="0 0 220 100" role="presentation">
            <rect x="34" y="26" width="38" height="38" rx="10" fill="#d5ebf1" />
            <rect x="94" y="18" width="38" height="38" rx="10" fill="#2f7f93" />
            <rect x="154" y="38" width="38" height="38" rx="10" fill="#d5ebf1" />
            <line x1="72" y1="45" x2="94" y2="37" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
            <line x1="132" y1="37" x2="154" y2="57" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
          </svg>
        </div>
        <span class="home-stage-index">02 / Algorithms</span>
        <h3>Inference, counting, and optimization</h3>
        <p>Bethe methods, graph covers, and structure-aware optimization become scalable algorithms.</p>
      </article>

      <article class="home-stage-card platforms">
        <div class="home-stage-art" aria-hidden="true">
          <svg viewBox="0 0 220 100" role="presentation">
            <rect x="40" y="30" width="24" height="24" rx="7" fill="#4f8b62" />
            <rect x="94" y="16" width="24" height="24" rx="7" fill="#4f8b62" />
            <rect x="94" y="62" width="24" height="24" rx="7" fill="#4f8b62" />
            <rect x="148" y="30" width="24" height="24" rx="7" fill="#4f8b62" />
            <line x1="64" y1="42" x2="94" y2="28" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="64" y1="42" x2="94" y2="74" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="118" y1="28" x2="148" y2="42" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="118" y1="74" x2="148" y2="42" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
          </svg>
        </div>
        <span class="home-stage-index">03 / Platforms</span>
        <h3>Distributed quantum systems</h3>
        <p>Quantum networks and distributed architectures extend the computational regime.</p>
      </article>

      <article class="home-stage-card impact">
        <div class="home-stage-art" aria-hidden="true">
          <svg viewBox="0 0 220 100" role="presentation">
            <path d="M36 68 C62 64, 74 36, 98 36 C126 36, 134 66, 162 66 C178 66, 188 56, 194 44" fill="none" stroke="#d9b14f" stroke-width="6" stroke-linecap="round" />
            <circle cx="98" cy="36" r="8" fill="#7a5614" />
            <circle cx="162" cy="66" r="8" fill="#7a5614" />
            <line x1="48" y1="76" x2="184" y2="76" stroke="#ead28d" stroke-width="4" stroke-linecap="round" />
          </svg>
        </div>
        <span class="home-stage-index">04 / Impact</span>
        <h3>Machine learning and efficient computation</h3>
        <p>Future directions include learning theory, efficient analytics, and large-scale decision making.</p>
      </article>
    </div>
  </section>

  <section class="home-panel home-section" id="selected-research">
    <div class="home-section-header">
      <p class="home-section-kicker">Selected research</p>
      <h2 class="home-section-title">Representative directions and papers</h2>
      <p class="home-section-copy">A compact view of the main threads running through the group and the papers that anchor them.</p>
    </div>

    <div class="home-directions-grid">
      <article class="home-direction-card teal">
        <div class="home-direction-media">
          <svg viewBox="0 0 320 170" role="img" aria-label="Graphical models illustration">
            <circle cx="58" cy="56" r="15" fill="#2f7f93" />
            <circle cx="122" cy="36" r="15" fill="#2f7f93" />
            <circle cx="124" cy="114" r="15" fill="#2f7f93" />
            <rect x="202" y="50" width="28" height="28" rx="7" fill="#8ec6d3" />
            <rect x="258" y="50" width="28" height="28" rx="7" fill="#8ec6d3" />
            <line x1="72" y1="56" x2="108" y2="36" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
            <line x1="72" y1="56" x2="110" y2="114" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
            <line x1="138" y1="36" x2="216" y2="64" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
            <line x1="140" y1="114" x2="216" y2="64" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
            <line x1="230" y1="64" x2="258" y2="64" stroke="#78b8c7" stroke-width="5" stroke-linecap="round" />
          </svg>
        </div>
        <span class="home-direction-label">Inference</span>
        <h3>Graphical models and Bethe methods</h3>
        <p>Bethe approximations, graph covers, and message passing for principled inference and counting.</p>
        <div class="home-citation-row">
          <a class="home-citation" href="{{ '/publication/characterizing-bethe-partition-factor-graphs' | relative_url }}">[ISIT2020]</a>
          <a class="home-citation" href="{{ '/publication/bethe-free-energy-global-minimum' | relative_url }}">[ITW2022]</a>
          <a class="home-citation" href="{{ '/publication/bethe-partition-spa-stable-polynomials' | relative_url }}">[ISIT2024]</a>
          <a class="home-citation" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-sub]</a>
        </div>
      </article>

      <article class="home-direction-card gold">
        <div class="home-direction-media">
          <svg viewBox="0 0 320 170" role="img" aria-label="Optimization illustration">
            <defs>
              <marker id="home-opt-arrow" viewBox="0 0 12 12" markerWidth="8" markerHeight="8" refX="10.5" refY="6" orient="auto" markerUnits="userSpaceOnUse">
                <path d="M1 1 L11 6 L1 11" fill="none" stroke="#d9b14f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
              </marker>
            </defs>
            <path d="M34 126 C84 92, 110 34, 156 34 C196 34, 220 108, 258 108 C278 108, 292 94, 302 60" fill="none" stroke="#d9b14f" stroke-width="6" stroke-linecap="round" marker-end="url(#home-opt-arrow)" />
            <circle cx="156" cy="34" r="10" fill="#7a5614" />
            <circle cx="258" cy="108" r="10" fill="#7a5614" />
            <line x1="58" y1="138" x2="280" y2="138" stroke="#ead28d" stroke-width="4" stroke-linecap="round" />
          </svg>
        </div>
        <span class="home-direction-label">Optimization</span>
        <h3>Optimization and combinatorial structure</h3>
        <p>Structure-exploiting optimization and permanent bounds with rigorous performance guarantees.</p>
        <div class="home-citation-row">
          <a class="home-citation" href="{{ '/publication/bounding-permanent-degree-m-bethe' | relative_url }}">[ISIT2023]</a>
          <a class="home-citation" href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">[TIT2024]</a>
          <a class="home-citation" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
        </div>
      </article>

      <article class="home-direction-card coral">
        <div class="home-direction-media">
          <svg viewBox="0 0 320 170" role="img" aria-label="Tensor network illustration">
            <defs>
              <marker id="home-tensor-arrow" viewBox="0 0 12 12" markerWidth="8" markerHeight="8" refX="10.5" refY="6" orient="auto" markerUnits="userSpaceOnUse">
                <path d="M1 1 L11 6 L1 11" fill="none" stroke="#cb6651" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
              </marker>
            </defs>
            <rect x="40" y="56" width="34" height="34" rx="9" fill="#efb2a7" />
            <rect x="96" y="56" width="34" height="34" rx="9" fill="#efb2a7" />
            <rect x="152" y="56" width="34" height="34" rx="9" fill="#efb2a7" />
            <rect x="208" y="56" width="34" height="34" rx="9" fill="#efb2a7" />
            <line x1="74" y1="73" x2="96" y2="73" stroke="#cb6651" stroke-width="5" stroke-linecap="round" />
            <line x1="130" y1="73" x2="152" y2="73" stroke="#cb6651" stroke-width="5" stroke-linecap="round" />
            <line x1="186" y1="73" x2="208" y2="73" stroke="#cb6651" stroke-width="5" stroke-linecap="round" />
            <path d="M242 73 L300 73" fill="none" stroke="#cb6651" stroke-width="6" stroke-linecap="round" marker-end="url(#home-tensor-arrow)" />
          </svg>
        </div>
        <span class="home-direction-label">Tensor methods</span>
        <h3>Tensor networks and quantum-enabled inference</h3>
        <p>Tensor-network representations and quantum-enabled methods for compact high-dimensional computation.</p>
        <div class="home-citation-row">
          <a class="home-citation" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT2021]</a>
          <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
        </div>
      </article>

      <article class="home-direction-card green">
        <div class="home-direction-media">
          <svg viewBox="0 0 320 170" role="img" aria-label="Quantum systems illustration">
            <rect x="48" y="56" width="28" height="28" rx="8" fill="#4f8b62" />
            <rect x="128" y="34" width="28" height="28" rx="8" fill="#4f8b62" />
            <rect x="128" y="98" width="28" height="28" rx="8" fill="#4f8b62" />
            <rect x="212" y="56" width="28" height="28" rx="8" fill="#4f8b62" />
            <rect x="270" y="88" width="28" height="28" rx="8" fill="#4f8b62" />
            <line x1="62" y1="70" x2="142" y2="48" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="62" y1="70" x2="142" y2="112" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="156" y1="48" x2="226" y2="70" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="156" y1="112" x2="226" y2="70" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
            <line x1="226" y1="70" x2="284" y2="102" stroke="#86b894" stroke-width="5" stroke-linecap="round" />
          </svg>
        </div>
        <span class="home-direction-label">Quantum systems</span>
        <h3>Distributed quantum systems</h3>
        <p>Distributed quantum architectures for large-scale optimization, inference, and data-intensive analytics.</p>
        <div class="home-citation-row">
          <a class="home-citation" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
          <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
        </div>
      </article>
    </div>
  </section>
</div>
