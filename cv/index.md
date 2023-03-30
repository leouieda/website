---
title: CV
banner_image: images/anatolia-himalayas-topography.jpg
banner_position: top left
banner_title: Curriculum Vitæ
banner_subtitle: A record of my professional activity
thumbnail: images/thumbnail/default.png
template: base.html
---

{% import "macros.html" as macros %}

<div class="callout callout-note mt-3">

**Looking for a summary?** I keep a short-form CV somewhat updated:
<a class="nowrap" href="https://www.leouieda.com/cv/leonardo_uieda_cv_summary.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer">
<i class="fa fa-download" aria-hidden="true"></i>
Download the PDF
</a>

**Curious about the CV template?** It's typeset in LaTeX and the source is
available from the GitHub repository
<a class="nowrap" href="https://github.com/leouieda/cv"><i class="mx-1 fab fa-github" aria-hidden="true"></i><code>leouieda/cv</code></a>.

</div>

## Professional Appointments

{{ macros.cv_section(page.work, site.author_names, section_id="edu") }}

## Education

{{ macros.cv_section(page.edu, site.author_names, section_id="edu") }}
