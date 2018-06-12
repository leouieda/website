---
title: <b>PhD</b> in Geophysics
thesis: "Forward modeling and inversion of gravitational fields in spherical coordinates"
date: 2016-04-29
start_date: 2011-11-01
degree: PhD
advisor: Valéria C. F. Barbosa
subject: Geophysics
repository: leouieda/phd-thesis
institution: Observatório Nacional, Brazil
pdf: phd-thesis.pdf
sucupira: 3627205
layout: publication
thumbnail: phd.png
tags: moho, tesseroids, fatiando
---

{% from "utils.html" import make_index %}

# About

After my [Master's degree][/about/masters],
I stayed at the Observatório Nacional for my PhD,
also with [Valéria C. F. Barbosa](http://lattes.cnpq.br/0391036221142471).
In 2016, I defended my thesis, which was submitted for publication in 3 parts:

<div>
    {% set papers = site|pages(["/papers/paper-moho-inversion-tesseroids-2016",
                                "/papers/paper-tesseroids-2016",
                                "/talks/scipy2013"]) %}
    {{ make_index(papers, site, hr=false, date=true, year_only=true) }}
</div>

During my PhD, I presented the following yearly seminars at the Observatório
Nacional:

* 2015: [leouieda/seminario-on-2015](https://github.com/leouieda/seminario-on-2015)
* 2014: [leouieda/seminario-on-2014](https://github.com/leouieda/seminario-on-2014)
* 2013: [leouieda/qualify](https://github.com/leouieda/qualify) (qualification exam)
* 2012: [leouieda/seminario-on-2012](https://github.com/leouieda/seminario-on-2012)

# PhD defense slides

<script async class="speakerdeck-embed"
data-id="db1324af5ddc4183b5961497fd87b057" data-ratio="1.33333333333333"
src="//speakerdeck.com/assets/embed.js"></script>


# Abstract

We present methodological improvements to forward modeling and regional
inversion of satellite gravity data. For this purpose, we developed two
open-source software projects. The first is a C language suite of command-line
programs called Tesseroids. The programs calculate the gravitational potential,
acceleration, and gradient tensor of a spherical prism, or tesseroid.
Tesseroids implements and extends an adaptive discretization algorithm to
automatically ensure the accuracy of the computations. Our numerical
experiments show that, to achieve the same level of accuracy, the gravitational
acceleration components require finner discretization than the potential. In
turn, the gradient tensor requires finner discretization still than the
acceleration. The second open-source project is Fatiando a Terra, a Python
language library for inversion, forward modeling, data processing, and
visualization. The library allows the user to combine the forward modeling and
inversion tools to implement new inversion methods. The gravity forward
modeling tools include an implementation of the algorithm used in the
Tesseroids software. We combined the inversion and tesseroid forward modeling
utilities of Fatiando a Terra to develop a new method for fast non-linear
gravity inversion. The method estimates the depth of the crust-mantle interface
(the Moho) based on observed gravity data using a spherical Earth
approximation. We extended the computationally efficient Bott's method to
include smoothness regularization and use tesseroids instead right rectangular
prisms. The inversion is controlled by three hyper-parameters: the
regularization parameter, the density-contrast between the real Earth and the
reference model (the Normal Earth), and the depth of the Moho of the Normal
Earth. We employ two cross-validation procedures to automatically estimate
these parameters. Tests on synthetic data confirm the capability of the
proposed method to estimate smoothly varying Moho depths and the three
hyper-parameters. Finally, we applied the inversion method developed to produce
a Moho depth model for South America. The estimated Moho depth model fits the
gravity data and seismological Moho depth estimates in the oceanic areas and
the central and eastern portions of the continent. We observe large misfits in
the Andes region, where Moho depth is largest. In Amazon, Solimões, and Paraná
Basins, the model fits the observed gravity but disagrees with seismological
estimates. These discrepancies suggest the existence of density-anomalies in
the crust or upper mantle, as has been suggested in the literature.
