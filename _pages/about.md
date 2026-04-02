---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ═══════════════════════════════════════════════════════
   RESET & FOUNDATIONS
   ═══════════════════════════════════════════════════════ */
.splash .page__content {
  font-family: "SF Pro Display", "Inter", "Segoe UI", "Helvetica Neue", sans-serif;
  max-width: none;
  padding: 0;
  margin: 0;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}
.splash .page__content p,
.splash .page__content h1,
.splash .page__content h2,
.splash .page__content h3 { margin: 0; }
.splash .page__content a { text-decoration: none; }

/* ═══════════════════════════════════════════════════════
   SCROLL REVEAL ANIMATIONS
   ═══════════════════════════════════════════════════════ */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.92); }
  to   { opacity: 1; transform: scale(1); }
}
@keyframes slideLeft {
  from { opacity: 0; transform: translateX(60px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes slideRight {
  from { opacity: 0; transform: translateX(-60px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes glowPulse {
  0%, 100% { opacity: 0.5; }
  50%      { opacity: 1; }
}
@keyframes drawLine {
  from { stroke-dashoffset: 300; }
  to   { stroke-dashoffset: 0; }
}
@keyframes nodePopIn {
  0%   { transform: scale(0); opacity: 0; }
  70%  { transform: scale(1.15); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}
@keyframes floatY {
  0%, 100% { transform: translateY(0); }
  50%      { transform: translateY(-6px); }
}
@keyframes orbitSpin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
@keyframes tensorPulse {
  0%, 100% { rx: 8; ry: 8; }
  50%      { rx: 10; ry: 10; }
}
@keyframes flowDash {
  to { stroke-dashoffset: -20; }
}

/* Reveal classes — elements start hidden, JS adds .is-visible */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: none;
}
.reveal.is-visible {
  animation: fadeUp 0.7s cubic-bezier(0.23, 1, 0.32, 1) forwards;
}
.reveal-scale {
  opacity: 0;
  transform: scale(0.92);
}
.reveal-scale.is-visible {
  animation: scaleIn 0.65s cubic-bezier(0.23, 1, 0.32, 1) forwards;
}

/* Stagger delays for card grids */
.stagger-1 { animation-delay: 0s !important; }
.stagger-2 { animation-delay: 0.12s !important; }
.stagger-3 { animation-delay: 0.24s !important; }
.stagger-4 { animation-delay: 0.36s !important; }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .reveal, .reveal-scale { opacity: 1; transform: none; }
  .reveal.is-visible, .reveal-scale.is-visible { animation: none; opacity: 1; transform: none; }
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}

/* ═══════════════════════════════════════════════════════
   SECTION SCAFFOLD
   ═══════════════════════════════════════════════════════ */
.hp-section {
  width: 100%;
  padding: clamp(3rem, 6vw, 5.5rem) clamp(1.4rem, 4vw, 3rem);
}
.hp-inner {
  max-width: 1080px;
  margin: 0 auto;
}

/* ═══════════════════════════════════════════════════════
   HERO
   ═══════════════════════════════════════════════════════ */
.hp-hero {
  position: relative;
  text-align: center;
  padding-top: clamp(3.5rem, 8vw, 6.5rem);
  padding-bottom: clamp(3rem, 6vw, 5rem);
  background: #fff;
  overflow: hidden;
}
/* Animated gradient orb behind hero */
.hp-hero::before {
  content: "";
  position: absolute;
  top: -20%;
  left: 50%;
  transform: translateX(-50%);
  width: 800px;
  height: 800px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(23,103,122,0.08) 0%, rgba(216,155,43,0.04) 40%, transparent 70%);
  animation: glowPulse 6s ease-in-out infinite;
  pointer-events: none;
}
.hp-hero-inner {
  position: relative;
  z-index: 1;
}
.hp-hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1.1rem;
  border-radius: 999px;
  background: linear-gradient(135deg, rgba(23,103,122,0.08) 0%, rgba(216,155,43,0.06) 100%);
  border: 1px solid rgba(23,103,122,0.1);
  color: #17677a;
  font-size: 0.92rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  margin-bottom: 1.8rem;
  animation: fadeIn 0.8s 0.2s ease both;
}
.hp-hero-badge .dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #17677a;
  animation: glowPulse 2s ease-in-out infinite;
}
.hp-hero h1 {
  font-size: clamp(2.6rem, 6vw, 4.8rem);
  font-weight: 800;
  line-height: 1.06;
  letter-spacing: -0.035em;
  color: #111;
  max-width: 16ch;
  margin: 0 auto;
  text-wrap: balance;
  animation: fadeUp 0.8s 0.1s cubic-bezier(0.23,1,0.32,1) both;
}
.hp-hero h1 .gradient-text {
  background: linear-gradient(135deg, #17677a 0%, #1d8fa8 50%, #d89b2b 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.hp-hero-sub {
  margin-top: 1.3rem;
  font-size: clamp(1.12rem, 1.8vw, 1.38rem);
  line-height: 1.65;
  color: #555;
  max-width: 42rem;
  margin-left: auto;
  margin-right: auto;
  animation: fadeUp 0.8s 0.25s cubic-bezier(0.23,1,0.32,1) both;
}
.hp-hero-chips {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 1.5rem;
  animation: fadeUp 0.8s 0.35s cubic-bezier(0.23,1,0.32,1) both;
}
.hp-chip {
  padding: 0.4rem 0.9rem;
  border-radius: 999px;
  border: 1px solid rgba(23,103,122,0.12);
  background: rgba(255,255,255,0.8);
  font-size: 0.92rem;
  font-weight: 600;
  color: #1a5d6c;
}
.hp-hero-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 2rem;
  animation: fadeUp 0.8s 0.45s cubic-bezier(0.23,1,0.32,1) both;
}
.hp-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 3.1rem;
  padding: 0.8rem 2rem;
  border-radius: 14px;
  font-size: 1.08rem;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.25s cubic-bezier(0.23,1,0.32,1);
  cursor: pointer;
}
.hp-btn-primary {
  background: linear-gradient(135deg, #17677a 0%, #1a7d94 100%);
  color: #fff !important;
  box-shadow: 0 4px 20px rgba(23,103,122,0.25), inset 0 1px 0 rgba(255,255,255,0.15);
}
.hp-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(23,103,122,0.35), inset 0 1px 0 rgba(255,255,255,0.15);
}
.hp-btn-secondary {
  background: rgba(23,103,122,0.06);
  border: 1.5px solid rgba(23,103,122,0.18);
  color: #17677a !important;
}
.hp-btn-secondary:hover {
  background: rgba(23,103,122,0.1);
  border-color: rgba(23,103,122,0.3);
  transform: translateY(-2px);
}

/* ═══════════════════════════════════════════════════════
   SECTION HEADERS
   ═══════════════════════════════════════════════════════ */
.hp-section-header {
  text-align: center;
  margin-bottom: clamp(2rem, 4vw, 3.2rem);
}
.hp-section-kicker {
  font-size: 0.88rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #17677a;
  margin-bottom: 0.6rem;
}
.hp-section-title {
  font-size: clamp(1.8rem, 3.8vw, 3rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.025em;
  color: #111;
  text-wrap: balance;
}
.hp-section-sub {
  margin-top: 0.8rem;
  font-size: clamp(1.05rem, 1.5vw, 1.22rem);
  line-height: 1.6;
  color: #666;
  max-width: 40rem;
  margin-left: auto;
  margin-right: auto;
}

/* ═══════════════════════════════════════════════════════
   RESEARCH AREA CARDS (with animated SVG art)
   ═══════════════════════════════════════════════════════ */
.hp-gray { background: #f7f7f8; }

.hp-cards {
  display: grid;
  gap: 1.2rem;
  grid-template-columns: 1fr;
}
@media (min-width: 760px) {
  .hp-cards { grid-template-columns: repeat(3, 1fr); }
}
.hp-card {
  position: relative;
  overflow: hidden;
  border-radius: 22px;
  border: 1px solid rgba(0,0,0,0.06);
  display: flex;
  flex-direction: column;
  transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s ease;
}
.hp-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 48px rgba(0,0,0,0.1);
}

/* Card animated art area */
.hp-card-art {
  position: relative;
  height: 200px;
  overflow: hidden;
}
.hp-card-art svg {
  width: 100%;
  height: 100%;
  display: block;
}
.hp-card-art-teal { background: linear-gradient(160deg, #daf1f7 0%, #eef9fc 100%); }
.hp-card-art-gold { background: linear-gradient(160deg, #fef2d6 0%, #fffbf0 100%); }
.hp-card-art-coral { background: linear-gradient(160deg, #fde8e1 0%, #fef5f2 100%); }

/* Card body */
.hp-card-body {
  padding: 1.5rem 1.6rem 1.8rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  flex: 1;
  background: #fff;
}
.hp-card-label {
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}
.hp-card-label.teal { color: #17677a; }
.hp-card-label.gold { color: #9a6a12; }
.hp-card-label.coral { color: #b04a33; }

.hp-card h3 {
  font-size: 1.3rem;
  font-weight: 700;
  line-height: 1.2;
  color: #111;
}
.hp-card p {
  font-size: 1.05rem;
  line-height: 1.6;
  color: #555;
}
.hp-card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: auto;
  padding-top: 0.5rem;
}
.hp-card-tags span {
  padding: 0.3rem 0.72rem;
  border-radius: 999px;
  background: #f3f3f5;
  font-size: 0.85rem;
  font-weight: 600;
  color: #444;
}

/* ═══════════════════════════════════════════════════════
   PIPELINE (dark strip)
   ═══════════════════════════════════════════════════════ */
.hp-dark {
  background: linear-gradient(180deg, #0f1b20 0%, #152830 100%);
  color: #f5f5f7;
}
.hp-dark .hp-section-kicker { color: rgba(255,255,255,0.4); }
.hp-dark .hp-section-title { color: #f0f0f2; }

.hp-pipeline {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}
@media (min-width: 760px) {
  .hp-pipeline { grid-template-columns: repeat(4, 1fr); }
}
.hp-stage {
  position: relative;
  padding: 1.8rem 1.4rem;
  border-radius: 18px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.06);
  transition: background 0.3s ease, border-color 0.3s ease;
}
.hp-stage:hover {
  background: rgba(255,255,255,0.08);
  border-color: rgba(255,255,255,0.12);
}
.hp-stage-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.4rem;
  height: 2.4rem;
  border-radius: 10px;
  background: rgba(255,255,255,0.08);
  font-size: 0.88rem;
  font-weight: 800;
  color: rgba(255,255,255,0.5);
  margin-bottom: 1rem;
}
.hp-stage h3 {
  font-size: 1.18rem;
  font-weight: 700;
  color: #eee;
  margin-bottom: 0.45rem;
}
.hp-stage p {
  font-size: 1rem;
  line-height: 1.55;
  color: rgba(255,255,255,0.5);
}

/* ═══════════════════════════════════════════════════════
   SELECTED RESEARCH (animated paper cards)
   ═══════════════════════════════════════════════════════ */
.hp-research-grid {
  display: grid;
  gap: 1.2rem;
  grid-template-columns: 1fr;
}
@media (min-width: 760px) {
  .hp-research-grid { grid-template-columns: repeat(2, 1fr); }
}
.hp-paper {
  position: relative;
  overflow: hidden;
  border-radius: 22px;
  border: 1px solid rgba(0,0,0,0.06);
  background: #fff;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s ease;
}
.hp-paper:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 44px rgba(0,0,0,0.1);
}
/* Paper animated header */
.hp-paper-art {
  position: relative;
  height: 160px;
  overflow: hidden;
}
.hp-paper-art svg {
  width: 100%;
  height: 100%;
  display: block;
}
.hp-paper-art-teal { background: linear-gradient(160deg, #d5eff6 0%, #edf9fc 100%); }
.hp-paper-art-gold { background: linear-gradient(160deg, #fceed0 0%, #fffbf2 100%); }
.hp-paper-art-coral { background: linear-gradient(160deg, #fce3da 0%, #fef4f0 100%); }
.hp-paper-art-green { background: linear-gradient(160deg, #d9f0de 0%, #eef8f0 100%); }

.hp-paper-body {
  padding: 1.4rem 1.5rem 1.6rem;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  flex: 1;
}
.hp-paper-label {
  display: inline-flex;
  width: fit-content;
  padding: 0.28rem 0.78rem;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.hp-paper-label.teal { background: rgba(23,103,122,0.1); color: #17677a; }
.hp-paper-label.gold { background: rgba(216,155,43,0.12); color: #8b5a10; }
.hp-paper-label.coral { background: rgba(203,102,81,0.1); color: #a14430; }
.hp-paper-label.green { background: rgba(79,139,98,0.1); color: #3a7049; }

.hp-paper h3 {
  font-size: 1.22rem;
  font-weight: 700;
  line-height: 1.25;
  color: #111;
}
.hp-paper p {
  font-size: 1.02rem;
  line-height: 1.6;
  color: #555;
}
.hp-cite-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  margin-top: auto;
  padding-top: 0.3rem;
}
.hp-cite {
  display: inline-flex;
  align-items: center;
  padding: 0.35rem 0.8rem;
  border-radius: 10px;
  border: 1px solid rgba(23,103,122,0.15);
  background: rgba(23,103,122,0.04);
  color: #17677a !important;
  font-size: 0.9rem;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.2s ease;
}
.hp-cite:hover {
  background: rgba(23,103,122,0.12);
  border-color: rgba(23,103,122,0.3);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(23,103,122,0.1);
}

/* ═══════════════════════════════════════════════════════
   RECRUIT SECTION
   ═══════════════════════════════════════════════════════ */
.hp-recruit {
  text-align: center;
  background:
    radial-gradient(ellipse 60% 50% at 50% 100%, rgba(216,155,43,0.05) 0%, transparent 70%),
    #fff;
}
.hp-recruit-title {
  font-size: clamp(1.8rem, 3.8vw, 3rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.025em;
  color: #111;
  text-wrap: balance;
}
.hp-recruit-sub {
  margin-top: 0.9rem;
  font-size: clamp(1.05rem, 1.5vw, 1.22rem);
  line-height: 1.6;
  color: #555;
  max-width: 44rem;
  margin-left: auto;
  margin-right: auto;
}
.hp-recruit-meta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1.2rem;
  padding: 0.45rem 1.1rem;
  border-radius: 999px;
  background: rgba(216,155,43,0.08);
  border: 1px solid rgba(216,155,43,0.15);
  font-size: 0.95rem;
  font-weight: 700;
  color: #8b5a10;
}
.hp-roles {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
  margin-top: 2.5rem;
  text-align: left;
}
@media (min-width: 760px) {
  .hp-roles { grid-template-columns: repeat(4, 1fr); }
}
.hp-role {
  padding: 1.5rem 1.3rem;
  border-radius: 18px;
  background: #f7f7f8;
  border: 1px solid rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.hp-role:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 28px rgba(0,0,0,0.06);
}
.hp-role h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #111;
}
.hp-role p {
  font-size: 1rem;
  line-height: 1.55;
  color: #555;
}
.hp-recruit-cta {
  margin-top: 2.5rem;
}
.hp-recruit-links {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  margin-top: 1rem;
}
.hp-recruit-links a {
  font-size: 1rem;
  font-weight: 600;
  color: #17677a !important;
  text-decoration: none !important;
  transition: color 0.2s ease;
}
.hp-recruit-links a:hover { color: #114e5d !important; }
.hp-recruit-links a::after { content: " \2197"; font-size: 0.8em; }

/* ═══════════════════════════════════════════════════════
   ANIMATED SVG HELPERS
   ═══════════════════════════════════════════════════════ */
.anim-line {
  stroke-dasharray: 300;
  stroke-dashoffset: 300;
}
.is-visible .anim-line {
  animation: drawLine 1.2s ease forwards;
}
.is-visible .anim-line.d2 { animation-delay: 0.2s; }
.is-visible .anim-line.d3 { animation-delay: 0.4s; }
.is-visible .anim-line.d4 { animation-delay: 0.6s; }

.anim-node {
  transform-origin: center;
  transform: scale(0);
  opacity: 0;
}
.is-visible .anim-node {
  animation: nodePopIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
.is-visible .anim-node.d2 { animation-delay: 0.15s; }
.is-visible .anim-node.d3 { animation-delay: 0.3s; }
.is-visible .anim-node.d4 { animation-delay: 0.45s; }
.is-visible .anim-node.d5 { animation-delay: 0.6s; }

.float-anim {
  animation: floatY 3s ease-in-out infinite;
}
.float-anim.slow { animation-duration: 4s; }
.float-anim.offset { animation-delay: -1.5s; }

/* Flowing dashed lines */
.flow-line {
  stroke-dasharray: 8 6;
  animation: flowDash 1.5s linear infinite;
}

/* Orbit ring */
.orbit-ring {
  transform-origin: center;
  animation: orbitSpin 12s linear infinite;
}
</style>

<!-- ════════════════════════════════════════════════════════
     HERO
     ════════════════════════════════════════════════════════ -->
<section class="hp-section hp-hero">
  <div class="hp-inner hp-hero-inner">
    <p class="hp-hero-badge"><span class="dot"></span> Yuwen Huang · Researcher</p>
    <h1>Provable methods for <span class="gradient-text">structured inference</span></h1>
    <p class="hp-hero-sub">
      Scalable algorithms with rigorous guarantees — built on graphical models, combinatorics, tensor networks, and distributed quantum systems.
    </p>
    <div class="hp-hero-chips">
      <span class="hp-chip">Bethe methods</span>
      <span class="hp-chip">Combinatorial counting</span>
      <span class="hp-chip">Tensor networks</span>
      <span class="hp-chip">Quantum systems</span>
    </div>
    <div class="hp-hero-actions">
      <a class="hp-btn hp-btn-primary" href="#positions">Open positions</a>
      <a class="hp-btn hp-btn-secondary" href="#research">Selected research</a>
    </div>
  </div>
</section>

<!-- ════════════════════════════════════════════════════════
     RESEARCH AREAS (animated SVG illustrations)
     ════════════════════════════════════════════════════════ -->
<section class="hp-section hp-gray">
  <div class="hp-inner">
    <div class="hp-section-header reveal">
      <p class="hp-section-kicker">Research areas</p>
      <h2 class="hp-section-title">Three pillars, one pursuit</h2>
      <p class="hp-section-sub">Turning mathematical structure into practical, scalable computation.</p>
    </div>
    <div class="hp-cards">

      <!-- INFERENCE CARD -->
      <article class="hp-card reveal-scale stagger-1">
        <div class="hp-card-art hp-card-art-teal">
          <svg viewBox="0 0 400 200" role="img" aria-label="Graphical model with message-passing illustration">
            <!-- Edges (animate draw) -->
            <line x1="90" y1="70" x2="180" y2="55" class="anim-line" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="90" y1="70" x2="160" y2="140" class="anim-line d2" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="180" y1="55" x2="270" y2="80" class="anim-line d3" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="160" y1="140" x2="270" y2="80" class="anim-line d3" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="270" y1="80" x2="340" y2="100" class="anim-line d4" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <!-- Message arrows (flowing) -->
            <line x1="120" y1="63" x2="155" y2="57" class="flow-line" stroke="#2f7f93" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="200" y1="62" x2="245" y2="75" class="flow-line" stroke="#2f7f93" stroke-width="2.5" stroke-linecap="round"/>
            <!-- Nodes -->
            <circle cx="90" cy="70" r="18" class="anim-node" fill="#2f7f93"/>
            <circle cx="180" cy="55" r="15" class="anim-node d2" fill="#2f7f93"/>
            <circle cx="160" cy="140" r="15" class="anim-node d3" fill="#5ba3b4"/>
            <circle cx="270" cy="80" r="17" class="anim-node d4" fill="#2f7f93"/>
            <circle cx="340" cy="100" r="14" class="anim-node d5" fill="#5ba3b4"/>
            <!-- Factor boxes -->
            <rect x="295" y="130" width="80" height="38" rx="10" class="anim-node d4" fill="#e0f3f8" stroke="#78b8c7" stroke-width="2"/>
            <rect x="302" y="140" width="8" height="18" rx="3" fill="#2f7f93" class="float-anim"/>
            <rect x="316" y="134" width="8" height="24" rx="3" fill="#78b8c7" class="float-anim offset"/>
            <rect x="330" y="138" width="8" height="20" rx="3" fill="#2f7f93" class="float-anim"/>
            <rect x="344" y="142" width="8" height="16" rx="3" fill="#78b8c7" class="float-anim offset"/>
            <text x="90" y="75" text-anchor="middle" fill="#fff" font-size="11" font-weight="800">x₁</text>
            <text x="180" y="60" text-anchor="middle" fill="#fff" font-size="11" font-weight="800">x₂</text>
            <text x="270" y="85" text-anchor="middle" fill="#fff" font-size="11" font-weight="800">x₃</text>
          </svg>
        </div>
        <div class="hp-card-body">
          <p class="hp-card-label teal">Inference</p>
          <h3>Structured graphical-model reasoning</h3>
          <p>Message passing, Bethe methods, and combinatorial structure for reliable inference and counting.</p>
          <div class="hp-card-tags">
            <span>Uncertainty</span><span>Counting</span><span>Graph covers</span>
          </div>
        </div>
      </article>

      <!-- OPTIMIZATION CARD -->
      <article class="hp-card reveal-scale stagger-2">
        <div class="hp-card-art hp-card-art-gold">
          <svg viewBox="0 0 400 200" role="img" aria-label="Optimization landscape illustration">
            <defs>
              <linearGradient id="opt-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#e8c75a"/>
                <stop offset="100%" stop-color="#d89b2b"/>
              </linearGradient>
              <marker id="opt-arr" viewBox="0 0 10 10" markerWidth="7" markerHeight="7" refX="9" refY="5" orient="auto">
                <path d="M1 1 L9 5 L1 9" fill="none" stroke="#d89b2b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
              </marker>
            </defs>
            <!-- Landscape curve -->
            <path d="M40 140 C80 110, 100 50, 150 50 C200 50, 220 135, 270 135 C305 135, 325 105, 355 65" class="anim-line" fill="none" stroke="url(#opt-grad)" stroke-width="5" stroke-linecap="round" marker-end="url(#opt-arr)"/>
            <!-- Critical points -->
            <circle cx="150" cy="50" r="12" class="anim-node d2 float-anim" fill="#8a5b10"/>
            <circle cx="270" cy="135" r="12" class="anim-node d3 float-anim offset" fill="#8a5b10"/>
            <!-- Bound labels -->
            <rect x="68" y="28" width="66" height="30" rx="10" class="anim-node d3" fill="#fff6de" stroke="#ead28d" stroke-width="2"/>
            <text x="101" y="48" text-anchor="middle" fill="#8a5b10" font-size="12" font-weight="800">Bounds</text>
            <rect x="280" y="28" width="82" height="30" rx="10" class="anim-node d4" fill="#fff6de" stroke="#ead28d" stroke-width="2"/>
            <text x="321" y="48" text-anchor="middle" fill="#8a5b10" font-size="12" font-weight="800">Algorithms</text>
            <!-- Baseline -->
            <line x1="60" y1="170" x2="340" y2="170" class="anim-line d4" stroke="#ead28d" stroke-width="3" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="hp-card-body">
          <p class="hp-card-label gold">Optimization</p>
          <h3>Provable optimization and decision-making</h3>
          <p>Structure-aware objectives, permanent bounds, and algorithmic guarantees for hard problems.</p>
          <div class="hp-card-tags">
            <span>Convex / nonconvex</span><span>Permanent bounds</span><span>Decisions</span>
          </div>
        </div>
      </article>

      <!-- QUANTUM & TENSORS CARD -->
      <article class="hp-card reveal-scale stagger-3">
        <div class="hp-card-art hp-card-art-coral">
          <svg viewBox="0 0 400 200" role="img" aria-label="Tensor network and quantum illustration">
            <!-- Tensor chain -->
            <line x1="82" y1="90" x2="132" y2="90" class="anim-line" stroke="#cb6651" stroke-width="4" stroke-linecap="round"/>
            <line x1="172" y1="90" x2="222" y2="90" class="anim-line d2" stroke="#cb6651" stroke-width="4" stroke-linecap="round"/>
            <line x1="262" y1="90" x2="312" y2="90" class="anim-line d3" stroke="#cb6651" stroke-width="4" stroke-linecap="round"/>
            <!-- Tensor nodes -->
            <rect x="42" y="72" width="40" height="36" rx="10" class="anim-node" fill="#efb2a7"/>
            <rect x="132" y="72" width="40" height="36" rx="10" class="anim-node d2" fill="#efb2a7"/>
            <rect x="222" y="72" width="40" height="36" rx="10" class="anim-node d3" fill="#efb2a7"/>
            <rect x="312" y="72" width="40" height="36" rx="10" class="anim-node d4" fill="#efb2a7"/>
            <!-- Vertical bonds -->
            <line x1="62" y1="72" x2="62" y2="52" class="anim-line d2" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <line x1="152" y1="72" x2="152" y2="52" class="anim-line d3" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <line x1="242" y1="72" x2="242" y2="52" class="anim-line d3" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <line x1="332" y1="72" x2="332" y2="52" class="anim-line d4" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <!-- Quantum orbit ring -->
            <g style="transform-origin: 200px 148px;" class="orbit-ring">
              <ellipse cx="200" cy="148" rx="55" ry="18" fill="none" stroke="#86b894" stroke-width="2" stroke-dasharray="5 4"/>
            </g>
            <circle cx="200" cy="148" r="10" class="anim-node d4" fill="#4f8b62"/>
            <circle cx="252" cy="144" r="7" class="anim-node d5 float-anim" fill="#86b894"/>
            <circle cx="148" cy="144" r="7" class="anim-node d5 float-anim offset" fill="#86b894"/>
          </svg>
        </div>
        <div class="hp-card-body">
          <p class="hp-card-label coral">Quantum &amp; Tensors</p>
          <h3>High-dimensional quantum computation</h3>
          <p>Tensor-network representations and distributed quantum systems for scalable computation.</p>
          <div class="hp-card-tags">
            <span>Tensor networks</span><span>Quantum systems</span><span>Scalability</span>
          </div>
        </div>
      </article>

    </div>
  </div>
</section>

<!-- ════════════════════════════════════════════════════════
     PIPELINE (dark)
     ════════════════════════════════════════════════════════ -->
<section class="hp-section hp-dark">
  <div class="hp-inner">
    <div class="hp-section-header reveal">
      <p class="hp-section-kicker">From theory to impact</p>
      <h2 class="hp-section-title">Structure becomes computation</h2>
    </div>
    <div class="hp-pipeline">
      <div class="hp-stage reveal stagger-1">
        <div class="hp-stage-num">01</div>
        <h3>Information theory &amp; statistical physics</h3>
        <p>Structure, correlation, and entropy motivate the underlying questions.</p>
      </div>
      <div class="hp-stage reveal stagger-2">
        <div class="hp-stage-num">02</div>
        <h3>Inference, counting, optimization</h3>
        <p>Bethe methods, graph covers, and structure-aware optimization.</p>
      </div>
      <div class="hp-stage reveal stagger-3">
        <div class="hp-stage-num">03</div>
        <h3>Distributed quantum systems</h3>
        <p>Quantum networks extending the computational regime.</p>
      </div>
      <div class="hp-stage reveal stagger-4">
        <div class="hp-stage-num">04</div>
        <h3>ML &amp; efficient computation</h3>
        <p>Learning theory, analytics, and large-scale decision making.</p>
      </div>
    </div>
  </div>
</section>

<!-- ════════════════════════════════════════════════════════
     SELECTED RESEARCH (with animated SVG per paper)
     ════════════════════════════════════════════════════════ -->
<section class="hp-section hp-gray" id="research">
  <div class="hp-inner">
    <div class="hp-section-header reveal">
      <p class="hp-section-kicker">Selected research</p>
      <h2 class="hp-section-title">Representative directions and papers</h2>
    </div>
    <div class="hp-research-grid">

      <!-- PAPER 1: Graphical models -->
      <article class="hp-paper reveal-scale stagger-1">
        <div class="hp-paper-art hp-paper-art-teal">
          <svg viewBox="0 0 400 160" role="img" aria-label="Graphical models">
            <line x1="80" y1="60" x2="150" y2="42" class="anim-line" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="80" y1="60" x2="130" y2="115" class="anim-line d2" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="150" y1="42" x2="240" y2="68" class="anim-line d3" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="130" y1="115" x2="240" y2="68" class="anim-line d3" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="240" y1="68" x2="310" y2="58" class="anim-line d4" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <line x1="310" y1="58" x2="350" y2="98" class="anim-line d4" stroke="#78b8c7" stroke-width="4" stroke-linecap="round"/>
            <!-- Graph cover overlay (dashed) -->
            <line x1="95" y1="54" x2="145" y2="38" class="flow-line" stroke="#2f7f93" stroke-width="2" stroke-linecap="round"/>
            <line x1="255" y1="62" x2="305" y2="54" class="flow-line" stroke="#2f7f93" stroke-width="2" stroke-linecap="round"/>
            <circle cx="80" cy="60" r="14" class="anim-node" fill="#2f7f93"/>
            <circle cx="150" cy="42" r="12" class="anim-node d2" fill="#2f7f93"/>
            <circle cx="130" cy="115" r="12" class="anim-node d3" fill="#5ba3b4"/>
            <circle cx="240" cy="68" r="14" class="anim-node d3" fill="#2f7f93"/>
            <circle cx="310" cy="58" r="11" class="anim-node d4" fill="#5ba3b4"/>
            <circle cx="350" cy="98" r="11" class="anim-node d5" fill="#2f7f93"/>
          </svg>
        </div>
        <div class="hp-paper-body">
          <span class="hp-paper-label teal">Inference</span>
          <h3>Graphical models and Bethe methods</h3>
          <p>Bethe approximations, graph covers, and message passing for principled inference and counting.</p>
          <div class="hp-cite-row">
            <a class="hp-cite" href="{{ '/publication/characterizing-bethe-partition-factor-graphs' | relative_url }}">[ISIT2020]</a>
            <a class="hp-cite" href="{{ '/publication/bethe-free-energy-global-minimum' | relative_url }}">[ITW2022]</a>
            <a class="hp-cite" href="{{ '/publication/bethe-partition-spa-stable-polynomials' | relative_url }}">[ISIT2024]</a>
            <a class="hp-cite" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-sub]</a>
          </div>
        </div>
      </article>

      <!-- PAPER 2: Optimization -->
      <article class="hp-paper reveal-scale stagger-2">
        <div class="hp-paper-art hp-paper-art-gold">
          <svg viewBox="0 0 400 160" role="img" aria-label="Optimization landscape">
            <defs>
              <marker id="p-opt-arr" viewBox="0 0 10 10" markerWidth="7" markerHeight="7" refX="9" refY="5" orient="auto">
                <path d="M1 1 L9 5 L1 9" fill="none" stroke="#d89b2b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
              </marker>
            </defs>
            <path d="M50 115 C90 85, 115 30, 160 30 C210 30, 230 110, 275 110 C310 110, 330 80, 355 50" class="anim-line" fill="none" stroke="#d9b14f" stroke-width="5" stroke-linecap="round" marker-end="url(#p-opt-arr)"/>
            <circle cx="160" cy="30" r="11" class="anim-node d2 float-anim" fill="#8a5b10"/>
            <circle cx="275" cy="110" r="11" class="anim-node d3 float-anim offset" fill="#8a5b10"/>
            <line x1="70" y1="138" x2="335" y2="138" class="anim-line d4" stroke="#ead28d" stroke-width="3" stroke-linecap="round"/>
            <!-- Gradient descent arrows -->
            <path d="M110 66 L140 40" class="anim-line d3" fill="none" stroke="#b38320" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="4 3"/>
            <path d="M310 88 L340 58" class="anim-line d4" fill="none" stroke="#b38320" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="4 3"/>
          </svg>
        </div>
        <div class="hp-paper-body">
          <span class="hp-paper-label gold">Optimization</span>
          <h3>Optimization and combinatorial structure</h3>
          <p>Structure-exploiting optimization and permanent bounds with rigorous guarantees.</p>
          <div class="hp-cite-row">
            <a class="hp-cite" href="{{ '/publication/bounding-permanent-degree-m-bethe' | relative_url }}">[ISIT2023]</a>
            <a class="hp-cite" href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">[TIT2024]</a>
            <a class="hp-cite" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
          </div>
        </div>
      </article>

      <!-- PAPER 3: Tensor methods -->
      <article class="hp-paper reveal-scale stagger-3">
        <div class="hp-paper-art hp-paper-art-coral">
          <svg viewBox="0 0 400 160" role="img" aria-label="Tensor network chain">
            <!-- Tensor chain bonds -->
            <line x1="90" y1="65" x2="140" y2="65" class="anim-line" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
            <line x1="180" y1="65" x2="230" y2="65" class="anim-line d2" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
            <line x1="270" y1="65" x2="320" y2="65" class="anim-line d3" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
            <!-- Tensor nodes -->
            <rect x="50" y="47" width="40" height="36" rx="10" class="anim-node" fill="#e8947f"/>
            <rect x="140" y="47" width="40" height="36" rx="10" class="anim-node d2" fill="#e8947f"/>
            <rect x="230" y="47" width="40" height="36" rx="10" class="anim-node d3" fill="#e8947f"/>
            <rect x="320" y="47" width="40" height="36" rx="10" class="anim-node d4" fill="#e8947f"/>
            <!-- Physical indices (vertical) -->
            <line x1="70" y1="47" x2="70" y2="27" class="anim-line d2" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <line x1="160" y1="47" x2="160" y2="27" class="anim-line d3" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <line x1="250" y1="47" x2="250" y2="27" class="anim-line d3" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <line x1="340" y1="47" x2="340" y2="27" class="anim-line d4" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <!-- Contraction arrow -->
            <path d="M360 65 L390 65" class="flow-line" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
            <!-- Result -->
            <rect x="120" y="110" width="180" height="30" rx="12" class="anim-node d5" fill="#fde8e1" stroke="#e8947f" stroke-width="2"/>
            <text x="210" y="130" text-anchor="middle" fill="#a14430" font-size="12" font-weight="700">Compact representation</text>
          </svg>
        </div>
        <div class="hp-paper-body">
          <span class="hp-paper-label coral">Tensor methods</span>
          <h3>Tensor networks and quantum-enabled inference</h3>
          <p>Compact high-dimensional computation via tensor-network representations.</p>
          <div class="hp-cite-row">
            <a class="hp-cite" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT2021]</a>
            <a class="hp-cite" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
          </div>
        </div>
      </article>

      <!-- PAPER 4: Distributed quantum -->
      <article class="hp-paper reveal-scale stagger-4">
        <div class="hp-paper-art hp-paper-art-green">
          <svg viewBox="0 0 400 160" role="img" aria-label="Distributed quantum network">
            <!-- Network links -->
            <line x1="82" y1="70" x2="172" y2="45" class="anim-line" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
            <line x1="82" y1="70" x2="172" y2="110" class="anim-line d2" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
            <line x1="172" y1="45" x2="260" y2="70" class="anim-line d3" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
            <line x1="172" y1="110" x2="260" y2="70" class="anim-line d3" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
            <line x1="260" y1="70" x2="340" y2="55" class="anim-line d4" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
            <line x1="260" y1="70" x2="340" y2="105" class="anim-line d4" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
            <!-- Entanglement pulses -->
            <line x1="110" y1="62" x2="145" y2="52" class="flow-line" stroke="#4f8b62" stroke-width="2" stroke-linecap="round"/>
            <line x1="195" y1="55" x2="235" y2="65" class="flow-line" stroke="#4f8b62" stroke-width="2" stroke-linecap="round"/>
            <line x1="285" y1="65" x2="318" y2="58" class="flow-line" stroke="#4f8b62" stroke-width="2" stroke-linecap="round"/>
            <!-- Quantum processor nodes -->
            <rect x="62" y="54" width="32" height="32" rx="9" class="anim-node" fill="#4f8b62"/>
            <rect x="156" y="29" width="32" height="32" rx="9" class="anim-node d2" fill="#4f8b62"/>
            <rect x="156" y="94" width="32" height="32" rx="9" class="anim-node d3" fill="#4f8b62"/>
            <rect x="244" y="54" width="32" height="32" rx="9" class="anim-node d3" fill="#4f8b62"/>
            <rect x="324" y="39" width="32" height="32" rx="9" class="anim-node d4" fill="#6aa67a"/>
            <rect x="324" y="89" width="32" height="32" rx="9" class="anim-node d5" fill="#6aa67a"/>
            <!-- Labels -->
            <text x="78" y="75" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Q₁</text>
            <text x="172" y="50" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Q₂</text>
            <text x="260" y="75" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Q₃</text>
          </svg>
        </div>
        <div class="hp-paper-body">
          <span class="hp-paper-label green">Quantum systems</span>
          <h3>Distributed quantum systems</h3>
          <p>Distributed quantum architectures for optimization, inference, and analytics.</p>
          <div class="hp-cite-row">
            <a class="hp-cite" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
            <a class="hp-cite" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
          </div>
        </div>
      </article>

    </div>
  </div>
</section>

<!-- ════════════════════════════════════════════════════════
     OPEN POSITIONS
     ════════════════════════════════════════════════════════ -->
<section class="hp-section hp-recruit" id="positions">
  <div class="hp-inner">
    <div class="reveal">
      <h2 class="hp-recruit-title">Join the group</h2>
      <p class="hp-recruit-sub">
        Recruiting RAs, MPhil/PhD students, and one Postdoc for Fall 2026 at HKUST (Guangzhou), Data Science and Analytics Thrust.
      </p>
      <p class="hp-recruit-meta">Tenure-track Assistant Professor · Information Hub · DSA</p>
    </div>
    <div class="hp-roles">
      <div class="hp-role reveal stagger-1">
        <h3>RA</h3>
        <p>Core research training and preparation for graduate study or industry roles.</p>
      </div>
      <div class="hp-role reveal stagger-2">
        <h3>MPhil</h3>
        <p>Structured transition into independent research with publication-minded training.</p>
      </div>
      <div class="hp-role reveal stagger-3">
        <h3>PhD</h3>
        <p>Ownership of deeper problems, broad collaboration, and long-term research support.</p>
      </div>
      <div class="hp-role reveal stagger-4">
        <h3>Postdoc</h3>
        <p>Shape an agenda, co-mentor students, and prepare for academic searches.</p>
      </div>
    </div>
    <div class="hp-recruit-cta reveal">
      <a class="hp-btn hp-btn-primary" href="mailto:{{ site.author.email }}">Apply by email</a>
    </div>
    <div class="hp-recruit-links reveal">
      <a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>
      <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
      <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
    </div>
  </div>
</section>

<!-- ════════════════════════════════════════════════════════
     SCROLL REVEAL SCRIPT
     ════════════════════════════════════════════════════════ -->
<script>
document.addEventListener("DOMContentLoaded", function () {
  var els = document.querySelectorAll(".reveal, .reveal-scale");
  if (!("IntersectionObserver" in window)) {
    // Fallback: just show everything
    els.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
  els.forEach(function (el) { observer.observe(el); });
});
</script>
