---
permalink: /
title: "Yuwen Huang"
layout: splash
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ══════════════════════════════════════════════════
   FOUNDATIONS
   ══════════════════════════════════════════════════ */
.splash .page__content {
  font-family: "SF Pro Display","Inter","Segoe UI","Helvetica Neue",sans-serif;
  max-width: none; padding: 0; margin: 0; overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}
.splash .page__content p,
.splash .page__content h1,
.splash .page__content h2,
.splash .page__content h3 { margin:0; }
.splash .page__content a { text-decoration:none; }

/* ══════════════════════════════════════════════════
   KEYFRAMES
   ══════════════════════════════════════════════════ */
@keyframes fadeUp   { from{opacity:0;transform:translateY(30px)} to{opacity:1;transform:translateY(0)} }
@keyframes scaleIn  { from{opacity:0;transform:scale(.93)} to{opacity:1;transform:scale(1)} }
@keyframes pulse    { 0%,100%{opacity:.45} 50%{opacity:1} }
@keyframes float1   { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
@keyframes float2   { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }
@keyframes drawPath { from{stroke-dashoffset:500} to{stroke-dashoffset:0} }
@keyframes flowDash { to{stroke-dashoffset:-24} }
@keyframes popNode  { 0%{transform:scale(0);opacity:0} 60%{transform:scale(1.18);opacity:1} 100%{transform:scale(1);opacity:1} }
@keyframes orbit    { from{transform:rotate(0)} to{transform:rotate(360deg)} }
@keyframes gradShift{ 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
@keyframes shimmer  { 0%{background-position:-200% 0} 100%{background-position:200% 0} }

/* Scroll reveal */
.rv { opacity:0; transform:translateY(28px); }
.rv.vis { animation: fadeUp .6s cubic-bezier(.22,1,.36,1) forwards; }
.rv-s { opacity:0; transform:scale(.93); }
.rv-s.vis { animation: scaleIn .55s cubic-bezier(.22,1,.36,1) forwards; }
.d1{animation-delay:0s!important} .d2{animation-delay:.1s!important} .d3{animation-delay:.2s!important} .d4{animation-delay:.3s!important}
@media(prefers-reduced-motion:reduce){
  .rv,.rv-s{opacity:1;transform:none}
  .rv.vis,.rv-s.vis{animation:none;opacity:1;transform:none}
  *,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}
}

/* ══════════════════════════════════════════════════
   LAYOUT
   ══════════════════════════════════════════════════ */
.s { width:100%; padding: clamp(2.2rem,4vw,3.5rem) clamp(1.2rem,3.5vw,2.5rem); }
.s-inner { max-width:1060px; margin:0 auto; }

/* ══════════════════════════════════════════════════
   HERO — personal intro + announcement
   ══════════════════════════════════════════════════ */
.hero {
  position:relative; overflow:hidden;
  padding-top: clamp(2rem,4vw,3.2rem);
  padding-bottom: clamp(2rem,4vw,3rem);
  background: linear-gradient(170deg, #f0fafe 0%, #fff 35%, #fffdf6 70%, #f7fbfc 100%);
}
.hero::before {
  content:""; position:absolute; top:-30%; right:-10%; width:600px; height:600px;
  border-radius:50%; background:radial-gradient(circle,rgba(23,103,122,.06) 0%,transparent 70%);
  animation:pulse 5s ease-in-out infinite; pointer-events:none;
}
.hero::after {
  content:""; position:absolute; bottom:-20%; left:-5%; width:400px; height:400px;
  border-radius:50%; background:radial-gradient(circle,rgba(216,155,43,.05) 0%,transparent 70%);
  animation:pulse 6s ease-in-out infinite 1s; pointer-events:none;
}
.hero-inner { position:relative; z-index:1; }

/* Top bar: photo + name + affiliation */
.hero-profile {
  display:flex; align-items:center; gap:1.2rem;
  margin-bottom:1.6rem;
  animation: fadeUp .7s .1s cubic-bezier(.22,1,.36,1) both;
}
.hero-avatar {
  width:72px; height:72px; border-radius:50%;
  object-fit:cover; border:3px solid #fff;
  box-shadow:0 4px 20px rgba(0,0,0,.08);
}
.hero-id h2 {
  font-size:1.5rem; font-weight:800; color:#111; line-height:1.2;
}
.hero-id p {
  font-size:1.02rem; color:#555; line-height:1.4; margin-top:.15rem;
}
.hero-id a { color:#17677a; font-weight:600; }
.hero-id a:hover { color:#114e5d; }

/* Announcement banner */
.hero-announce {
  display:inline-flex; align-items:center; gap:.6rem;
  padding:.5rem 1.1rem; border-radius:12px;
  background: linear-gradient(135deg, rgba(216,155,43,.1) 0%, rgba(23,103,122,.08) 100%);
  border:1px solid rgba(216,155,43,.18);
  margin-bottom:1.5rem;
  animation: fadeUp .7s .2s cubic-bezier(.22,1,.36,1) both;
}
.hero-announce .dot {
  width:8px;height:8px;border-radius:50%;
  background:linear-gradient(135deg,#d89b2b,#17677a);
  animation:pulse 2s ease-in-out infinite;
  flex-shrink:0;
}
.hero-announce span {
  font-size:.95rem; font-weight:700; color:#6b4510; line-height:1.35;
}
.hero-announce a { color:#17677a; font-weight:800; }

/* Headline */
.hero h1 {
  font-size: clamp(2.2rem,5vw,3.8rem);
  font-weight:800; line-height:1.08; letter-spacing:-.03em; color:#111;
  max-width:18ch;
  animation: fadeUp .7s .15s cubic-bezier(.22,1,.36,1) both;
}
.hero h1 em {
  font-style:normal;
  background: linear-gradient(135deg,#17677a 0%,#1e99b5 40%,#d89b2b 100%);
  background-size:200% 200%;
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent;
  animation: gradShift 6s ease infinite;
}
.hero-sub {
  margin-top:.9rem;
  font-size: clamp(1.08rem,1.6vw,1.28rem);
  line-height:1.6; color:#444; max-width:48rem;
  animation: fadeUp .7s .25s cubic-bezier(.22,1,.36,1) both;
}

/* Chips */
.hero-chips {
  display:flex; flex-wrap:wrap; gap:.5rem; margin-top:1.2rem;
  animation: fadeUp .7s .3s cubic-bezier(.22,1,.36,1) both;
}
.chip {
  padding:.38rem .85rem; border-radius:10px;
  border:1px solid rgba(23,103,122,.12);
  background:rgba(255,255,255,.8);
  font-size:.92rem; font-weight:600; color:#1a5d6c;
}

/* CTAs */
.hero-cta {
  display:flex; flex-wrap:wrap; gap:.8rem; margin-top:1.5rem;
  animation: fadeUp .7s .35s cubic-bezier(.22,1,.36,1) both;
}
.btn {
  display:inline-flex; align-items:center; justify-content:center;
  min-height:2.9rem; padding:.7rem 1.7rem; border-radius:12px;
  font-size:1.05rem; font-weight:700; cursor:pointer;
  text-decoration:none!important;
  transition:all .22s cubic-bezier(.22,1,.36,1);
}
.btn-p {
  background:linear-gradient(135deg,#17677a,#1a8199);
  color:#fff!important;
  box-shadow:0 3px 16px rgba(23,103,122,.22);
}
.btn-p:hover { transform:translateY(-2px); box-shadow:0 6px 28px rgba(23,103,122,.32); }
.btn-s {
  background:rgba(23,103,122,.06); border:1.5px solid rgba(23,103,122,.16);
  color:#17677a!important;
}
.btn-s:hover { background:rgba(23,103,122,.1); border-color:rgba(23,103,122,.28); transform:translateY(-2px); }

/* ══════════════════════════════════════════════════
   SECTION HEADERS
   ══════════════════════════════════════════════════ */
.sh { text-align:center; margin-bottom:clamp(1.5rem,3vw,2.2rem); }
.sh-k { font-size:.86rem; font-weight:700; letter-spacing:.07em; text-transform:uppercase; color:#17677a; margin-bottom:.4rem; }
.sh-t { font-size:clamp(1.7rem,3.5vw,2.6rem); font-weight:800; line-height:1.1; letter-spacing:-.02em; color:#111; }
.sh-sub { margin-top:.5rem; font-size:clamp(1.02rem,1.4vw,1.15rem); line-height:1.55; color:#666; max-width:38rem; margin-left:auto; margin-right:auto; }
.dark .sh-k { color:rgba(255,255,255,.4); }
.dark .sh-t { color:#eee; }

/* ══════════════════════════════════════════════════
   RESEARCH CARDS — bold animated SVGs
   ══════════════════════════════════════════════════ */
.bg-g { background:#f5f5f7; }

.cards { display:grid; gap:1rem; }
@media(min-width:760px){ .cards{grid-template-columns:repeat(3,1fr)} }
.card {
  border-radius:20px; border:1px solid rgba(0,0,0,.06);
  overflow:hidden; display:flex; flex-direction:column;
  transition:transform .28s cubic-bezier(.22,1,.36,1),box-shadow .28s ease;
}
.card:hover { transform:translateY(-5px); box-shadow:0 18px 40px rgba(0,0,0,.1); }

/* Card art — taller, bolder */
.card-art { position:relative; height:180px; overflow:hidden; display:flex; align-items:center; justify-content:center; }
.card-art svg { width:92%; height:92%; }
.card-art-t { background:linear-gradient(145deg,#d0eef6 0%,#e8f7fb 100%); }
.card-art-g { background:linear-gradient(145deg,#fcefd2 0%,#fffaf0 100%); }
.card-art-c { background:linear-gradient(145deg,#fce0d6 0%,#fef3ef 100%); }

.card-body {
  padding:1.3rem 1.4rem 1.5rem; display:flex; flex-direction:column;
  gap:.45rem; flex:1; background:#fff;
}
.card-lbl { font-size:.82rem; font-weight:800; letter-spacing:.06em; text-transform:uppercase; }
.card-lbl-t { color:#17677a; } .card-lbl-g { color:#9a6a12; } .card-lbl-c { color:#b04a33; }
.card h3 { font-size:1.22rem; font-weight:700; line-height:1.2; color:#111; }
.card p  { font-size:1.02rem; line-height:1.55; color:#555; }
.card-tags { display:flex; flex-wrap:wrap; gap:.35rem; margin-top:auto; padding-top:.4rem; }
.card-tags span { padding:.28rem .65rem; border-radius:8px; background:#f0f0f2; font-size:.84rem; font-weight:600; color:#444; }

/* SVG anim helpers — always visible, looping */
.nd { transform-origin:center; animation: popNode .5s cubic-bezier(.34,1.56,.64,1) both; }
.nd-2{animation-delay:.12s} .nd-3{animation-delay:.24s} .nd-4{animation-delay:.36s} .nd-5{animation-delay:.48s}
.ln { stroke-dasharray:500; stroke-dashoffset:500; animation: drawPath 1.4s ease forwards; }
.ln-2{animation-delay:.15s} .ln-3{animation-delay:.3s} .ln-4{animation-delay:.45s}
.fl { animation: float1 3s ease-in-out infinite; }
.fl-2 { animation: float2 3.5s ease-in-out infinite .8s; }
.fd { stroke-dasharray:10 8; animation: flowDash 1.2s linear infinite; }

/* ══════════════════════════════════════════════════
   PIPELINE (dark)
   ══════════════════════════════════════════════════ */
.dark { background:linear-gradient(180deg,#0d1a1f,#15282f); color:#f0f0f2; }
.pipe { display:grid; gap:.8rem; }
@media(min-width:760px){ .pipe{grid-template-columns:repeat(4,1fr)} }
.stg {
  padding:1.4rem 1.2rem; border-radius:16px;
  background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06);
  transition:background .3s ease,border-color .3s ease;
}
.stg:hover { background:rgba(255,255,255,.08); border-color:rgba(255,255,255,.12); }
.stg-n {
  display:inline-flex; align-items:center; justify-content:center;
  width:2.2rem; height:2.2rem; border-radius:9px;
  background:rgba(255,255,255,.08); font-size:.86rem; font-weight:800;
  color:rgba(255,255,255,.45); margin-bottom:.8rem;
}
.stg h3 { font-size:1.12rem; font-weight:700; color:#e5e5e7; margin-bottom:.35rem; }
.stg p  { font-size:.98rem; line-height:1.5; color:rgba(255,255,255,.5); }

/* ══════════════════════════════════════════════════
   SELECTED PAPERS — animated headers
   ══════════════════════════════════════════════════ */
.pgrid { display:grid; gap:1rem; }
@media(min-width:760px){ .pgrid{grid-template-columns:repeat(2,1fr)} }
.pcard {
  border-radius:20px; border:1px solid rgba(0,0,0,.06); background:#fff;
  overflow:hidden; display:flex; flex-direction:column;
  transition:transform .28s cubic-bezier(.22,1,.36,1),box-shadow .28s ease;
}
.pcard:hover { transform:translateY(-4px); box-shadow:0 16px 38px rgba(0,0,0,.09); }
.pcard-art { height:140px; overflow:hidden; display:flex; align-items:center; justify-content:center; }
.pcard-art svg { width:90%; height:90%; }
.pa-t { background:linear-gradient(150deg,#c8eaf3,#e6f6fa); }
.pa-g { background:linear-gradient(150deg,#faeabc,#fef8ec); }
.pa-c { background:linear-gradient(150deg,#f8d4c9,#fef0ea); }
.pa-gr{ background:linear-gradient(150deg,#c8e8ce,#e8f5eb); }

.pcard-body { padding:1.2rem 1.3rem 1.4rem; display:flex; flex-direction:column; gap:.45rem; flex:1; }
.pcard-lbl {
  display:inline-flex; width:fit-content; padding:.22rem .7rem; border-radius:8px;
  font-size:.78rem; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
}
.pcard-lbl-t { background:rgba(23,103,122,.1); color:#17677a; }
.pcard-lbl-g { background:rgba(216,155,43,.12); color:#8b5a10; }
.pcard-lbl-c { background:rgba(203,102,81,.1); color:#a14430; }
.pcard-lbl-gr{ background:rgba(79,139,98,.1); color:#3a7049; }
.pcard h3 { font-size:1.15rem; font-weight:700; line-height:1.22; color:#111; }
.pcard p  { font-size:1rem; line-height:1.55; color:#555; }
.cites { display:flex; flex-wrap:wrap; gap:.4rem; margin-top:auto; padding-top:.3rem; }
.ct {
  display:inline-flex; align-items:center; padding:.32rem .72rem;
  border-radius:9px; border:1px solid rgba(23,103,122,.15);
  background:rgba(23,103,122,.04); color:#17677a!important;
  font-size:.88rem; font-weight:700; text-decoration:none!important;
  transition:all .2s ease;
}
.ct:hover { background:rgba(23,103,122,.12); border-color:rgba(23,103,122,.3); transform:translateY(-2px); box-shadow:0 3px 10px rgba(23,103,122,.1); }

/* ══════════════════════════════════════════════════
   RECRUIT
   ══════════════════════════════════════════════════ */
.recruit { text-align:center; background:#fff; }
.recruit-t { font-size:clamp(1.7rem,3.5vw,2.6rem); font-weight:800; line-height:1.1; letter-spacing:-.02em; color:#111; }
.recruit-sub { margin-top:.6rem; font-size:clamp(1.02rem,1.4vw,1.15rem); line-height:1.55; color:#555; max-width:42rem; margin-left:auto; margin-right:auto; }
.recruit-meta {
  display:inline-flex; align-items:center; gap:.45rem; margin-top:1rem;
  padding:.4rem 1rem; border-radius:10px;
  background:rgba(216,155,43,.08); border:1px solid rgba(216,155,43,.15);
  font-size:.92rem; font-weight:700; color:#8b5a10;
}
.roles { display:grid; gap:.8rem; margin-top:2rem; text-align:left; }
@media(min-width:760px){ .roles{grid-template-columns:repeat(4,1fr)} }
.role {
  padding:1.3rem 1.2rem; border-radius:16px; background:#f5f5f7;
  border:1px solid rgba(0,0,0,.04);
  display:flex; flex-direction:column; gap:.4rem;
  transition:transform .22s ease,box-shadow .22s ease;
}
.role:hover { transform:translateY(-3px); box-shadow:0 8px 24px rgba(0,0,0,.06); }
.role h3 { font-size:1.1rem; font-weight:700; color:#111; }
.role p  { font-size:.98rem; line-height:1.5; color:#555; }
.recruit-cta { margin-top:2rem; }
.recruit-links { display:flex; justify-content:center; flex-wrap:wrap; gap:.4rem 1.2rem; margin-top:.8rem; }
.recruit-links a { font-size:.98rem; font-weight:600; color:#17677a!important; text-decoration:none!important; }
.recruit-links a:hover { color:#114e5d!important; }
.recruit-links a::after { content:" \2197"; font-size:.8em; }
</style>

<!-- ═══════════════════ HERO ═══════════════════ -->
<section class="s hero">
<div class="s-inner hero-inner">

  <div class="hero-profile">
    <img class="hero-avatar" src="{{ '/images/yuwen_photo.jpg' | relative_url }}" alt="Yuwen Huang">
    <div class="hero-id">
      <h2>Yuwen Huang</h2>
      <p>Postdoctoral Researcher, <a href="https://www.cse.cuhk.edu.hk/">CSE Dept., CUHK</a></p>
    </div>
  </div>

  <div class="hero-announce">
    <span class="dot"></span>
    <span>Joining <a href="https://dsa.hkust-gz.edu.cn/">Data Science and Analytics Thrust</a>, <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>, <a href="https://www.hkust-gz.edu.cn/">HKUST (Guangzhou)</a> as tenure-track Assistant Professor, Fall 2026</span>
  </div>

  <h1>Provable methods for <em>structured inference and optimization</em></h1>

  <p class="hero-sub">
    I develop scalable algorithms with rigorous guarantees using graphical models, combinatorics, tensor networks, and distributed quantum systems, with growing directions in machine learning and learning theory.
  </p>

  <div class="hero-chips">
    <span class="chip">Bethe methods &amp; graph covers</span>
    <span class="chip">Combinatorial inference</span>
    <span class="chip">Tensor networks</span>
    <span class="chip">Distributed quantum systems</span>
  </div>

  <div class="hero-cta">
    <a class="btn btn-p" href="#positions">Open positions</a>
    <a class="btn btn-s" href="#research">Selected research</a>
  </div>

</div>
</section>

<!-- ═══════════════════ RESEARCH AREAS ═══════════════════ -->
<section class="s bg-g">
<div class="s-inner">
  <div class="sh rv">
    <p class="sh-k">Research areas</p>
    <h2 class="sh-t">Three pillars, one pursuit</h2>
    <p class="sh-sub">Turning mathematical structure into practical, scalable computation.</p>
  </div>
  <div class="cards">

    <!-- INFERENCE -->
    <article class="card rv-s d1">
      <div class="card-art card-art-t">
        <svg viewBox="0 0 320 180" aria-label="Graphical model inference">
          <!-- edges -->
          <line x1="70" y1="60" x2="145" y2="42" class="ln" stroke="#5ba8bb" stroke-width="5" stroke-linecap="round"/>
          <line x1="70" y1="60" x2="130" y2="130" class="ln ln-2" stroke="#5ba8bb" stroke-width="5" stroke-linecap="round"/>
          <line x1="145" y1="42" x2="220" y2="75" class="ln ln-3" stroke="#5ba8bb" stroke-width="5" stroke-linecap="round"/>
          <line x1="130" y1="130" x2="220" y2="75" class="ln ln-3" stroke="#5ba8bb" stroke-width="5" stroke-linecap="round"/>
          <line x1="220" y1="75" x2="280" y2="60" class="ln ln-4" stroke="#5ba8bb" stroke-width="5" stroke-linecap="round"/>
          <!-- message flow -->
          <line x1="95" y1="53" x2="125" y2="46" class="fd" stroke="#17677a" stroke-width="3" stroke-linecap="round"/>
          <line x1="165" y1="52" x2="200" y2="68" class="fd" stroke="#17677a" stroke-width="3" stroke-linecap="round"/>
          <!-- nodes -->
          <circle cx="70" cy="60" r="22" class="nd" fill="#2a8a9e"/>
          <circle cx="145" cy="42" r="18" class="nd nd-2" fill="#2a8a9e"/>
          <circle cx="130" cy="130" r="18" class="nd nd-3" fill="#4da8b8"/>
          <circle cx="220" cy="75" r="20" class="nd nd-4" fill="#2a8a9e"/>
          <circle cx="280" cy="60" r="16" class="nd nd-5" fill="#4da8b8"/>
          <!-- labels -->
          <text x="70" y="66" text-anchor="middle" fill="#fff" font-size="14" font-weight="800">x&#x2081;</text>
          <text x="145" y="48" text-anchor="middle" fill="#fff" font-size="13" font-weight="800">x&#x2082;</text>
          <text x="220" y="81" text-anchor="middle" fill="#fff" font-size="14" font-weight="800">x&#x2083;</text>
          <!-- bar chart -->
          <rect x="235" y="110" width="55" height="40" rx="8" fill="#e0f3f8" stroke="#78b8c7" stroke-width="2"/>
          <rect x="243" y="130" width="8" height="16" rx="3" fill="#2a8a9e" class="fl"/>
          <rect x="255" y="122" width="8" height="24" rx="3" fill="#5ba8bb" class="fl-2"/>
          <rect x="267" y="126" width="8" height="20" rx="3" fill="#2a8a9e" class="fl"/>
          <rect x="279" y="132" width="8" height="14" rx="3" fill="#5ba8bb" class="fl-2"/>
        </svg>
      </div>
      <div class="card-body">
        <p class="card-lbl card-lbl-t">Inference</p>
        <h3>Structured graphical-model reasoning</h3>
        <p>Message passing, Bethe methods, and combinatorial structure for reliable inference and counting.</p>
        <div class="card-tags"><span>Uncertainty</span><span>Counting</span><span>Graph covers</span></div>
      </div>
    </article>

    <!-- OPTIMIZATION -->
    <article class="card rv-s d2">
      <div class="card-art card-art-g">
        <svg viewBox="0 0 320 180" aria-label="Optimization landscape">
          <defs>
            <linearGradient id="og" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#e8c75a"/><stop offset="100%" stop-color="#d89b2b"/></linearGradient>
            <marker id="oa" viewBox="0 0 10 10" markerWidth="8" markerHeight="8" refX="9" refY="5" orient="auto">
              <path d="M1 1L9 5L1 9" fill="none" stroke="#d89b2b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </marker>
          </defs>
          <!-- curve -->
          <path d="M30 130 C65 100,90 40,135 40 C180 40,200 120,245 120 C275 120,295 90,310 55" class="ln" fill="none" stroke="url(#og)" stroke-width="6" stroke-linecap="round" marker-end="url(#oa)"/>
          <!-- critical pts -->
          <circle cx="135" cy="40" r="14" class="nd nd-2 fl" fill="#8a5b10"/>
          <circle cx="245" cy="120" r="14" class="nd nd-3 fl-2" fill="#8a5b10"/>
          <!-- descent arrows -->
          <path d="M95 75 L120 48" class="fd" stroke="#b38320" stroke-width="3" stroke-linecap="round" fill="none"/>
          <path d="M275 105 L298 72" class="fd" stroke="#b38320" stroke-width="3" stroke-linecap="round" fill="none"/>
          <!-- labels -->
          <rect x="55" y="18" width="60" height="26" rx="9" class="nd nd-3" fill="#fff6de" stroke="#ead28d" stroke-width="2"/>
          <text x="85" y="36" text-anchor="middle" fill="#8a5b10" font-size="12" font-weight="800">Bounds</text>
          <rect x="230" y="18" width="72" height="26" rx="9" class="nd nd-4" fill="#fff6de" stroke="#ead28d" stroke-width="2"/>
          <text x="266" y="36" text-anchor="middle" fill="#8a5b10" font-size="12" font-weight="800">Algorithms</text>
          <!-- baseline -->
          <line x1="45" y1="158" x2="290" y2="158" class="ln ln-4" stroke="#ead28d" stroke-width="4" stroke-linecap="round"/>
        </svg>
      </div>
      <div class="card-body">
        <p class="card-lbl card-lbl-g">Optimization</p>
        <h3>Provable optimization and decision-making</h3>
        <p>Structure-aware objectives, permanent bounds, and algorithmic guarantees for hard problems.</p>
        <div class="card-tags"><span>Convex / nonconvex</span><span>Permanent bounds</span><span>Decisions</span></div>
      </div>
    </article>

    <!-- QUANTUM & TENSORS -->
    <article class="card rv-s d3">
      <div class="card-art card-art-c">
        <svg viewBox="0 0 320 180" aria-label="Tensor network and quantum">
          <!-- tensor chain bonds -->
          <line x1="72" y1="70" x2="108" y2="70" class="ln" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
          <line x1="148" y1="70" x2="184" y2="70" class="ln ln-2" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
          <line x1="224" y1="70" x2="260" y2="70" class="ln ln-3" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
          <!-- tensor nodes -->
          <rect x="32" y="52" width="40" height="36" rx="10" class="nd" fill="#e08a78"/>
          <rect x="108" y="52" width="40" height="36" rx="10" class="nd nd-2" fill="#e08a78"/>
          <rect x="184" y="52" width="40" height="36" rx="10" class="nd nd-3" fill="#e08a78"/>
          <rect x="260" y="52" width="40" height="36" rx="10" class="nd nd-4" fill="#e08a78"/>
          <!-- physical indices -->
          <line x1="52" y1="52" x2="52" y2="32" class="ln ln-2" stroke="#cb6651" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="128" y1="52" x2="128" y2="32" class="ln ln-3" stroke="#cb6651" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="204" y1="52" x2="204" y2="32" class="ln ln-3" stroke="#cb6651" stroke-width="3.5" stroke-linecap="round"/>
          <line x1="280" y1="52" x2="280" y2="32" class="ln ln-4" stroke="#cb6651" stroke-width="3.5" stroke-linecap="round"/>
          <!-- quantum orbit -->
          <g style="transform-origin:170px 140px" class="nd nd-5">
            <ellipse cx="170" cy="140" rx="65" ry="18" fill="none" stroke="#86b894" stroke-width="2.5" stroke-dasharray="6 5" style="transform-origin:170px 140px;animation:orbit 10s linear infinite"/>
            <circle cx="170" cy="140" r="12" fill="#4f8b62"/>
            <circle cx="232" cy="136" r="8" fill="#86b894" class="fl"/>
            <circle cx="108" cy="136" r="8" fill="#86b894" class="fl-2"/>
          </g>
          <!-- label -->
          <text x="170" y="145" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Q</text>
        </svg>
      </div>
      <div class="card-body">
        <p class="card-lbl card-lbl-c">Quantum &amp; Tensors</p>
        <h3>High-dimensional quantum computation</h3>
        <p>Tensor-network representations and distributed quantum systems for scalable computation.</p>
        <div class="card-tags"><span>Tensor networks</span><span>Quantum systems</span><span>Scalability</span></div>
      </div>
    </article>

  </div>
</div>
</section>

<!-- ═══════════════════ PIPELINE ═══════════════════ -->
<section class="s dark">
<div class="s-inner">
  <div class="sh rv">
    <p class="sh-k">From theory to impact</p>
    <h2 class="sh-t">Structure becomes computation</h2>
  </div>
  <div class="pipe">
    <div class="stg rv d1"><div class="stg-n">01</div><h3>Information theory &amp; statistical physics</h3><p>Structure, correlation, and entropy motivate the underlying questions.</p></div>
    <div class="stg rv d2"><div class="stg-n">02</div><h3>Inference, counting, optimization</h3><p>Bethe methods, graph covers, and structure-aware optimization.</p></div>
    <div class="stg rv d3"><div class="stg-n">03</div><h3>Distributed quantum systems</h3><p>Quantum networks extending the computational regime.</p></div>
    <div class="stg rv d4"><div class="stg-n">04</div><h3>ML &amp; efficient computation</h3><p>Learning theory, analytics, and large-scale decision making.</p></div>
  </div>
</div>
</section>

<!-- ═══════════════════ SELECTED RESEARCH ═══════════════════ -->
<section class="s bg-g" id="research">
<div class="s-inner">
  <div class="sh rv">
    <p class="sh-k">Selected research</p>
    <h2 class="sh-t">Representative directions and papers</h2>
  </div>
  <div class="pgrid">

    <!-- 1 Graphical models -->
    <article class="pcard rv-s d1">
      <div class="pcard-art pa-t">
        <svg viewBox="0 0 340 130" aria-label="Graphical models">
          <line x1="60" y1="50" x2="130" y2="35" class="ln" stroke="#5ba8bb" stroke-width="4" stroke-linecap="round"/>
          <line x1="60" y1="50" x2="115" y2="100" class="ln ln-2" stroke="#5ba8bb" stroke-width="4" stroke-linecap="round"/>
          <line x1="130" y1="35" x2="210" y2="60" class="ln ln-3" stroke="#5ba8bb" stroke-width="4" stroke-linecap="round"/>
          <line x1="115" y1="100" x2="210" y2="60" class="ln ln-3" stroke="#5ba8bb" stroke-width="4" stroke-linecap="round"/>
          <line x1="210" y1="60" x2="275" y2="48" class="ln ln-4" stroke="#5ba8bb" stroke-width="4" stroke-linecap="round"/>
          <line x1="85" y1="44" x2="112" y2="38" class="fd" stroke="#17677a" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="150" y1="42" x2="190" y2="55" class="fd" stroke="#17677a" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="60" cy="50" r="16" class="nd" fill="#2a8a9e"/>
          <circle cx="130" cy="35" r="14" class="nd nd-2" fill="#2a8a9e"/>
          <circle cx="115" cy="100" r="14" class="nd nd-3" fill="#4da8b8"/>
          <circle cx="210" cy="60" r="16" class="nd nd-4" fill="#2a8a9e"/>
          <circle cx="275" cy="48" r="13" class="nd nd-5" fill="#4da8b8"/>
        </svg>
      </div>
      <div class="pcard-body">
        <span class="pcard-lbl pcard-lbl-t">Inference</span>
        <h3>Graphical models and Bethe methods</h3>
        <p>Bethe approximations, graph covers, and message passing for principled inference and counting.</p>
        <div class="cites">
          <a class="ct" href="{{ '/publication/characterizing-bethe-partition-factor-graphs' | relative_url }}">[ISIT2020]</a>
          <a class="ct" href="{{ '/publication/bethe-free-energy-global-minimum' | relative_url }}">[ITW2022]</a>
          <a class="ct" href="{{ '/publication/bethe-partition-spa-stable-polynomials' | relative_url }}">[ISIT2024]</a>
          <a class="ct" href="{{ '/publication/bethe-partition-function-graph-covers-extended' | relative_url }}">[TIT-sub]</a>
        </div>
      </div>
    </article>

    <!-- 2 Optimization -->
    <article class="pcard rv-s d2">
      <div class="pcard-art pa-g">
        <svg viewBox="0 0 340 130" aria-label="Optimization">
          <defs><marker id="pa" viewBox="0 0 10 10" markerWidth="7" markerHeight="7" refX="9" refY="5" orient="auto"><path d="M1 1L9 5L1 9" fill="none" stroke="#d89b2b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
          <path d="M35 95 C65 72,85 28,125 28 C170 28,185 88,225 88 C255 88,275 65,300 38" class="ln" fill="none" stroke="#d9b14f" stroke-width="5" stroke-linecap="round" marker-end="url(#pa)"/>
          <circle cx="125" cy="28" r="12" class="nd nd-2 fl" fill="#8a5b10"/>
          <circle cx="225" cy="88" r="12" class="nd nd-3 fl-2" fill="#8a5b10"/>
          <path d="M85 55 L110 35" class="fd" stroke="#b38320" stroke-width="2.5" stroke-linecap="round" fill="none"/>
          <line x1="50" y1="115" x2="280" y2="115" class="ln ln-4" stroke="#ead28d" stroke-width="3" stroke-linecap="round"/>
        </svg>
      </div>
      <div class="pcard-body">
        <span class="pcard-lbl pcard-lbl-g">Optimization</span>
        <h3>Optimization and combinatorial structure</h3>
        <p>Structure-exploiting optimization and permanent bounds with rigorous guarantees.</p>
        <div class="cites">
          <a class="ct" href="{{ '/publication/bounding-permanent-degree-m-bethe' | relative_url }}">[ISIT2023]</a>
          <a class="ct" href="{{ '/publication/degree-m-bethe-sinkhorn-permanent' | relative_url }}">[TIT2024]</a>
          <a class="ct" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
        </div>
      </div>
    </article>

    <!-- 3 Tensor methods -->
    <article class="pcard rv-s d3">
      <div class="pcard-art pa-c">
        <svg viewBox="0 0 340 130" aria-label="Tensor network">
          <line x1="78" y1="55" x2="112" y2="55" class="ln" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
          <line x1="152" y1="55" x2="186" y2="55" class="ln ln-2" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
          <line x1="226" y1="55" x2="260" y2="55" class="ln ln-3" stroke="#cb6651" stroke-width="5" stroke-linecap="round"/>
          <rect x="38" y="38" width="40" height="34" rx="10" class="nd" fill="#e08a78"/>
          <rect x="112" y="38" width="40" height="34" rx="10" class="nd nd-2" fill="#e08a78"/>
          <rect x="186" y="38" width="40" height="34" rx="10" class="nd nd-3" fill="#e08a78"/>
          <rect x="260" y="38" width="40" height="34" rx="10" class="nd nd-4" fill="#e08a78"/>
          <line x1="58" y1="38" x2="58" y2="20" class="ln ln-2" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
          <line x1="132" y1="38" x2="132" y2="20" class="ln ln-3" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
          <line x1="206" y1="38" x2="206" y2="20" class="ln ln-3" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
          <line x1="280" y1="38" x2="280" y2="20" class="ln ln-4" stroke="#cb6651" stroke-width="3" stroke-linecap="round"/>
          <!-- result bar -->
          <rect x="100" y="92" width="160" height="26" rx="10" class="nd nd-5" fill="#fde8e1" stroke="#e08a78" stroke-width="2"/>
          <text x="180" y="110" text-anchor="middle" fill="#a14430" font-size="11" font-weight="700">Compact representation</text>
        </svg>
      </div>
      <div class="pcard-body">
        <span class="pcard-lbl pcard-lbl-c">Tensor methods</span>
        <h3>Tensor networks and quantum-enabled inference</h3>
        <p>Compact high-dimensional computation via tensor-network representations.</p>
        <div class="cites">
          <a class="ct" href="{{ '/publication/sets-of-marginals-chsh' | relative_url }}">[ISIT2021]</a>
          <a class="ct" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
        </div>
      </div>
    </article>

    <!-- 4 Distributed quantum -->
    <article class="pcard rv-s d4">
      <div class="pcard-art pa-gr">
        <svg viewBox="0 0 340 130" aria-label="Distributed quantum network">
          <line x1="72" y1="58" x2="140" y2="38" class="ln" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
          <line x1="72" y1="58" x2="140" y2="92" class="ln ln-2" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
          <line x1="140" y1="38" x2="215" y2="60" class="ln ln-3" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
          <line x1="140" y1="92" x2="215" y2="60" class="ln ln-3" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
          <line x1="215" y1="60" x2="278" y2="42" class="ln ln-4" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
          <line x1="215" y1="60" x2="278" y2="90" class="ln ln-4" stroke="#86b894" stroke-width="4" stroke-linecap="round"/>
          <line x1="96" y1="50" x2="120" y2="42" class="fd" stroke="#4f8b62" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="160" y1="44" x2="195" y2="55" class="fd" stroke="#4f8b62" stroke-width="2.5" stroke-linecap="round"/>
          <rect x="52" y="42" width="32" height="32" rx="9" class="nd" fill="#4f8b62"/>
          <rect x="124" y="22" width="32" height="32" rx="9" class="nd nd-2" fill="#4f8b62"/>
          <rect x="124" y="76" width="32" height="32" rx="9" class="nd nd-3" fill="#4f8b62"/>
          <rect x="199" y="44" width="32" height="32" rx="9" class="nd nd-4" fill="#4f8b62"/>
          <rect x="262" y="26" width="32" height="32" rx="9" class="nd nd-5" fill="#6aa67a"/>
          <rect x="262" y="74" width="32" height="32" rx="9" class="nd nd-5" fill="#6aa67a"/>
          <text x="68" y="63" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Q&#x2081;</text>
          <text x="140" y="43" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Q&#x2082;</text>
          <text x="215" y="65" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Q&#x2083;</text>
        </svg>
      </div>
      <div class="pcard-body">
        <span class="pcard-lbl pcard-lbl-gr">Quantum systems</span>
        <h3>Distributed quantum systems</h3>
        <p>Distributed quantum architectures for optimization, inference, and analytics.</p>
        <div class="cites">
          <a class="ct" href="{{ '/publication/quantum-algorithms-finite-horizon-mdp' | relative_url }}">[ICML2025]</a>
          <a class="ct" href="{{ '/publication/scalable-distributed-quantum-optimization-factor-graph' | relative_url }}">[QUANTUM-sub]</a>
        </div>
      </div>
    </article>

  </div>
</div>
</section>

<!-- ═══════════════════ OPEN POSITIONS ═══════════════════ -->
<section class="s recruit" id="positions">
<div class="s-inner">
  <div class="rv">
    <h2 class="recruit-t">Join the group</h2>
    <p class="recruit-sub">Recruiting RAs, MPhil/PhD students, and one Postdoc for Fall 2026 at HKUST (Guangzhou), Data Science and Analytics Thrust.</p>
    <p class="recruit-meta">Tenure-track Assistant Professor &middot; Information Hub &middot; DSA</p>
  </div>
  <div class="roles">
    <div class="role rv d1"><h3>RA</h3><p>Core research training and preparation for graduate study or industry roles.</p></div>
    <div class="role rv d2"><h3>MPhil</h3><p>Structured transition into independent research with publication-minded training.</p></div>
    <div class="role rv d3"><h3>PhD</h3><p>Ownership of deeper problems, broad collaboration, and long-term research support.</p></div>
    <div class="role rv d4"><h3>Postdoc</h3><p>Shape an agenda, co-mentor students, and prepare for academic searches.</p></div>
  </div>
  <div class="recruit-cta rv"><a class="btn btn-p" href="mailto:{{ site.author.email }}">Apply by email</a></div>
  <div class="recruit-links rv">
    <a href="https://dsa.hkust-gz.edu.cn/">DSA Thrust</a>
    <a href="https://www.hkust-gz.edu.cn/academics/hubs-and-thrust-areas/information-hub/">Information Hub</a>
    <a href="https://www.hkust-gz.edu.cn/">HKUST Guangzhou</a>
  </div>
</div>
</section>

<!-- ═══════════════════ SCROLL REVEAL ═══════════════════ -->
<script>
document.addEventListener("DOMContentLoaded",function(){
  var els=document.querySelectorAll(".rv,.rv-s");
  if(!("IntersectionObserver" in window)){els.forEach(function(e){e.classList.add("vis")});return}
  var io=new IntersectionObserver(function(ents){
    ents.forEach(function(en){if(en.isIntersecting){en.target.classList.add("vis");io.unobserve(en.target)}})
  },{threshold:.12,rootMargin:"0px 0px -30px 0px"});
  els.forEach(function(e){io.observe(e)});
});
</script>
