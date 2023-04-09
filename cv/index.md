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

{{ macros.cv_sections(page.sections, page, config.coauthors) }}
