---
title: "The future of Fatiando a Terra"
date: 2018-03-25
---

I started developing the [Fatiando a Terra](http://www.fatiando.org) Python
library in 2010.
Since then, many other open-source Python libraries for geophysics have
appeared, each with unique capabilities.
In this post, I'll explore where I think Fatiando fits in this larger
ecosystem and how we can better fill our niche.


## What is Fatiando a Terra?

*Fatiando* is a Python library for modeling and inversion in geophysics.
It's composed of different *subpackages*:

* `fatiando.gridder`: functions for dealing with spatial data. It's mostly used
  to generate point scatters or coordinate arrays for regular grids. Both are
  required as inputs for modeling or creating synthetic datasets.
* `fatiando.mesher`: classes that represent geometric objects (polygons,
  prisms, spheres, etc) and regular meshes. These
  classes are used to define the geometry and physical properties of our
  models. They are often the inputs for gravity and magnetic modeling
  functions.
* `fatiando.vis`: utilities for plotting data using matplotlib and 3D models
  using Mayavi. Mostly deprecated but there is a lot of useful code for
  displaying `fatiando.mesher` elements in Mayavi.
* `fatiando.inversion`: classes for solving inverse problems. The idea is that
  the user needs only to implement the forward problem (the forward function
  and the Jacobian matrix) and the classes take care of the rest. Ideally, this
  would form the basis for all inversions in Fatiando.
* `fatiando.datasets`: functions for loading data from common file formats and
  loading sample datasets packaged with Fatiando.
* `fatiando.seismic`: functions and classes for modeling seismic data and some
  basic inversions. Mostly toy problems.
* `fatiando.geothermal`: geothermal modeling functions. Has a single module for
  modeling how temperature perturbations at the surface propagate down into the
  Earth.
* `fatiando.gravmag`: functions for gravity and magnetic processing, modeling,
  and inversion. By far the most developed package, though some components have
  lagged behind.


## Fatiando's niche

We set out with the goal of modeling the whole Earth using all geophysical
methods.
Humble, right?
Turns out this is extremely hard and way beyond what a couple of grad students
can do in a couple of years.
Back then, there were very few Python geophysical modeling libraries.
A decade later, the ecosystem has expanded.
The five currently on going projects of which I'm aware are (let me
know in the comments if I missed any):

* [PyGMI](https://github.com/Patrick-Cole/pygmi): GUI + library for 3D modeling
  of gravity and magnetic data.
* [SimPEG](http://simpeg.xyz/): Forward modeling and inversion library based on
  the finite volume method.
* [pyGIMLi](https://www.pygimli.org/): Forward modeling and inversion library
  based on the finite element and finite volume methods.
* [Bruges](https://github.com/agile-geoscience/bruges): Modeling and processing
  for seismic and petrophysics.
* [Pyrocko](https://pyrocko.org): A collection of tools and libraries, mostly
  for seismology.

The two projects that are most similar to us (SimPEG and pyGIMLi) implement
flexible
[partial differential equation](https://en.wikipedia.org/wiki/Partial_differential_equation)
solvers that they use to run all forward modeling calculations.
This makes a lot of sense because it gives them a unified framework to model
most geophysical methods.
It is the most sensible approach to build joint inversions of multiple
geophysical datasets.
However, there are some inverse problems that don't fit this paradigm, like
[inverting Moho relief from gravity data](/publications)
and some [non-conventional inversion algorithms](/publications)
(see the animation below).

<div class="ratio ratio-16x9 mb-3">
<iframe src="https://widgets.figshare.com/articles/91469/embed?show_title=0" frameborder="0"></iframe>
</div>

It's no coincidence that Fatiando mostly contains the tools needed to implement
this type of inverse problem (i.e., analytical solutions for the gravity and
magnetic fields of geometric objects).
This is precisely the type of research that we do at the
[PINGA lab](http://www.pinga-lab.org/).
We also develop processing methods for gravity and magnetics.

The niche I see for Fatiando is in gravity and magnetic methods, particularly
using these analytical solutions.
The processing functions are an important feature because there are hardly any
open-source alternatives out there to commercial software like
[Oasis Montaj](http://www.geosoft.com/)
and [Intrepid](https://www.intrepid-geophysics.com/).


## The current state

Fatiando has grown over the years as I slowly learned how to develop and
maintain an open-source Python project.
As a result, the codebase is littered with the bad choices that I made along
the way.
The most urgent problems that need to be fixed are:

* **Python 3 support.** It's no longer a huge sacrifice to make the switch
  because all of our dependencies are supported. Actually, some of them [don't
  even support Python 2 anymore](https://python3statement.org/). Support both
  versions is a bit of a pain and it's not worth it. The [conda
  environments](https://conda.io/docs/using/envs.html) also make using multiple
  versions of Python easy. We should just migrate to Python 3 only and be done
  with it.
* **Test coverage is sparse and a lot of code is not maintained.**
  There is a lot of old code in Fatiando that was included before I learned how
  to write good tests. As a result, they have little to no tests and are
  largely unused. They might be broken right now and I would have no way of
  knowing.
  We should only include code that we are willing to use and maintain.
* **Too many "toy problems".** Mostly in the seismic package. They are
  useful for teaching and I don't think we need to delete all of it. But we
  have to be careful how we advertise these features. They shouldn't be
  packaged with well-tested and robust production code.
* **A single package.** The meshing, inversion, and gridding code is not really
  dependent on the rest of Fatiando. There is no reason why they can't be
  standalone projects. This modularity might help lower the barrier for other
  projects to use them. Installing can still be easy by using `fatiando` as a
  metapackage (like Jupyter).


## A way forward

The best way forward for Fatiando that I can see, is to become an ecosystem of
specialized tools and libraries, rather than a single Python package.
Having things in separate libraries allows us to better indicate what is robust
and professional and what is experimental or meant as a teaching tool.
In particular, the meshing library has some overlap with
[discretize](https://github.com/simpeg/discretize) and we should be considering
a merger of our projects.
Separating what we have in a library will help us articulate the
requirements of Fatiando so that we can see if a merger is beneficial.
We can also include experimental libraries (like `fatiando.seismic.wavefd`) and
CLI or GUI programs as independent projects.

This is how I envision the Fatiando ecosystem in the future (I have already
started working on some of these projects):

* `fatiando`: A metapackage that can be used to install all the whole stack
  (like the `jupyter` package).
* `deeplook`: the inversion package. Should define a scikit-learn like
  interface and provide all of the standard tools (regularization,
  optimization, etc).
* `geometric`: the geometric objects and meshes. Includes an optional way of
  plotting them on Mayavi and matplotlib. The way physical properties are
  handled needs to be redesigned and meshes need to support slicing and fancy
  indexing.
* `verde`: the gridding package. It will include some new Green's functions based
  interpolation on which I've been working. Should also include the functions
  for calculating derivatives that are currently in `fatiando.gravmag.transform`.
* `harmonica`: the gravity and magnetic methods package. Will port over most of
  the code from `fatiando.gravmag`.
* `sismica`: a package for seismics and seismology. For now, will include some
  of the toy examples from the `fatiando.seismic`.
* `wavefd`: the experimental 2D FD wave propagation code (useful for teaching
  but I don't trust it enough for research).
* `moulder`: GUI for 2D gravity and magnetic modeling.

All of these packages will be tied together in the
[`fatiando` GitHub organization](https://github.com/fatiando/)
and the [fatiando.org](http://www.fatiando.org/) website, which will include
instructions for installing the entire stack.
The website will also link to individual packages (as is done right now for the
subpackages) and any other project in the `fatiando` umbrella.
Members of the organization will be free to create new repositories and we'll
provide a template for doing so.

The requirements and goals for these new packages are:

* All code will be Python 3 only.
* All docstrings will use the numpy style.
* Each package will have it's own docs page with tutorials,
  API reference, install instructions, changelog, and gallery. They will share
  a common template and a simple theme.
* All repos will include a Code of Conduct and Contributing Guide.
* All main packages will have a comprehensive test suite. Anything not tested
  or experimental will be moved to separate packages. Full test coverage (or as
  much as possible) will be a requirement for merging a contribution.

This is how I think we could implement this:

1. Release Fatiando 0.6 with what we currently have in the *master* branch
   along with a note that this will be the last release to support Python 2.7.
2. Create a package template repository with the shared infrastructure
   (`setup.py`, docs, continuous integration configuration, `Makefile`,
   testing, etc).
3. Start repositories for each of the packages listed above.
4. Specify clear goals for each package and an example of how we want the
   API to look.
5. Focus on redesigning the inversion package first. This is the basis for many
   other packages.
6. Slowly copy over code from `fatiando/fatiando` while ensuring that
   everything is tested and documented.


## Help!

The goal of all these changes is to make *Fatiando* better for users and
developers by making the code more robust and well documented.
I'm curious to know what the Python geophysics community thinks about all of
this.
Do I have it all wrong?
What should be done differently?
And most importantly, **would you like to help?**
