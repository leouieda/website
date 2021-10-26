---
title: "Design ideas and goals for the GMT Python interface"
date: 2017-03-29
---

As you may already know, I'm away on a [postdoct writing a Python interface
for the Generic Mapping Tools](/blog/hawaii-gmt-postdoc.html).
Recently, I started laying out our goals for the project and some of my design
ideas.
This all lives on the
[GenericMappingTools/gmt-python](https://github.com/GenericMappingTools/gmt-python)
GitHub repository, which is where the code will eventually be as well.
I thought it would be good to post it here as well to have a snapshot of this
phase of the project for future reference.

I have also submitted a [talk proposal for Scipy 2017 about the
project](/blog/scipy2017-proposal-gmt.html).

---

## Goals

* Provide access to GMT modules from Python using the GMT C API (no system
  calls).
* Input and output using Python native containers: numpy `ndarray` or pandas
  `DataFrame` for data tables and [xarray](http://xarray.pydata.org) `Dataset`
  for netCDF grids.
* Integration with the [Jupyter notebook](http://jupyter.org/) to display plots
  and maps inline.
* API design familiar for veteran GMT users (arguments `R`, `J`, etc) with more
  newbie-friendly alternatives/aliases (`region=[10, 20, -30, -10]`,
  `projection='M'`, etc).

## Previous work

To my knowledge, there have been 3 attempts at a GMT Python interface:

-   [gmtpy](https://github.com/emolch/gmtpy) by [Sebastian
    Heimann](https://github.com/emolch)
-   [pygmt](https://github.com/ian-r-rose/pygmt) by [Ian
    Rose](https://github.com/ian-r-rose)
-   [PyGMT](https://github.com/glimmer-cism/PyGMT) by [Magnus
    Hagdorn](https://github.com/mhagdorn)

Only `gmtpy` has received commits since 2014 and is the more mature
alternative. However, the project [doesn't seem to be very
active](https://github.com/emolch/gmtpy/graphs/contributors). Both
`gmtpy` and `PyGMT` use system class (through `subprocess.Popen`) and
pass input and output through `subprocess.PIPE`. `pygmt` seems to call
the GMT C API directly through a hand-coded Python C extension. This
might compromise the portability of the package across operating systems
and makes distribution very painful.

## Design

`gmt-python` is made for the future. We will support **only Python 3.5
or later** and require the [new "modern" mode of
GMT](http://gmt.soest.hawaii.edu/projects/gmt/wiki/Modernization)
(currently only in the `trunk` of the SVN repository). The `modern` mode
removes the need for `-O -K` and explicitly redirecting to a `.ps` file. This
all happens in the background. A final call to `gmt psconvert` brings the plot
out of hiding and finalizes the Postscript. This mode is perfect for the Python
interface, which would have to handle generation of the Postscript file in the
background anyway.

We will wrap the GMT C API using the
[ctypes](https://docs.python.org/3/library/ctypes.html) module of the
Python standard library. `ctypes` grants access to C data types and
foreign functions in DDLs and shared libraries, making it possible to
wrap these libraries with pure Python code. Not having compiled modules
makes packaging and distribution of Python software a lot easier.

Wrappers for GMT data types and C functions will be implemented in a
lower level wrapper library. These will be direct `ctypes` wrappers of
the GMT module functions and any other function that is needed on the
Python side. The low-level functions will not handle any data type
conversion or setting up of argument list.

We'll also provide higher level functions that mirror all GMT modules.
These functions will be built on top of the low-level library and will
handle all data conversions and parsing of arguments. This is the part
of the library with which the user will interact (the GMT Python API).

### The GMT Python API

Each GMT module has a function in the `gmt` package. Command-line
arguments are passes as function keyword arguments. Data can be passed
as file names or in-memory data.

The simplest usage would be with data in a file and generating a PDF
output figure, just as a normal GMT script:

    import gmt

    cpt = gmt.makecpt(C='cubhelix', T=[-4500, 4500])
    gmt.grdimage(input='grid.nc', J='M6i', B='af', P=True, C=cpt)
    gmt.psscale(C=cpt, D='jTC+w6i/0.2i+h+e+o0/1i', B='af')
    gmt.psconvert(T='f', F='my-figure')

Arguments can also be passed as in the GMT command-line by using a
single string:

    import gmt

    gmt.makecpt('-Ccubhelix -T-4500/4500', output='my.cpt')
    gmt.grdimage('grid.nc -JM6i -Baf -P -Cmy.cpt')
    gmt.psscale('-Cmy.cpt -DjTC+w6i/0.2i+h+e+o0/1i -Baf')
    gmt.psconvert('-Tf -Fmy-figure')

Notice that output that would be redirected to a file is specified using
the `output` keyword argument.

You can also pass in data from Python. Grids in netCDF format are passed
as xarray `Datasets` that can come from a netCDF file or generated in
memory:

    import gmt
    import xarray as xr

    data = xr.open_dataset('grid.nc')

    cpt = gmt.makecpt(C='cubhelix', T='-4500/4500')
    gmt.grdimage(input=data, J='M6i', B='af', P=True, C=cpt)
    gmt.psconvert(T='f', F='my-figure')

Tabular data can be passed as numpy arrays:

    import numpy as np
    import gmt

    data = np.loadtxt('data_file.csv')

    cpt = gmt.makecpt(C="red,green,blue", T="0,70,300,10000")
    gmt.pscoast(R='g', J='N180/10i', G='bisque', S='azure1', B='af', X='c')
    gmt.psxy(input=data, S='ci', C=cpt, h='i1', i='2,1,3,4+s0.02')
    gmt.psconvert(T='f', F='my-figure')

In the Jupyter notebook, we can preview the plot by calling
`gmt.show()`, which embeds the image in the notebook:

    import numpy as np
    import gmt

    data = np.loadtxt('data_file.csv')

    cpt = gmt.makecpt(C="red,green,blue", T="0,70,300,10000")
    gmt.pscoast(R='g', J='N180/10i', G='bisque', S='azure1', B='af', X='c')
    gmt.psxy(input=data, S='ci', C=cpt, h='i1', i='2,1,3,4+s0.02')
    gmt.show()

`gmt.show` will call `psconvert` in the background to get a PNG image
back and use `IPython.display.Image` to insert it into the notebook.

**TODO**: We're still thinking of the best way to call `gmt.psconvert`
first to generate a high-quality PDF and right after call `gmt.show()`
for an inline preview. The issue is that `psconvert` deletes the
temporary Postscript file that was being constructed on the background,
this calling it a second time through `gmt.show()` would not work. Any
suggestions are welcome!


### Package organization

The general layout of the Python package will probably look something
like this:

    gmt/
        c_api/     ## Package with low-level wrappers for the C API
            ...
        modules/  ## Defines the functions corresponding to GMT modules
            ...

### The module functions

The functions corresponding to GMT modules (`pscoast`, `psconvert`, etc)
are how the user interacts with the Python API. They will be organized
in different files in the `gmt.modules` package but will all be
accessible from the `gmt` package namespace. For example, `pscoast` can
live in `gmt/modules/ps_generating.py` but can be called as
`gmt.pscoast`.

Here is what a module function will look like:

    def module_function(**kwargs):
        """
        Docstring explaining what each option is and all the aliases.

        Likely derived from the GMT documentation.
        """
        ## Convert any inputs into things the C API can digest
        ...
        ## Parse the keyword arguments and make an "args" list
        ...
        ## Call the module function from the C API with the inputs
        ...
        ## Process any outputs from the C API into Python data types
        ...
        return output

We will automate this process as much as possible:

* Common options in the docstrings can be reused from an `OPTIONS` dictionary.
* Parsing of common arguments (R, J, etc) can be done by a function.
* Creating the GMT session and calling the module can be automated.
* Conversion of inputs and outputs will most likely be: tables to numpy arrays,
  grids to xarray `Datasets`, text to Python text.

Most of the work in this part will be wrapping all of the many GMT
modules, parsing non-standard options, and making sure the docstrings
are accurate. It might even be possible to automatically generate the
docstrings or parts of them from the command-line help messages by
passing a Python callback as the `print_func` when creating a GMT
session.

### The low-level wrappers

The low-level wrapper functions will be bare-bones `ctypes` foreign
functions from the `libgmt.so` shared library. The functions can be
accessed from Python like so:

    import ctypes as ct

    libgmt = ct.cdll.LoadLibrary("libgmt.so")

    ## Functions are accessed as members of the 'libgmt' object
    GMT_Call_Module = libgmt.GMT_Call_Module

    ## Call them like normal Python functions
    GMT_Call_Module(... inputs ...)

The tricky part is making sure the functions get the input types they
need. `ctypes` provides access to C data types and a way to specify the
data type conversions that the function requires:

    GMT_Call_Module.argstypes = [ct.c_void_p, ct.c_char_p, ct.c_int, ct.c_void_p]

This is fine for standard data types like `int`, `char`, etc, but will
need extra work for custom GMT `struct`. These data types will need to
be wrapped by Python classes that inherit from `ctypes.Structure`.

The `gmt.c_api` module will expose these foreign functions (with output
and input types specified) and GMT data types for the modules to use.

The main entry point into GMT will be through the `GMT_Call_Module`
function. This is what the `gmt` command-line application uses to run a
given module, like `GMT_pscoast` for example. We will use it to run the
modules from the Python side as well. It has the following signature:

    int GMT_Call_Module (void *V_API, const char *module, int mode, void *args)

The arguments `module`, `mode`, and `args` (the command-line argument
list) are plain C types and can be generated easily using `ctypes`. The
Python module code will need to generate the `args` array from the given
function arguments. The `V_API` argument is a "GMT Session" and is
created through the `GMT_Create_Session` function, which will have to be
wrapped as well.

The input and output of Python data will be handled through the GMT
virtual file machinery. This allows us to write data to a memory
location instead of a file without GMT knowing the difference. For
input, we can use `GMT_Open_VirtualFile` and point it to the location in
memory of the Python data, for example using
[numpy.ndarray.ctypes](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html).
We can also translate the Python data into `ctypes` compatible types.
The virtual file pointer can also be passed as the output option for the
module, for example as `-G` or through redirection (`->`). We can read
the contents of the virtual file using `GMT_Read_VirtualFile`.


## Final thoughts

There are gonna be some rough edges on the C API that will have to get sorted
before all of this is usable.
The API is new (from 2013) and hasn't been much used by third-party libraries.
Some of the details aren't documented and require diving into the GMT source
code or having access to a [GMT guru](http://www.soest.hawaii.edu/wessel/),
like I have.
Hopefully this work will make it more robust and new GMT wrappers can be made
for other languages without so much effort.

All of this work in its very early stages and I'd love to get some feedback and
ideas!
You can leave a comment below or
[create an issue on the GitHub repository](https://github.com/GenericMappingTools/gmt-python/issues).
