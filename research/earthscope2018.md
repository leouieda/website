---
title: "NSF-EAR: The EarthScope/GMT Analysis and Visualization Toolbox"
author: pwessel, uieda, bridget
date: 2018-09-01
period: 2018-2020
role: Co-Principal Investigator
award: <a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1829371">1829371</a>
agency: National Science Foundation
funds: USD 174,975
institution: University of Hawai'i at Mānoa
layout: publication
thumbnail: earthscope2018.png
tags: earthscope2018
---

{% from "utils.html" import make_tag %}

# About

This is my first grant as co-PI and it will fund the development of the new
[GMT](https://github.com/GenericMappingTools/gmt) "modern mode" on which the
[GMT/Python wrapper is based][/blog/gmt-python-design]. It also includes many other
improvements to GMT and the development of a new interpolation method for GPS data.
The latter is where most of my efforts will be directed. The interpolation method will
rely heavily on the infrastructure developed in [Verde][/papers/verde].

All outputs (posters, papers, talks, etc) related to this grant will be collected under
the {{ make_tag("earthscope2018") }} tag.


# Abstract

Research under the EarthScope umbrella involves both data processing and display of
results. The Generic Mapping Tools (GMT) is a set of scientific analysis and plotting
modules that are widely used in the Earth Sciences, particularly because they allow for
specialized processing and imaging suitable for the geosciences. GMT is a long-lived
(~30 years) and robust NSF-funded software toolset that originated in the ocean sciences
but has spread to all aspects of the geosciences and beyond. This project will add
numerous enhancements to GMT, including a much simplified usage syntax called modern
mode. In addition, new modules for simplifying the creation of animations, 3-D stacking
and interpolation of grids, conversion of imagery for placement in Google Earth, and
greatly improved interactive documentation will be built during the project.

The Generic Mapping Tools (GMT) scripting has remained remarkably similar over its 30
years of existence. Because thousands of GMT classic scripts have been written, making
major changes has been problematic, even if such changes would simplify its usage. The
proposed modern mode will solve this dilemma as it introduces two new commands (begin
and end) that starts and end a modern mode session. Hence it is not possible to
accidentally enter modern mode without the use of those commands, thus allowing all
existing GMT scripts to run unchanged. Once in modern mode, the required syntax will be
simplified to avoid repetitive options and the user will no longer be responsible for
assembling a composite PostScript file. The default output format will be PDF but more
than one format may be selected, including standard raster image formats. Improved
interactive documentation will be added to showcase modern mode (while maintaining the
documentation for classic mode). To strengthen EarthScope science there will be new
modules for 3-D grid stacking and interpolation, KML image quadtree building for Google
Earth, and a new animation module that vastly simplifies the task of building scientific
animations. It is anticipated that UNAVCO will assist with annual workshops aimed at
EarthScope scientists using GMT in shell, MATLAB, or Python environments.
