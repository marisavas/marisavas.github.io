---
layout: page
title: "Publications"
permalink: /publications/
custom_css:
  - styles-global
  - styles-publications
---



<main class="container-publications">

  <div class="cards-row">

    <!-- Conferences -->
    <div class="publication-card">
      <h2><i class="fa-solid fa-microphone"></i> Conferences</h2>
      <ul class="publication-list" id="conferences-list"></ul>
      <div class="pagination">
        <button id="conferences-prev" class="btn-pagination" style="display:none">Previous</button>
        <button id="conferences-next" class="btn-pagination primary">Next</button>
      </div>
      <script type="application/json" id="conferences-data">
        {{ site.data.publications | jsonify | replace: '</', '<\/' }}
      </script>
    </div>

    <!-- Journals -->
    <div class="publication-card">
      <h2><i class="fa-solid fa-book-open"></i> Journals</h2>
      <ul class="publication-list" id="journals-list"></ul>
      <div class="pagination">
        <button id="journals-prev" class="btn-pagination" style="display:none">Previous</button>
        <button id="journals-next" class="btn-pagination primary">Next</button>
      </div>
      <script type="application/json" id="journals-data">
        {{ site.data.journals | jsonify | replace: '</', '<\/' }}
      </script>
    </div>

    <!-- Patents -->
    <div class="publication-card">
      <h2><i class="fa-solid fa-lightbulb"></i> Patents</h2>
      <ul class="publication-list" id="patents-list"></ul>
      <div class="pagination">
        <button id="patents-prev" class="btn-pagination" style="display:none">Previous</button>
        <button id="patents-next" class="btn-pagination primary">Next</button>
      </div>
      <script type="application/json" id="patents-data">
        {{ site.data.patents | jsonify | replace: '</', '<\/' }}
      </script>
    </div>

  </div>

</main>

<script src="{{ '/assets/js/publications.js' | relative_url }}"></script>
