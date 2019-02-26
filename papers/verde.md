---
title: "Verde: Processing and gridding spatial data using Green's functions"
date: 2018-10-11
author: uieda
repository: fatiando/verde
journal: Journal of Open Source Software
doi: 10.21105/joss.00957
citation: "Uieda, L. (2018). Verde: Processing and gridding spatial data using Green's functions. Journal of Open Source Software, 3(30), 957. doi:10.21105/joss.00957"
alm: true
thumbnail: verde.png
layout: publication
tags: fatiando, open-source, equivalent-layer
oa: true
---

# About

This paper marks the first release of [Verde](http://www.fatiando.org/verde), a Python
library for processing and gridding spatial data. Verde is the first part of my
[refactoring the Fatiando a Terra project][/blog/future-of-fatiando] into separate
packages.

*Verde* is the foundation that I developed for my work on
[GPS interpolation][/talks/aogs2018] and
[equivalent layer methods][/papers/paper-polynomial-eqlayer-2013] in general.

The peer-review at JOSS is open and can be found at
[openjournals/joss-reviews#957](https://github.com/openjournals/joss-reviews/issues/957).


# Abstract

*Verde* is a Python library for gridding spatial data using different Green's functions.
It differs from the radial basis functions in `scipy.interpolate` by providing an API
inspired by scikit-learn. The *Verde* API should be familiar to scikit-learn users but
is tweaked to work with spatial data, which has Cartesian or geographic coordinates and
multiple data components instead of an `X` feature matrix and `y` label vector. The
library also includes more specialized Green's functions, utilities for trend estimation
and data decimation (which are often required prior to gridding), and more. Some of
these interpolation and data processing methods already exist in the Generic Mapping
Tools (GMT), a command-line program popular in the Earth Sciences. However, there are no
model selection tools in GMT and it can be difficult to separate parts of the processing
that are done internally by its modules. *Verde* is designed to be modular, easily
extended, and integrated into the scientific Python ecosystem. It can be used to
implement new interpolation methods by subclassing the `verde.base.BaseGridder` class,
requiring only the implementation of the new Green's function. For example, it is
currently being used to develop a method for interpolation of 3-component GPS data.
