---
title: Publications
banner_image: images/pacific-bathymetry.jpg
banner_position: top left
banner_title: Publications
banner_subtitle: A full list of all of my academic publications
enable_alm: true
thumbnail: images/thumbnail/publications.png
template: base.html
---

{%- import "macros.html" as macros %}

## Preprints

{{ macros.publication_list(page.preprints, config.coauthors) }}

## Papers

{{ macros.publication_list(page.papers, config.coauthors) }}

## Other

{{ macros.publication_list(page.other, config.coauthors) }}

## Conference proceedings

{{ macros.publication_list(page.proceedings, config.coauthors) }}
