---
layout: page
title: Code
---

The programs from each lecture, one page per lecture, in the order we wrote them. Each program starts with a heading saying what it shows, and ends with the output it printed in class. To run one, copy it into a new file in IDLE and press **F5**. A few programs have mistakes in them on purpose, to show an error message.

Unit 6 programs need `anim.py` saved in the same folder as your program. Download it from the *Setup* line under Unit 6.

{% assign files = site.static_files | where_exp: "f", "f.path contains '/code/'" | sort: "path" -%}
{%- assign unit = "" -%}
{%- for f in files -%}
{%- assign parts = f.path | split: "/" -%}
{%- assign u = parts[2] -%}
{%- if u != unit -%}
{%- if unit != "" %}
</ul>
{%- endif %}
<h2>{% case u %}{% when "1-variables" %}Unit 1 — Variables, expressions and input{% when "2-conditionals" %}Unit 2 — Conditionals{% when "3-loops" %}Unit 3 — Loops{% when "4-sequences" %}Unit 4 — Strings and lists as sequences{% when "5-functions" %}Unit 5 — Functions{% when "6-animation" %}Unit 6 — Animation{% else %}{{ u }}{% endcase %}</h2>
<ul>
{%- assign unit = u -%}
{%- endif -%}
{%- if parts.size > 4 %}
<li>Setup: <a href="{{ f.path | relative_url }}" download>{{ f.name }}</a> (download)</li>
{%- else -%}
{%- assign lec = site.lectures | where: "slug", f.basename | first %}
<li><a href="{{ f.path | relative_url }}">{% if lec %}{{ lec.title }}{% else %}{{ f.basename }}{% endif %}</a>{% if lec %} · <a href="{{ lec.url | relative_url }}">notes</a>{% endif %}</li>
{%- endif -%}
{%- endfor %}
{% if unit != "" %}</ul>{% endif %}
