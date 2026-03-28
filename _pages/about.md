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
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin: 0 0 0.75rem;
    padding: 0;
    border: 0;
    color: #16323c;
    font-size: 1.35rem;
    font-weight: 800;
    letter-spacing: 0.01em;
  }

  .page__content .home-section-title::after {
    content: "";
    flex: 1 1 auto;
    height: 1px;
    background: linear-gradient(90deg, rgba(29, 102, 119, 0.24) 0%, rgba(29, 102, 119, 0) 100%);
  }

  .home-intro {
    position: relative;
    overflow: hidden;
    display: grid;
    gap: 1rem;
    margin-bottom: 1.1rem;
    padding: 1.3rem;
    border: 1px solid rgba(54, 118, 134, 0.15);
    border-radius: 28px;
    background:
      radial-gradient(circle at top right, rgba(216, 155, 43, 0.15) 0%, rgba(216, 155, 43, 0) 24%),
      linear-gradient(135deg, rgba(242, 250, 252, 0.98) 0%, rgba(255, 255, 255, 0.99) 52%, rgba(255, 248, 232, 0.98) 100%);
    box-shadow: 0 18px 42px rgba(18, 54, 64, 0.08);
  }

  .home-intro::after {
    content: "";
    position: absolute;
    right: -70px;
    bottom: -85px;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(29, 102, 119, 0.12) 0%, rgba(29, 102, 119, 0) 72%);
    pointer-events: none;
  }

  .home-header {
    display: grid;
    gap: 0.55rem;
    max-width: 68rem;
    margin: 0 auto;
    text-align: center;
    justify-items: center;
  }

  .home-eyebrow {
    margin: 0;
    color: #16677a;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.075em;
    text-transform: uppercase;
  }

  .home-heading {
    position: relative;
    margin: 0;
    max-width: 64rem;
    color: #17313a;
    font-size: clamp(1.42rem, 2.3vw, 1.9rem);
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.022em;
    text-wrap: balance;
  }

  .home-lead {
    position: relative;
    margin: 0;
    max-width: 60rem;
    color: #304d57;
    font-size: 1.05rem;
    line-height: 1.7;
  }

  .home-recruiting-spotlight {
    position: relative;
    width: 100%;
    max-width: 60rem;
    margin: 0 auto;
    padding: 1.1rem;
    border: 1px solid rgba(216, 155, 43, 0.26);
    border-radius: 24px;
    background:
      linear-gradient(135deg, rgba(255, 244, 220, 0.96) 0%, rgba(255, 255, 255, 0.98) 42%, rgba(242, 250, 252, 0.98) 100%);
    box-shadow: 0 18px 34px rgba(78, 66, 28, 0.08);
  }

  .home-recruiting-spotlight::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    border-radius: 24px 24px 0 0;
    background: linear-gradient(90deg, #d89b2b 0%, #1d6677 55%, #4f8b62 100%);
  }

  .home-spotlight-grid {
    display: grid;
    gap: 0.95rem;
    align-items: start;
  }

  .home-spotlight-main {
    display: grid;
    gap: 0.58rem;
    min-width: 0;
  }

  .home-recruiting-label {
    display: inline-flex;
    width: fit-content;
    margin: 0;
    padding: 0.18rem 0.62rem;
    border-radius: 999px;
    background: rgba(216, 155, 43, 0.15);
    color: #8a5b10;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .home-recruiting-title {
    margin: 0;
    color: #17313a;
    font-size: clamp(1.18rem, 2vw, 1.5rem);
    font-weight: 800;
    line-height: 1.12;
  }

  .home-recruiting-meta {
    margin: 0;
    color: #8a5b10;
    font-size: 0.9rem;
    font-weight: 700;
    line-height: 1.45;
  }

  .home-recruiting-copy {
    margin: 0;
    color: #4d5f67;
    font-size: 0.98rem;
    line-height: 1.5;
  }

  .home-recruiting-preference {
    margin: 0;
    color: #1a5968;
    font-size: 0.98rem;
    font-weight: 700;
    line-height: 1.48;
  }

  .home-institution-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.1rem;
  }

  .home-institution-links a {
    display: inline-flex;
    align-items: center;
    padding: 0.22rem 0.6rem;
    border: 1px solid rgba(23, 103, 122, 0.15);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.78);
    color: #17677a;
    font-size: 0.84rem;
    font-weight: 700;
    line-height: 1.35;
    text-decoration: none !important;
  }

  .home-institution-links a:hover {
    color: #0f4f5e;
    border-color: rgba(15, 79, 94, 0.28);
    background: rgba(255, 255, 255, 0.96);
  }

  .home-role-section {
    display: grid;
    gap: 0.72rem;
    margin-top: 0.88rem;
    padding-top: 0.88rem;
    border-top: 1px solid rgba(29, 102, 119, 0.12);
  }

  .home-role-heading {
    margin: 0;
    color: #17313a;
    font-size: 0.98rem;
    font-weight: 800;
    line-height: 1.2;
  }

  .home-role-grid {
    display: grid;
    gap: 0.72rem;
  }

  .home-role-card {
    padding: 0.82rem 0.88rem;
    border: 1px solid rgba(34, 84, 97, 0.1);
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.78);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.72);
  }

  .home-role-card.teal {
    background: linear-gradient(180deg, #eef8fb 0%, rgba(255, 255, 255, 0.92) 100%);
  }

  .home-role-card.gold {
    background: linear-gradient(180deg, #fff8e7 0%, rgba(255, 255, 255, 0.92) 100%);
  }

  .home-role-card.green {
    background: linear-gradient(180deg, #eef8f1 0%, rgba(255, 255, 255, 0.92) 100%);
  }

  .home-role-card.coral {
    background: linear-gradient(180deg, #fff1ee 0%, rgba(255, 255, 255, 0.92) 100%);
  }

  .home-role-card h3 {
    margin: 0 0 0.34rem;
    color: #17313a;
    font-size: 0.98rem;
    line-height: 1.2;
  }

  .home-role-list {
    margin: 0;
    padding-left: 1.05rem;
    color: #4d5f67;
  }

  .home-role-list li {
    margin: 0.16rem 0;
    line-height: 1.42;
  }

  .home-apply-panel {
    display: grid;
    gap: 0.62rem;
    padding: 0.95rem 1rem;
    border: 1px solid rgba(29, 102, 119, 0.12);
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.76);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.72);
  }

  .home-apply-panel h3 {
    margin: 0;
    color: #17313a;
    font-size: 1rem;
    line-height: 1.2;
  }

  .home-apply-panel p {
    margin: 0;
    color: #4d5f67;
    font-size: 0.95rem;
    line-height: 1.5;
  }

  .home-apply-list {
    margin: 0;
    padding-left: 1.15rem;
    color: #4d5f67;
  }

  .home-apply-list li {
    margin: 0.18rem 0;
    line-height: 1.45;
  }

  .home-apply-subsection {
    display: grid;
    gap: 0.28rem;
    padding: 0.72rem 0.82rem;
    border: 1px solid rgba(29, 102, 119, 0.1);
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.7);
  }

  .home-apply-subsection h4 {
    margin: 0;
    color: #1a5968;
    font-size: 0.84rem;
    font-weight: 800;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }

  .home-apply-subsection p {
    font-size: 0.91rem;
  }

  .home-apply-subject {
    padding: 0.68rem 0.78rem;
    border: 1px solid rgba(29, 102, 119, 0.12);
    border-radius: 16px;
    background: linear-gradient(180deg, rgba(241, 248, 250, 0.98) 0%, rgba(255, 255, 255, 0.96) 100%);
  }

  .home-apply-subject strong {
    display: block;
    margin-bottom: 0.28rem;
    color: #1a5968;
    font-size: 0.84rem;
    font-weight: 800;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }

  .home-apply-subject code {
    display: block;
    margin-top: 0.22rem;
    color: #17313a;
    font-size: 0.84rem;
    font-weight: 700;
    line-height: 1.45;
    white-space: normal;
    overflow-wrap: anywhere;
    background: transparent;
  }

  .home-apply-cta {
    display: inline-flex;
    width: fit-content;
    align-items: center;
    justify-content: center;
    padding: 0.62rem 0.98rem;
    border-radius: 999px;
    background: linear-gradient(135deg, #1d6677 0%, #184d5a 100%);
    color: #ffffff;
    font-weight: 700;
    line-height: 1.2;
    text-decoration: none !important;
    box-shadow: 0 12px 22px rgba(29, 102, 119, 0.16);
    transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
  }

  .home-apply-cta:hover {
    color: #ffffff;
    background: linear-gradient(135deg, #175565 0%, #143f49 100%);
    box-shadow: 0 14px 24px rgba(29, 102, 119, 0.2);
    transform: translateY(-1px);
  }

  .home-intro-copy {
    display: grid;
    gap: 0.95rem;
    max-width: 60rem;
    margin: 0 auto;
  }

  .home-summary-grid {
    display: grid;
    gap: 0.85rem;
  }

  .home-summary-card {
    position: relative;
    padding: 0.92rem 1rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 20px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.94) 0%, rgba(249, 252, 253, 0.92) 100%);
    box-shadow: 0 12px 24px rgba(18, 54, 64, 0.05);
  }

  .home-summary-card.accent {
    background: linear-gradient(135deg, rgba(255, 248, 232, 0.96) 0%, rgba(255, 255, 255, 0.92) 100%);
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
    line-height: 1.6;
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
    max-width: 60rem;
    margin: 0 auto;
    padding: 1rem;
    border: 1px solid rgba(34, 84, 97, 0.1);
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.72);
  }

  .hero-flow-note {
    margin: 0 0 0.6rem;
    color: #214d5a;
    font-size: 0.84rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .hero-flow-grid {
    display: grid;
    gap: 0.6rem;
    justify-items: center;
  }

  .hero-node {
    width: 100%;
    max-width: 100%;
    padding: 0.85rem 0.95rem 0.82rem;
    border-radius: 20px;
    border: 2px solid transparent;
    text-align: center;
    box-sizing: border-box;
    box-shadow: 0 10px 20px rgba(18, 54, 64, 0.05);
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
    padding: 1.15rem;
    border: 1px solid rgba(34, 84, 97, 0.12);
    border-radius: 26px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.98) 0%, rgba(249, 252, 253, 0.98) 100%);
    box-shadow: 0 18px 36px rgba(18, 54, 64, 0.05);
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
    gap: 0.9rem;
    margin-top: 0.8rem;
  }

  .direction-card {
    padding: 0.92rem;
    border: 1px solid rgba(34, 84, 97, 0.1);
    border-radius: 22px;
    background: linear-gradient(180deg, #ffffff 0%, #fbfdfe 100%);
    box-shadow: 0 14px 28px rgba(18, 54, 64, 0.04);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }

  .direction-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 30px rgba(18, 54, 64, 0.08);
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
    margin-bottom: 0.68rem;
    padding: 0.66rem;
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
    padding: 0.9rem 1rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #184554 0%, #1e6170 65%, #25546a 100%);
    color: #ffffff;
    box-shadow: 0 16px 28px rgba(24, 69, 84, 0.14);
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
    .home-intro {
      gap: 1.15rem;
      padding: 1.55rem;
    }

    .home-recruiting-spotlight {
      padding: 1.2rem;
    }

    .home-spotlight-grid {
      grid-template-columns: minmax(0, 1.36fr) minmax(280px, 0.96fr);
    }

    .home-role-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
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

</style>

<section class="home-intro">
  <div class="home-header">
    <p class="home-eyebrow">Information Theory · Statistical Physics · Optimization · Quantum Information</p>
    <h1 class="home-heading">Structured inference and optimization with rigorous guarantees</h1>
  </div>

  <div class="home-recruiting-spotlight">
    <div class="home-spotlight-grid">
      <div class="home-spotlight-main">
        <span class="home-recruiting-label">Open Positions</span>
        <h2 class="home-recruiting-title">Recruiting RAs, MPhil/PhD students, and Postdocs</h2>
        <p class="home-recruiting-meta">I will join HKUST (Guangzhou) as a tenure-track assistant professor in Fall 2026 in the Data Science and Analytic Thrust (DSA), Information Hub.</p>
        <p class="home-recruiting-copy">I am building a research group on graphical models, inference, optimization, machine learning, and quantum information, with an emphasis on mathematically rigorous ideas that lead to scalable algorithms.</p>
        <p class="home-recruiting-preference">I welcome applications and inquiries from research assistants, MPhil students, PhD students, and Postdocs who are excited by theory-driven work with algorithmic and systems impact.</p>
        <div class="home-institution-links">
          <a href="https://dsa.hkust-gz.edu.cn/">DSA</a>
          <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
          <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
        </div>
      </div>

      <div class="home-apply-panel">
        <h3>How to apply</h3>
        <p>Please send a concise email introducing your background and interests, together with the materials below.</p>
        <div class="home-apply-subject">
          <strong>Email title</strong>
          <code>[RA Application] Your Name - Current Institution</code>
          <code>[MPhil Inquiry] Your Name - Current Institution</code>
          <code>[PhD Inquiry] Your Name - Current Institution</code>
          <code>[Postdoc Application] Your Name - Current Institution</code>
        </div>
        <div class="home-apply-subsection">
          <h4>RA / MPhil / PhD</h4>
          <p>Include a short motivation note in the email body, plus your CV and transcript.</p>
        </div>
        <div class="home-apply-subsection">
          <h4>Postdoc</h4>
          <p>Include your CV and a short research statement describing your interests and future agenda.</p>
        </div>
        <a class="home-apply-cta" href="mailto:{{ site.author.email }}">Send application by email</a>
      </div>
    </div>

    <div class="home-role-section">
      <h3 class="home-role-heading">What I provide</h3>
      <div class="home-role-grid">
        <article class="home-role-card teal">
          <h3>RA</h3>
          <ul class="home-role-list">
            <li>Close research mentoring in structured inference, optimization, and graphical models.</li>
            <li>Hands-on exposure to mathematically grounded algorithm design and analysis.</li>
            <li>Preparation for MPhil/PhD study or algorithm-focused industry roles.</li>
          </ul>
        </article>
        <article class="home-role-card gold">
          <h3>MPhil</h3>
          <ul class="home-role-list">
            <li>A structured transition from coursework into independent research problems.</li>
            <li>Training that combines theory, applications, and rigorous performance guarantees.</li>
            <li>Preparation for PhD study or advanced R&amp;D roles in data science and systems.</li>
          </ul>
        </article>
        <article class="home-role-card green">
          <h3>PhD</h3>
          <ul class="home-role-list">
            <li>Ownership of deeper research directions at the interface of theory, algorithms, and systems.</li>
            <li>Opportunities to publish, collaborate broadly, and build an academic research profile.</li>
            <li>Preparation for academic positions or long-term research careers.</li>
          </ul>
        </article>
        <article class="home-role-card coral">
          <h3>Postdoc</h3>
          <ul class="home-role-list">
            <li>Support for building an independent research agenda and publication leadership.</li>
            <li>Opportunities to co-mentor students and shape a growing research group.</li>
            <li>Preparation for academic job searches and broader collaboration networks.</li>
          </ul>
        </article>
      </div>
    </div>
  </div>

  <div class="home-intro-copy">
    <p class="home-lead">
      I am a postdoctoral researcher at CUHK developing provable and scalable methods for inference, counting, and optimization in structured systems. My work brings together probabilistic graphical models, Bethe and graph-cover methods, combinatorics, tensor-network representations, and distributed quantum computation to turn mathematical structure into practical algorithms with rigorous guarantees.
    </p>

    <div class="home-summary-grid">
      <article class="home-summary-card">
        <h3>Current work</h3>
        <p>Structure-aware inference, combinatorial counting, optimization, and distributed quantum computation.</p>
      </article>
      <article class="home-summary-card accent">
        <h3>Future direction</h3>
        <p>Bringing structure-aware inference and optimization into machine learning, learning theory, and quantum information processing.</p>
        <div class="home-citation-row">
          <a class="home-citation" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
          <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
        </div>
      </article>
    </div>
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
        <a class="home-citation" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-sub]</a>
      </div>
    </article>

    <article class="direction-card gold">
      <div class="direction-visual">
        <svg class="figure-svg" viewBox="0 0 320 150" role="img" aria-label="Optimization illustration">
          <defs>
            <marker id="opt-arrow-head" viewBox="0 0 12 12" markerWidth="8" markerHeight="8" refX="10.5" refY="6" orient="auto" markerUnits="userSpaceOnUse">
              <path d="M1 1 L11 6 L1 11" fill="none" stroke="#d9b14f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
            </marker>
          </defs>
          <path d="M34 114 C78 82, 104 34, 150 34 C188 34, 210 104, 248 104 C270 104, 288 89, 300 58" fill="none" stroke="#d9b14f" stroke-width="5" stroke-linecap="round" marker-end="url(#opt-arrow-head)" />
          <circle cx="150" cy="34" r="8" fill="#7a5614" />
          <circle cx="248" cy="104" r="8" fill="#7a5614" />
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
          <defs>
            <marker id="tensor-arrow-head" viewBox="0 0 12 12" markerWidth="8" markerHeight="8" refX="10.5" refY="6" orient="auto" markerUnits="userSpaceOnUse">
              <path d="M1 1 L11 6 L1 11" fill="none" stroke="#cb6651" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
            </marker>
          </defs>
          <rect x="42" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <rect x="96" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <rect x="150" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <rect x="204" y="44" width="34" height="34" rx="8" fill="#efb2a7" />
          <line x1="76" y1="61" x2="96" y2="61" stroke="#cb6651" stroke-width="4" />
          <line x1="130" y1="61" x2="150" y2="61" stroke="#cb6651" stroke-width="4" />
          <line x1="184" y1="61" x2="204" y2="61" stroke="#cb6651" stroke-width="4" />
          <path d="M238 61 L296 61" stroke="#cb6651" stroke-width="5" stroke-linecap="round" marker-end="url(#tensor-arrow-head)" />
        </svg>
      </div>
      <h3>Tensor networks and quantum-enabled methods</h3>
      <p>Tensor-network representations and quantum-enabled methods for compact, high-dimensional computation.</p>
      <div class="home-citation-row">
        <a class="home-citation" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT2021]</a>
        <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
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
        <a class="home-citation" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
      </div>
    </article>
  </div>

  <div class="framework-goal">
    <span>Shared Goal</span>
    <strong>Turn mathematical structure into scalable algorithms with provable guarantees.</strong>
  </div>
</section>
