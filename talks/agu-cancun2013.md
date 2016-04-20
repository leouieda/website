---
title: 3D magnetic inversion by planting anomalous densities
author: uieda, barbosa
date: 2013-05-01
repository: leouieda/agu-cancun2013
presentation: oral
doi: 10.6084/m9.figshare.703651
slides: 10.6084/m9.figshare.703651
event: AGU Meeting of the Americas
thumbnail: agu-cancun2013.png
alm: true
layout: publication
---

# Presentation

<script async class="speakerdeck-embed"
data-id="47e71fe41d9d4f1fa7859454577a6d3f" data-ratio="1.33159947984395"
src="//speakerdeck.com/assets/embed.js"></script>

# About

This talk presents an adaptation of the gravity-gradient inversion method I
developed for my Masters degree dissertation
"[/papers/paper-planting-anomalous-densities-2012]" to invert magnetic data.

As you may have noticed, there is an **error in the title**. We do not, in
fact, invert magnetic data using **density** anomalies. This illustrates the
perils of copy-pasting combined with a looming deadline.

The inversion method was developed along a few iterations and presented at
different meetings
(in order):

* 2011: [/talks/eage2011]
* 2011: [/talks/seg2011]
* 2011: [/talks/sbgf2011]
* 2012: [/papers/paper-planting-anomalous-densities-2012] (the paper)
* 2012: [/talks/seg2012]
* 2013: This talk

I have added an **open-source** implementation of the gravity-gradient
inversion method to the Python library [Fatiando a
Terra](http://www.fatiando.org). In version `0.1` to `0.4`, the code is in
module `fatiando.gravmag.harvester`.

# Abstract

**AGU abstract ID**: GP22A-01

We present a new 3D magnetic inversion algorithm based on the computationally
efficient method of planting anomalous densities. The algorithm consists of an
iterative growth of the anomalous bodies around prismatic elements called
"seeds". These seeds are user-specified and have known magnetizations. Thus,
the seeds provide a way for the interpreter to specify the desired skeleton of
the anomalous bodies. The inversion algorithm is computationally efficient due
to various optimizations made possible by the iterative nature of the growth
process. The control provided by the use of seeds allows one to test different
hypothesis about the geometry and magnetization of targeted anomalous bodies.
To demonstrate this capability, we applied our inversion method to the Morro do
Engenho (ME) and A2 magnetic anomalies, central Brazil (Figure 1a). ME is an
outcropping alkaline intrusion formed by dunites, peridotites and pyroxenites
with known magnetization. A2 is a magnetic anomaly to the Northeast of ME and
is thought to be a similar intrusion that is not outcropping. Therefore, a
plausible hypothesis is that A2 has the same magnetization as ME. We tested
this hypothesis by performing an inversion using a single seed for each body.
Both seeds had the same magnetization. Figure 1b shows that the inversion
produced residuals up to 2000 nT over A2 (i.e., a poor fit) and less than 400
nT over ME (i.e., an acceptable fit). Figure 1c shows that ME is a compact
outcropping body with bottom at approximately 5 km, which is in agreement with
previous interpretations. However, the estimate produced by the inversion for
A2 is outcropping and is not compact. In summary, the estimate for A2 provides
a poor fit to the observations and is not in accordance with the geologic
information. This leads to the conclusion that A2 does not have the same
magnetization as ME. These results indicate the usefulness and capabilities of
the inversion method here proposed.
