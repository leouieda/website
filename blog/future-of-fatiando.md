---
title: "The future of Fatiando a Terra"
date: 2018-03-24
thumbnail: fatiando.png
layout: post
---

I started developing the [Fatiando a Terra][/software/fatiando] Python library
in 2010.
Since then, many other open-source Python libraries for geophysics have
surfaced with unique capabilities and some overlap.
In this post, I'll explore where I think Fatiando fits in this larger
ecosystem, how we can better fill our niche, and possible ways to start
integrating the existing libraries.


# What is Fatiando a Terra

*Fatiando* is a Python library for modeling and inversion in geophysics.
It's composed of different *subpackages* for handling specific tasks:

* `fatiando.gridder`: functions for dealing with spatial data. It's mostly used
  to generate point scatters or coordinates for regular grids. Both are
  required as inputs for modeling or creating synthetic datasets.
* `fatiando.mesher`: classes that represent geometric objects (polygons,
  prisms, spheres, etc) and regular meshes of some of these objects. These
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
* `fatiando.datasets`: functions for loading data from common file formats or
  loading datasets packaged with Fatiando.
* `fatiando.seismic`: functions and classes for modeling seismic data and some
  basic inversions. Mostly toy problems.
* `fatiando.geothermal`: geothermal modeling functions. Has a single module for
  modeling how temperature perturbations at the surface propagate down into the
  Earth.
* `fatiando.gravmag`: functions for gravity and magnetic processing, modeling,
  and inversion. By far the most developed package, though some components lag
  behind.


# Fatiando's niche

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
flexible [partial differential equation](https://en.wikipedia.org/wiki/Partial_differential_equation)
solver libraries.
This makes a lot of sense because it gives them a unified framework to model
all geophysical phenomena (which what we set out to do initially).
But, there are some inverse problems that just don't fit this paradigm, like
[inverting relief from gravity data][/papers/paper-moho-inversion-tesseroids-2016]
and [non-conventional inversion algorithms][/papers/paper-planting-anomalous-densities-2012]
(see the animation below).

<div class="embed-responsive embed-responsive-16by9">
<iframe src="http://wl.figshare.com/articles/91469/embed?show_title=0"
width="568" height="481" frameborder="0"></iframe>
</div>

It's no coincidence that Fatiando implements mostly analytical solutions for
the gravity and magnetic fields of geometric objects (prisms, polygonal
prisms, spheres, ellipsoids).
This is precisely the type of research that we do at the [PINGA
lab](http://www.pinga-lab.org/).
We also implement several processing methods for gravity and magnetics.

The niche I see for Fatiando is in gravity and magnetic methods, particularly
in these analytical solutions.
The processing functions are an important feature because there are hardly any
open-source alternatives out there.


# The current state

Fatiando has grown over the years as I learned how to develop and maintain a
Python project.
As a result, I made some bad choices in the beginning that are still haunting
the codebase.
The main problems that need to be fixed in the code are:

* **Python 3 support.** It's no longer a huge sacrifice to make the switch
  because all of our dependencies are supported. Actually, some of them [don't
  even support Python 2 anymore](https://python3statement.org/). Support both
  versions is a bit of a pain and it's not worth it. We should just migrate to
  Python 3 only and be done with it.
* **Test coverage is sparse and a lot of code is not maintained.**
  There is a lot of old code in Fatiando that was included before I learned how
  to write good tests. As a result, they have no tests and are largely unused.
  They might be broken right now and I would have no way of knowing.
  We should only include code we are willing to use and maintain.
* **Too many "toy problems".** This is most of the seismic package. They are
  useful for teaching and I don't think we need to delete all of it. But we
  have to be careful how we advertise these features. They shouldn't be
  packaged with well-tested and robust production code.
* **A single package.** The meshing, inversion, and gridding code is not really
  dependent on the rest of Fatiando. There is no reason why they can't be
  standalone projects. This modularity might help lower the barrier for other
  projects to adopt them. Installing can still be easy by using `fatiando` as a
  metapackage (like Jupyter).



# A way forward

Having things in separate libraries allows us to better indicate what is robust
and professional and what is experimental or meant as a toy problem.

The experimental stuff should be in it's own library with a lot of warnings,
like wavefd.

The release cycle for each library is independent.


Separating the mesh, grid, and inversion packages lowers the barrier for other
libraries to adopt them.

We can't know how to reuse things if we don't understand what each library
needs.

Having these libraries will start a conversation and help us articulate the
requirements of Fatiando so that we can think of merging with something like
discretize.

We can also include experimental libraries and CLI or GUI programs.
This is being done already for Moulder.

This is what I envision the Fatiando ecosystem of packages in the future:

* `fatiando`: A metapackage that can be used to install all the whole stack
  (like the `jupyter` package).
* `deeplook`: the inversion package. Scikit-learn like interface.
* `geometric`: the geometric objects and meshed. Includes a way of plotting
  them on Mayavi and matplotlib.
* `verde`: the gridding package. Will include some new Green's functions based
  gridding that I'm working on.
* `harmonica`: the gravity and magnetic methods. They are solutions to
  Laplace's equation, or harmonic functions.
* `sismica`: the toy examples from the seismic package which have tests.
* `wavefd`: the experimental 2D FD wave propagation code (useful for teaching
  but wouldn't trust it enough for research).
* `moulder`: GUI for 2D gravmag modeling

All of these packages will be tied together in the
[`fatiando` Github organization](https://github.com/fatiando/)
and the [fatiando.org](http://www.fatiando.org/) website.
Members of the organization will be free to create new packages  anyone wants to include a new package, they can.


* All code will be Python 3 only.
* The `fatiando/fatiando` repository with the metapackage and main website
  sources. Each new release of `fatiando` will pin specific versions of each
  package that are tested together (or the minimum version that works).
  The website will include instructions for installing the entire stack.
* The main website will link to individual packages (as is done right now for
  the subpackages) and any other project in the `fatiando` umbrela.
* Each package will have it's own docs page with tutorials,
  API reference, install instructions, changelog, and gallery. They will share
  a common template and theme.
* All repos will include a COC and contributing guide.
* All main packages will have a comprehensive test suite. Anything not tested
  or experimental will be moved to separate packages. Full test coverage (or as
  much as possible) will be a requirement for merging a contribution.
* The geothermal and seismic.wavefd packages will be marked as experimental
  and separated into their own repositories. They can still be used but
  shouldn't be packaged with well tested and robust code.
* The 2D visualization code will be removed or moved into it's own package
  (mostly the seismic plotting functions).
* The 3D visualization code (Mayavi) will be included in the mesher package.



The convolution and lame will be moved to bruges.

This is how I'm planning to implement this.

1. Release Fatiando 0.6 with what we currently have in master.
2. Start repositories with the basic infratructure (testing, CI, docs) for each
   package.
3. Slowly copy over code from `fatiando/fatiando` ensuring
