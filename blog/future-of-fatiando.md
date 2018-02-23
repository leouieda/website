---
title: "The future of Fatiando a Terra"
date: 2018-02-07
thumbnail: fatiando.png
layout: post
---

The [Fatiando a Terra][/software/fatiando] Python library has been in
development since 2010.
Since then, many other open-source Python libraries for geophysics have
surfaced with unique capabilities and some overlap.
In this post, I'll explore where I think Fatiando fits in this larger
ecosystem, how we can minimize repetition, and how to better integrate the
existing libraries.

# Fatiando's niche

We set out with the goal of modeling the whole Earth using all geophysical
methods.
Humble, right?
Turns out this is extremely hard and way beyond what a couple of grad students
can do in a couple of years.

Back then, there were very few Python geophysical modeling libraries.
A decade later, the ecosystem has expanded.
The four currently on going projects of which I'm aware are (let me
know in the comments if I missed any):

* [PyGMI](https://github.com/Patrick-Cole/pygmi): GUI + library for 3D modeling
  of gravity and magnetic data.
* [SimPEG](http://simpeg.xyz/): Forward modeling and inversion library based on
  the finite volume method.
* [pyGIMLi](https://www.pygimli.org/): Forward modeling and inversion library
  based on the finite element and finite volume methods.
* Bruges
* [Fatiando a Terra](http://www.fatiando.org): Forward modeling, inversion, and
  data processing library. Based mostly on analytical (non-PDE) solutions.


# A way forward


Need Python 3.

Too much untested and unmaintained code. Only include code we are willing to
use and maintain.

Too many "toy problems". They can be there but we have to be careful how we
advertise them.

Too tightly integrated. The meshing, inversion, and gridding code is not really
dependent on the rest of Fatiando. So why not be standalone.

Too loosely integrated. There is not really any communication between the
methods.
The way we envisioned things bound together through the mesh was short-sighted
and doesn't apply to our kind of forward modeling.
It works well for SimPEG and pyGIMli because their forward modeling is highly
standardized across methods.
It's all PDEs.
This is great but it imposes more restrictions on the kind of problem that can
be solved.
Fatiando and our research group always focused more on analytical solutions to
geometrical shapes.
This allows us to have something like the bolachinha inversion and the planting
inversion.
Not possible with PDEs.

So if the methods don't really share this underlying methodology, do they need
to be in the same library?

By far the most developed is gravity and magnetics.

The seismic code is very experimental or just toy problems.

It shouldn't be packaged with the more well tested and robust gravmag stuff.

We want to inspire trust in our code so we should be careful of what makes it
in to the main library.

There is already a paper showing that our prism forward modeling is more
accurate than commercial software.

Having things in separate libraries allows us to better indicate what is robust
and professional and what is experimental or meant as a toy problem.

The experimental stuff should be in it's own library with a lot of warnings,
like wavefd.

The release cycle for each library is independent.

Installing can still be easy using a `fatiando` metapackage (like Jupyter) and
dependencies.

Separating the mesh, grid, and inversion packages lowers the barrier for other
libraries to adopt them.

We can't know how to reuse things if we don't understand what each library
needs.

Having these libraries will start a conversation and help us articulate the
requirements of Fatiando so that we can think of merging with something like
discretize.

We can also include experimental libraries and CLI or GUI programs.
This is being done already for Moulder.


## The plan

What it will look like.

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
* All code will be Python 3 only.

The packages that will make up the Fatiando ecosystem:

* `fatiando`: the metapackage that ties it all together. Not importable.
* `deeplook`: the inversion package. Scikit-learn like interface.
* `verde`: the gridding package. Will include some new Green's functions based
  gridding that I'm working on.
* `geometric`: the geometric objects and meshed. Includes a way of plotting
  them on Mayavi and matplotlib.
* `harmonica`: the gravity and magnetic methods. They are solutions to
  Laplace's equation, or harmonic functions.
* `sismica`: the toy examples from the seismic package which have tests.
* `wavefd`: the experimental 2D FD wave propagation code (useful for teaching
  but wouldn't trust it enough for research).
* `moulder`: GUI for 2D gravmag modeling

If anyone wants to include a new package, they can.


The convolution and lame will be moved to bruges.

This is how I'm planning to implement this.

1. Release Fatiando 0.6 with what we currently have in master.
2. Start repositories with the basic infratructure (testing, CI, docs) for each
   package.
3. Slowly copy over code from `fatiando/fatiando` ensuring
