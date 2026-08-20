---
layout: page
title: Code
---

I will do my best to include all in-class coding examples here. If there is something missing, email me.

<ul>
{% assign snippets = site.static_files | where_exp: "f", "f.path contains '/code/'" | sort: "name" %}
{% for snippet in snippets %}
  <li><a href="{{ snippet.path | relative_url }}">{{ snippet.basename }}{{ snippet.extname }}</a></li>
{% endfor %}
</ul>
