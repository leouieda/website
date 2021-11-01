---
title: About
banner_image: images/hawaii-lava-photoshoot.jpg
banner_position: top left
banner_title: About me
banner_subtitle: A bit more about me and my work
template: base.html
---

<section class="mb-5">

## The slightly longer version

I'm first and foremost a Dedicated Involved Loving Father.
On the rare occasions where I find myself with free time, I enjoy
playing Incineroar in Smash Bros Ultimate,
baking sourdough bread,
making noise with my ukulele and off-tune baritone,
listening to podcasts,
and reading sci-fi and fantasy.
My favorite show by far is Avatar: The Last Airbender.

I work as Lecturer in Geophysics at the University of Liverpool's
[Department of Earth, Ocean and Ecological Sciences][deoes] in the UK,
where I'm starting the [Computer-Oriented Geoscience Lab][compeolab].
Before coming to Liverpool, I was a visiting research scholar at the
University of Hawaiʻi at Mānoa, where I worked with the
[Generic Mapping Tools][gmt] team to create [PyGMT][pygmt], a widely-used
Python library for processing and visualizing geophysical data.
Prior to Hawaiʻi, I worked for three years as Assistant Professor at the
Universidade do Estado do Rio de Janeiro, Brazil.

My research and teaching make heavy use of open-source software and computing
in general to gain insights on the inner workings of the Earth.
I am one of the core developers and maintainer of the
[Fatiando a Terra][fatiando] project, a community-developed set of open-source
Python libraries for the Geosciences.

Along with my role at the University of Liverpool, I'm also:

* Topic Editor for the [Journal of Open Source Software](https://joss.theoj.org/)
* Member of the Advisory Council for [EarthArXiv](https://eartharxiv.org/)
* Fellow of the [Software Sustainability Institute][ssi-fellowship]

<figure class="mt-5">

![Me teaching git and GitHub at AGU2019](../images/teaching-git-at-agu2019.jpg)

<figcaption>

Me teaching git and GitHub at [AGU2019](https://github.com/agu-ossi/2019-agu-oss).

</figcaption>
</figure>

</section>
<section class="mb-5">

<h2 id="cv">Curriculum Vitae</h2>

I keep a full length version of my CV updated and publicly available:

<a class="btn btn-primary mb-3" href="https://www.leouieda.com/cv/leonardo_uieda_cv.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer">
<i class="me-1 fa fa-download" aria-hidden="true"></i>
Download my CV in PDF
</a>

<div class="callout">

**Curious about the CV template?** It's typeset in LaTeX using a custom
template. The source is available from the GitHub repository
<a class="nowrap" href="https://github.com/leouieda/cv"><i class="mx-1 fab fa-github" aria-hidden="true"></i><code>leouieda/cv</code></a>.

</div>

</section>
<section class="mb-5">

## Education

{% import "macros.html" as macros %}

{# The education list is defined in about/data.yml #}
{% for item in page.education %}

<div class="mb-3">
{%- set id = loop.index %}
<h2 class="fs-4 mb-1">
  {{ item.level|trim }}
</h2>
<p class="mb-1">
  <span class="text-muted">{{ item.year }}</span>
  |
  {{ item.institution|trim }}
</p>
<p class="mb-1 text-muted fs-6">
  Thesis: {{ item.title|trim }}
</p>
<p class="mb-1 text-muted fs-6">
  Advisor: {{ item.advisor }}
</p>
<p class="text-muted fs-6">
  doi:<a href="https://doi.org/{{ item.doi }}">{{ item.doi }}</a>
</p>
<button class="btn btn-secondary btn-sm me-1 mb-2" type="button"
    data-bs-toggle="collapse" data-bs-target="#collapse-abstract-{{ id }}"
    aria-expanded="false" aria-controls="collapse-abstract-{{ id }}">
  Find out more <i class="fa fa-chevron-circle-down ms-1" aria-hidden="true"></i>
</button>
{{ macros.button_link("https://doi.org/" ~ item.doi, "PDF", type="btn-primary", icon="fa fa-file-pdf") }}
{{ macros.button_link("https://github.com/" ~ item.github, "Code", type="btn-light", icon="fab fa-github") }}
{{ macros.button_link(item.slides, "Slides", type="btn-light", icon="fa fa-desktop") }}
<div id="collapse-abstract-{{ id }}" class="collapse paper-info mt-2 overflow-hidden">
  <h3 class="">About</h3>
  {{ item.notes }}
  <h3 class="">Abstract</h3>
  <p>{{ item.abstract|trim }}</p>
</div>
</div>

{% endfor %}

</section>


[deoes]: https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/
[compeolab]: https://www.compgeolab.org
[gmt]: https://www.generic-mapping-tools.org
[pygmt]: https://www.pygmt.org/
[fatiando]: https://www.fatiando.org
[ssi-fellowship]: https://software.ac.uk/about/fellows/leonardo-uieda
[swung]: https://softwareunderground.org/
