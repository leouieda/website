---
title: Fast non-linear gravity inversion in spherical coordinates with application to the South American Moho
author: uieda, barbosa
layout: publication
date: 2016-04-01
journal: Geophysical Journal International
repository: pinga-lab/paper-moho-inversion-tesseroids
thumbnail: paper-moho-inversion-2016.png
inreview: true
---

# About

This paper is a chapter of my PhD thesis.
It describes a new gravity inversion method to estimate the depth of the
crust-mantle interface (the Moho).
The inversion uses a spherical Earth approximation by discretizing the Earth
into tesseroids (spherical prisms).
The forward modeling method used is described in the paper
[/papers/paper-tesseroids-2016].
We applied the inversion to estimate the Moho depth for South America.

# Open-source implementation

The inversion method proposed here is implemented in the Python programming
language.
The code uses the forward modeling and inversion packages of the library
[/software/fatiando].
You'll find the source code and all you need to produce the results
from the paper on the Github repository
[pinga-lab/paper-moho-inversion-tesseroids](https://github.com/pinga-lab/paper-moho-inversion-tesseroids)


# Abstract

Estimating the relief of the Moho from gravity data is a computationally
intensive non-linear inverse problem.  What is more, the modeling must take the
Earths curvature into account when the study area is of regional scale or
greater.  We present a regularized non-linear gravity inversion method that has
a low computational footprint and employs a spherical Earth approximation.  To
achieve this, we combine the highly efficient Bott's method with smoothness
regularization and a discretization of the anomalous Moho into tesseroids
(spherical prisms).  The computational efficiency of our method is attained by
harnessing the fact that all matrices involved are sparse.  The inversion
results are controlled by three hyper-parameters: the regularization parameter,
the anomalous Moho density-contrast, and the reference Moho depth.  We estimate
the regularization parameter using the method of hold-out cross-validation.
Additionally, we estimate the density-contrast and the reference depth using
knowledge of the Moho depth at certain points.  We apply the proposed method to
estimate the Moho depth for the South American continent using satellite
gravity data and seismological data.  The final Moho model is in accordance
with previous gravity-derived models and seismological data.  The misfit to the
gravity and seismological data is worse in the Andes and best in oceanic areas,
central Brazil and Patagonia, and along the Atlantic coast.  Similarly to
previous results, the model suggests a thinner crust of 30-35 km under the
Andean foreland basins.  Discrepancies with the seismological data are greatest
in the Guyana Shield, the central Solimões and Amazonas Basins, the Paraná
Basin, and the Borborema province.  These differences suggest the existence of
crustal or mantle density anomalies that were unaccounted for during gravity
data processing.
