---
title: Research
layout: page
order: date
banner: pacific-bathymetry.jpg
banner_description: "Bathymetry of the Pacific Ocean around the Hawaiian islands."
---

{% from "utils.html" import make_index, make_tags %}

# Summary

My main research focus is
the development of methods
to solve inverse problems,
mainly for potential fields.
Central to all of my projects
is the open-source software
that implements the new methods.

Method development.


# Gravity and magnetic inverse problems

As a geophysicist,
my ultimate goal is
to infer knowledge about the inner Earth
and its processes
from surface observations,
such as its gravity and magnetic fields,
topography,
or propagation patterns of seismic waves.
%
Ubiquitous to all of geophysics
is the fact that this inference
is an ill-posed inverse problem,
to which a solution might not exist
or be non-unique and unstable.

<div>
    {{ make_tags(["inversion", "gravity", "magnetic", "euler-deconvolution"], icon=true) }}
    {{ make_index(site.reflinks["/tag/inversion"].content[:4], site, hr=false, date=false) }}
</div>


# Processing using equivalent layers


<div>
    {{ make_tags(["equivalent-layer"], icon=true) }}
    {{ make_index(site.reflinks["/tag/equivalent-layer"].content[:4], site, hr=false, date=false) }}
</div>


# Forward modeling


<div>
    {{ make_tags(["tesseroids"], icon=true) }}
    {{ make_index(site.reflinks["/tag/tesseroids"].content[:4], site, hr=false, date=false) }}
</div>


# Open-source software

Methodological development requires
much prototyping and iteration.

Thus,
a researcher needs
a flexible environment
and a large collection of tools
for experimentation.
The approach I have taken is
to develop an open-source library
called Fatiando a Terra\footnote{\url{http://www.fatiando.org}}
that collects the basic tools
required for building an inversion method.
The library is implemented in Python,
a dynamically typed interpreted language
known for its simplicity
and large ecosystem of scientific libraries.
Fatiando is developed in the
open\footnote{\url{https://github.com/fatiando/fatiando}}
with the help of a growing, though yet small,
developer community.
I use it as the basis for
all of my research projects
as well as for teaching geophysics.
My first open-source project
was \textit{Tesseroids}\footnote{\url{http://tesseroids.leouieda.com/}},
a collection of command-line programs
for forward modeling gravitational fields
using spherical prisms.
It is written entirely in C
and is my most widely used software project to date.

<div>
    {{ make_tags(["open-source"], icon=true) }}
    {{ make_index(site.reflinks["/tag/open-source"].content[:4], site, hr=false, date=false) }}
</div>
