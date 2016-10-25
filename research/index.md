---
title: Research Interests
order: date
layout: page
---

As a geophysicist,
my ultimate goal is
to infer knowledge about the inner Earth
and its processes
from surface observations,
such as its gravity and magnetic fields.
Ubiquitous to all of geophysics
is the fact that this inference
is an ill-posed inverse problem,
to which a solution might not exist
or be non-unique and unstable.

My main research focus is
the development of methods
to solve inverse problems,
mainly for potential fields.
Central to all of my projects
is the open-source software
that implements the new methods.


<h2>Software development</h2>
<hr>

<div class="row">

<div class="col-md-4 col-sm-5 col-xs-6">
    <img title="Screenshot of some source code" src="/images/research-code-example.png" class="img-responsive">
</div>

<div class="col-md-8 col-sm-7 col-xs-6">

Methodological development requires
much prototyping and iteration.
Thus,
a researcher needs
a flexible environment
and a large collection of tools
for experimentation.

The approach I have taken is
to develop an open-source library
called Fatiando a Terra
that collects the basic tools
required for building an inversion method.
The library is implemented in Python,
a dynamically typed interpreted language
known for its simplicity
and large ecosystem of scientific libraries.
Fatiando is developed in the
open
with the help of a growing, though yet small,
developer community.
I use it as the basis for
all of my research projects
as well as for teaching geophysics.

My first open-source project
was Tesseroids,
a collection of command-line programs
for forward modeling gravitational fields
using spherical prisms.
It is written entirely in C
and is my most widely used software project to date.

</div>
</div> <!--Row-->


<h2>Inverse problems</h2>
<hr>

<div class="row">

<div class="col-md-8 col-sm-7 col-xs-6">

During my graduate studies,
I have developed two novel inversion methods
for gravity data.
The first is a 3D gravity gradient inversion
using a heuristic algorithm
that grows the solution from starting seeds.
The method is computationally efficient
and can handle problems with millions of unknowns
on a mid-range laptop computer.

The second method inverts gravity data
to estimate the relief
of the crust-mantle boundary
using a spherical approximation for the Earth.

A common theme of my research has been
to use, adapt, and improve upon
highly efficient algorithms
to solve the problems of geophysical inversion.

</div>

<div class="col-md-4 col-sm-5 col-xs-6">
    <img title="Example image of an inversion result" src="/images/research-inversion-example.png" class="img-responsive">
</div>

</div> <!--Row-->


<h2>Reproducible research</h2>
<hr>

<div class="row">

<div class="col-md-4 col-sm-5 col-xs-6">
    <img title="Screenshot of some source code" src="/images/research-code-example.png" class="img-responsive">
</div>

<div class="col-md-8 col-sm-7 col-xs-6">

Computational experiments
are difficult, if not impossible, to reproduce
without access to the code used to generate them.
I attempt to tackle
some of these issues
on my own research
by making all source-code and data
(as much as legally possible)
from my own publications
available in public repositories.
I hope to train my students
in these practices from the start
and provide guidance for others to do the same.
Though I cannot claim
to generate fully reproducible results,
I have been refining this process over time
and hope that my efforts will contribute
to advance the reproducibility of our science.

</div>
</div> <!--Row-->
