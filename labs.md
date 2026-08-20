---
layout: page
title: Labs
---

Lab assignments, posted here as PDFs. I will do my best to keep this consistent with Canvas, but you should default to what is on Canvas.

<ul>
{% assign labs = site.static_files | where_exp: "f", "f.path contains '/labs/'" | sort: "name" %}
{% for lab in labs %}
  <li><a href="{{ lab.path | relative_url }}">{{ lab.basename }}{{ lab.extname }}</a></li>
{% endfor %}
</ul>
