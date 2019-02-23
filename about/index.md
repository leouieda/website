---
title: About
layout: page
content:
    - phd
    - masters
    - bachelors
banner: monte-roraima.jpg
banner_description: "Hiking Monte Roraima in the border of Brazil and Venezuela."
---


{% from "utils.html" import fa, ai %}

# TL;DR

<div class="row">
<div class="col-md-6">
<ul>
<li>Brazilian geophysicist and open-sourceror living abroad.</li>
<li>Researching gravity and magnetic inverse problems.</li>
<li>Building open-source software like
    <a href="http://www.tesseroids.org">Tesseroids</a>,
    <a href="https://www.fatiando.org">Fatiando a Terra</a>,
    and a <a href="https://www.pygmt.org">Python wrapper for GMT</a>.
</li>
<li>Hiker, traveler, ukulele player, sourdough bread baker.</li>
</ul>
</div>
<div class="col-md-6">
<img src="/images/banner/valley-of-fire.jpg"
     title="Overlooking the Valley of Fire national park in Nevada, USA"
     style="">
</div>
</div>

# Summary

Geophysicist researching methods for determining the inner structure of the Earth from
geophysical observations, mainly disturbances in the Earth's gravity and magnetic
fields.
Developer of open-source software for processing, modeling, and visualizing geophysical
data.
Advocate for openness in the scientific process and the adoption of best practices in
computational research.

# Curriculum Vitae

I keep a PDF version of my CV in a more traditional format.
It is typeset in Latex using a custom open-source template.
The source is available on the Github repository
[leouieda/cv](https://github.com/leouieda/cv).

<a href="https://www.leouieda.com/cv/leonardo_uieda_cv.pdf" target="_blank" type="application/pdf" rel="external noopener noreferrer"><i class="fa fa-file-pdf-o"></i> Download Curriculum Vitæ</a>


# Around the internet

I post about my research on social networking sites and have a moderate
presence on Twitter (links at the top of the page).
Most of my research output is available around the internet, usually through
Github repositories.
You can find me and my research, code, articles, and data at:

<ul class="fa-ul">

<li><i class="fa-li fa fa-github fa-fw"></i>
<a href="https://github.com/leouieda">Github</a>:
<em>software projects, repositories for papers and talks</em>
</li>

<li><i class="fa-li ai ai-orcid fa-fw"></i>
<a href="http://orcid.org/0000-0001-6123-9515">ORCID</a> ( 0000-0001-6123-9515 ):
<em>aggregates all of my scientific output that have DOIs</em>
</li>

<li><i class="fa-li ai ai-impactstory fa-fw"></i>
<a href="https://impactstory.org/u/0000-0001-6123-9515">ImpactStory</a>:
<em>hub for article level metrics and further impact of research</em>
</li>

<li><i class="fa-li ai ai-google-scholar fa-fw"></i>
<a href="http://scholar.google.com.br/citations?user=qfmPrUEAAAAJ">Google Scholar</a>:
<em>the best source of citation information</em>
</li>

<li><i class="fa-li ai ai-figshare fa-fw"></i>
<a href="http://figshare.com/authors/Leonardo%20Uieda/97471">figshare</a>:
<em>where I publish most supplemental material, slides, posters</em>
</li>

<li><i class="fa-li ai ai-publons fa-fw"></i>
<a href="https://publons.com/a/1328468/">Publons</a>:
<em>registry for my peer-review contributions</em>
</li>

<li><i class="fa-li ai ai-researchgate fa-fw"></i>
<a href="https://www.researchgate.net/profile/Leonardo_Uieda">ResearchGate</a>:
<em>academic social network</em>
</li>

<li><i class="fa-li ai ai-lattes fa-fw"></i>
<a href="http://lattes.cnpq.br/8939551682050504">Currículo Lattes</a>:
<em>Brazilian online resume</em>
</li>

</ul>


# Experience

## Visiting Research Scientist

<ul class="fa-ul">
    <li><i class="fa-li fa fa-calendar fa-fw"></i>
        Feb 2017 - Present
    </li>
    <li><i class="fa-li fa fa-university fa-fw"></i>
        Department of Earth Sciences -
        SOEST -
        <a href="http://www.soest.hawaii.edu/GG/index.html">University of
        Hawai'i at Mānoa</a>
    </li>
    <li><i class="fa-li fa fa-info-circle fa-fw"></i>
        I came to UH on <a href="/blog/hawaii-gmt-postdoc.html">a
        postdoc scholarship</a> to build a Python wrapper and high-level API
        for the <a href="http://gmt.soest.hawaii.edu/">Generic Mapping Tools
        (GMT)</a>.
    </li>
</ul>

## Assistant Professor of Geophysics

<ul class="fa-ul">
    <li><i class="fa-li fa fa-calendar fa-fw"></i>
        Feb 2014 - Feb 2018
    </li>
    <li><i class="fa-li fa fa-university fa-fw"></i>
        Departamento de Geologia Aplicada -
        Faculdade de Geologia -
        <a href="http://www.uerj.br">Universidade do Estado do Rio de Janeiro (UERJ)</a>
    </li>
    <li><i class="fa-li fa fa-info-circle fa-fw"></i>
        At UERJ, I developed and taught the
        <a href="/teaching/geofisica1.html">Geophysics 1 (Gravity and
        Magnetics)</a> and
        <a href="/teaching/geofisica2.html">Geophysics 2 (Seismology)</a>
        courses for the Geology program, the
        <a href="/teaching/matematica-especial.html">Special Mathematics 1
        (Programming and Numerical Methods)</a> course for the Oceanography
        program, and <a href="/teaching">a range of short courses</a>.
    </li>
</ul>


# Education

<div>
    {%- for edu in this.content -%}
        <h3><a href="{{ edu.url }}">{{ edu.title }}  »</a></h3>
        <ul class="fa-ul">
            <li><i class="fa-li fa fa-calendar fa-fw"></i>
                {{ edu.start_date.year}}-{{ edu.date.year }}
            </li>
            <li><i class="fa-li fa fa-university fa-fw"></i>
                {{ edu.institution }}
            </li>
            <li><i class="fa-li fa fa-graduation-cap fa-fw"></i>
                Advisor: {{ edu.advisor }}
            </li>
            <li><i class="fa-li fa fa-book fa-fw"></i>
                Thesis: {{ edu.thesis }}
            </li>
        </ul>
    {%- endfor -%}
</div>
