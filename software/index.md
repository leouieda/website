---
title: Software
banner_image: images/github-graph.jpg
banner_position: center
banner_title: Software
banner_subtitle: The open-source software projects with which I'm involved
template: base.html
---

{% import "macros.html" as macros %}

## Fatiando a Terra

<i class="fa fa-external-link-square-alt" aria-hidden="true"></i>
Website: <a href="https://www.fatiando.org" target="_blank">www.fatiando.org</a>

Fatiando provides Python libraries for data processing, modeling, and inversion
across the Geosciences.
It is built by a community of geoscientists and software developers with a
passion for well-designed tools and helping our peers.

I've been working on Fatiando since around 2010 when I started my MSc.
It's been the main focus of my career and it permeates all aspects of my work,
from research to teaching.


## xlandsat

<i class="fa fa-external-link-square-alt" aria-hidden="true"></i>
Website: <a href="https://www.compgeolab.org/xlandsat" target="_blank">www.compgeolab.org/xlandsat</a>

A small Python library for loading Landsat multi-spectral remote sensing scenes
from downloaded from [USGS EarthExplorer](https://earthexplorer.usgs.gov/) into
``xarray.Dataset`` containers. It takes care of reading the metadata and
organizing the bands into a single data structure for easier manipulation,
processing, and visualization.

`xlandsat` started as code I wrote for my
[remote sensing class at Liverpool](../teaching) which I made into a package to
make sure students can get started manipulating data with as little overhead as
possible.
It's also what I used to make some
[pretty images of the 2022 Mauna Loa volcano eruption](../blog/mauna-loa.html).


## Nēnē

<i class="fa fa-external-link-square-alt" aria-hidden="true"></i>
Website: <a href="https://nene.leouieda.com" target="_blank">nene.leouieda.com</a>

Nēnē is a no-frills static site generator. It's the side project that I use to
blow off steam and experiment with Python without the pressures of backwards
compatibility and testing that my research software work requires.
It's also what I use to build this website.

The name is a nod to [Urubu](https://github.com/jandecaluwe/urubu), which I
used to build my website before, and the
[unforgettable time I spent in Hawai'i](/blog/hawaii-gmt-postdoc.html).


## Generic Mapping Tools (GMT)

<i class="fa fa-external-link-square-alt" aria-hidden="true"></i>
Website: <a href="https://www.generic-mapping-tools.org" target="_blank">www.generic-mapping-tools.org</a>

GMT is one of the most widely used open-source software projects in the Earth
Sciences. It's been around for decades and is to many the very symbol of
open-source. I had the pleasure to
[join the GMT team](/blog/hawaii-gmt-postdoc.html) during my postdoc working
on [PyGMT](https://www.pygmt.org).

Recently, my contributions to GMT and PyGMT have been more on the community and
guidance side than actual coding.
Thankfully, they don't really need me for the coding parts.


## Tesseroids

<i class="fa fa-external-link-square-alt" aria-hidden="true"></i>
Website: <a href="https://tesseroids.leouieda.com" target="_blank">tesseroids.leouieda.com</a>

A collection of command-line programs for modelling the gravitational attraction
of spherical prisms (tesseroids).

This was my first open-source project. I started working on Tesseroids as part
of my BSc dissertation project with
[Naomi Ussami](http://lattes.cnpq.br/6704246490515612) and
[Carla Braitenberg](https://www2.units.it/braitenberg/).
Through Tesseroids, I learned about documentation, unit tests,
cross-compilation, version control, and more.
