---
title: "Step-by-step NMO correction"
date: 2017-02-01
author: uieda
repository: pinga-lab/nmo-tutorial
journal: The Leading Edge
oa: true
alm: true
doi: 10.1190/tle36020179.1
thumbnail: nmo-tutorial.png
citation: "Uieda, L. (2017), Step-by-step NMO correction, The Leading Edge, 36(2), 179-180, doi:10.1190/tle36020179.1"
layout: publication
tags: seismic, tutorial
---


# About

*This is a part of The Leading Edge [tutorials
series](https://doi.org/10.1190/tle35020190.1).
All tutorials are open-access and include open-source code examples.*

The manuscript was written in [Authorea](https://www.authorea.com).
You can view and comment on the text
[online at Authorea](https://www.authorea.com/users/1856/articles/142722/_show_article)
and even edit it on the
[SEG Wiki](http://wiki.seg.org/wiki/Step-by-step_NMO_correction).
The final (pretty) PDF version is free to download from the publisher website
(follow the doi link).

The Jupyter notebook that accompanies the tutorial (see the source code
repository on Github) contains the full source code, along with documentation
and tests. Both figures of the tutorial are produced by the code in the
notebook.

The code and idea for this tutorial came from my [/teaching/geofisica2] course.
I came across the problem of implementing NMO correction while preparing my
lecture and practical exercises on this topic.
This is a clear example of how learning happens both ways in a classroom.


# Abstract

Open any text book about seismic data processing and you will inevitably find a
section about the normal moveout (NMO) correction.
When applied to a common midpoint (CMP) section, the correction is supposed to
turn the hyperbola associated with a reflection into a straight horizontal
line.
What most text books won't tell you is *how, exactly, do you apply this
equation to the data*?

That is what this tutorial will teach you (hopefully).

![](/images/nmo-tutorial-application.png)
