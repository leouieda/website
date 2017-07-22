---
title: "GMT/Python update and feedback from Scipy 2017"
date: 2017-07-21
thumbnail: gmt-after-scipy2017.png
layout: post
---

Last week [I presented the first working prototype][/talks/scipy2017] of
[GMT/Python][/software/gmt-python] at Scipy 2017, which is my favorite
conference.
I got a lot of excellent feedback about the project and will need to make some
major changes as a result.
Sadly, I wasn't very good at managing my time and didn't get to show the
internals of the library.
So I'll use this post to describe how things are currently implemented, what I
learned from the feedback, and what changes I'm making to the code base.

Before we dive in, you can watch my talk on Youtube or just take a quick look
at [my slides](https://docs.google.com/presentation/d/15he1klG9gCvBgGr3jGeQhTbcY5xShKv54l4BVnIxYBg/pub?start=false&loop=false&delayms=3000).

<div class="embed-responsive embed-responsive-16by9">
<iframe width="560" height="315"
src="https://www.youtube.com/embed/93M4How7R24" frameborder="0"
allowfullscreen></iframe>
</div>

# Running the code

You can try out the
[demo notebook](http://nbviewer.jupyter.org/github/GenericMappingTools/scipy2017/blob/master/demo.ipynb)
from the talk if you're on Linux or OSX
(sorry Windows users,
[we're working on it](https://github.com/conda-forge/gmt-feedstock/pull/15)).
First, you'll need to install an alpha version of GMT 6.0.0 from
[conda-forge](https://github.com/conda-forge/gmt-feedstock/):

    conda install gmt=6.0.0a5 -c conda-forge/label/dev

I should note that this only works because of
[the amazing help I got](https://github.com/conda-forge/gmt-feedstock/pull/5)
from
[Filipe Fernandes](https://github.com/ocefpaf),
[Mike Hearne](https://github.com/mhearne-usgs), and
[Ray Donnelly](https://github.com/mingwandroid) during the Scipy sprints.

Now you can install the GMT/Python version from the talk:

    pip install https://github.com/GenericMappingTools/gmt-python/archive/0e2b118.zip



# Current implementation

All our code is hosted on the
[GenericMappingTools/gmt-python](https://github.com/GenericMappingTools/gmt-python)
repository on Github.
The Python package itself is called `gmt` so that you can `import gmt`
instead of `import gmt-python` (which looks a bit silly).
The following example wasn't on the video but it shows what is currently
possible with the library:

```python
import gmt

# Start a new figure
gmt.figure()
# Plot coastlines of North America using readable aliases for the arguments
gmt.pscoast(region=[-130, -70, 24, 52], projection="B-100/35/33/45/6i",
            land='gray', frame='a', portrait=True, shorelines='thinnest',
            borders='1/thickest', area_thresh=500)
# Embed the figure in the notebook
gmt.show()
```

![](/images/gmt-after-scipy2017/sample-map.png)


Here is what the file structure of the `gmt` package looks like:

    gmt
    ├── __init__.py
    ├── clib/
    │   ├── __init__.py
    │   ├── constants.py
    │   ├── core.py
    ├── decorators.py
    ├── extra_modules.py
    ├── ps_modules.py
    ├── session_management.py
    ├── tests/
    │   ├── __init__.py
    │   ├── baseline/
    │   ├── data/
    │   ├── test_*.py
    │   └── utils.py
    └── utils.py

The subpackage `gmt.clib` contains all of the low-level `ctypes` code that
interfaces with `libgmt`.
A user will not need see or use this package.
Each [GMT module](http://gmt.soest.hawaii.edu/doc/latest/index.html)
(`pscoast`, `grdgradient`, etc) is implemented as a function in one of the
`*.py` files in the `gmt` package.
For example, the Postscript generating modules live in `gmt/ps_modules.py`.
These "module functions" are all accessible from the top-level package
namespace.
This means that you can access them as `gmt.pscoast` instead of
`gmt.ps_modules.pscoast`.

All of the unit and integration tests live in `gmt.tests` and are shipped with
the package.
Also included is a `gmt.test()` function that runs all of our tests using
[pytest](https://docs.pytest.org).
I'll go over how we run the tests below.


## Module wrapper functions

This is what a function that wraps a GMT module looks like:

```python
@fmt_docstring
@use_alias(R='region', J='projection', A='area_thresh', B='frame',
           D='resolution', P='portrait', I='rivers', N='borders',
           W='shorelines', G='land', S='water')
@kwargs_to_strings(R='sequence')
def pscoast(**kwargs):
    """
    Plot continents, shorelines, rivers, and borders on maps

    ...

    {gmt_module_docs}

    {aliases}

    Parameters
    ----------
    {J}
    {R}
    A : int, float, or str
        ``'min_area[/min_level/max_level][+ag|i|s|S][+r|l][+ppercent]'``
        Features with an area smaller than min_area in km^2 or of hierarchical
        level that is lower than min_level or higher than max_level will not be
        plotted.
    {B}
    C : str
        Set the shade, color, or pattern for lakes and river-lakes.
    ...

    """
    with APISession() as session:
        call_module(session, 'pscoast', build_arg_string(kwargs))

```

The function takes keyword arguments (`**kwargs`) and must have the same name
as the corresponding GMT module, in this case `pscoast`.
In the Python wrapper, the `ps` prefix doesn't really make much sense because
we don't need to care that this module writes Postscript.
We'll implement aliases for the function names later on to deal with this.
The body of the function is quite simple and is only two lines.

First, we need to create a `GMTAPI_CTRL` C structure that is required by all
GMT functions.
The `APISession` context manager takes care of creating the structure by
calling `GMT_Create_Session` from the C API, handing us a pointer in the
`session` variable, and destroying it on exit using `GMT_Destroy_Session`.

Next, we use `call_module` to execute the `pscoast` GMT module.
This function wraps `GMT_Call_Module` from the C API
and receives inputs as a string of command-line arguments, like `'-R1/2/3/4
-JM4i ...'`.
Function `build_arg_string` from the `gmt.utils` module takes care of
transforming the `kwargs` dictionary into that string.


