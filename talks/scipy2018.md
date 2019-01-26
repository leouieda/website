---
title: Building an object-oriented Python interface for the Generic Mapping Tools
author: uieda, pwessel
date: 2018-07-13
repository: leouieda/scipy2018
slides: 10.6084/m9.figshare.6814052
event: Python in Science Conference
thumbnail: scipy2018.png
license: CC-BY
youtube: 6wMtfZXfTRM
layout: publication
alm: true
tags: pygmt, open-source
---

{% from "utils.html" import youtube_embed %}

# About

This was the second talk I gave at Scipy about [GMT/Python](https://www.gmtpython.xyz),
a wrapper that [I'm building for the Generic Mapping Tools][/blog/hawaii-gmt-postdoc].
It showed the progress that we made in the past year, what our struggles and successes
were, and our plans for the future.

I gave a live demo using the notebook from [try.gmtpython.xyz](http://try.gmtpython.xyz)


# Video recording

Scipy records all of the presentations and [makes them available on
YouTube](https://www.youtube.com/playlist?list=PLYx7XA2nY5Gd-tNhm79CNMe_qvi35PgUR).
Here is the video of mine:

{{ youtube_embed("6wMtfZXfTRM") }}


# Slides

I made the slides in Google Drive. You can see them below:

<div class="embed-responsive embed-responsive-16by9">
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ2ULpSNf0_tHJYIrRvSdFC0e7diKm5vUiX0_eaWtBPKKBr7T_UJLB-5hKJRHGWlDW3wpe8x4EhhZVD/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>


## Short summary

We are building a Python wrapper for the Generic Mapping Tools (GMT), a set of
command-line programs used across the Earth, Atmospheric, and Ocean Sciences to
process and visualize geographic data. At Scipy 2017, we presented the project
goals and an initial prototype. The feedback received led to improvements in
the design of the library, mainly the creation of an object-oriented API. We
will present the newest developments including support for numpy arrays and
pandas Dataframes, interactive visualization in the Jupyter notebook using NASA
WorldWind, and more. Once again, we seek feedback from the community to guide
us moving forward.

## Abstract

The [GMT/Python library](http://www.gmtpython.xyz) has been in development for
approximately 1 year. Much of the current design of the library was inspired by
the [feedback that we received following our presentation at Scipy
2017](http://www.leouieda.com/blog/gmt-after-scipy2017.html). Since then, we
have been implementing this design, establishing a solid low-level API on which
to build the rest of the library, and exploring new ways to interface with the
Jupyter notebook. In this talk, we will present the current state of the
project, including: the design of the low-level wrapper for the GMT C API (the
`gmt.clib.LibGMT` class); the new object-oriented plotting API (the
`gmt.Figure` class); the support for numpy arrays and pandas Dataframes; using
GMT's built-in topography grids and sample datasets; interactive visualization
in the Jupyter notebook using the [NASA WorldWind Web Javascript
library](https://worldwind.arc.nasa.gov); and more. An online demo of these
features is available through the Binder service at http://try.gmtpython.xyz.
We will also share the lessons learned from using ctypes to build the wrapper
and the changes that were required in the C API to make the wrapping process as
smooth as possible when porting to other languages. Finally, we will layout our
development plans and solicit feedback and contributions to help guide the
future of the project.

GMT has an extensive feature set that goes well beyond data visualization. It
has sophisticated algorithms for processing and interpolating data in Cartesian
and spherical coordinates that is still unmatched in the Scipy ecosystem. GMT
is also the basis for specialized software like
[MB-System](https://www.mbari.org/products/research-software/mb-system) for
processing and visualizing bathymetry and backscatter imagery data derived from
multibeam, interferometry, and sidescan sonars and
[GMTSAR](http://topex.ucsd.edu/gmtsar) for processing Interferometric
Synthetic-Aperture Radar (InSAR) data. A well designed wrapper for the GMT C
API is the first step to bring these powerful tools to the Scipy community. The
data visualization landscape in Python has grown immensely in the past few
years with the advent of Boheh, Altair, Cartopy, Holoviews, etc. GMT/Python can
help diversify this ecosystem and bring important lessons learned during the
28+ years of continuous development of GMT.
