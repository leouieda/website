---
title: <b>MSc</b> in Geophysics
thesis: "Robust 3D gravity gradient inversion by planting anomalous densities"
date: 2011-11-01
start_date: 2010-03-01
advisor: Valéria C. F. Barbosa
degree: MSc
subject: Geophysics
repository: pinga-lab/paper-planting-densities
institution: Observatório Nacional, Brazil
pdf: msc-dissertation.pdf
layout: publication
thumbnail: masters.png
tags: planting-inversion
---

{% from "utils.html" import make_index %}

# About

I did my Master's degree in Geophysics at the Observatório Nacional in Rio de
Janeiro, Brazil, under the supervision of
[Valéria C. F. Barbosa](http://lattes.cnpq.br/0391036221142471).
I started in March 2010 and defended my dissertation in October 2011.

The method that we developed is implemented in the software
[Fatiando a Terra](https://www.fatiando.org).
The dissertation was later published as the paper:

<div>
    {{ make_index(site|pages(["/papers/paper-planting-anomalous-densities-2012"]), site, hr=false, date=true, year_only=true) }}
</div>

During my Masters, I presented the following yearly seminars:

* 2011: [leouieda/seminario-on-2011](https://github.com/leouieda/seminario-on-2011)
* 2010: [leouieda/seminario-on-2010](https://github.com/leouieda/seminario-on-2010)


# Dissertation defense slides

<script async class="speakerdeck-embed"
data-id="bd870aa438774d84974048becca502a1" data-ratio="1.33159947984395"
src="//speakerdeck.com/assets/embed.js"></script>

# Abstract

We have developed a new gravity gradient inversion method for estimating a 3D
density-contrast distribution defined on a grid of rectangular prisms. Our
method consists of an iterative algorithm that does not require the solution of
an equation system. Instead, the solution grows systematically around
user-specified prismatic elements, called “seeds,” with given density
contrasts. Each seed can be assigned a different density-contrast value,
allowing the interpretation of multiple sources with different density
contrasts and that produce interfering signals. In real world scenarios, some
sources might not be targeted for the interpretation. Thus, we developed a
robust procedure that neither requires the isolation of the signal of the
targeted sources prior to the inversion nor requires substantial prior
information about the nontargeted sources. In our iterative algorithm, the
estimated sources grow by the accretion of prisms in the periphery of the
current estimate. In addition, only the columns of the sensitivity matrix
corresponding to the prisms in the periphery of the current estimate are needed
for the computations. Therefore, the individual columns of the sensitivity
matrix can be calculated on demand and deleted after an accretion takes place,
greatly reducing the demand for computer memory and processing time. Tests on
synthetic data show the ability of our method to correctly recover the geometry
of the targeted sources, even when interfering signals produced by nontargeted
sources are present. Inverting the data from an airborne gravity gradiometry
survey flown over the iron ore province of Quadrilátero Ferrífero, southeastern
Brazil, we estimated a compact iron ore body that is in agreement with geologic
information and previous interpretations.
