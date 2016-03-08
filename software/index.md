---
title: Software projects
layout: page
content:
    - fatiando
    - tesseroids
---

Most of my research work involves writing software. These are some of the
open-source packages I have developed.

{% from "utils.html" import card %}

{%- for row in this.content|batch(4) -%}
<div class="row">
    {%- for article in row -%}
        <div class="col-md-3 col-sm-3">
            {{ card(article, date=false) }}
        </div>
    {% endfor %}
</div>
{% endfor %}
