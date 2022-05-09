---
title: Presentations
banner_image: images/anatolia-himalayas-topography.jpg
banner_position: center
banner_title: Presentations
banner_subtitle: Slides, posters, abstracts, and recordings of my presentations
template: base.html
---

{%- import "macros.html" as macros %}

{%- for item in page.presentations %}
  {%- set id = loop.index %}
<div class="mb-5">
  <h2 class="fs-4 mb-1">
    {{ item.title|trim }}
  </h2>
  <p class="mb-1 fs-6">
    <span class="text-muted">{{ item.year }}</span> |
    {{ item.authors|trim }}
  </p>
  <p class="text-muted fs-6">
    {%- if item.invited is defined and item.invited %}
      <span class="badge bg-success fw-normal me-1">
        <i class="fa fa-paper-plane me-1" aria-hidden="true"></i>
        invited
      </span>
    {%- endif %}
    {{ item.event }}
    {%- if item.doi is defined %}
      | doi:<a target="_blank" href="https://doi.org/{{ item.doi }}">{{ item.doi }}</a>
    {%- endif %}
  </p>
  <button class="btn btn-secondary btn-sm me-1 mb-2" type="button"
      data-bs-toggle="collapse" data-bs-target="#collapse-{{ id }}"
      aria-expanded="false" aria-controls="collapse-{{ id }}">
    Find out more <i class="fa fa-chevron-circle-down ms-1" aria-hidden="true"></i>
  </button>
  {%- if item.slides is defined %}
    {{ macros.button_link(item.slides, "Slides", type="btn-primary", icon="fa fa-desktop") }}
  {%- endif %}
  {%- if item.poster is defined %}
    {{ macros.button_link(item.poster, "Poster", type="btn-primary", icon="fa fa-image") }}
  {%- endif %}
  {%- if item.recording is defined %}
    {{ macros.button_link("https://www.youtube.com/watch?v=" ~ item.recording, "Recording", type="btn-light", icon="fab fa-youtube") }}
  {%- endif %}
  {%- if item.data is defined %}
    {{ macros.button_link("https://doi.org/" ~ item.data, "Data", type="btn-light", icon="fa fa-chart-bar") }}
  {%- endif %}
  {%- if item.github is defined %}
    {{ macros.button_link("https://github.com/" ~ item.github, "Code", type="btn-light", icon="fab fa-github") }}
  {%- endif %}
  <div id="collapse-{{ id }}" class="collapse paper-info mt-2 overflow-hidden">
    {%- if item.note is defined %}
      <div class="callout callout-note mb-4">
        <p><strong>Note:</strong> {{ item.note|trim }}</p>
      </div>
    {%- endif %}
    {%- if item.about is defined %}
      <h3 class="fs-4">About</h3>
      {{ item.about|trim }}
    {%- endif %}
    {%- if item.abstract is defined %}
        <h3 class="fs-4">Abstract</h3>
        <p>{{ item.abstract|trim }}</p>
    {%- endif %}
    {%- if item.poster_embed is defined %}
      <h3 class="fs-4">Poster</h3>
      <div class="mb-3">
      {{ item.poster_embed|trim }}
      </div>
    {%- endif %}
    {%- if item.citation is defined %}
      <h3 class="fs-4">Cite as</h3>
      <blockquote class="mb-4">{{ item.citation|trim }}</blockquote>
    {%- endif %}
  </div>
</div>
{%- endfor %}
