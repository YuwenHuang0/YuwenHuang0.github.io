---
title: "Block-OBS-GS: Exact Per-Block Joint Brain Surgery with Gauss–Seidel Refinement for LLM Pruning"
authors:
  - Yuwen Huang
  - Xiang Pan
collection: publications
category: conferences
permalink: /publication/block-obs-gs
excerpt: "A post-training LLM pruning method that jointly reconstructs surviving weights within blocks and refines the fixed-mask solution with Gauss–Seidel updates."
date: '2026-09-25'
publication_date: '2026-12-01'
status: To appear
venue: "Conference on Neural Information Processing Systems (NeurIPS)"
topic: machine-learning
sole_first: true
corresponding_authors:
  - Xiang Pan
---

Block-OBS-GS improves the reconstruction of large language models after post-training pruning. It jointly adjusts the weights retained within each block, then uses a Gauss–Seidel sweep to refine the solution across blocks. The paper analyzes the fixed-mask reconstruction problem and evaluates the trade-off between model quality and pruning time.
