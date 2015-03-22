title: Using Fatiando a Terra to solve inverse problems in geophysics
author: Uieda, L., V. C. Oliveira Jr and V. C. F. Barbosa
date: 01-07-2014
repository: leouieda/scipy2014
type: poster
poster: 10.6084/m9.figshare.1089987
event: Python in Science Conference
slug: scipy2014
thumbnail: images/scipy2014hashtag.gif

## Poster

![The poster]({filename}/images/poster-scipy2014.png)

## Abstract

Inverse problems haunt the nightmares of geophysics graduate students.
I'll demonstrate how to conquer them using Fatiando a Terra.
The new machinery in Fatiando
contains many ready-to-use components
and automates as much of the process as possible.
You can go from zero to regularized gravity inversion
with as little as 30 lines of code.
I'll walk through an example to show you how.

The inner properties of the Earth
can usually only be inferred
through indirect measurements of their effects.
For example,
density variations
cause disturbances in the gravity field
and seismic velocity variations
affect the path of seismic waves.
From a mathematical point of view,
this inference is an inverse problem.
To complicate things, geophysical inverse problems are usually ill-posed,
meaning that a solution:

* doesn't exist;
* exists but is non-unique;
* exists and is unique but is unstable;

These problems can usually be resolved
through least-squares estimation and regularization.

Research in geophysical inverse problems
involves the development of:
new methodologies for parametrization,
different approaches to regularization,
new algorithms to handle large-scale problems,
combinations of existing methods,
etc.
All of the aforementioned developments
require the creation of software,
usually from scratch.
Furthermore,
most scientific software
are not designed with reuse in mind,
making remixing published methods difficult,
if not impossible.

We tackled these problems
by developing `fatiando.inversion`,
a framework for solving inverse problems
in [Fatiando a Terra](http://www.fatiando.org).
The goals of `fatiando.inversion` are:

* Enable writing code that
  intuitively maps to the theory (equations);
* Provide a consistent interface for all solvers
  (similar to that adopted by [scikit-learn](http://scikit-learn.org/));
* Automate the process of implementing a new inverse problem;
* Allow reuse and remixing with as little code as possible;

In this talk,
I'll briefly cover
the mathematics involved
and the design of our new API.
I'll walk through the process of
implementing a new inverse problem
(in about 30 lines of code)
using the example of
estimating the relief of a sedimentary basin
from its gravity anomaly.
Finally,
I'll conclude by outlining
how we are using this framework in our own research,
what we are currently working on,
and our plans for the future.
