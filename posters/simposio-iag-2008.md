---
title: Utilização de tesseróides na modelagem de dados de gradiometria gravimétrica
author: uieda, ussami
date: 2008-03-01
repository: leouieda/simposio-iag-2008
license: Creative Commons Attribution
poster: 10.6084/m9.figshare.4779760
event: XIII Simpósio de Iniciação Científica do IAG-USP
thumbnail: simposio-iag-2008.png
alm: true
layout: publication
tags: tesseroids, gravity, forward-modeling
---

# About

![The poster](/images/poster-simposio-iag-2008.jpg)

This is the first poster I presented about my [undergraduate
research][/about/bachelors] on forward modeling with tesseroids (spherical
prisms). This would eventually become the software
[Tesseroids](http://www.tesseroids.org), the paper [/papers/paper-tesseroids-2016],
and a part of my [PhD thesis][/about/phd].


# Abstract

A ESA (European Space Agency) planeja lançar no outono de 2008 a missão GOCE
(Gravity field and steady-state Ocean Circulation Explorer). A missão foi
planejada para medir o campo gravitacional da Terra com acurácia e resolução
sem precedentes. Para isso, fará uso de um gradiômetro de gravidade
eletrostático que consiste de três pares de acelerômetros idênticos mutuamente
ortogonais. O GOCE fornecerá dados do tensor gradiente da gravidade (TGG) a uma
altitude de órbita de aproximadamente 250 km.

Está sendo desenvolvido um programa computacional para analisar dados do TGG
sobre as bacias sedimentares brasileiras. O programa utilizará o método da
Quadratura Gauss-Legendre para efetuar a modelagem direta do TGG gerado por
feições ou corpos geológicos com geometria esférica. A modelagem será feita
discretizando o corpo por tesseróides, também denominados prismas esféricos. Os
tesseróides são segmentos de uma casca esférica de espessura finita limitados
por linhas de grade geográficas. A geometria dos tesseróides possibilita a
construção de modelos levando em conta a curvatura da Terra. Isto se torna
importante na modelagem de corpos geológicos com grande extensão lateral, como
por exemplo, a bacia do Paraná. Será criado um modelo de densidade desta bacia
a partir de dados de poços e dados sísmicos e utilizaremos o programa
desenvolvido para obter estimativas do TGG. As estimativas serão comparadas com
os futuros dados do GOCE na tentativa de separar o componente gravimétrico
associado às variações de densidade na parte mais profunda da bacia.
