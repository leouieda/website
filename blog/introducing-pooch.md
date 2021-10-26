---
title: "Introducing Pooch"
date: 2018-07-20
---

> A friend to fetch your sample data files.

[Pooch](https://github.com/fatiando/pooch) is a Python package that manages downloading
data files over HTTP and storing them in a local directory.
It is meant to be used by other Python libraries that ship sample data files for use in
documentation, workshops, demos, etc.

For example, your package could define a `datasets.py` module that has functions to load
sample data
([like scikit-learn does](http://scikit-learn.org/0.19/modules/classes.html#module-sklearn.datasets)).
If you want the data to live on the web (like in the GitHub repo) instead of shipping it
with your package, Pooch can keep track of it and download it to the user's computer
only when it's needed.

This is what a `datasets.py` module would look like using Pooch:


```python
"""
Module mypackage/datasets.py
"""
import pooch

## Get the version string from your project. You have one of these, right?
from . import __version__


## Create a new friend to manage your sample data storage
GOODBOY = pooch.create(
    ## Folder where the data will be stored. For a sensible default, use the default
    ## cache folder for your OS.
    path=pooch.os_cache("mypackage"),
    ## Base URL of the remote data store. Will call .format on this string to insert
    ## the version (see below).
    base_url="https://github.com/myproject/mypackage/raw/{version}/data/",
    ## Pooches are versioned so that you can use multiple versions of a package
    ## simultaneously. Use PEP440 compliant version number. The version will be
    ## appended to the path.
    version=__version__,
    ## If a version as a "+XX.XXXXX" suffix, we'll assume that this is a dev version
    ## and replace the version with this string.
    version_dev="master",
    ## An environment variable that overwrites the path.
    env="MYPACKAGE_DATA_DIR",
    ## The cache file registry. A dictionary with all files managed by this pooch.
    ## Keys are the file names (relative to *base_url*) and values are their
    ## respective SHA256 hashes. Files will be downloaded automatically when needed
    ## (see fetch_gravity_data).
    registry={"gravity-data.csv": "89y10phsdwhs09whljwc09whcowsdhcwodcy0dcuhw"}
)
## You can also load the registry from a file. Each line contains a file name and
## it's sha256 hash separated by a space. This makes it easier to manage large
## numbers of data files. The registry file should be in the same directory as this
## module.
GOODBOY.load_registry("registry.txt")


## Define functions that your users can call to get back some sample data in memory
def fetch_gravity_data():
    """
    Load some sample gravity data to use in your docs.
    """
    ## Fetch the path to a file in the local storae. If it's not there, we'll
    ## download it.
    fname = GOODBOY.fetch("gravity-data.csv")
    ## Load it with numpy/pandas/etc
    data = ...
    return data
```


## Features

* Download a file only if it's still not in the local storage.
* Check the SHA256 hash to make sure the file is not corrupted or needs updating.
* If the hash is different from the registry, Pooch will download a new version of the
  file.
* If the hash still doesn't match, Pooch will raise an exception warning of possible
  data corruption.


## About

I started coding up Pooch at the [Scipy2018](https://scipy2018.scipy.org/) sprints last
week.
At one point, I realised that I was writing the same code to fetch sample data multiple
times.
I asked [John Leeman](http://www.johnrleeman.com/) if such a package would be useful to
[MetPy](https://github.com/Unidata/MetPy)
and, as it turns out, he was in the middle of
[implementing the same thing](https://github.com/Unidata/MetPy/pull/760).
So I decided to write this as a standalone package that we could all share.

Pooch is the first package released as part of the
[breakup of the Fatiando a Terra project](/blog/future-of-fatiando.html).
It will be used in most other packages in the new Fatiando ecosystem, like
[Verde](https://www.fatiando.org/verde/).


## Taking it for a test drive

Pooch is still a bit experimental but has complete test coverage and builds successfully
on Linux, Mac, and Windows. I encourage you to give our first alpha release a try
(v0.1a1):

```
pip install pooch==0.1a1
```

The documentation at [fatiando.org/pooch](http://www.fatiando.org/pooch/) has
instructions for training your pooch to fetch data. There is also an API reference that
lists all of the configuration options available.


## Getting involved

The code is [BSD licensed](https://github.com/fatiando/pooch/blob/master/LICENSE.txt)
and we would love contributions of any form!
Checkout the Github repository [fatiando/pooch](https://github.com/fatiando/pooch) and
please report any issues that you might encounter or features you would like to have.

We have
[Contributing Guide](https://github.com/fatiando/pooch/blob/master/CONTRIBUTING.md) to
help you get started and a
[Code of Conduct](https://github.com/fatiando/pooch/blob/master/CODE_OF_CONDUCT.md)
to keep you safe.

**Update (2018-08-10):** Pooch now works on Python 2.7 ([PR17](https://github.com/fatiando/pooch/pull/17))
but we'll only support it until mid 2019.
