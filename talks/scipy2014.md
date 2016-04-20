---
title: Using Fatiando a Terra to solve inverse problems in geophysics
author: uieda, oliveira-jr, barbosa
date: 2014-07-01
repository: leouieda/scipy2014
presentation: poster
poster: 10.6084/m9.figshare.1089987
doi: 10.6084/m9.figshare.1089987
event: Python in Science Conference
thumbnail: scipy2014.png
alm: true
layout: publication
---

# Poster

![The poster](/images/poster-scipy2014.png)

# Abstract

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

# Bonus

As a bonus, I made this gif for the Twitter hashtag
[#scipy2014](https://twitter.com/hashtag/SciPy2014?src=hash):

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p
lang="en" dir="ltr">.<a href="https://twitter.com/kwinkunks">@kwinkunks</a> <a
href="https://twitter.com/AdventureMomo">@AdventureMomo</a> <a
href="https://twitter.com/_row1">@_row1</a> how about this? (code is here <a
href="https://t.co/9T3J27p0CG">https://t.co/9T3J27p0CG</a>) <a
href="https://twitter.com/hashtag/scipy2014?src=hash">#scipy2014</a> <a
href="http://t.co/5ryXw0L66X">pic.twitter.com/5ryXw0L66X</a></p>&mdash;
Leonardo Uieda (@leouieda) <a
href="https://twitter.com/leouieda/status/486917338092929024">July 9,
2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[![#scipy!](/images/scipy2014hashtag.gif)](https://twitter.com/leouieda/status/486917338092929024)
