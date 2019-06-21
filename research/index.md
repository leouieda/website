---
title: Research
layout: page
order: date
banner: pacific-bathymetry.jpg
banner_description: "Bathymetry of the Pacific Ocean around the Hawaiian islands."
---

{% from "utils.html" import make_index, make_tags, make_tag, fa %}

My main topic of research is the development of methods to solve
[inverse problems in geophysics](https://en.wikipedia.org/wiki/Inverse_problem).
For example, estimating
[density anomalies in the subsurface from measured disturbances in gravity][/papers/paper-planting-anomalous-densities-2012]
or the [direction of magnetization of a buried structure from the anomalies that it produces in the Earth's magnetic field][/papers/paper-mag-dir-2015].
Most methods that I develop are related to gravity and magnetics
but I'm also interested in [seismology][/papers/nmo-tutorial] and
[geodesy][/talks/aogs2018].
Central to all of my projects is the open-source software upon which I
implement the new methods.

I have an **open by default** policy for my research and teaching output.
Pretty much everything I do is freely available online, usually on
[Github](https://github.com/leouieda/).

# Grants

These are funded research projects in which I participate as PI or co-PI:

<div class="research-index">
    {{ make_index(site.reflinks["/research"].content[:4], site, hr=false, date=false) }}
</div>


# Research Themes

## Inverse problems

As a geophysicist, my ultimate goal is to infer the physical properties of the
inner Earth and its processes from surface observations.
This is an ill-posed inverse problem, to which a solution might not exist or be
non-unique and unstable.
I develop methods for solving different kinds of inverse problems using
several sets of constraints to overcome the instability of the solution.

<div class="research-index">
    {{ make_tags(["inversion", "gravity", "magnetic", "euler-deconvolution"], icon=true) }}
    {{ make_index(site.reflinks["/tag/inversion"].content[:4], site, hr=false, date=false) }}
</div>


## Forward modeling

A key component for solving an inverse problem is first solve the "forward
problem".
This is jargon for predicting data given a set of model parameters.
One of the first research problems on which I worked was developing a method
for forward modeling gravitational fields caused by
[a tesseroid](https://doi.org/10.6084/m9.figshare.1495521) (a spherical prism).
I'm still doing work related to this theme.

<div class="research-index">
    {{ make_tags(["forward-modeling", "tesseroids"], icon=true) }}
    {{ make_index(site.reflinks["/tag/forward-modeling"].content[:4], site, hr=false, date=false) }}
</div>


## Data processing

There is no turning back from the machine learning frenzy that has taken over
the world.
Geoscientists have been doing similar things for decades but with different
names and objectives.
One of these things is called the
"[equivalent layer technique][/papers/paper-polynomial-eqlayer-2013]"
in gravity and magnetics.
Similar methods in different fields have many different names, for example
[radial basis functions](https://en.wikipedia.org/wiki/Radial_basis_function)
or [Green's functions interpolation](https://doi.org/10.1002/2016GL070340).
All of these methods are linear regressions in which we fit a linear model to
some data and then use the model to predict new data.
The difference with standard machine learning is that the linear model we use
has physical meaning.
For gravity data, the model is the gravitational attraction of point sources,
whereas for GPS data, the model is the elastic deformation of medium.
Given the many similarities, I have been very interested in applying other
machine learning techniques, like model selection, to these geophysical
problems.

<div class="research-index">
    {{ make_tags(["equivalent-layer"], icon=true) }}
    {{ make_index(site.reflinks["/tag/equivalent-layer"].content[:4], site, hr=false, date=false) }}
</div>


# Open-source software

Programming is a requirement for method development.
By definition, there is no existing software that implements your new method.
I program mostly in [Python](https://www.python.org/) but I'm also proficient
in [C](https://en.wikipedia.org/wiki/C_(programming_language)).
All of my software contributions are
[open-source](https://en.wikipedia.org/wiki/Open-source_software)
and hosted on [Github](https://github.com/leouieda/).

<div class="research-index">
    {{ make_tags(["open-source"], icon=true) }}
    {{ make_index(site.reflinks["/tag/open-source"].content[:4], site, hr=false, date=false) }}
</div>

I'm the creator and/or maintainer of the following projects:

<div class="research-index">
</div>


## Fatiando a Terra ([www.fatiando.org](https://www.fatiando.org))

Fatiando is a Python library for modeling and inversion in geophysics.
The name is Portuguese for "*slicing the Earth*" (like a loaf of bread).
I started development of Fatiando in 2010 while working on my
[Masters degree][/about/masters].
I now use it regularly for my research and also for much of my teaching
material.
My [Geophysics classes at UERJ][/teaching] used Fatiando and [Jupyter
notebooks](http://jupyter.org/) to provide students with interactive examples
and synthetic data.
Most recent papers published by the [PINGA lab](http://www.pinga-lab.org) use
it in some way.
Fatiando was featured in the
[89th Boletim SBGf (PDF in Portuguese)](/pdf/boletim-sbgf-fatiando-89-2014.pdf).

In 2018, I started work to [convert Fatiando into several independent
packages][/blog/future-of-fatiando]:

* [Verde](https://www.fatiando.org/verde/): The first one I started working on. A
  library for gridding and spatial data processing.
* [Pooch](https://www.fatiando.org/pooch/): A small Python library that manages the
  download and caching of sample data sets. It will be used in support of the other
  packages.
* [RockHound](https://www.fatiando.org/rockhound/): Download common geophysical models
  and datasets (think PREM, CRUST1.0, ETOPO1) and load them into Python data structures.
* [Harmonica](https://www.fatiando.org/harmonica/dev/): Library for processing and
  modeling gravity and magnetic data.

<div class="research-index">
    {{ make_tags(["fatiando"], icon=true) }}
    {{ make_index(site.reflinks["/tag/fatiando"].content[:4], site, hr=false, date=false) }}
</div>

## Tesseroids  ([www.tesseroids.org](http://www.tesseroids.org))

Command-line programs for gravity forward modeling. This was my first software
project. I started working on *Tesseroids* in 2008 for my [Bachelor's thesis
project][/about/bachelors] and continued in collaboration with Professor [Carla
Braitenberg](https://www2.units.it/braitenberg/) from the [University of
Trieste](https://dmg.units.it/). The paper "[/papers/paper-tesseroids-2016]"
describes the algorithms behind [version
1.2.0](https://doi.org/10.5281/zenodo.16033) of the software, which ended up
becoming a chapter of my [PhD thesis][/about/phd].

<div class="research-index">
    {{ make_tags(["tesseroids"], icon=true) }}
    {{ make_index(site.reflinks["/tag/tesseroids"].content[:4], site, hr=false, date=false) }}
</div>

## PyGMT ([www.pygmt.org](https://www.pygmt.org))

A modern Python interface for the [Generic Mapping Tools](http://gmt.soest.hawaii.edu/).
I started building PyGMT (formerly GMT/Python) in 2017 as part of my
[postdoc at the University of Hawaii][/blog/hawaii-gmt-postdoc] with
[Paul Wessel](http://www.soest.hawaii.edu/wessel) (the co-creator and main developer of
GMT).
Work is still in early stages but there is a minimum working example on the
website. PyGMT was used to generate the bathymetry and topography banner
images for this website.

<div class="research-index">
    {{ make_tags(["pygmt"], icon=true) }}
    {{ make_index(site.reflinks["/tag/pygmt"].content[:4], site, hr=false, date=false) }}
</div>
