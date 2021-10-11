---
title: Publications
banner_image: images/arctic-bathymetry.jpg
banner_position: top left
banner_title: Publications
banner_subtitle: A full list of all of my academic publications
template: base.html
---

{%- import "macros.html" as macros %}

{%- if page.review %}
<section>

## Under review

{{ macros.make_publication_list(page.review, base_id="review") }}

</section>

<hr class="mb-5">
{%- endif %}

<section>

## Published

{{ macros.make_publication_list(page.papers, base_id="papers") }}

</section>
