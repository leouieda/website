---
title: Curriculum Vitæ
banner_image: images/teaching-git-at-agu2019.jpg
banner_position: center right
banner_title: Curriculum Vitæ
banner_subtitle: My academic CV, containing most things I have done so far in my career
thumbnail: images/thumbnail/default.png
template: base.html
sections:
    - [work, Professional appointments]
    - [community, Community service]
    - [edu, Education]
    - [grants, Grants & fellowships]
    - [preprints, Preprints]
    - [papers, Papers]
    - [other-publications, Other publications]
    - [proceedings, Conference proceedings]
    - [media, Media & outreach]
    - [awards, Awards & honors]
    - [examiner-thesis, Thesis examination]
    - [convener, Conference sessions and events]
    - [supervision-phd, PhD students]
    - [supervision-msc, MSc students]
    - [supervision-bsc, BSc students]
---

{% import "macros.html" as macros %}

<div class="callout">

**Looking for a career summary?**
I keep a somewhat updated
<a href="https://github.com/leouieda/cv/raw/pdf/leonardo_uieda_cv_summary.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer">short-form CV in PDF format</a>.
It's typeset in LaTeX and the source is available from the
{{ macros.github_link("leouieda/cv") }} GitHub repository.

</div>

<hr>
<p id="navigation">
  <i class="fas fa-list" aria-hidden="true"></i>
  CV sections
</p>
<nav aria-label="Page">
  <ul role="list" class="list-inline">
  {%- for data, title in page.sections %}
    <li><a href="#{{ data }}">{{ title }}</a></li>
  {%- endfor %}
  </ul>
</nav>

{%- for data, title in page.sections %}
  <h2 id="{{ data }}">{{ title }}</h2>
  {%- for item in page[data] %}
    <div>
      <p>
        <span class="text-muted font-small">{{ item.year }}.</span>
        {{ item.title|trim }}.
        {%- if item.institution is defined %}
          <span class="text-muted">
          {{ item.institution|trim }}{%- if item.country is defined %}, {{ item.country }}{%- endif %}.
          </span>
        {%- endif %}
      </p>
    <details>
      <summary>More information</summary>
      <div class="details-body flow flow-small">
        {%- if item.authors is defined %}
          <p><strong>Authors:</strong> {{ macros.author_list(item.authors, config) }}</p>
        {%- endif %}
        {%- if item.doi is defined %}
          <p><strong>DOI:</strong> {{ macros.doi_link(item.doi) }}</p>
        {%- endif %}
        {%- if item.preprint is defined %}
          <p><strong>Preprint DOI (open access):</strong> {{ macros.doi_link(item.preprint) }}</p>
        {%- endif %}
        {%- if item.github is defined %}
          <p><strong>GitHub:</strong> {{ macros.github_link(item.github) }}</p>
        {%- endif %}
        {%- if item.data is defined %}
          <p><strong>Data and code archive DOI:</strong> {{ macros.doi_link(item.data) }}</p>
        {%- endif %}
        {%- if item.pdf is defined %}
          <p><strong>PDF download:</strong> <a href="{{ item.pdf }}" target="_blank">{{ item.pdf[7:] }}</a></p>
        {%- endif %}
        {%- if item.slides is defined %}
          <p><strong>Slides:</strong> <a href="{{ item.slides }}" target="_blank">{{ item.slides }}</a></p>
        {%- endif %}
        {%- if item.department is defined %}
          <p><strong>Department:</strong> {{ item.department }}</p>
        {%- endif %}
        {%- if item.thesis is defined %}
          <p><strong>Thesis:</strong> {{ item.thesis }}</p>
        {%- endif %}
        {%- if item.funder is defined %}
          <p><strong>Funding agency:</strong> {{ item.funder }}</p>
        {%- endif %}
        {%- if item.committee is defined %}
          <p><strong>Committee:</strong> {{ item.committee }}</p>
        {%- endif %}
        {%- if item.advisor is defined %}
          <p><strong>Advisor:</strong> {{ item.advisor }}</p>
        {%- endif %}
        {%- if item.coadvisor is defined %}
          <p><strong>Co-advisor(s):</strong> {{ item.coadvisor }}</p>
        {%- endif %}
        {%- if item.award is defined %}
          <p><strong>Award:</strong> <a href="{{ item.award_link }}" target="_blank">{{ item.award }}</a></p>
        {%- endif %}
        {%- if item.award_amount is defined %}
          <p><strong>Amount:</strong> {{ item.award_amount }}</p>
        {%- endif %}
        {%- if item.journal is defined %}
          <p><strong>Journal:</strong> {{ item.journal }}</p>
        {%- endif %}
        {%- if item.conference is defined %}
          <p><strong>Conference:</strong> {{ item.conference }}</p>
        {%- endif %}
        {%- if item.about is defined %}
          <p><strong>About:</strong> {{ item.about }}</p>
        {%- endif %}
        {%- if item.roles is defined %}
          <p><strong>Roles:</strong>
          <ul>
          {%- for role in item.roles %}
            <li>{{ role.date }}: {{ role.title }}</li>
          {%- endfor %}
          </ul>
        {%- endif %}
        {%- if item.citation is defined %}
          <p><strong>Citation:</strong> {{ item.citation}}</p>
        {%- endif %}
        {%- if item.abstract is defined %}
          <p><strong>Abstract:</strong> {{ item.abstract }}</p>
        {%- endif %}
      </div>
    </details>
  </div>
  {%- endfor %}
  <p class="">
    <a href="#navigation">
      <i class="far fa-arrow-alt-circle-up" aria-hidden="true"></i>
      Back to the top
    </a>
  </p>
{%- endfor %}
