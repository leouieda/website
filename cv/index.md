---
title: Curriculum Vitæ
banner_image: images/teaching-git-at-agu2019.jpg
banner_position: center right
banner_title: Curriculum Vitæ
banner_subtitle: A list of pretty much everything I've done so far in my career
template: base.html
sections:
  - title: Professional
    numbered: False
    entries:
      - [work, Appointments]
      - [community, Community service]
      - [edu, Education]
  - title: Distinctions
    numbered: False
    entries:
      - [grants, Grants & fellowships]
      - [awards, Awards & honors]
  - title: Publications
    numbered: True
    entries:
      - [preprints, Preprints]
      - [papers, Papers]
      - [proceedings, Conference proceedings]
      - [other-publications, Other publications]
  - title: Presentations
    numbered: True
    entries:
      - [presentations-invited, Invited talks]
      - [presentations-department, Department seminars]
      - [presentations-conference, Conference presentations]
      - [presentations-other, Other presentations]
  - title: Teaching
    numbered: True
    entries:
      - [teaching-classes, University courses]
      - [teaching-workshops, Workshops]
  - title: Supervision
    numbered: True
    entries:
      - [supervision-phd, PhD students]
      - [supervision-msc, MSc students]
      - [supervision-bsc, BSc students]
  - title: Service
    numbered: True
    entries:
      - [examiner-thesis, Thesis examination]
      - [examiner-jobs, Hiring committees]
      - [convener, Conference sessions and events]
  - title: Other
    numbered: True
    entries:
      - [media, Media & outreach]
---

{% import "macros.html" as macros %}

<div class="callout">

**Looking for a career summary?**
Here is a
<a href="https://github.com/leouieda/cv/raw/pdf/cv.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer"><i class="fa fa-file-pdf" aria-label="PDF file"></i> short CV</a>.
(LaTeX source code is in the {{ macros.github_link("leouieda/cv") }} GitHub
repository).

**Want to read a narrative version?**
I wrote an
<a href="https://github.com/leouieda/memorial2023/raw/gh-pages/memorial.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer"><i class="fa fa-file-pdf" aria-label="PDF file"></i> academic autobiography</a> (in Portuguese)
as part of my application for my current job at USP (LaTeX source code is in
the {{ macros.github_link("leouieda/memorial2023") }} GitHub repository).

</div>

<h2 id="navigation">
  <i class="fas fa-list" aria-hidden="true"></i>
  Contents
</h2>
<nav aria-label="Page">
  <ul role="list" class="list-inline">
  {%- for section in page.sections %}
    <li><a class="text-muted" href="#{{ loop.index }}">{{ loop.index }}. {{ section.title }}</a></li>
  {%- endfor %}
  </ul>
</nav>

{%- for section in page.sections %}
  {% set section_id = loop.index %}
  <h2 id="{{ section_id }}">{{ section_id }}. {{ section.title }}</h2>
  {%- for data, title in section.entries %}
    <h3 id="{{ data }}">{{ section_id }}.{{ loop.index }} {{ title }}</h3>
    {{ macros.list_cv_items(page[data], config, numbered=section.numbered) }}
    {%- if not loop.last %}
    {%- endif %}
  {%- endfor %}
    <p class="text-center">
      <a href="#navigation">
        <i class="far fa-arrow-alt-circle-up" aria-hidden="true"></i>
        Back to Contents
      </a>
    </p>
{%- endfor %}
