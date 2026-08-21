---
layout: page
title: Labs
permalink: /labs/
---

Lab assignments and starter files, one page per lab. I will do my best to keep this consistent with Canvas, but you should default to what is on Canvas.

{%- comment -%}
  Lists every labs/<something>/index.md. The `where: "name", "index.md"` step
  is what keeps this page from listing itself.
{%- endcomment -%}

{%- assign lab_pages = site.pages | where: "name", "index.md" | where_exp: "p", "p.dir contains '/labs/'" | sort: "order" -%}

<ul class="lab-index">
{%- for lab in lab_pages %}
  <li>
    <a href="{{ lab.url | relative_url }}">{{ lab.title }}</a>
    {%- if lab.due %} <span class="lab-index-due">due {{ lab.due }}</span>{% endif %}
  </li>
{%- endfor %}
</ul>
