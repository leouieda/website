---
title: "Why should geologists learn how to code?"
date: 2022-03-07
---

I've been teaching introductory courses in programming and using programming in
my geophysics courses for a decade now.

Last week, before the second day of my 4-week "Introduction to Python for
Geoscientists" workshop, I was asked by a student why they needed to learn how
to code.
After all, they are training to become a geologist, not a geophysicist, and
couldn't see how this would be useful in their future career.
It was a fair question since, by that point, all we had seen were variables and
basic data types and operations.
Day 2 of the workshop covers loading that
with numpy and making plots (following the excellent
[Software Carpentry "Programming with Python" lesson](https://swcarpentry.github.io/python-novice-inflammation/)),
which is less abstract and luckily helped show them how this skill is useful,
though for now they could still have done the same thing with Excel just as
easily.
But not being a professional geologist myself, it's hard to come up with
specific examples.
I also wanted to stay away from the argument that coding is skill that can help
you survive a downturn in geoscience by pivoting to data science.
While true, it's not particularly encouraging for first year students to be
told that they need to plan to move away from the field.

Luckily, I have access to a wide network of professional geologists who code
through the [Software Underground](https://softwareunderground.org/) community!
So I asked them **"How has coding helped you do your job?"**

Here are some of their replies (with slight edits by me marked in `[]`).

---

<blockquote class="blockquote">

Although I am not a geologist specifically, I did have a lot of geology
training in my BSc before choosing geophysics. My suggestions would be:

1. 3D model creation using Python interfaces \[to graphical software\] or [GemPy](https://www.gempy.org/).
1. Any graph theory application (material fluxes). \[For examples, see\] [Phillips et al. (2015)](https://doi.org/10.1016/j.earscirev.2015.02.002).
1. Automated fracture or discontinuity mapping. \[For examples, see\] [Vöge et al. (2013)](https://doi.org/10.1016/j.enggeo.2013.07.008) and [Prabhakaran et al. (2021)](https://doi.org/10.1016/j.jsg.2021.104405).
1. \[Creating\] virtual outcrops.
1. Sped up tectonic forces and erosion.
1. You could build [geological models in Minecraft](https://www.bgs.ac.uk/discovering-geology/maps-and-resources/maps/minecraft-3d-geological-models/) (\[using their\] Python interface).
1. Maybe most importantly: **Automate the boring things.**

</blockquote>
<p class="blockquote-footer">
<a href="https://www.researchgate.net/profile/Alex-Hobe">Alex Hobé</a>,
PhD candidate in Geothermal Energy at Uppsala University
</p>

---

<blockquote class="blockquote">

\[Here are\] a couple of points for motivation that I give my students:

* **Data analysis:** Automation of processing (including graph generation), reproducibility, transparency.
* **Creativity:** Find solutions \[to the problems you come across\] in a creative way.
* **Freedom:** Don't be stuck in a program that defines for you what you are able to do.
* It is a tool set that makes you more independent in the future job choice.
* I also like the general viewpoint of **computational thinking as a
  problem-solving art**. Being able to deconstruct complex problems into single
  tasks can also be transferred to non-computational problems in geology!

But maybe more directly to geology:

* More and more data now gathered and automated processing developed, also
  meaning that a lot of jobs will become obsolete. But if you are
  able to combine geological knowledge with programming, then a lot of
  opportunities open up.
* As success stories: A lot of my students found jobs **because they were able
  to combine geological knowledge with programming**. I received a super nice
  letter last year from \[a former student\] where he made it very clear how much
  that helped and opened his mind.
* I also tell the story from our industrial advisory member in the last study
  program accreditation where the advisor mentioned explicitly that the
  programming skills we teach are essential for many jobs in industry in the
  future (was from raw materials, but I am sure you could get similar quotes from
  geothermal, geotech, etc.).

Of course, the key difficulty I see for our education: we need to teach
students both geoscientific skills and knowledge and a set of tools - and there
is only limited time.
But programming is certainly a part of the standard tool set that is expected
(or seen as an advantage) for many industry jobs (or will be in the near
future).

</blockquote>
<p class="blockquote-footer">
<a href="https://www.cgre.rwth-aachen.de/go/id/qoyf/?lidx=1">Florian Wellmann</a>,
Professor at RWTH Aachen University
</p>

---

<blockquote class="blockquote">

Learning to code helped me to get a better grasp of mathematics as well as you
can focus on the math part rather then "calculating".
You can build your own tools to solve problems and avoid cumbersome tasks and
focus on the fun parts.

In industry (at least in my experience) everything is statistical. Rather then
one best estimate we try to cover the range of possible outcomes to base
decisions on. Coding allows you to do that relative easy.

But the hardest point to bring across is that \[before you start\] you don't
know all the things and ideas you will have once you can code.
You have a new set of tools at your hand and start to see all kind of problems
that could be solved.

What Florian Wellmann mentioned is right.
For me learning to code opened a new chapter in my life and how much it changed
is hard to put into words here.
**The easiest thing to describe is that it got me the job I have right now and it
was one of the most empowering experiences in my life.**

</blockquote>
<p class="blockquote-footer">
<a href="https://github.com/WestfalNamur">Stefan Crummenerl</a>,
Reservoir Engineer at Equinor.
</p>

---

<blockquote class="blockquote">

Doing any real (geo)statistics really asks for a good programming knowledge.
From data handling to analysis and understanding.
There are many things non-coders can not do (they are stuck with commercial
software).

</blockquote>
<p class="blockquote-footer">
<a href="https://github.com/ahartikainen">Ari Hartikainen</a>
</p>

---

<blockquote class="blockquote">

When they have to type in their weekly report and all their statistics from
their drilling program by hand,
then redo when their head of commercial wants it done differently,
build a 300 layer 3d project and you have to do 25 of them,
organise all your assays from the last 10 years...

</blockquote>
<p class="blockquote-footer">
<a href="">Richard Scott</a>,
</p>

---

<blockquote class="blockquote">

When I think of core geology skills I think of making maps.
Possibly the last time they’ll make a contour map by hand is in school.
After that, they will have to use software to be productive.
It is crucial to understand how these algorithms work, when to use them, and
their pitfalls.
One could learn how krigging works (math), and then code a simple
implementation to bring it home (learning math by coding).

Also, coding is great for automation.
Even Petrel, \[a standard commercial software in the oil and gas industry\],
has a very important area for developing workflows to automate data
preparation, regrid, and all things needed for statical modeling.
It is not a real programming language, but it has units of code blocks (for
loops, if then else, while) that if you had never been exposed to before, might
make hard to grasp their use and connect the dots to solve your problems.

</blockquote>
<p class="blockquote-footer">
<a href="">Rafael Pinto</a>,
</p>

---

<blockquote class="blockquote">

I'm not a graduated geologist yet, but knowing how to code in Python brought me
several opportunities in terms of joining research groups and finding
interesting internships.
I use Python very often for automation on GIS and for data cleaning to input in
a few software \[tools\], like MODFLOW.
I'm also developing some geowebapps in order to allow free and open source data
processing.
So far, I have developed only one, and a few more are on the way! You can check
it out [here](https://share.streamlit.io/rodreras/piper_diagram/main/geoapp_hidro.py).

</blockquote>
<p class="blockquote-footer">
<a href="">Rodrigo Brust</a>,
</p>

---

<blockquote class="blockquote">

I think I've been in their shoes.
As a second year geology undergrad, I decided to take Computer Science 101
because someone told me it would be useful.
I more or less decided it was a waste of my time, mostly because I couldn't
connect the dots to how it would apply to my studies or career.
Currently, I think the points that Florian Wellmann brought up around data analysis
(automation of processing, reproducibility, transparency) are some of the most
important reasons to code.
But to someone whose definition of "big data" might be data that takes more
than a few minutes to transcribe from their field notebook to Excel, this might
be a bit abstract.

What did start to make it click for me some years later were finding examples
of geologic workflows done in Python that I could build on top of.
Great examples are:

* \[Agile Scientific's\] [X Lines of Python series](https://agilescientific.com/blog/category/X+Lines)
* [Jesse Pisel's 5 minutes of Python](https://github.com/jessepisel/5minutesofpython)
* [Michael Pyrcz's Python Numerical Demos](https://github.com/GeostatsGuy/PythonNumericalDemos)
(check out the readme of that repo for 9 reasons scientists should learn to
code)
* [Brendon Hall's famous Facies classification using machine learning tutorial](https://doi.org/10.1190/tle35100906.1)

But to answer your actual question:
the two biggest ways coding has helped me do my job as a geologist in
industry (apart from data analysis) are task automation and extension of
proprietary software workflows.

1. A lot of tasks assigned to entry level, and non-entry level for that
   matter, geologists are repetitive. For example, you might make some geologic
   interpretations and file them in a standard report or form that you will then
   pass on to a colleague to make some engineering designs. You may have to do
   this 10s or more times in a week. A lot of this type of work can be automated
   with code.
1. Second, much of the work done by geologists, in my experience (O&G) , is
   done inside of some large proprietary software package like Petrel, DSG,
   ArcMap etc. Why should we learn to code if we have these made for us? Rafael
   Pinto made some good points about this already. I will add that these software
   packages have great workflows, and you should use them if you are able to. But
   many times they can't do exactly what you need. In these cases it's a
   superpower to be able to read the data and your interpretations from these
   packages into Python, and do a few steps of analysis to get you exactly what
   you need.

</blockquote>
<p class="blockquote-footer">
<a href="">Michael Harty</a>,
</p>

---

<blockquote class="blockquote">
</blockquote>
<p class="blockquote-footer">
<a href=""></a>,
</p>

---

By the way, if you are **interested in geoscience and coding/technology at any
level**, the [Software Underground](https://softwareunderground.org/) is the
best place to find your peers!

They are a registered non-profit and a legit professional society, the likes of
which you won't find anywhere is the geoscience space.
**Signing up for the Slack with over 4000 members is free** and you can also
join as a paying member to help support the community.
