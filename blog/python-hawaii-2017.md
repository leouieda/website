---
title: Thoughts from the Introduction to Python Workshop at UH Manoa
date: 2017-04-28
---


Last week, I taught a 3-day Python workshop at the
[Department of Geology and Geophysics of the University of Hawaii at
Manoa](http://www.soest.hawaii.edu/GG/index.html),
where I'm currently [doing a postdoc](/blog/hawaii-gmt-postdoc.html).
It covered the basics of computer programming with Python, starting from the
very beginning.
Below are thoughts and information about the workshop, the demographics of
people who signed up, and the feedback that I got from the participants.

See the [GitHub repository](https://github.com/leouieda/python-hawaii-2017) for
more information and links to material used.


## My goals

I wanted this to be a hands-on workshop of the basic concepts needed to use
Python for research. Participants who complete the workshop should be able to
use Python to gather data from one or more files, process the data, run an
analysis, make publication quality figures, and save the output.
Most importantly, I wanted participants to know what they should type into
Google to learn more about Python.


## Materials

The class is based on a mixture of the
[Software Carpentry](https://software-carpentry.org/)
lessons
[Plotting and Programming in Python (under development)](http://swcarpentry.github.io/python-novice-gapminder/)
and [Programming with Python](http://swcarpentry.github.io/python-novice-inflammation).
However, I use temperature data from
[Berkeley Earth](http://berkeleyearth.org/)
instead of the [Gapminder](http://www.gapminder.org/) and inflammation data
used by Software Carpentry.
For example, our goal for the second day of the workshop was to reproduce the
figure for
[average temperature variation in Hawaii](http://berkeleyearth.lbl.gov/regions/hawaii)
from the [Berkeley Earth](http://berkeleyearth.lbl.gov/regions/hawaii) website.

On the last day, we finished with some code that processed a list of country
names to download the respective data file (using `requests`), load it into
Python, make a figure, and save it to a different folder
(see [this Jupyter notebook for the
code](https://github.com/leouieda/python-hawaii-2017/blob/master/notebooks/exercise-download-a-bunch-of-data.ipynb)).

I also used a few techniques from the
[Software Carpentry Instructor Training](http://swcarpentry.github.io/instructor-training/),
mainly the shared class notes (I used Google Docs instead of Etherpad)
and colored sticky notes.
The sticky notes were in two colors: pink and blue.
Learners kept the blue sticky note on their laptop lid if everything was OK.
They put up the pink one if they have a problem or need help.
This way, myself and the teaching assistants can know at a glance who needs
help.
I had them write positive and negative feedback on the sticky notes at the
end of the workshop.

The notebooks that I created during class and some notes for myself are in the
GitHub repository (in the `notebooks` and `notes` folders, respectively).


## Who attended

I asked all participants to sign up through a Google Form that asked a few
questions regarding their operating system, background in programming, and
position at the university.
The file
[`demographics.csv`](https://github.com/leouieda/python-hawaii-2017/blob/master/demographics.csv)
in the GitHub repository has the anonymous information from this form.
I wrote some code to analyze the data and generate the figures below using
[pandas](http://pandas.pydata.org/) and [matplotlib](http://matplotlib.org/).
You can find in the
[`demographics-analysis.ipynb`](http://nbviewer.jupyter.org/github/leouieda/python-hawaii-2017/blob/master/demographics-analysis.ipynb)
Jupyter notebook (also in the GitHub repo).

First, lets look at how many people signed up and then actually attended each
day.

![Number of attendants per day of the workshop.](/images/python-hawaii-2017/attendance.jpg)

We were very lucky that most people who signed up also attended the workshop on
the first day, even though there was no sign up fee.
It seems that the workshop really fills a need in the community!
Some people gave up after the first day.
Maybe it was too fast, or too basic, or life just happened.
I can't really tell because I failed to collect feedback at the end of each
day.
That is something to keep in mind for the next iteration: **get feedback every
day**.

![Prior education of attendants](/images/python-hawaii-2017/education.jpg)

The experience level of participants was more evenly distributed than I
expected.
I was very pleased with the number of people who had never programmed before.
But the distribution made it challenging to keep everyone motivated and
following along.
From the feedback (see below), it seems that I managed it well enough.

![Programming language experience of attendants](/images/python-hawaii-2017/programming-languages.jpg)

Not surprisingly, most participants who already programmed know Matlab.
What was a bit surprising is how few people reported experience with Fortran.
Is this a reflection of the age of participants (a lot of young grad students)?
The number of Fortran users does correlate with the number of faculty who
signed up, so maybe yes.

![Job title of attendants](/images/python-hawaii-2017/position.jpg)

I was very pleased to have someone from the
[Nā Kūpuna Senior Citizen Visitor Program](https://www.hawaii.edu/diversity/seed-programs/na-kupuna-senior-citizen-visitor-program/)
and a not insignificant number of faculty.
We even had an "interested citizen" who studies film production and education
(a personal friend)!


## Feedback

![Feedback on the colored sticky notes.](/images/python-hawaii-2017/sticky-note-feedback.jpg)

This is a synthesis from the feedback given by participants on the last day
(using the pink and blue sticky notes):

| The Good                                        | # |
|:------------------------------------------------|:--|
|Instructor style                                 | 5 |
|Examples and exercises                           | 5 |
|Dense but efficient (learn a lot in little time) |	3 |
|Using real data                                  | 3 |
|Simple and accessible level                      | 3 |
|Shared notes                                     | 1 |

| The Bad                                               | # |
|:------------------------------------------------------|:--|
| Too short                                             | 5 |
| Too fast                                              | 3 |
| Too slow                                              | 3 |
| Hard to multi-task (pay attention + notes + exercise) | 2 |
| No TA on Monday                                       | 2 |
| Instructor took too many tangents when teaching       | 1 |
| Too many people                                       | 1 |
| Ran late                                              | 1 |
| Jupyter Google maps example failed                    | 1 |

It was a very funny coincidence that the exact same number of people complained
about the pace being either too fast or too slow.


## Lessons learned

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

A few things that I would have done differently:

* **Get feedback through sticky notes at the end of each day**. The Software
  Carpentry material actually recommends this but I completely forgot.
* **Use more pair programming activities**. This is also something recommended
  by Software Carpentry and that I had planned on doing. In the end, I left
  this as optional and didn't explicitly pair learners. A lot of people were
  interacting naturally but I would have liked to see more of it.


*Have you taught or participated in a workshop like this before? What were your
experiences?*
