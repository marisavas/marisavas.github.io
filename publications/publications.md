---
layout: default
title: Publications
tags:
categories: publications
future: true
permalink: /publications/

---



<style>



body {
  background-color: #efe9e4;
}


  .bottom-three {
     margin-bottom: 5px;
     margin-top:7px;
  }

   ol.bibliography li {
    list-style-type: none;
    margin: 0;
    padding: 0;
 }

 ol.bibliography li:before {
      list-style-type: none;
      content: "";
      color: blue;

}

  button {
     font-size: 14px;
  }

  .my_text{
      font-size: 14px;
  }

  .leftcell{
    float: left;
    text-align:right;
  }
  .rightcell{
   float: left;
   text-align: left;
   font-size: 14px;
   padding-left: 5px; /* give some spacing here to fake cell padding */
}

.font_bib
{
  font-family: "Open Sans",Helvetica Neue,Helvetica,Arial,sans-serif;
  font-size: 15px;
  line-height: 28px;
  color: #404040;

}


</style>



<p style="position:absolute;top:67px;left:86px;white-space:nowrap" class="about02">PUBLICATIONS</p>
<!-- <header class="c-article__header">
<h1 class="c-article__title">{{page.title}}</h1>

</header> -->


<div class="c-article__footer u-clearfix"> <!-- barra de links -->
<div class="c-article__tag">
<a href="#conferences">#conferences</a>&nbsp;<a href="#journals">#journals</a> <a href="#patents">#patents</a> <a href="#awards">#awards</a> <a href="#professional_service">#professional Service</a>&nbsp;<a href="#talks">#talks</a>&nbsp;
</div></div>

<style>
th, td{
text-align: left;
padding: 5px 10px;
border-bottom: 1px solid #e5e5e5;
}

h4 {
   color:#494949;
   font-size:20px;
   font-family:"Volkhov","Times New Roman",Times,serif;
   font-weight:400;
   line-height:initial;
   position:relative;
   left:86px;
}

tbody > tr:last-child > td {
  border-bottom: 0;
}
</style>
<div class=".c-wrap-content font_bib" style="position:absolute;top:150px">
<table>

<tr><td>
<a id="conferences"><h4>Conferences</h4></a>
{% bibliography --file publications %}
</td></tr>

<tr><td>
<br>
<a id="journals"><h4>Journals</h4></a>
{% bibliography --file journals %}
</td></tr>

<tr><td>
<br>
<a id="patents">
<h4>Patents</h4></a>  
{% bibliography --file patents --sort_by year,month --order descending %}
</td></tr>

<tr><td>
<br><a id="awards">
<h4>Awards/Honors</h4></a>
<ol class="bibliography">
{% for award in site.data.services.awards %}
<li>
<div style="width:1100px;">
<div style="float:left;position:relative;width:200px;text-align:left;font-size:16px;padding-left:80px;">{{award.date}}</div>
<div style="float:left;position:relative;width:900px;text-align:left;font-size:16px;padding-left:50px;line-height:20px;padding-bottom:20px">{{award.description}}</div>

</div>

<p class="bottom-three" style="margin-bottom:20px">&nbsp;</p>
{% unless forloop.last %}<div style= "border: 1px solid #e5e5e5"> </div>{% endunless %}
</li>
{% endfor %}
</ol>
</td>
</tr>

<tr><td>
<br>
<a id="professional_service">
<h4>Professional Service</h4></a>
<ol class="bibliography">
{% for service in site.data.services.roles %}
<li>
<div style="width:1130px;">
<div style="float:left;position:relative;width:230px;text-align:left;font-size:16px;padding-top:10px;padding-left:80px;">{{service.name}}</div>
<div style="float:left;position:relative;width:900px;text-align:left;font-size: 16px;padding-left:20px;line-height:20px;">
{% for description in service.description %}
{{description.text}}
<br>
{% endfor %}
</div>
</div>
<p class="bottom-three">&nbsp;</p>
{% unless forloop.last %}<div style= "border: 1px solid #e5e5e5"> </div>{% endunless %}
</li>
{% endfor %}

</ol>
</td></tr>



<tr><td>
<br><a id="talks">
<h4>Talks</h4></a>
<ol class="bibliography">
{% for talk in site.data.services.talks %}
<li>
<div style="width:1130px;">
<div style="float:left;position:relative;width:230px;text-align:left;font-size:16px;padding-left:80px;">{{talk.date}}</div>
<div style="float:left;position:relative;width:900px;text-align:left;font-size:16px;padding-left:20px;line-height:20px;">{{talk.title}}
</div>
</div>
<p class="bottom-three">&nbsp;</p>
{% unless forloop.last %}<div style= "border: 1px solid #e5e5e5"> </div>{% endunless %}
</li>
{% endfor %}
</ol>
</td>
</tr>




</table>
</div>
