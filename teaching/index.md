---
title: Teaching
banner_image: images/teaching-git-at-agu2019.jpg
banner_position: center right
banner_title: Teaching
banner_subtitle: Open-source material for my classes and workshops
template: base.html
---

{%- import "macros.html" as macros %}

These are some the classes I've taught or am teaching at the moment. Most have
<i class="fab fa-github" aria-hidden="true"></i> GitHub repositories with
open-source teaching resources (lecture slides, code for computer practicals).

{%- macro course_list(courses, base_id) %}
{%- for item in courses %}
  {%- set id = base_id ~ "-" ~ loop.index %}
<div class="mb-5">
  <h2 class="fs-4 mb-1">
    {{ item.title|trim }}
  </h2>
  <p class="text-muted fs-6">
    {{ item.location|trim }}
  </p>
  <button class="btn btn-secondary btn-sm me-1 mb-2" type="button"
      data-bs-toggle="collapse" data-bs-target="#collapse-{{ id }}"
      aria-expanded="false" aria-controls="collapse-{{ id }}">
    Find out more <i class="fa fa-chevron-circle-down ms-1" aria-hidden="true"></i>
  </button>
  {%- if item.github is defined %}
    {{ macros.button_link("https://github.com/" ~ item.github, "Teaching resources", type="btn-primary", icon="fab fa-github") }}
  {%- endif %}
  {%- if item.recording is defined %}
    {{ macros.button_link("https://www.youtube.com/watch?v=" ~ item.recording, "Recording", type="btn-light", icon="fab fa-youtube") }}
  {%- endif %}
  <div id="collapse-{{ id }}" class="collapse paper-info mt-2 overflow-hidden">
    <section class="row gx-5">
      <div class="col-lg-6">
        {%- if item.note is defined %}
          <div class="callout callout-note mb-4">
            <p><strong>Note:</strong> {{ item.note|trim }}</p>
          </div>
        {%- endif %}
        <h3 class="fs-4">About</h3>
        {{ item.about|trim }}
      </div>
      <div class="col-lg-6">
        {%- if item.recording is defined %}
          <h3 class="fs-4">Recording</h3>
          {{ macros.youtube_embed(item.recording) }}
        {%- endif %}
      </div>
    </section>
  </div>
</div>
{%- endfor %}
{%- endmacro %}


## University of Liverpool



<hr class="my-5">

## Workshops and short courses


<hr class="my-5">

## Universidade do Estado do Rio de Janeiro

{{ course_list(page.uerj, base_id="uerj") }}
