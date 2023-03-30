---
title: About
banner_image: images/hawaii-lava-photoshoot.jpg
banner_position: top left
banner_title: About me
banner_subtitle: More about me and what I do
thumbnail: images/thumbnail/about.png
template: base.html
---

{% import "macros.html" as macros %}

## Who am I?

I'm first and foremost a Dedicated Involved Loving Father.
On the rare occasions where I find myself with free time, I enjoy
playing Incineroar in [Super Smash Bros Ultimate][smash],
baking sourdough bread,
making noise with my ukulele and off-tune baritone,
listening to podcasts,
and reading sci-fi and fantasy.
My favorite show is by far [Avatar: The Last Airbender][avatar]
and I've been sucked into the [Cosmere books][cosmere] by
[Brandon Sanderson][sanderson].

I work as Lecturer in Geophysics at the University of Liverpool's
[Department of Earth, Ocean and Ecological Sciences][deoes] in the UK,
where I started the [Computer-Oriented Geoscience Lab]({{ config.links.compgeolab }}).
Before coming to Liverpool, I was a visiting research scholar at the
University of Hawaiʻi at Mānoa, where I worked with the
[Generic Mapping Tools]({{ config.links.gmt }}) team to create
[PyGMT]({{ config.links.pygmt }}), a widely-used Python library for processing
and visualizing geophysical data.
Prior to Hawaiʻi, I worked for three years as Assistant Professor at the
Universidade do Estado do Rio de Janeiro, Brazil.

My research and teaching make heavy use of open-source software and computing
in general to gain insights on the inner workings of the Earth.
I am one of the core developers and maintainer of the
[Fatiando a Terra]({{ config.links.fatiando }}) project, a community-developed set of open-source
Python libraries for the Geosciences.

{{ macros.figure("../images/teaching-git-at-agu2019.jpg", 'Me teaching git and GitHub at <a href="https://github.com/agu-ossi/2019-agu-oss">AGU2019</a>.', class="mt-4") }}

[deoes]: https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/
[ssi-fellowship]: https://software.ac.uk/about/fellows/leonardo-uieda
[smash]: https://en.wikipedia.org/wiki/Super_Smash_Bros._Ultimate
[sanderson]: https://en.wikipedia.org/wiki/Brandon_Sanderson
[cosmere]: https://coppermind.net/
[avatar]: https://en.wikipedia.org/wiki/Avatar%3A_The_Last_Airbender

<div class="callout callout-note mt-4">

**Looking for a career summary?** I keep a short-form CV somewhat updated:
<a class="nowrap" href="https://www.leouieda.com/cv/leonardo_uieda_cv_summary.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer">
<i class="fa fa-download" aria-hidden="true"></i>
Download the PDF
</a>

**Curious about the CV template?** It's typeset in LaTeX and the source is
available from the GitHub repository
<a class="nowrap" href="https://github.com/leouieda/cv"><i class="mx-1 fab fa-github" aria-hidden="true"></i><code>leouieda/cv</code></a>.

</div>

## Professional Appointments

{{ macros.cv_section(page.work, config.coauthors, section_id="work") }}

## Education

{{ macros.cv_section(page.edu, config.coauthors, section_id="edu") }}

## Grants & Fellowships

{{ macros.cv_section(page.grants, config.coauthors, section_id="grants") }}
