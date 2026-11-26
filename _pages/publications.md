---
layout: page
title: Publications
permalink: /publications/
custom_css:
  - styles-global
---

<h1>Publications</h1>

<p class="page-note">Selected work below. The full list is further down this page, on <a href="https://scholar.google.com/citations?user=e5IvuJgAAAAJ">Google Scholar</a> and in my CV.</p>

{% assign groups = "rai|Responsible AI and AI governance,sc|Social computing" | split: "," %}

<section aria-labelledby="selected-title">
  <h2 id="selected-title">Selected publications</h2>
  {% for g in groups %}
  {% assign parts = g | split: "|" %}
  {% assign key = parts[0] %}
  <h3 class="sub">{{ parts[1] }}</h3>
  <ul class="dated pubs">
    {% for e in site.data.publications.selected[key] %}
    <li>
      <time>{{ e.year }}</time>
      <div>
        <span class="pub-title">{% if e.url != "" %}<a href="{{ e.url }}">{{ e.title }}</a>{% else %}{{ e.title }}{% endif %}</span>
        <span class="pub-authors">{% for a in e.authors %}{% if a.me %}<strong>{{ a.name }}</strong>{% else %}{{ a.name }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}</span>
        <span class="pub-venue">{{ e.venue }}{% if e.award != "" %} <span class="pub-award">{{ e.award }}</span>{% endif %}</span>
        {% if e.note != "" %}<span class="pub-note">{{ e.note }}</span>{% endif %}
      </div>
    </li>
    {% endfor %}
  </ul>
  {% endfor %}
</section>

<section aria-labelledby="patents-title">
  <h2 id="patents-title">Patents</h2>
  <p class="page-note">{{ site.data.patents.granted | size }} granted US patents, filed at IBM Research.</p>
  <details class="all">
    <summary>Show all patents</summary>
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
      {% for p in site.data.patents.pending %}
      <li>
        <time>{{ p.year }}</time>
        <div>
          <span class="pub-title">{{ p.title }}</span>
          <span class="pub-venue">{{ p.number }}, pending</span>
        </div>
      </li>
      {% endfor %}
    </ul>
  </details>
</section>

<section aria-labelledby="all-title">
  <h2 id="all-title">All publications</h2>
  <details class="all">
    <summary>Show all publications</summary>
    {% for section in site.data.publications.sections %}
    <h3 class="sub">{{ section.label }}</h3>
    <ul class="dated pubs">
      {% assign prev_year = "" %}
      {% for e in section.entries %}
      <li>
        <time>{% if e.year != prev_year %}{{ e.year }}{% endif %}</time>
        <div>
          <span class="pub-title">{% if e.url != "" %}<a href="{{ e.url }}">{{ e.title }}</a>{% else %}{{ e.title }}{% endif %}</span>
          <span class="pub-authors">{% for a in e.authors %}{% if a.me %}<strong>{{ a.name }}</strong>{% else %}{{ a.name }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}</span>
          <span class="pub-venue">{{ e.venue }}{% if e.award != "" %} <span class="pub-award">{{ e.award }}</span>{% endif %}</span>
          {% if e.note != "" %}<span class="pub-note">{{ e.note }}</span>{% endif %}
        </div>
      </li>
      {% assign prev_year = e.year %}
      {% endfor %}
    </ul>
    {% endfor %}
  </details>
</section>