---
title: Introduction to Python Workshop (UH Manoa - G&G)
date: 2017-04-17
institution: Department of Geology and Geophysics - University of Hawaii at Manoa
course: short
repository: leouieda/python-hawaii-2017
thumbnail: python-hawaii-2017.png
license: CC-BY
layout: publication
---

# About

This was a 3-day workshop held at the Department of Geology and Geophysics of
the University of Hawaii at Manoa.
It covers the basics of computer programming with Python, starting from the
very beginning.
The workshop had no prerequisites and it was a bit challenging to balance
people who have never programmed before with veteran programmers who are new to
Python.

Below is some information about the workshop, the demographics of people who
signed up,
and the feedback that I got from the participants.


# Goals

I wanted this to be a hands-on workshop of the basic concepts needed to use
Python for research. Participants who complete the workshop should be able to
use Python to gather data from one or more files, process the data, run an
analysis, make publication quality figures, and save the output.


# Materials

The class is based on a mixture of the
[Software Carpentry](https://software-carpentry.org/)
lessons
[Plotting and Programming in Python (under development)](http://swcarpentry.github.io/python-novice-gapminder/)
and [Programming with Python](http://swcarpentry.github.io/python-novice-inflammation).
However, I use temperature data from
[Berkeley Earth](http://berkeleyearth.org/)
instead of the [Gapminder](http://www.gapminder.org/) and inflammation data
used by Software Carpentry.
For example, our goal for the second day of the workshop is to reproduce the
figure for
[average temperature in Hawaii](http://berkeleyearth.lbl.gov/regions/hawaii)
from the website:


[![](http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Figures/hawaii-TAVG-Trend.png)](http://berkeleyearth.lbl.gov/regions/hawaii)


I also used a few techniques from the
[Software Carpentry Instructor Training](http://swcarpentry.github.io/instructor-training/),
mainly the shared class notes (I used Google Docs instead of Etherpad)
and colored sticky notes.
The sticky notes were in two colors: pink and blue.
Learners kept the blue sticky note on their laptop lid if everything was OK.
They put up the pink one if they have a problem or need help.
This way me and the teaching assistants can know at a glance who needs help.
I also had them write positive and negative feedback on the sticky notes at the
end of the workshop.


# Who attended

The file
[`demographics.csv`](https://github.com/leouieda/python-hawaii-2017/blob/master/demographics.csv)
in the Github repository has anonymous information about everyone who signed up
for the workshop.
An analysis of this data and code to generate the figures below using
[pandas](http://pandas.pydata.org/) and [matplotlib](http://matplotlib.org/)
is available in the
[`demographics-analysis.ipynb`](http://nbviewer.jupyter.org/github/leouieda/python-hawaii-2017/blob/master/demographics-analysis.ipynb)
Jupyter notebook (also in the Github repo).


![Number of attendants per day of the workshop.](/images/python-hawaii-2017/attendance.jpg)

![](/images/python-hawaii-2017/education.jpg)

![](/images/python-hawaii-2017/programming-languages.jpg)

![](/images/python-hawaii-2017/position.jpg)


# Feedback

![Feedback on the colored sticky notes.](/images/python-hawaii-2017/sticky-note-feedback.jpg)

This is a synthesis from the feedback given by participants on the last day
(using the pink and blue sticky notes):

| The Good                                        | # | The Bad                                               | # |
|:------------------------------------------------|:--|:------------------------------------------------------|:--|
|Instructor style                                 | 5 | Too short                                             | 5 |
|Examples and exercises                           | 5 | Too fast                                              | 3 |
|Dense but efficient (learn a lot in little time) |	3 | Too slow                                              | 3 |
|Using real data                                  | 3 | Hard to multi-task (pay attention + notes + exercise) | 2 |
|Simple and accessible level                      | 3 | No TA on Monday                                       | 2 |
|Shared notes                                     | 1 | Instructor took too many tangents when teaching       | 1 |
|                                                 |   | Too many people                                       | 1 |
|                                                 |   | Ran late                                              | 1 |
|                                                 |   | Jupyter Google maps example failed                    | 1 |


# Lessons learned

I was glad to see that the hands-on approach worked and the students
appreciated using real data during the exercises.
We had very little time (6h total) to cover a lot of material.
So it's no wonder that people thought it was too short and maybe didn't explain
quite as thoroughly some concepts (like `for` and `if`).
Regarding the pace, it's hard to satisfy everyone.
I expect that novices might have found the pace a bit too fast and more
experienced programmers found it too slow (but I don't have data to back that
up).
Since only 6 people complained about the pace, I guess it wasn't too bad.
Not having a TA on Monday (the first day) was not good because that is when the
most serious problems occur (Jupyter won't start, where is my Python?, lost my
files, etc).
The next two days of the workshop were much smoother thanks to the generous
help of volunteer TAs Sam Murphy and Julie Schnurr.
We also didn't get to cover the last few topics on the last day (functions and
getting data from headers).
