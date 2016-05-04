---
title: "BSc in Geophysics: Cálculo do tensor gradiente gravimétrico utilizando tesseroides"
date: 2009-12-01
thumbnail: agu2010.png
doi: 10.6084/m9.figshare.963547
repository: leouieda/barchelor-thesis
institution: Universidade de São Paulo, Brazil
alm: true
layout: publication
---

# About

My Bachelor's degree in Geophysics is from the Universidade de São Paulo,
Brazil, where I studied from 2004 until 2009.
I did an undergraduate research project and eventually my thesis under the
supervision of [Naomi Ussami](http://lattes.cnpq.br/6704246490515612).
This was when I started development of the software
[Tesseroids][/software/tesseroids] and the research that lead to the paper
[/papers/paper-tesseroids-2016], which is the first part of my
[PhD thesis][/about/phd].

You can download a PDF of my thesis (in Portuguese) from
[figshare](http://figshare.com) at
doi:[10.6084/m9.figshare.963547](http://dx.doi.org/10.6084/m9.figshare.963547).

Presentations about this topic:

* [/talks/goce2011]
* [/talks/agu2010]
* [leouieda/simposio-iag-2008](https://github.com/leouieda/simposio-iag-2008)

Other work that uses this research:

* [/papers/paper-moho-inversion-tesseroids-2016]
* [/talks/egu2014]

Slides from my thesis defense:

<script async class="speakerdeck-embed"
data-id="169b9ea3da7043ff932a297100824ab7" data-ratio="1.33333333333333"
src="//speakerdeck.com/assets/embed.js"></script>

# Abstract

The GOCE satellite mission has the objective of measuring the Earths
gravitational field with an unprecedented accuracy through the measurement of
the gravity gradient tensor (GGT). The data provided by this mission could be
used to study large areas, where the flat Earth approximation can have its
limitations. In these cases the modeling could be done with tesseroids, also
called spherical prisms, in order to take the Earths curvature into account.
The GGT caused by a tesseroid can be calculated with numerical integration
methods, such as the Gauss-Legendre Quadrature (GLQ). In the current project, a
computer program was developed for the direct calculation of the GGT using the
GLQ. The accuracy of this implementation was evaluated by comparing its results
with the result of analytical formulas for the special case of a spherical cap.
Next, the developed program was used to calculate the differences in the GGT
caused by the flat Earth approximation. These differences reach are up to 30%
in the Tzz component for a 50 deg x 50 deg x 10 km model. Finally, the computer
program was used to calculate the effect caused by the topographic masses on
the GGT at 250 km altitude for the Paraná basin region. In regions of large
topographical variations, the components of the GGT due to the topographic
masses have amplitudes of the same order of magnitude as the GGT components due
to density anomalies in the interior of the crust and mantle.
