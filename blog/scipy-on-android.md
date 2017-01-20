---
title: Running Jupyter and the Scipy stack on Android
date: 2017-01-20
thumbnail: scipy-on-android.png
layout: post
---

I bought my first tablet last October, an
[NVIDIA Shield K1](https://www.amazon.com/NVIDIA-SHIELD-K1-Tablet-Black/dp/B0171BS9CG/ref=sr_1_2?s=pc&ie=UTF8&qid=1484937529&sr=1-2&keywords=nvidia+shield+k1).
I had been putting off getting one because I never could think of a good use
for them.
I have my phone for messaging and Internet, my kindle for reading, and my
Linux laptop for working.
It seemed to me that the tablet would be a nice toy but not something I could
use and justify the purchase.

The dream would be to be able to ditch my laptop and do actual work on the
tablet.
Mark O'Connor wrote about doing just that on
[Yield
Thought](http://yieldthought.com/post/12239282034/swapped-my-macbook-for-an-ipad)
but he cheats a bit by running everything on a Linode server.
And how does anyone do scientific programming these days without a Jupyter
notebook?

I finally gave in, thinking that I would use the tablet mainly for reading
papers and taking notes.
Maybe even play a few games.
Then I discovered [Termux](https://termux.com/).


# Show, don't tell

Here is a screencast of me running a Jupyter notebook
server on my tablet.
Notice that the URL is `localhost:8888/` so this is not a remote server.

![Screencast of Termux running the Jupyter notebook on my Shield K1 tablet](/images/termux-running-jupyter.gif)


# How to set this up

![Blank Termux startup screen](/images/blank-termux.png)


![IPython running inside Termux](/images/termux-ipython-numpy.png)


Living with vim: remap esc


# Things missing

* Anaconda/conda (for easily getting binaries)
* conda-env (for managing conda environments)
* conda-forge (for building your own conda packages)


---

*The Jupyter logo was downloaded from their Github repository
([jupyter/design](https://github.com/jupyter/design)).
The Android logo is [CC BY 2.5](http://creativecommons.org/licenses/by/2.5)
Google Inc.,
[via Wikimedia Commons](https://commons.wikimedia.org/wiki/File%3AAndroid_robot.svg).*
