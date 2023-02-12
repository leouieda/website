---
title: Publications
banner_image: images/pacific-bathymetry.jpg
banner_position: top left
banner_title: Publications
banner_subtitle: A full list of all of my academic publications
enable_alm: true
thumbnail: images/thumbnail/publications.png
template: base.html
sections:
    - [preprints, Preprints]
    - [papers, Papers]
    - [proceedings, Conference proceedings]
    - [other, Other publications]
---

{%- import "macros.html" as macros %}

{{ macros.publication_sections(page.sections, page, config.coauthors) }}
