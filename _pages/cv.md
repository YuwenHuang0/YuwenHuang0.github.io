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
  /* ── CV entries ── */
  .cv-section {
    margin-bottom: 3rem;
  }
  .cv-section h2 {
    font-size: clamp(1.2rem, 2vw, 1.5rem) !important;
    font-weight: 700 !important;
    letter-spacing: -.015em;
    color: var(--text-primary, #1d1d1f) !important;
    border-bottom: 1px solid rgba(0,0,0,.06) !important;
    padding-bottom: .6em !important;
    margin-top: 0 !important;
    margin-bottom: 1rem !important;
  }

  .cv-entry {
    padding: 1rem 1.5rem;
    margin-bottom: .4rem;
    border-radius: 16px;
    background: var(--bg-secondary, #f5f5f7);
    border: 1px solid rgba(0,0,0,.03);
    transition: box-shadow .3s ease, transform .3s ease;
  }
  .cv-entry:hover {
    box-shadow: 0 8px 32px rgba(0,0,0,.06);
    transform: translateY(-2px);
  }
  .cv-entry-main {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-primary, #1d1d1f);
    line-height: 1.4;
    margin: 0;
  }
  .cv-entry-date {
    font-size: .88rem;
    font-weight: 600;
    color: var(--text-secondary, #6e6e73);
  }
  .cv-entry-detail {
    font-size: .92rem;
    color: #424245;
    line-height: 1.55;
    margin: .2rem 0 0;
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
    gap: .4rem;
    margin-top: .5rem;
  }
  .cv-tag {
    display: inline-flex;
    padding: .25rem .7rem;
    border-radius: 980px;
    background: var(--bg-secondary, #f5f5f7);
    border: 1px solid rgba(0,0,0,.04);
    font-size: .84rem;
    font-weight: 500;
    color: #424245;
  }

  .cv-list {
    list-style: none;
    padding: 0;
    margin: .3rem 0 0;
  }
  .cv-list li {
    padding: .65rem 1.5rem;
    margin-bottom: .3rem;
    border-radius: 16px;
    background: var(--bg-secondary, #f5f5f7);
    border: 1px solid rgba(0,0,0,.03);
    font-size: .94rem;
    line-height: 1.55;
    color: #424245;
    transition: box-shadow .3s ease;
  }
  .cv-list li:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,.04);
  }
  .cv-list li strong {
    color: var(--text-primary, #1d1d1f);
  }
</style>

<div class="inner-page">
<h1 class="inner-page-title">CV</h1>

<div class="cv-section">
<h2>Education</h2>

<div class="cv-entry">
<p class="cv-entry-main"><span class="cv-entry-date">2018–2024</span> · Ph.D. in Information Engineering</p>
<p class="cv-entry-detail">The Chinese University of Hong Kong (CUHK), Hong Kong</p>
<p class="cv-entry-detail">Thesis: <em>Characterizing the Bethe partition function of double-edge factor graphs via graph covers</em></p>
<p class="cv-entry-detail">Supervisor: <a href="https://sites.google.com/site/pascalvontobel/">Prof. Pascal O. Vontobel</a></p>
</div>

<div class="cv-entry">
<p class="cv-entry-main"><span class="cv-entry-date">2014–2018</span> · B.Eng. in Electronic and Information Engineering</p>
<p class="cv-entry-detail">South China University of Technology (SCUT), Guangzhou, China</p>
<p class="cv-entry-detail">Supervisor: <a href="https://scholar.google.com/citations?hl=en&user=8xjRAYUAAAAJ&view_op=list_works&sortby=pubdate">Prof. Yuan Liu</a></p>
</div>
</div>

<div class="cv-section">
<h2>Work Experience</h2>

<div class="cv-entry">
<p class="cv-entry-main"><span class="cv-entry-date">11/2024–present</span> · Postdoctoral Researcher</p>
<p class="cv-entry-detail">Department of Computer Science and Engineering, CUHK, Hong Kong</p>
<p class="cv-entry-detail">Supervisor: <a href="https://www.cse.cuhk.edu.hk/~cslui/">Prof. John C.S. Lui</a></p>
<p class="cv-entry-detail">Develop novel models for distributed quantum computing in collaboration with faculty, targeting high-impact journal publications.</p>
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
<p class="cv-entry-detail">Y. Huang, X. Lin, B. Luo and J. C. S. Lui. Submitted to <em>Quantum</em>, 2026. <a href="https://arxiv.org/abs/2603.07673">arXiv:2603.07673</a></p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Characterizing the Bethe partition function of double-edge factor graphs via graph covers (extended version)</p>
<p class="cv-entry-detail">Y. Huang and P. O. Vontobel. Submitted to <em>IEEE Transactions on Information Theory</em>, 2024. <a href="https://arxiv.org/abs/2412.05942">arXiv:2412.05942</a></p>
</div>
</div>

<div class="cv-section">
<h2>Journal Papers</h2>

<div class="cv-entry">
<p class="cv-entry-main">Degree-M Bethe and Sinkhorn permanent based bounds on the permanent of a non-negative matrix</p>
<p class="cv-entry-detail">Y. Huang, N. Kashyap and P. O. Vontobel. <em>IEEE Transactions on Information Theory</em>, vol. 70, no. 4, pp. 5289–5308, Jul. 2024.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">NOMA-aided mobile edge computing via user cooperation</p>
<p class="cv-entry-detail">Y. Huang, Y. Liu and F. Chen. <em>IEEE Transactions on Communications</em>, vol. 68, no. 4, pp. 2221–2235, Apr. 2020.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Energy efficiency of distributed antenna systems with wireless power transfer</p>
<p class="cv-entry-detail">Y. Huang, Y. Liu and G. Y. Li. <em>IEEE Journal on Selected Areas in Communications</em>, vol. 37, no. 1, pp. 89–99, Jan. 2019.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Energy-efficient SWIPT in IoT distributed antenna systems</p>
<p class="cv-entry-detail">Y. Huang, M. Liu and Y. Liu. <em>IEEE Internet of Things Journal</em>, vol. 5, no. 4, pp. 2646–2656, Aug. 2018.</p>
</div>
</div>

<div class="cv-section">
<h2>Conference Papers</h2>

<div class="cv-entry">
<p class="cv-entry-main">Quantum algorithms for finite-horizon Markov decision processes</p>
<p class="cv-entry-detail">B. Luo*, Y. Huang, J. Allcock, X. Lin, S. Zhang and J. C.S. Lui. <em>ICML</em>, 2025. (*corresponding author)</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">The Bethe partition function and the SPA for factor graphs based on homogeneous real stable polynomials</p>
<p class="cv-entry-detail">Y. Huang and P. O. Vontobel. <em>IEEE ISIT</em>, Athens, Greece, Jul. 2024, pp. 3029–3034.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Bounding the permanent of a non-negative matrix via its degree-M Bethe and Sinkhorn permanents</p>
<p class="cv-entry-detail">Y. Huang and P. O. Vontobel. <em>IEEE ISIT</em>, Taipei, Taiwan, Jun. 2023, pp. 2774–2779.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">On the relationship between the global minimum of the Bethe free energy function of a factor graph and sum-product algorithm fixed points</p>
<p class="cv-entry-detail">Y. Huang and P. O. Vontobel. <em>IEEE ITW</em>, Mumbai, India, Nov. 2022, pp. 666–671.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Sets of marginals and Pearson-correlation-based CHSH inequalities for a two-qubit system</p>
<p class="cv-entry-detail">Y. Huang and P. O. Vontobel. <em>IEEE ISIT</em>, Melbourne, Australia, Jul. 2021, pp. 1338–1343.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Characterizing the Bethe partition function of double-edge factor graphs via graph covers</p>
<p class="cv-entry-detail">Y. Huang and P. O. Vontobel. <em>IEEE ISIT</em>, Los Angeles, USA, Jun. 2020, pp. 1331–1336. <a href="/files/slides/isit2020.pdf">Slides</a></p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">User cooperation for NOMA-based mobile edge computing</p>
<p class="cv-entry-detail">Y. Huang and Y. Liu. <em>IEEE ICCS</em>, Chengdu, China, Dec. 2018, pp. 395–400.</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Energy-Efficient SWIPT in Distributed Antenna Systems</p>
<p class="cv-entry-detail">Y. Huang and Y. Liu. <em>IEEE Globecom Workshops</em>, Singapore, Dec. 2017, pp. 1–6.</p>
</div>
</div>

<div class="cv-section">
<h2>Talks</h2>

<div class="cv-entry">
<p class="cv-entry-main">Bethe Approximations for Matrix Permanents and Contingency Table Counting</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Jan. 2026</span> · Data Science and Analytics Thrust, HKUST (Guangzhou) · <a href="/files/slides/talk_hkustgz.pdf">Slides</a></p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">The Bethe approximation for binary contingency table counting and nonnegative matrix permanents</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Feb. 2025</span> · Department of Computer Science, TU Dortmund University (virtual)</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">The Bethe partition function and the SPA for factor graphs based on homogeneous real stable polynomials</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Sept. 2024</span> · School of Cyber Science and Engineering, Southeast University (virtual)</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Bounding the permanent of a non-negative matrix via its degree-M Bethe and Sinkhorn permanents</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Mar. 2023</span> · Institute of Theoretical Computer Science and Communications, CUHK</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">On the relationship between the minimum of the Bethe free energy function of a factor graph and sum-product algorithm fixed points</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Nov. 2022</span> · Institute of Theoretical Computer Science and Communications, CUHK</p>
</div>

<div class="cv-entry">
<p class="cv-entry-main">Sets of marginals and Pearson-correlation-based CHSH inequalities for a two-qubit system</p>
<p class="cv-entry-detail"><span class="cv-entry-date">Apr. 2022</span> · Prof. Marco Tomamichel's research group, National University of Singapore (virtual)</p>
</div>
</div>

<div class="cv-section">
<h2>Teaching</h2>
<ul class="cv-list">
<li><strong>2022</strong> · Electronic Circuit Design Laboratory (Teaching Assistant), CUHK (also 2019, 2020)</li>
<li><strong>2022</strong> · Social Media and Human Information Interaction (Teaching Assistant), CUHK</li>
<li><strong>2021</strong> · Basic Analog and Digital Circuits (Teaching Assistant), CUHK</li>
<li><strong>2021</strong> · Linear Algebra for Engineers (Teaching Assistant), CUHK</li>
<li><strong>2018–2020</strong> · Principles of Communication Systems (Teaching Assistant), CUHK</li>
</ul>
</div>

<div class="cv-section">
<h2>Service and Leadership</h2>
<ul class="cv-list">
<li>Journal reviewer for <em>IEEE Communications Magazine</em>, <em>IEEE Transactions on Communications</em>, <em>IEEE Journal of Selected Topics in Signal Processing</em>, and <em>IEEE Communications Letters</em></li>
<li>Conference reviewer for IEEE International Symposium on Information Theory, IEEE International Conference on Communications, and IEEE Wireless Communications and Networking Conference</li>
</ul>
</div>

<div class="cv-section">
<h2>Awards</h2>
<ul class="cv-list">
<li><strong>2024</strong> · Student Travel Grant, IEEE International Symposium on Information Theory</li>
<li><strong>2018</strong> · Bachelor's Thesis Award, South China University of Technology</li>
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
