---
title: Modeling the Earth with Fatiando a Terra
author: uieda, oliveira-jr, barbosa
date: 2013-06-01
pdf: scipy-2013.pdf
repository: leouieda/scipy2013
slides: <a href="http://www.leouieda.com/scipy2013/?theme=night#/">HTML slides</a>
event: Python in Science Conference
supplement: 10.6084/m9.figshare.708390
thumbnail: scipy2013.png
youtube: Ec38h1oB8cc
doi: 10.25080/Majora-8b375195-010
citation: Uieda, L., V. C. Oliveira Jr and V. C. F. Barbosa (2013), Modeling the Earth with Fatiando a Terra, Proceedings of the 12th Python in Science Conference, pp. 90-96
alm: true
layout: publication
tags: fatiando, open-source
---

{% from "utils.html" import youtube_embed %}

# About

This was the first presentation that I made about [Fatiando a
Terra](https://www.fatiando.org), a Python library for modeling and inversion in
geophysics.
The proceedings paper that accompanies this talk became the second chapter of
my [PhD thesis][/about/phd].


# Video recording

Scipy records all of the presentations and [makes them available on
YouTube](https://www.youtube.com/playlist?list=PLYx7XA2nY5GeTWcUQTbXVdllyp-Ie3r-y).
Here is the video of mine:

{{ youtube_embed("Ec38h1oB8cc") }}


# Abstract

**Conference proceedings site**:
[http://conference.scipy.org/proceedings/scipy2013/uieda.html](http://conference.scipy.org/proceedings/scipy2013/uieda.html)

Solid Earth geophysics is the science of using physical observations of the
Earth to infer its inner structure. Generally, this is done with a variety of
numerical modeling techniques and inverse problems. The development of new
algorithms usually involves copy and pasting of code, which leads to errors and
poor code reuse. Added to this is a modeling pipeline composed of various tools
that don't communicate with each other (Fortran/C for computations, large
complicated I/O files, Matlab/VTK for visualization, etc). Fatiando a Terra is
a Python library that aims to unify the modeling pipeline inside of the Python
language. This allows users to replace the traditional shell scripting with
more versatile and powerful Python scripting. Together with the new IPython
notebook, Fatiando a Terra can integrate all stages of the geophysical modeling
process, like data pre-processing, inversion, statistical analysis, and
visualization. However, the library can also be used for quickly developing
stand-alone programs that can be integrated into existing pipelines. Plus,
because functions inside Fatiando a Terra use a common data and mesh format,
existing algorithms can be combined and new ideas can build upon existing
functionality. This flexibility facilitates reproducible computations,
prototyping of new algorithms, and interactive teaching exercises. Although the
project has so far focused on potential field methods (gravity and magnetics),
some numerical tools for other geophysical methods have been developed as well.
The library already contains: fast implementations of forward modeling
algorithms (using Numpy and Cython), generic inverse problem solvers, unified
geometry classes (prism meshes, polygons, etc), functions to automate
repetitive plotting tasks with Matplotlib (automatic griding, simple GUIs,
picking, projections, etc) and Mayavi (automatic conversion of geometry classes
to VTK, drawing continents, etc). In the future, we plan to continuously
implement classic and state-of-the-art algorithms as well as sample problems to
help teach geophysics.
