---
title: "Pooch: A friend to fetch your data files"
date: 2020-01-17
author: uieda, santiago, remi, hugo, mattturk, shapero, anderson, leeman
repository: fatiando/pooch
journal: Journal of Open Source Software
doi: 10.21105/joss.01943
citation: "Uieda, L., Soler, S.R., Rampin, R., van Kemenade, H., Turk, M., Shapero, D., Banihirwe, A., and Leeman, J. (2020). Pooch: A friend to fetch your data files. Journal of Open Source Software, 5(45), 1943. doi:10.21105/joss.01943"
alm: true
thumbnail: pooch.png
layout: publication
tags: fatiando, open-source
oa: true
---

# About

This paper marks the release of [Pooch](http://www.fatiando.org/pooch) v0.7.1,
a Python library for downloading and managing data files.
Pooch is a part of the new ecosystem of packages in
[Fatiando a Terra](https://www.fatiando.org).
It's used by most of the other packages to manage the sample data files used
for testing and documentation.

Pooch was first introduced in [this blog post from 2018][/blog/introducing-pooch].

The peer-review at JOSS is open and can be found at
[openjournals/joss-reviews#1943](https://github.com/openjournals/joss-reviews/issues/1943).

# Abstract

Scientific software is usually created to acquire, analyze, model, and
visualize data. As such, many software libraries include sample datasets in
their distributions for use in documentation, tests, benchmarks, and workshops.
A common approach is to include smaller datasets in the GitHub repository
directly and package them with the source and binary distributions (e.g.,
scikit-learn and scikit-image do this). As data files increase in size, it
becomes unfeasible to store them in GitHub repositories. Thus, larger datasets
require writing code to download the files from a remote server to the user's
computer. The same problem is faced by scientists using version control to
manage their research projects. While downloading a data file over HTTPS can be
done easily with modern Python libraries, it is not trivial to manage a set of
files, keep them updated, and check for corruption. For example, scikit-learn,
Cartopy, and PyVista all include code dedicated to this particular task.
Instead of scientists and library authors recreating the same code, it would be
best to have a minimalistic and easy to set up tool for fetching and
maintaining data files.

Pooch is a Python library that fills this gap. It manages a data *registry*
(containing file names, SHA-256 cryptographic hashes, and download URLs) by
downloading files from one or more remote servers and storing them in a local
data cache. Pooch is written in pure Python and has minimal dependencies. It
can be easily installed from the Python Package Index (PyPI) and conda-forge on
a wide range of Python versions: 2.7 (up to Pooch 0.6.0) and from 3.5 to 3.8.
