---
title: "The Generic Mapping Tools Version 6"
date: 2019-11-01
author: pwessel, joaquim, uieda, remko, wobbe, walter, dongdong
journal: Geochemistry, Geophysics, Geosystems
thumbnail: gmt6.png
layout: publication
tags: gmt, open-source, earthscope2018
alm: true
oa: true
supplement: 10.6084/m9.figshare.8171339
doi: 10.1029/2019GC008515
citation: "Wessel, P., Luis, J. F., Uieda, L., Scharroo, R., Wobbe, F., Smith, W. H. F., & Tian, D. ( 2019). The Generic Mapping Tools version 6. Geochemistry, Geophysics, Geosystems, 20. doi:10.1029/2019GC008515"
---

# About

This paper marks the release of [GMT](https://www.generic-mapping-tools.org/) version 6.
Most of the work done for this release had the goal of reducing barriers to entry for
new users. The user experience as a whole has been improved and these changes are the
foundation for [my work on PyGMT][/tag/pygmt].

The development of the new *modern mode* was funded by our [NSF EarthScope
grant][/research/earthscope2018].

# Plain language summary

The Generic Mapping Tools software is widely used in Earth and Ocean sciences to process
data and make maps and illustrations. This new version simplifies usage, adds quick
access to key data sets and provides a tool for making scientific animations.

# Abstract

The Generic Mapping Tools (GMT) software is ubiquitous in the Earth and Ocean sciences.
As a cross-platform tool producing high quality maps and figures, it is used by tens of
thousands of scientists around the world. The basic syntax of GMT scripts has evolved
very slowly since the 1990s, despite the fact that GMT is generally perceived to have a
steep learning curve with many pitfalls for beginners and experienced users alike.
Reducing these pitfalls means changing the interface, which would break compatibility
with thousands of existing scripts. With the latest GMT version 6, we solve this
conundrum by introducing a new "modern mode" to complement the interface used in
previous versions, which GMT 6 now calls "classic mode". GMT 6 defaults to classic mode
and thus is a recommended upgrade for all GMT 5 users. Nonetheless, new users should
take advantage of modern mode to make shorter scripts, quickly access commonly used
global data sets, and take full advantage of the new tools to draw subplots, place
insets, and create animations.
