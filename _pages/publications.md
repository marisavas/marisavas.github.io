---
layout: page
title: "Publications"
permalink: /publications/
custom_css:
    - styles_publications
---


<div class="container-publications"></div>
<main>
   <section class="navbar-section">
        <div class="c-article__footer u-clearfix"> 
            <div class="c-article__tag">
                <a href="#conferences">#conferences</a>&nbsp;
                <a href="#journals">#journals</a>&nbsp;
                <a href="#patents">#patents</a>
            </div>
        </div>
    </section>
    <section class="publication-section">
        <a id="conferences">
            <h2 class="highlight">Conferences</h2>
        </a>
        {% bibliography --file publications %}
        <hr class="publication-section">        
    </section> 
    <section class="publication-section">
        <a id="journals">
            <h2 class="highlight">Journals</h2>
        </a>
                {% bibliography --file journals %}
        <hr class="publication-section">        
    </section>
    <section class="publication-section">
        <a id="patents">
            <h2 class="highlight">Patents</h2>
        </a>
            {% bibliography --file patents --sort_by year,month --order descending %}
    </section> 
    
    

</main>


