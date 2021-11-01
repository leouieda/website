---
title: Publications
banner_image: images/arctic-bathymetry.jpg
banner_position: top left
banner_title: Publications
banner_subtitle: A full list of all of my academic publications
enable_alm: true
template: base.html
---

{%- import "macros.html" as macros %}

<div class="callout callout-note mb-5">

For citation information, see
[Google Scholar]({{ config.googlescholar }})
and [Publons]({{ config.publons }}).
A more complete list of my work can be found on
[ORCID](https://orcid.org/{{ config.orcid }})
• {{ config.orcid }}

Find out more about my research at the
[Computer-Oriented Geoscience Lab](https://www.compgeolab.org/).

</div>

{%- for paper in page.papers %}
  {%- set id = loop.index %}
  {%- if paper.doi is defined %}
    {%- set doi = paper.doi %}
  {%- else %}
    {%- set doi = paper.preprint %}
  {%- endif %}
  {%- if paper.openaccess is defined and paper.openaccess %}
    {%- set pdf = "https://doi.org/" ~ paper.doi %}
  {%- elif paper.preprint is defined %}
    {%- set pdf = "https://doi.org/" ~ paper.preprint %}
  {%- elif paper.pdf is defined %}
    {%- set pdf = paper.pdf %}
  {%- endif %}
<div class="mb-5">
  <h2 class="fs-4 mb-1">
    {{ paper.title|trim }}
  </h2>
  <p class="mb-1">
    <span class="text-muted">{{ paper.year }}</span>
    |
    {{ paper.authors|trim }}
  </p>
  <p class="text-muted fs-6">
    {%- if paper.openaccess is defined and paper.openaccess %}
      <span class="badge bg-success fw-normal me-1">
        <i class="ai ai-open-access me-1" aria-hidden="true"></i>
        open-access
      </span>
    {%- endif %}
    {%- if paper.preprint is defined and not paper.doi is defined %}
      <span class="badge bg-warning text-dark fw-normal me-1">
        preprint
      </span>
    {%- endif %}
    {{ paper.journal }},
    doi:<a target="_blank" href="https://doi.org/{{ doi }}">{{ doi }}</a>
  </p>
  <button class="btn btn-secondary btn-sm me-1 mb-2" type="button"
      data-bs-toggle="collapse" data-bs-target="#collapse-{{ id }}"
      aria-expanded="false" aria-controls="collapse-{{ id }}">
    Find out more <i class="fa fa-chevron-circle-down ms-1" aria-hidden="true"></i>
  </button>
  {{ macros.button_link(pdf, "PDF", type="btn-primary", icon="fa fa-file-pdf") }}
  {%- if paper.data is defined %}
    {{ macros.button_link("https://doi.org/" ~ paper.data, "Data", type="btn-light", icon="fa fa-chart-bar") }}
  {%- endif %}
  {%- if paper.github is defined %}
    {{ macros.button_link("https://github.com/" ~ paper.github, "Code", type="btn-light", icon="fab fa-github") }}
  {%- endif %}
  <div id="collapse-{{ id }}" class="collapse paper-info mt-2 overflow-hidden">
    {%- if paper.note is defined %}
      <div class="callout callout-note mb-4">
        <p><strong>Note:</strong> {{ paper.note|trim }}</p>
      </div>
    {%- endif %}
    <h3 class="fs-4">Abstract</h3>
    <p>{{ paper.abstract|trim }}</p>
    <h3 class="fs-4">Cite as</h3>
    <blockquote class="mb-4">{{ paper.citation|trim }}</blockquote>
    <h3 class="fs-4">BibTex</h3>
    <pre class="mb-4"><code>{{ paper.bibtex|trim|escape }}</code></pre>
    <h3 class="fs-4 mb-4">Citations</h3>
    <span class="__dimensions_badge_embed__" data-doi="{{ doi }}"></span>
  </div>
</div>
{%- endfor %}
