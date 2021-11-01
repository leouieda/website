---
title: Contact
banner_image: images/liverpool-clock-tower.jpg
banner_position: top left
banner_title: Contact
banner_subtitle: How to reach me online and offline
template: base.html
---

<section class="mb-5">

## Online

These are best ways to reach me online:

<ul class="fa-ul my-4">
  <li><i class="fa-li fa fa-envelope fa-fw" aria-hidden="true"></i>
  <a href="mailto:Leonardo.Uieda@liverpool.ac.uk">Leonardo.Uieda@liverpool.ac.uk</a>
  </li>
  <li><i class="fa-li fab fa-twitter fa-fw" aria-hidden="true"></i>
  <a href="https://twitter.com/leouieda">@leouieda</a> on Twitter
  </li>
  <li><i class="fa-li fab fa-slack fa-fw" aria-hidden="true"></i>
  On the <a href="https://softwareunderground.org/">Software Underground</a>
  Slack
  </li>
</ul>

Find out more about me and my work at:

{%- macro social_button(link, icon, name) -%}
  <a class="btn btn-light me-2 mb-3" target="_blank" href="{{ link }}"><i class="{{ icon }} me-1" aria-hidden="true"></i> {{ name }}</a>
{%- endmacro -%}

<div id="social-links">
{{ social_button("https://github.com/" ~ config.github, icon="fab fa-github", name="GitHub") }}
{{ social_button(config.linkedin, icon="fab fa-linkedin", name="LinkedIn") }}
{{ social_button(config.youtube, icon="fab fa-youtube", name="YouTube") }}
{{ social_button("https://orcid.org/" ~ config.orcid, icon="ai ai-orcid", name="ORCID") }}
{{ social_button("https://profiles.impactstory.org/u/" ~ config.orcid, icon="ai ai-impactstory", name="ImpactStory") }}
{{ social_button("http://figshare.com/authors/Leonardo%20Uieda/97471", icon="ai ai-figshare", name="figshare") }}
{{ social_button(config.googlescholar, icon="ai ai-google-scholar", name="Google Scholar") }}
{{ social_button(config.publons, icon="ai ai-publons", name="Publons") }}
{{ social_button(config.researchgate, icon="ai ai-researchgate", name="ResearchGate") }}
</div>

</section>
<section>

## At the University of Liverpool

My office is in the Jane Herdman Building - Room A2.06 (second floor of the
annex).
You probably want to **email me first** to make sure I'm in the office (I work
from home some days of the week).

Here is the full address:

> Dr. Leonardo Uieda
> <br>
> Jane Herdman Building
> <br>
> 4 Brownlow Street
> <br>
> Liverpool, United Kingdom
> <br>
> L69 3GP

</section>
