---
title: Contact
banner_image: images/amazon-delta.jpg
banner_position: center
banner_title: Contact
banner_subtitle: How to reach me online and offline
template: base.html
---

## Online

These are best ways to reach me online:

<ul class="fa-ul">
  <li>
    <i class="fa-li fa fa-envelope fa-fw" aria-hidden="true"></i>
    Email:
    <a href="mailto:{{ config.email }}">{{ config.email }}</a>
  </li>
  <li>
    <i class="fa-li fab fa-mastodon fa-fw" aria-hidden="true"></i>
    Mastodon:
    <a target="_blank" href="https://{{ config.mastodon_server }}/@{{ config.mastodon }}">{{ config.mastodon }}@{{ config.mastodon_server }}</a>
  </li>
  <li>
    <i class="fa-li fas fa-comment fa-fw" aria-hidden="true"></i>
    Matrix:
    <a target="_blank" href="https://matrix.to/#/{{ config.matrix }}">{{ config.matrix }}</a>
  </li>
  <li>
    <i class="fa-li fab fa-slack fa-fw" aria-hidden="true"></i>
    Slack:
    @leouieda on the <a target="_blank" href="{{ config.links.swung }}">Software Underground</a>
  </li>
  <li>
    <i class="fa-li fas fa-key fa-fw" aria-hidden="true"></i>
    GPG public key:
    <a href="../assets/leouieda.asc"><code>leouieda.asc</code></a>
  </li>
</ul>
