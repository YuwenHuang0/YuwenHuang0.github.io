# BP+OSD for DQI: matched-cost finite-code audit

## Exact decoder metrics

| case | decoder | Z | J | R | dZ | dJ | dR | edge updates | OSD trials | rerank bit ops | complete ML fibers |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cycle-complete-9x6 | BP + syndrome projection | 0.851986813 | 0.768263166 | 0.228556680 | -2.161e-03 | -3.949e-04 | -9.171e-04 | 384 | 0 | 0 | 1.000 |
| cycle-complete-9x6 | BP+OSD, conventional BP-metric tie | 0.854148239 | 0.768658081 | 0.229473827 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 384 | 7 | 0 | 1.000 |
| cycle-complete-9x6 | DQI-aware BP+OSD, canonical tie | 0.854148239 | 0.772595185 | 0.232836697 | +0.000e+00 | +3.937e-03 | +3.363e-03 | 384 | 7 | 63 | 1.000 |
| cycle-complete-9x6 | exact canonical ML ceiling | 0.854148239 | 0.772595185 | 0.232836697 | +0.000e+00 | +3.937e-03 | +3.363e-03 | 0 | 0 | 0 | 1.000 |
| cycle-complete-12x7 | BP + syndrome projection | 0.741230561 | 0.739985223 | 0.177884381 | -2.238e-04 | -3.484e-04 | -3.120e-04 | 504 | 0 | 0 | 1.000 |
| cycle-complete-12x7 | BP+OSD, conventional BP-metric tie | 0.741454363 | 0.740333617 | 0.178196409 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 504 | 16 | 0 | 1.000 |
| cycle-complete-12x7 | DQI-aware BP+OSD, canonical tie | 0.741454363 | 0.744551089 | 0.181323472 | +0.000e+00 | +4.217e-03 | +3.127e-03 | 504 | 16 | 192 | 1.000 |
| cycle-complete-12x7 | exact canonical ML ceiling | 0.741454363 | 0.744551089 | 0.181323472 | +0.000e+00 | +4.217e-03 | +3.127e-03 | 0 | 0 | 0 | 1.000 |
| cycle-rich-16x7 | BP + syndrome projection | 0.477139081 | 0.676514536 | 0.084221983 | -1.033e-02 | -4.807e-03 | -4.166e-03 | 696 | 0 | 0 | 0.969 |
| cycle-rich-16x7 | BP+OSD, conventional BP-metric tie | 0.487466468 | 0.681321061 | 0.088387937 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 696 | 29 | 0 | 0.969 |
| cycle-rich-16x7 | DQI-aware BP+OSD, canonical tie | 0.487466468 | 0.684486599 | 0.089931031 | +0.000e+00 | +3.166e-03 | +1.543e-03 | 696 | 29 | 464 | 0.969 |
| cycle-rich-16x7 | exact canonical ML ceiling | 0.487466468 | 0.684486599 | 0.089931031 | +0.000e+00 | +3.166e-03 | +1.543e-03 | 0 | 0 | 0 | 0.969 |
| random-sparse-18x8 | BP + syndrome projection | 0.460087278 | 0.669519977 | 0.077993985 | -2.385e-02 | -8.396e-03 | -8.106e-03 | 1296 | 0 | 0 | 0.492 |
| random-sparse-18x8 | BP+OSD, conventional BP-metric tie | 0.483934323 | 0.677916362 | 0.086099834 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 1296 | 29 | 0 | 0.492 |
| random-sparse-18x8 | DQI-aware BP+OSD, canonical tie | 0.483934323 | 0.684213305 | 0.089147141 | +0.000e+00 | +6.297e-03 | +3.047e-03 | 1296 | 29 | 522 | 0.492 |
| random-sparse-18x8 | exact canonical ML ceiling | 0.484200281 | 0.687415193 | 0.090746489 | +2.660e-04 | +9.499e-03 | +4.647e-03 | 0 | 0 | 0 | 0.492 |
| random-sparse-22x9 | BP + syndrome projection | 0.363951022 | 0.653174115 | 0.055747876 | -1.908e-02 | -6.836e-03 | -5.542e-03 | 1584 | 0 | 0 | 0.361 |
| random-sparse-22x9 | BP+OSD, conventional BP-metric tie | 0.383034911 | 0.660010474 | 0.061289598 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 1584 | 29 | 0 | 0.361 |
| random-sparse-22x9 | DQI-aware BP+OSD, canonical tie | 0.383034911 | 0.666040157 | 0.063599177 | +0.000e+00 | +6.030e-03 | +2.310e-03 | 1584 | 29 | 638 | 0.361 |
| random-sparse-22x9 | exact canonical ML ceiling | 0.383931749 | 0.670052364 | 0.065288502 | +8.968e-04 | +1.004e-02 | +3.999e-03 | 0 | 0 | 0 | 0.361 |

## Paired-estimator accuracy

| case | decoder | pairs | calls | RMSE(Z) | RMSE(J) | RMSE(R) |
|---|---|---:|---:|---:|---:|---:|
| cycle-complete-9x6 | BP+OSD, conventional BP-metric tie | 128 | 256 | 2.986e-02 | 1.290e-02 | 1.597e-02 |
| cycle-complete-9x6 | BP+OSD, conventional BP-metric tie | 512 | 1024 | 1.071e-02 | 5.939e-03 | 5.411e-03 |
| cycle-complete-9x6 | BP+OSD, conventional BP-metric tie | 2048 | 4096 | 5.804e-03 | 2.405e-03 | 2.239e-03 |
| cycle-complete-9x6 | BP+OSD, conventional BP-metric tie | 8192 | 16384 | 4.119e-03 | 1.333e-03 | 1.793e-03 |
| cycle-complete-9x6 | DQI-aware BP+OSD, canonical tie | 128 | 256 | 2.920e-02 | 8.854e-03 | 1.200e-02 |
| cycle-complete-9x6 | DQI-aware BP+OSD, canonical tie | 512 | 1024 | 1.496e-02 | 6.180e-03 | 7.542e-03 |
| cycle-complete-9x6 | DQI-aware BP+OSD, canonical tie | 2048 | 4096 | 6.971e-03 | 3.414e-03 | 3.781e-03 |
| cycle-complete-9x6 | DQI-aware BP+OSD, canonical tie | 8192 | 16384 | 3.555e-03 | 1.291e-03 | 1.667e-03 |
| cycle-complete-12x7 | BP+OSD, conventional BP-metric tie | 128 | 256 | 3.482e-02 | 1.578e-02 | 1.698e-02 |
| cycle-complete-12x7 | BP+OSD, conventional BP-metric tie | 512 | 1024 | 1.659e-02 | 7.912e-03 | 7.912e-03 |
| cycle-complete-12x7 | BP+OSD, conventional BP-metric tie | 2048 | 4096 | 9.290e-03 | 4.080e-03 | 3.454e-03 |
| cycle-complete-12x7 | BP+OSD, conventional BP-metric tie | 8192 | 16384 | 4.975e-03 | 1.877e-03 | 1.912e-03 |
| cycle-complete-12x7 | DQI-aware BP+OSD, canonical tie | 128 | 256 | 4.172e-02 | 1.567e-02 | 1.717e-02 |
| cycle-complete-12x7 | DQI-aware BP+OSD, canonical tie | 512 | 1024 | 1.805e-02 | 6.632e-03 | 8.128e-03 |
| cycle-complete-12x7 | DQI-aware BP+OSD, canonical tie | 2048 | 4096 | 9.238e-03 | 3.160e-03 | 3.290e-03 |
| cycle-complete-12x7 | DQI-aware BP+OSD, canonical tie | 8192 | 16384 | 4.704e-03 | 1.804e-03 | 1.808e-03 |
| cycle-rich-16x7 | BP+OSD, conventional BP-metric tie | 128 | 256 | 4.531e-02 | 1.486e-02 | 1.129e-02 |
| cycle-rich-16x7 | BP+OSD, conventional BP-metric tie | 512 | 1024 | 2.199e-02 | 8.219e-03 | 6.260e-03 |
| cycle-rich-16x7 | BP+OSD, conventional BP-metric tie | 2048 | 4096 | 9.743e-03 | 4.682e-03 | 3.470e-03 |
| cycle-rich-16x7 | BP+OSD, conventional BP-metric tie | 8192 | 16384 | 5.307e-03 | 2.450e-03 | 1.633e-03 |
| cycle-rich-16x7 | DQI-aware BP+OSD, canonical tie | 128 | 256 | 4.747e-02 | 1.862e-02 | 1.357e-02 |
| cycle-rich-16x7 | DQI-aware BP+OSD, canonical tie | 512 | 1024 | 2.509e-02 | 1.024e-02 | 7.161e-03 |
| cycle-rich-16x7 | DQI-aware BP+OSD, canonical tie | 2048 | 4096 | 8.729e-03 | 6.630e-03 | 3.763e-03 |
| cycle-rich-16x7 | DQI-aware BP+OSD, canonical tie | 8192 | 16384 | 5.798e-03 | 2.280e-03 | 1.662e-03 |
| random-sparse-18x8 | BP+OSD, conventional BP-metric tie | 128 | 256 | 5.002e-02 | 1.880e-02 | 1.263e-02 |
| random-sparse-18x8 | BP+OSD, conventional BP-metric tie | 512 | 1024 | 1.579e-02 | 6.620e-03 | 4.426e-03 |
| random-sparse-18x8 | BP+OSD, conventional BP-metric tie | 2048 | 4096 | 1.151e-02 | 4.405e-03 | 2.711e-03 |
| random-sparse-18x8 | BP+OSD, conventional BP-metric tie | 8192 | 16384 | 5.996e-03 | 1.973e-03 | 1.773e-03 |
| random-sparse-18x8 | DQI-aware BP+OSD, canonical tie | 128 | 256 | 6.542e-02 | 2.273e-02 | 1.769e-02 |
| random-sparse-18x8 | DQI-aware BP+OSD, canonical tie | 512 | 1024 | 1.699e-02 | 9.221e-03 | 5.405e-03 |
| random-sparse-18x8 | DQI-aware BP+OSD, canonical tie | 2048 | 4096 | 1.084e-02 | 6.185e-03 | 3.339e-03 |
| random-sparse-18x8 | DQI-aware BP+OSD, canonical tie | 8192 | 16384 | 5.222e-03 | 3.548e-03 | 2.363e-03 |
| random-sparse-22x9 | BP+OSD, conventional BP-metric tie | 128 | 256 | 4.007e-02 | 2.326e-02 | 9.583e-03 |
| random-sparse-22x9 | BP+OSD, conventional BP-metric tie | 512 | 1024 | 2.005e-02 | 1.129e-02 | 5.411e-03 |
| random-sparse-22x9 | BP+OSD, conventional BP-metric tie | 2048 | 4096 | 9.007e-03 | 5.835e-03 | 2.493e-03 |
| random-sparse-22x9 | BP+OSD, conventional BP-metric tie | 8192 | 16384 | 5.558e-03 | 2.768e-03 | 1.345e-03 |
| random-sparse-22x9 | DQI-aware BP+OSD, canonical tie | 128 | 256 | 3.556e-02 | 1.682e-02 | 9.165e-03 |
| random-sparse-22x9 | DQI-aware BP+OSD, canonical tie | 512 | 1024 | 1.569e-02 | 1.437e-02 | 6.137e-03 |
| random-sparse-22x9 | DQI-aware BP+OSD, canonical tie | 2048 | 4096 | 8.912e-03 | 5.927e-03 | 2.667e-03 |
| random-sparse-22x9 | DQI-aware BP+OSD, canonical tie | 8192 | 16384 | 4.236e-03 | 2.896e-03 | 1.615e-03 |

## Common-random-number estimate of the DQI-aware gain

| case | pairs | calls | exact dJ | mean dJ | RMSE(dJ) | exact dR | mean dR | RMSE(dR) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| cycle-complete-9x6 | 128 | 512 | +3.937e-03 | +5.598e-03 | 1.746e-02 | +3.363e-03 | +5.422e-03 | 1.288e-02 |
| cycle-complete-9x6 | 512 | 2048 | +3.937e-03 | +5.097e-03 | 8.408e-03 | +3.363e-03 | +5.252e-03 | 6.984e-03 |
| cycle-complete-9x6 | 2048 | 8192 | +3.937e-03 | +4.145e-03 | 4.342e-03 | +3.363e-03 | +3.565e-03 | 4.055e-03 |
| cycle-complete-9x6 | 8192 | 32768 | +3.937e-03 | +4.153e-03 | 1.717e-03 | +3.363e-03 | +3.237e-03 | 1.394e-03 |
| cycle-complete-12x7 | 128 | 512 | +4.217e-03 | +4.964e-03 | 1.128e-02 | +3.127e-03 | +3.614e-03 | 9.650e-03 |
| cycle-complete-12x7 | 512 | 2048 | +4.217e-03 | +4.760e-03 | 6.837e-03 | +3.127e-03 | +3.586e-03 | 5.343e-03 |
| cycle-complete-12x7 | 2048 | 8192 | +4.217e-03 | +3.994e-03 | 3.726e-03 | +3.127e-03 | +2.520e-03 | 3.017e-03 |
| cycle-complete-12x7 | 8192 | 32768 | +4.217e-03 | +4.262e-03 | 1.778e-03 | +3.127e-03 | +3.351e-03 | 1.415e-03 |
| cycle-rich-16x7 | 128 | 512 | +3.166e-03 | +1.120e-02 | 2.407e-02 | +1.543e-03 | +4.744e-03 | 1.101e-02 |
| cycle-rich-16x7 | 512 | 2048 | +3.166e-03 | +2.740e-03 | 7.174e-03 | +1.543e-03 | +4.518e-04 | 3.509e-03 |
| cycle-rich-16x7 | 2048 | 8192 | +3.166e-03 | +3.906e-03 | 4.155e-03 | +1.543e-03 | +2.125e-03 | 2.052e-03 |
| cycle-rich-16x7 | 8192 | 32768 | +3.166e-03 | +3.277e-03 | 1.928e-03 | +1.543e-03 | +1.615e-03 | 1.033e-03 |
| random-sparse-18x8 | 128 | 512 | +6.297e-03 | +3.255e-03 | 2.573e-02 | +3.047e-03 | +8.758e-04 | 1.137e-02 |
| random-sparse-18x8 | 512 | 2048 | +6.297e-03 | +8.703e-03 | 1.280e-02 | +3.047e-03 | +4.379e-03 | 5.887e-03 |
| random-sparse-18x8 | 2048 | 8192 | +6.297e-03 | +6.786e-03 | 6.642e-03 | +3.047e-03 | +3.510e-03 | 3.387e-03 |
| random-sparse-18x8 | 8192 | 32768 | +6.297e-03 | +6.775e-03 | 3.426e-03 | +3.047e-03 | +3.277e-03 | 1.652e-03 |
| random-sparse-22x9 | 128 | 512 | +6.030e-03 | -6.875e-04 | 2.571e-02 | +2.310e-03 | +1.164e-03 | 1.014e-02 |
| random-sparse-22x9 | 512 | 2048 | +6.030e-03 | +5.696e-03 | 1.439e-02 | +2.310e-03 | +2.274e-03 | 5.840e-03 |
| random-sparse-22x9 | 2048 | 8192 | +6.030e-03 | +2.008e-03 | 6.490e-03 | +2.310e-03 | +1.607e-03 | 2.653e-03 |
| random-sparse-22x9 | 8192 | 32768 | +6.030e-03 | +6.060e-03 | 2.737e-03 | +2.310e-03 | +2.078e-03 | 8.961e-04 |

## Scope

The exact metrics enumerate all syndromes and are ground truth only for these small codes. The paired estimator remains scalable because it uses two decoder calls per pair. The BP1 qubit count is a comparator only: soft BP+OSD needs fixed-precision arithmetic, sorting, elimination, list storage, and uncomputation that are not included in that formula.
