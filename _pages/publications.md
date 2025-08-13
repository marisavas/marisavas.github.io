---
layout: page
title: "Publications"
permalink: /publications/
custom_css:
  - styles_publications
---

<main class="container-publications">

  <div class="cards-row">

    <!-- Conferences -->
    <div class="publication-card" id="conferences-card">
      <h2>Conferences</h2>
        <ul class="publication-list" id="conferences-list"></ul>
        <div class="pagination">
            <button id="conferences-prev" class="prev" style="display:none">Previous</button>
            <button id="conferences-next" class='next'>Next</button>
        </div>
            
        <script type="application/json" id="conferences-data">
            {{ site.data.publications | jsonify }}
        </script>
    </div>
        
    <!-- Journals -->
    <div class="publication-card" id="journals-card">
      <h2>Journals</h2>
      <ul class="publication-list" id="journals-list"></ul>
      <div class="pagination">
        <button id="journals-prev" class="prev" style="display:none">Previous</button>
        <button id="journals-next" class='next'>Next</button>
      </div>
      <script type="application/json" id="journals-data">
        {{ site.data.journals | jsonify }}
      </script>
    </div>

    <!-- Patents -->
    <div class="publication-card" id="patents-card">
      <h2>Patents</h2>
      <ul class="publication-list" id="patents-list"></ul>
      <div class="pagination">
        <button id="patents-prev" class="prev" style="display:none">Previous</button>
        <button id="patents-next" class='next'>Next</button>
      </div>
      <script type="application/json" id="patents-data">
        {{ site.data.patents | jsonify }}
      </script>
    </div>
  </div>

</main>

<script src="{{ '/assets/js/publications.js' | relative_url }}"></script>
