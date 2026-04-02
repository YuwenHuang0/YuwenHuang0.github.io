---
layout: splash
title: "CV"
permalink: /cv/
author_profile: false
redirect_from:
  - /resume
---

{% include base_path %}

<style>
  /* ── Ultra-compact CV ── */
  .cv-section {
    margin-bottom: .9rem;
  }
  .cv-section h2 {
    font-size: .88rem !important;
    font-weight: 700 !important;
    letter-spacing: -.01em;
    color: var(--text-primary, #1d1d1f) !important;
    border-bottom: 1px solid rgba(0,0,0,.08) !important;
    padding-bottom: .25em !important;
    margin-top: 0 !important;
    margin-bottom: .25rem !important;
  }

  .cv-entry {
    padding: .15rem 0;
    border-bottom: 1px solid rgba(0,0,0,.03);
  }
  .cv-entry:last-child { border-bottom: none; }
  .cv-entry-main {
    font-size: .82rem;
    font-weight: 600;
    color: var(--text-primary, #1d1d1f);
    line-height: 1.25;
    margin: 0;
  }
  .cv-entry-date {
    font-size: .75rem;
    font-weight: 600;
    color: #6e6e73;
  }
  .cv-entry-detail {
    font-size: .78rem;
    color: #6e6e73;
    line-height: 1.35;
    margin: .02rem 0 0;
  }
  .cv-entry-detail a {
    color: #06c !important;
    text-decoration: none !important;
    font-weight: 500;
  }
  .cv-entry-detail a:hover {
    text-decoration: underline !important;
  }

  .cv-tags {
    display: flex;
    flex-wrap: wrap;
    gap: .2rem;
    margin-top: .1rem;
  }
  .cv-tag {
    display: inline-flex;
    padding: .08rem .4rem;
    border-radius: 980px;
    background: #f0f0f2;
    font-size: .72rem;
    font-weight: 500;
    color: #424245;
  }

  .cv-list {
    list-style: none;
    padding: 0;
    margin: .1rem 0 0;
  }
  .cv-list li {
    padding: .15rem 0;
    border-bottom: 1px solid rgba(0,0,0,.03);
    font-size: .78rem;
    line-height: 1.35;
    color: #6e6e73;
  }
  .cv-list li:last-child { border-bottom: none; }
  .cv-list li strong {
    color: var(--text-primary, #1d1d1f);
    font-weight: 600;
  }

  /* Inline links for slides etc */
  .cv-entry-detail .pub-link {
    display: inline-flex;
    padding: .05rem .35rem;
    border-radius: 980px;
    font-size: .62rem;
    font-weight: 600;
    border: 1px solid rgba(138, 91, 16, 0.15);
    background: #fff5dd;
    color: #8a5b10 !important;
    text-decoration: none !important;
    margin-left: .15rem;
  }
</style>

<div class="inner-page" style="padding-top:clamp(1.2rem,2vw,2rem);">
<h1 class="inner-page-title" style="font-size:clamp(1.3rem,2.5vw,1.8rem);margin-bottom:.15rem;">CV</h1>

<div class="cv-section">
<h2>Education</h2>
<div class="cv-entry">
<p class="cv-entry-main"><span class="cv-entry-date">2018–2024</span> · Ph.D. in Information Engineering</p>
<p class="cv-entry-detail">The Chinese University of Hong Kong · Supervisor: <a href="https://sites.google.com/site/pascalvontobel/">Prof. Pascal O. Vontobel</a></p>
</div>
<div class="cv-entry">
<p class="cv-entry-main"><span class="cv-entry-date">2014–2018</span> · B.Eng. in Electronic and Information Engineering</p>
<p class="cv-entry-detail">South China University of Technology · Supervisor: <a href="https://scholar.google.com/citations?hl=en&user=8xjRAYUAAAAJ&view_op=list_works&sortby=pubdate">Prof. Yuan Liu</a></p>
</div>
</div>

<div class="cv-section">
<h2>Work Experience</h2>
<div class="cv-entry">
<p class="cv-entry-main"><span class="cv-entry-date">11/2024–present</span> · Postdoctoral Researcher, CSE, CUHK</p>
<p class="cv-entry-detail">Supervisor: <a href="https://www.cse.cuhk.edu.hk/~cslui/">Prof. John C.S. Lui</a> · Distributed quantum computing models</p>
</div>
</div>

<div class="cv-section">
<h2>Research Interests</h2>
<div class="cv-tags">
<span class="cv-tag">Probabilistic graphical models</span>
<span class="cv-tag">Optimization</span>
<span class="cv-tag">Information theory</span>
<span class="cv-tag">Foundations of data science</span>
<span class="cv-tag">Quantum information processing</span>
</div>
</div>

<div class="cv-section">
<h2>Journal Papers (submitted)</h2>
<div class="cv-entry">
<p class="cv-entry-main">A Scalable Distributed Quantum Optimization Framework via Factor Graph Paradigm</p>
<p class="cv-entry-detail">Y. Huang, X. Lin, B. Luo, J. C. S. Lui. Submitted to <em>Quantum</em>, 2026. <a href="https://arxiv.org/abs/2603.07673">arXiv</a></p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Characterizing the Bethe partition function of double-edge factor graphs via graph covers (extended)</p>
<p class="cv-entry-detail">Y. Huang, P. O. Vontobel. Submitted to <em>IEEE Trans. Inf. Theory</em>, 2024. <a href="https://arxiv.org/abs/2412.05942">arXiv</a></p>
</div>
</div>

<div class="cv-section">
<h2>Journal Papers</h2>
<div class="cv-entry">
<p class="cv-entry-main">Degree-M Bethe and Sinkhorn permanent based bounds on the permanent of a non-negative matrix</p>
<p class="cv-entry-detail">Y. Huang, N. Kashyap, P. O. Vontobel. <em>IEEE Trans. Inf. Theory</em>, 70(4):5289–5308, 2024.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">NOMA-aided mobile edge computing via user cooperation</p>
<p class="cv-entry-detail">Y. Huang, Y. Liu, F. Chen. <em>IEEE Trans. Commun.</em>, 68(4):2221–2235, 2020.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Energy efficiency of distributed antenna systems with wireless power transfer</p>
<p class="cv-entry-detail">Y. Huang, Y. Liu, G. Y. Li. <em>IEEE J. Sel. Areas Commun.</em>, 37(1):89–99, 2019.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Energy-efficient SWIPT in IoT distributed antenna systems</p>
<p class="cv-entry-detail">Y. Huang, M. Liu, Y. Liu. <em>IEEE Internet Things J.</em>, 5(4):2646–2656, 2018.</p>
</div>
</div>

<div class="cv-section">
<h2>Conference Papers</h2>
<div class="cv-entry">
<p class="cv-entry-main">Quantum algorithms for finite-horizon Markov decision processes</p>
<p class="cv-entry-detail">B. Luo*, Y. Huang, J. Allcock, X. Lin, S. Zhang, J. C.S. Lui. <em>ICML</em>, 2025.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">The Bethe partition function and the SPA for factor graphs based on homogeneous real stable polynomials</p>
<p class="cv-entry-detail">Y. Huang, P. O. Vontobel. <em>IEEE ISIT</em>, Athens, 2024, pp. 3029–3034.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Bounding the permanent of a non-negative matrix via its degree-M Bethe and Sinkhorn permanents</p>
<p class="cv-entry-detail">Y. Huang, P. O. Vontobel. <em>IEEE ISIT</em>, Taipei, 2023, pp. 2774–2779.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">On the relationship between the global minimum of the Bethe free energy function and SPA fixed points</p>
<p class="cv-entry-detail">Y. Huang, P. O. Vontobel. <em>IEEE ITW</em>, Mumbai, 2022, pp. 666–671.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Sets of marginals and Pearson-correlation-based CHSH inequalities for a two-qubit system</p>
<p class="cv-entry-detail">Y. Huang, P. O. Vontobel. <em>IEEE ISIT</em>, Melbourne, 2021, pp. 1338–1343.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Characterizing the Bethe partition function of double-edge factor graphs via graph covers</p>
<p class="cv-entry-detail">Y. Huang, P. O. Vontobel. <em>IEEE ISIT</em>, Los Angeles, 2020, pp. 1331–1336. <a class="pub-link" href="/files/slides/isit2020.pdf">Slides</a></p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">User cooperation for NOMA-based mobile edge computing</p>
<p class="cv-entry-detail">Y. Huang, Y. Liu. <em>IEEE ICCS</em>, Chengdu, 2018, pp. 395–400.</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Energy-Efficient SWIPT in Distributed Antenna Systems</p>
<p class="cv-entry-detail">Y. Huang, Y. Liu. <em>IEEE Globecom Workshops</em>, Singapore, 2017, pp. 1–6.</p>
</div>
</div>

<div class="cv-section">
<h2>Talks</h2>
<div class="cv-entry">
<p class="cv-entry-main">Bethe Approximations for Matrix Permanents and Contingency Table Counting</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Jan. 2026</span> · DSA Thrust, HKUST (Guangzhou) <a class="pub-link" href="/files/slides/talk_hkustgz.pdf">Slides</a></p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">The Bethe approximation for binary contingency table counting and nonnegative matrix permanents</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Feb. 2025</span> · CS Dept., TU Dortmund University (virtual)</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">The Bethe partition function and the SPA for factor graphs based on homogeneous real stable polynomials</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Sept. 2024</span> · School of Cyber Science and Engineering, Southeast University (virtual)</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Bounding the permanent of a non-negative matrix via its degree-M Bethe and Sinkhorn permanents</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Mar. 2023</span> · ITCSC, CUHK</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">On the relationship between the minimum of the Bethe free energy function and SPA fixed points</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Nov. 2022</span> · ITCSC, CUHK</p>
</div>
<div class="cv-entry">
<p class="cv-entry-main">Sets of marginals and Pearson-correlation-based CHSH inequalities for a two-qubit system</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Apr. 2022</span> · Prof. Tomamichel's group, NUS (virtual)</p>
</div>
</div>

<div class="cv-section">
<h2>Teaching</h2>
<ul class="cv-list">
<li><strong>2022</strong> · Electronic Circuit Design Lab (TA), CUHK (also 2019, 2020)</li>
<li><strong>2022</strong> · Social Media and Human Information Interaction (TA), CUHK</li>
<li><strong>2021</strong> · Basic Analog and Digital Circuits (TA), CUHK</li>
<li><strong>2021</strong> · Linear Algebra for Engineers (TA), CUHK</li>
<li><strong>2018–2020</strong> · Principles of Communication Systems (TA), CUHK</li>
</ul>
</div>

<div class="cv-section">
<h2>Service</h2>
<ul class="cv-list">
<li>Journal reviewer: <em>IEEE Commun. Mag.</em>, <em>IEEE Trans. Commun.</em>, <em>IEEE J. Sel. Topics Signal Process.</em>, <em>IEEE Commun. Lett.</em></li>
<li>Conference reviewer: IEEE ISIT, IEEE ICC, IEEE WCNC</li>
</ul>
</div>

<div class="cv-section">
<h2>Awards</h2>
<ul class="cv-list">
<li><strong>2024</strong> · Student Travel Grant, IEEE ISIT</li>
<li><strong>2018</strong> · Bachelor's Thesis Award, SCUT</li>
</ul>
</div>

<div class="cv-section">
<h2>Languages</h2>
<div class="cv-tags">
<span class="cv-tag">Cantonese (native)</span>
<span class="cv-tag">Mandarin (native)</span>
<span class="cv-tag">English (fluent)</span>
</div>
</div>

</div>
