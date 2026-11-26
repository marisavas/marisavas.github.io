---
layout: page
title: Publications
permalink: /publications/
custom_css:
  - styles-global
---

<h1>Publications</h1>

<p class="page-note">Full list with citation counts on <a href="https://scholar.google.com/citations?user=e5IvuJgAAAAJ">Google Scholar</a>.</p>

<nav class="page-index" aria-label="Sections">
  <ul>
    {% for section in site.data.publications %}
    <li><a href="#{{ section.key }}">{{ section.label }}</a></li>
    {% endfor %}
    <li><a href="#patents">Patents</a></li>
  </ul>
</nav>

{% for section in site.data.publications %}
<section id="{{ section.key }}" aria-labelledby="{{ section.key }}-title">
  <h2 id="{{ section.key }}-title">{{ section.label }}</h2>
  <ul class="dated pubs">
    {% assign prev_year = "" %}
    {% for e in section.entries %}
    <li>
      <time>{% if e.year != prev_year %}{{ e.year }}{% endif %}</time>
      <div>
        <span class="pub-title">{% if e.url != "" %}<a href="{{ e.url }}">{{ e.title }}</a>{% else %}{{ e.title }}{% endif %}</span>
        <span class="pub-authors">{% for a in e.authors %}{% if a.me %}<strong>{{ a.name }}</strong>{% else %}{{ a.name }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}</span>
        <span class="pub-venue">{{ e.venue }}{% if e.award != "" %} <span class="pub-award">{{ e.award }}</span>{% endif %}</span>
      </div>
    </li>
    {% assign prev_year = e.year %}
    {% endfor %}
  </ul>
</section>
{% endfor %}

<section id="patents" aria-labelledby="patents-title">
  <h2 id="patents-title">Patents</h2>
  <p class="page-note">{{ site.data.patents.granted | size }} granted US patents, filed at IBM Research.</p>
  <ul class="dated pubs">
    {% assign prev_year = "" %}
    {% for p in site.data.patents.granted %}
    <li>
      <time>{% if p.year != prev_year %}{{ p.year }}{% endif %}</time>
      <div>
        <span class="pub-title">{{ p.title }}</span>
        <span class="pub-venue">{{ p.number }}</span>
      </div>
    </li>
    {% assign prev_year = p.year %}
    {% endfor %}
  </ul>

  {% if site.data.patents.pending %}
  <h3 class="sub">Pending</h3>
  <ul class="dated pubs">
    {% for p in site.data.patents.pending %}
    <li>
      <time>{{ p.year }}</time>
      <div>
        <span class="pub-title">{{ p.title }}</span>
        <span class="pub-venue">{{ p.number }}</span>
      </div>
    </li>
    {% endfor %}
  </ul>
  {% endif %}
</section>