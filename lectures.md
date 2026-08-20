---
layout: page
title: Lecture Notes
---

<ul>
{% for lecture in site.lectures %}
  <li><a href="{{ lecture.url | relative_url }}">{{ lecture.title }}</a></li>
{% endfor %}
</ul>
