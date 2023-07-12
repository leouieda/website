---
title: CV
banner_image: images/anatolia-himalayas-topography.jpg
banner_title: Curriculum Vitæ
banner_subtitle: My academic CV, with most things I ever did
thumbnail: images/thumbnail/default.png
template: base.html
sections:
    - [work, Professional Appointments]
    - [community, Community Service]
    - [edu, Education]
    - [grants, Grants & Fellowships]
---

{% import "macros.html" as macros %}

<div class="callout callout-note mt-4">

**Looking for a career summary?**
I keep a short-form CV somewhat updated in PDF format:
<a class="nowrap" href="https://github.com/leouieda/cv/raw/pdf/leonardo_uieda_cv_summary.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer"><i class="fa fa-download" aria-hidden="true"></i> Download the PDF</a>.
It's typeset in LaTeX and the source is available from the GitHub repository:
<a class="nowrap" href="https://github.com/leouieda/cv"><i class="mx-1 fab fa-github" aria-hidden="true"></i><code>leouieda/cv</code></a>.

</div>

<div class="callout mt-4">

<i class="fa fa-tools me-1" aria-hidden="true"></i>
**This is a work in progress.** I'm currently migrating information from the
<a class="nowrap" href="https://github.com/leouieda/cv/raw/pdf/leonardo_uieda_cv.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer">PDF version</a>
of my CV. This HTML version should be more accessible and easier to maintain.

</div>

{%- for data, title in page.sections %}
  <h2 id="data">{{ title }}</h2>
  {%- for item in page[data] %}
  <div>
  <p>
  <span class="text-muted font-small">{{ item.year }}</span>:
  <strong>{{ item.title|trim }}.</strong>
  {%- if item.institution is defined %}
  <span class="text-muted">
  {{ item.institution|trim }}{%- if item.country is defined %}, {{ item.country }}{%- endif %}.
  </span>
  {%- endif %}
  </p>
  <details class="flow flow-small">
  <summary>More information</summary>
  {%- if item.department is defined %}
    <p><strong>Department:</strong> {{ item.department }}</p>
  {%- endif %}
  {%- if item.funder is defined %}
    <p><strong>Funding agency:</strong> {{ item.funder }}</p>
  {%- endif %}
  {%- if item.authors is defined %}
    <p><strong>Authors:</strong>
      {%- for author in item.authors %}
        {%- if author == "Me" %}
          <span class="authors-me">{{ config.coauthors[author] }}</span>
        {%- else %}
          {{ config.coauthors[author] }}
        {%- endif %}
        {%- if not loop.last -%},{%- endif -%}
      {%- endfor %}
    </p>
  {%- endif %}
  {%- if item.doi is defined %}
    <p><strong>doi:</strong>
    <a href="https://doi.org/{{ item.doi }}" target="_blank">{{ item.doi }}</a>
    </p>
  {%- endif %}
  {%- if item.github is defined %}
    <p><strong>GitHub:</strong>
    <a href="https://github.com/{{ item.github }}" target="_blank">{{ item.github }}</a>
    </p>
  {%- endif %}
  {%- if item.slides is defined %}
    <p><strong>Slides:</strong>
    <a href="{{ item.slides }}" target="_blank">{{ item.slides }}</a>
    </p>
  {%- endif %}
  {%- if item.thesis is defined %}
    <p><strong>Thesis:</strong> {{ item.thesis }}</p>
  {%- endif %}
  {%- if item.advisor is defined %}
    <p><strong>Advisor:</strong> {{ item.advisor }}</p>
  {%- endif %}
  {%- if item.award is defined %}
    <p><strong>Award:</strong>
    <a href="{{ item.award_link }}" target="_blank">{{ item.award }}</a>
    </p>
  {%- endif %}
  {%- if item.award_amount is defined %}
    <p><strong>Amount:</strong> {{ item.award_amount }}</p>
  {%- endif %}
  {%- if item.about is defined %}
    <p><strong>About:</strong> {{ item.about }}</p>
  {%- endif %}
  {%- if item.roles is defined %}
    <p><strong>Roles:</strong>
    <ul>
    {%- for role in item.roles %}
      <li>{{ role["date"] }}: <strong>{{ role["title"] }}</strong></li>
    {%- endfor %}
    </ul>
  {%- endif %}
  {%- if item.abstract is defined %}
    <p><strong>Abstract:</strong> {{ item.abstract }}</p>
  {%- endif %}
  </details>
  </div>
  {%- endfor %}
{%- endfor %}
