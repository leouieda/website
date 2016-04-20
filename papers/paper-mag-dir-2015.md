---
title: Estimation of the total magnetization direction of approximately spherical bodies
layout: publication
date: 2015-04-24
journal: Nonlinear Processes in Geophysics
doi: 10.5194/npg-22-215-2015
repository: pinga-lab/Total-magnetization-of-spherical-bodies
supplement: 10.5281/zenodo.16191
alm: true
oa: true
author: oliveira-jr, daiana, barbosa, uieda
thumbnail: paper-mag-dir-2015.png
citation: Oliveira Jr., V. C., D. P. Sales, V. C. F. Barbosa, and L. Uieda (2015), Estimation of the total magnetization direction of approximately spherical bodies, Nonlin. Processes Geophys., 22(2), 215-232, doi:10.5194/npg-22-215-2015.
---

# Open-source implementation

The method described in this article has been implemented in the open-source
geophysics library [Fatiando a Terra](http://www.fatiando.org).
The method was first introduced in
[version 0.3](http://www.fatiando.org/changelog.html#version-0-3)
as the `fatiando.gravmag.magdir.DipoleMagDir` class
(see [PR 87](https://github.com/fatiando/fatiando/pull/87)
for the full development history of this implementation).
See the project documentation
and the code repository of this paper
([pinga-lab/Total-magnetization-of-spherical-bodies](https://github.com/pinga-lab/Total-magnetization-of-spherical-bodies))
for more information about using this class.

# Open peer-review

This paper has undergone open peer-review.
The original submission, reviews, and replies can be viewed at
[doi:10.5194/npgd-1-1465-2014](http://dx.doi.org/10.5194/npgd-1-1465-2014).

# Abstract

We have developed a fast total-field anomaly inversion to estimate the
magnetization direction of multiple sources with approximately spherical shapes
and known centres. Our method is an overdetermined inverse problem that can be
applied to interpret multiple sources with different but homogeneous
magnetization directions. It requires neither the prior computation of any
transformation-like reduction to the pole nor the use of regularly spaced data
on a horizontal grid. The method contains flexibility to be implemented as a
linear or non-linear inverse problem, which results, respectively, in a
least-squares or robust estimate of the components of the magnetization vector
of the sources. Applications to synthetic data show the robustness of our
method against interfering anomalies and errors in the location of the sources'
centre. Besides, we show the feasibility of applying the upward continuation to
interpret non-spherical sources. Applications to field data over the Goiás
alkaline province (GAP), Brazil, show the good performance of our method in
estimating geologically meaningful magnetization directions. The results
obtained for a region of the GAP, near to the alkaline complex of Diorama,
suggest the presence of non-outcropping sources marked by strong remanent
magnetization with inclination and declination close to −70.35 and −19.81°,
respectively. This estimated magnetization direction leads to predominantly
positive reduced-to-the-pole anomalies, even for other region of the GAP, in
the alkaline complex of Montes Claros de Goiás. These results show that the
non-outcropping sources near to the alkaline complex of Diorama have almost the
same magnetization direction of those ones in the alkaline complex of Montes
Claros de Goiás, strongly suggesting that these sources have been emplaced in
the crust within almost the same geological time interval.

# Bibtex

    @article{oliveira_jr._estimation_2015,
        title = {Estimation of the total magnetization direction of approximately spherical bodies},
        volume = {22},
        issn = {1607-7946},
        doi = {10.5194/npg-22-215-2015},
        number = {2},
        journal = {Nonlin. Processes Geophys.},
        author = {Oliveira Jr., V. C. and Sales, D. P. and Barbosa, V. C. F. and Uieda, L.},
        year = {2015},
        pages = {215--232},
    }
