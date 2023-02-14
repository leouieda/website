---
title: Presentations
banner_image: images/amazon-delta.jpg
banner_position: bottom left
banner_title: Presentations
banner_subtitle: Slides, posters, abstracts, and recordings of my presentations
thumbnail: images/thumbnail/presentations.png
template: base.html
sections:
    - [invited, Invited conference presentations]
    - [seminars, Department seminars]
    - [conferences, Conference presentations]
    - [other, Other]
---

{%- import "macros.html" as macros %}

{{ macros.publication_sections(page.sections, page, config.coauthors) }}
