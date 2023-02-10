---
title: "Reviews of our Scipy 2017 talk proposal: Bringing the Generic Mapping Tools to Python"
date: 2017-05-11
---

This year, [Scipy is using a double-open peer-review
system](https://scipy2017.scipy.org/ehome/220975/532468/), meaning that both
authors and reviewers know each others identities.
These are the reviews that we got for
[our proposal](/blog/scipy2017-proposal-gmt.html)
and our replies/comments
(posted with permission from the reviewers).
**My sincerest thanks to all reviewers and editors for their time and effort**.

The open review model is great because it increases the transparency of the
process and
[might even result in better reviews](https://doi.org/10.1136/bmjopen-2015-008707).
I started signing my reviews a few years ago and I found that I'm more careful
with the tone of my review to make sure I don't offend anyone and provide
constructive feedback.

Now, on to the reviews!


## Review 1 - [Paul Celicourt](http://hydrounits.com/)

> The paper introduces a Python wrapper for the C-based Generic Mapping Tools
> used to process and analyze time series and gridded data. The content is well
> organized, but I encourage the authors to consider the following comments:
> While the authors promise to demonstrate an initial prototype of the wrapper,
> it is not sure that a WORKING prototype will be available by the time of the
> conference as claimed by the authors when looking at the potential
> functionalities to be implemented and presented in the second paragraph of
> the extended abstract. Furthermore, it is not clear what would be the
> functionalities of the initial prototype. On top of that, the approach to the
> implementation is not fully presented. For instance, the Simplified Wrapper
> and Interface Generator (SWIG) tool may be used to reduce the workload but
> the authors do not mention whether the wrapper would be manually developed or
> using an automated tool such as the SWIG. Finally, the portability of the
> shared memory process has not been addressed.

Thanks for all your comments, Paul! They are good questions and we should have
addressed them better in the abstract.

That is a valid concern regarding the working prototype.  We're not sure how
much of the prototype will be ready for the conference. We are sure that we'll
have *something* to show, even if it's not complete. The focus of the talk will
be on our design decisions, implementation details, and the changes in the GMT
modern execution mode on which the Python wrappers are based. We'll run some
examples of whatever we have working mostly for the "Oooh"s and "Aaah"s.

The wrapper will be manually generated using
[ctypes](http://docs.python.org/library/ctypes.html).
We chose this over [SWIG](http://www.swig.org/) or [Cython](http://cython.org/)
because ctypes allows us to write pure Python code.
It's a much simpler way of wrapping a C library.
Not having any compiled extension modules also greatly facilitates distributing
the package across operating systems.
The same wrapper code can work on Windows, OSX, and Linux (as long as the GMT
shared library is available).

The amount of C functions that we'll have to wrap is not that large.
Mainly, we need `GMT_Call_Module` to run a command (like `psxy`),
`GMT_Create_Session` for generating the session structure,
and `GMT_Open_VirtualFile` and `GMT_Read_VirtualFile` for passing data to and
from Python.
The majority of the work will be in creating the Python functions for each GMT
command, documenting them, and parsing the Python function arguments into
something that `GMT_Call_Module` accepts.
This work would have to be done manually using SWIG or Cython as well, so
ctypes is not a disadvantage with regard to this.
There are some more details about this in
[our initial design and goals](/blog/gmt-python-design.html).



## Review 2 - [Ricardo Barros Lourenço](https://github.com/ricardobarroslourenco)

> The authors submitted a clear abstract, in the sense that they will present a
> new Python library, which is a binding to the Generic Mapping Tools (GMT) C
> library, which is widely adopted by the Geosciences community. They were
> careful in detailing their reasoning in such implementation, and also in
> analogue initiatives by other groups.
>
> In terms of completeness, the abstract precisely describes that the design
> plans and some of the implementation would be detailed and explained, as well
> on a demo of their current version of the library. It was very interesting
> that the authors, while describing their implementation, also pointed that
> the library could be used in other applications not necessarily related to
> geoscientific applications, by the generation of general line plots, bar
> graphs, histograms, and 3D surfaces. It would be beneficial to the audience
> to see how this aspect is sustained, by comparing such capabilities with
> other libraries (such as Matplotlib and Seaborn) and evaluating their
> contribution to the geoscientific domain, and also on the expanded related
> areas.
>
> The abstract is highly compelling to the Earth Sciences community members at
> the event because the GMT module is already used for high-quality
> visualization (both in electronic, but also in printed outputs - maps - which
> is an important contribution to) , but with a Python integration it could
> simplify the integration of "Pythonic" workflows into it, expanding the
> possibilities in geoscientific visualization, especially in printed maps.
>
> It would be interesting, aside from a presumed comparison in online
> visualization with matplotlib and cartopy, if the authors would also discuss
> in their presentation other possible contributions, such as online tile
> generation in map servers, which is very expensive in terms of computational
> resources and is still is challenging in an exclusive "Pythonic" environment.
> Additionally, it would be interesting if the authors provide some
> clarification if there is any limitation on the usage of such library, more
> specifically to the high variance in geoscientific data sources, and also in
> how netCDF containers are consumed in their workflow (considering that these
> containers don't necessarily conform to a strict standard, allowing users to
> customize their usage) in terms of the automation of this I/O.
>
> The topic of high relevance because there is still few options for spatial
> data visualization in a "fully pythonic" environment, and none of them is
> used in the process of plotting physical maps, in a production setting, such
> as GMT is.  Considering these aspects, I recommend such proposal for
> acceptance.

Thank you, Ricardo, for your incentives and suggestions for the presentation!

I hadn't thought about the potential use in map tiling but we'll keep an eye on
that from now on and see if we have anything to say about it. Thanks!

Regarding netCDF, the idea is to leverage the
[xarray](http://xarray.pydata.org) library for I/O and use their `Dataset`
objects as input and output arguments for the grid related GMT commands.
There is also the option of giving the Python functions the file name of a grid
and have GMT handle I/O, as it already does in the command line.
The appeal of using xarray is that it integrates well with numpy and pandas and
can be used instead of `gmt grdmath` (no need to tie your head in knots over
[RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation) anymore!).


## Review 3 - [Ryan May](https://github.com/dopplershift)

> Python bindings for GMT, as demonstrated by the authors, are very much in
> demand within the geoscience community. The work lays out a clear path
> towards implementation, so it's an important opportunity for the community to
> be able offer API and interaction feedback. I feel like this talk would be
> very well received and kick off an important dialogue within the geoscience
> Python community.

Thanks, Ryan! Getting community feedback was the motivation for submitting a
talk without having anything ready to show yet.
It'll be much easier to see what the community wants and thinks before we have
fully committed to an implementation.
We're very much open and looking forward to getting a ton of questions!

<hr class="my-5">

**What would you like to see in a GMT Python library?
Let us know if there are any questions/suggestions before the conference.
See you at Scipy in July!**
