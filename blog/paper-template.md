---
title: A template for reproducible papers
date: 2018-03-15
thumbnail: paper-template.png
layout: post
---

At the [PINGA lab](http://www.pinga-lab.org/), we have been experimenting with
ways to increase the reproducibility of our research by publishing the git
repositories that accompany our papers on our
[Github organzation](https://github.com/pinga-lab).
I've synthesized the experience of the last 4 years into a template in the
[pinga-lab/paper-template](https://github.com/pinga-lab/paper-template)
repository.

*SCREENSHOT OF THE REPOSITORY*.

The template reflects the tools we've been using and the type of research that
we do.
Most papers are proposing a new methodology rather than the analysis of a
dataset.
However, there is always an application to a dataset included in the paper.
Our code is usually written in Python and executed in Jupyter notebooks.
The focus of the paper is on the methodology, not the code.
As such, the code is more of a proof-of-concept than a full blown application
library.
The paper itself is written in LaTeX and usually included in the repository.

It certainly won't fit everyone's needs but I hope that you can at least use a
few bits and pieces.
Of course, the code is open-source (BSD license).
The template includes a sample application to climate change data, complete
with a Python package, automated tests, an analysis notebook, a notebook that
generates the paper figure, raw data, and a LaTeX text.
Something about running everything with a single `make`.

*SCREENSHOT OF RUNNING MAKE TO PRODUCE THE PDF*.

The main features of the template are:

* Uses `Makefile`s to automate the workflow.
* You can build and test the software, generate results and figures, and
  compile the PDF with a single `make` command.
* A `Makefile` for building the manuscript PDF with extra rules for
  running [proselint](https://github.com/amperser/proselint), counting words,
  and opening the PDF.
* A starter [conda
  environment](https://conda.io/docs/user-guide/tasks/manage-environments.html)
  for managing dependencies and making sure everyone gets the same version of
  the dependencies.
* Boilerplate instructions for downloading the code and reproducing the
  results.
* A `Makefile` for building the Python package, testing it with
  [pytest](https://docs.pytest.org), running static code
  checks ([flake8](http://flake8.pycqa.org) and
  [pylint](https://www.pylint.org/)), and generating results and figures from
  the notebooks.
* The code `Makefile` can run the notebooks using `jupyter nbconvert` to
  guarantee that the notebooks are executed in sequential order (top to
  bottom). A major concern with notebooks is that the order in which they are
  executed is difficult to reproduce.  I would love to use
  [nbflow](https://github.com/jhamrick/nbflow) but the
  [SCons](http://scons.org/) requirement puts me off a bit. `make` works fine
  and the basic syntax is easier to understand.
* An example of using code to write experimental parameters in a `.tex` file.
  The file defines new variables that are used in the main text. This
  guarantees that the values cited in the text are the ones that you actually
  used to produce the results.
