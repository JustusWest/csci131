---
layout: page
title: Lecture Notes
---

{%- comment -%}
  Lectures dated in the future are excluded from the build (see `future:
  false` in _config.yml), so they'd 404 if linked. Filter them out of this
  index too, otherwise the last one written still shows a dead link right up
  until its date arrives.
{%- endcomment -%}
{%- assign visible_lectures = site.lectures | where_exp: "l", "l.date <= site.time" -%}

<ul>
{% for lecture in visible_lectures %}
  <li><a href="{{ lecture.url | relative_url }}">{{ lecture.title }}</a></li>
{% endfor %}
</ul>
