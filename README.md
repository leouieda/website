# Souce code for leouieda.com

[![Build Status](https://img.shields.io/travis/leouieda/website/master.svg?style=flat-square)](https://travis-ci.org/leouieda/website)
[![Powered by Pelican](https://img.shields.io/badge/powered_by-pelican-blue.svg?style=flat-square)](http://getpelican.com/)
[![Powered by Bootstrap](https://img.shields.io/badge/powered_by-bootstrap-blue.svg?style=flat-square)](http://getbootstrap.com/)
[![Theme by Bootswatch](https://img.shields.io/badge/theme_by-bootswatch-blue.svg?style=flat-square)](http://bootswatch.com/)

This is the source code for my personal site
[leouieda.com](http://www.leouieda.com).

It's built using [Pelican](http://getpelican.com/) and hosted on
[Github pages](https://github.com/leouieda/leouieda.github.com).

## Dependencies

You'll need the following to build the website:

* Pelican (3.5.0)
* markdown (2.4)
* beautifulsoup4 (4.3.2)

You can install these libraries using `pip`:

    pip install pelican==3.5.0 markdown==2.4 beautifulsoup4==4.3.2

After cloning this repository, you'll need to initialized the git submodules
for the `pelican-plugins`:

    cd pelican-plugins
    git submodule init
    git submodule update

This only needs to be done once.

## Compiling the site

Use the `Makefile`:

    make
    make serve

The command `make serve` will start a simple server at the `output` dir
where the built HTML files are.
Point your browser to [http://127.0.0.1:8001](http://127.0.0.1:8001)
to view the site.
Use `Ctrl+C` to kill the server.

## The theme

The website theme is made using [bootstrap](http://getbootstrap.com/)
and tweaked from the Cosmo [Bootswatch](http://bootswatch.com/) theme.
Icons are provided by [FontAwesome](http://fontawesome.io/) and
[Academicons](http://jpswalsh.github.io/academicons/).

The Jinja2 templates and CSS are located in the `theme` folder.
I really should make this theme more generic and provide it to the world.
But, you know, time and things.
You can still use it by copying the `theme` folder to your own project.
I can't guarantee that things will work without my specific folder struture in
`content`.

## Adding an article/talk/course/software

The papers, talks, courses and software entries are basically blog posts, each
in a different category.
Categories are defined as folders in `content`.
Each entry gets it's own `.md` file.
The site theme takes a lot of extra metadata in the post to make the "Info"
section of each entry.

To add a new entry, create the `.md` file in the corresponding category.

## Metadata for entries

### Papers

Required:

    title: Geophysical tutorial: Euler deconvolution of potential-field data
    date: 01-04-2014
    slug: paper-tle-euler-tutorial-2014
    author: Uieda, L., V. C. Oliveira Jr, and V. C. F. Barbosa
    journal: The Leading Edge
    citation: Uieda, L., V. C. Oliveira Jr, and V. C. F. Barbosa (2014), Geophysical tutorial: Euler deconvolution of potential-field data, The Leading Edge, 33(4), 448-450, doi:10.1190/tle33040448.1

Note that `citation` has to be in a single line.

Optional:

    repository: pinga-lab/paper-tle-euler-tutorial
    doi: 10.1190/tle33040448.1
    supplement: 10.6084/m9.figshare.923450
    thumbnail: images/thumb/paper-tle-euler-tutorial-2014.png
    pdf: paper-tle.pdf
    tags: OA, review

The `tags` metadata has special entries: `OA` and `review`.
An entry with the `OA` tag will be marked as open-acess.
Setting the `review` tag will mark the entry as under peer-review
(unpublished).

The PDF file should be provided in the `content/pdf` folder.

### Talks

Required:

    title: Use of the "shape-of-anomaly" data misfit in 3D inversion by planting anomalous densities
    author: Uieda, L., and V. C. F. Barbosa
    slug: seg2012
    date: 01-11-2012
    type: oral
    event: SEG Annual Meeting

`type` can be either `oral` or `poster`.

Optional:

    tags: expanded
    pdf: seg-2012.pdf
    repository: leouieda/seg2012
    slides: 10.6084/m9.figshare.156864
    poster: 10.6084/m9.figshare.1089987
    doi: 10.1190/segam2012-0383.1
    thumbnail: images/thumb/seg2012.png
    citation: Uieda, L., and V. C. F. Barbosa (2012), Use of the "shape-of-anomaly" data misfit in 3D inversion by planting anomalous densities, SEG Technical Program Expanded Abstracts, pp. 1-6, doi:10.1190/segam2012-0383.1

If `tags` has the word `expanded`, will place an info alert saying that there
is an expanded abstract or short paper available with this entry.

## Automatic deploy with TravisCI

The site is automatically built and deployed to
[leouieda/leouieda.github.com](https://github.com/leouieda/leouieda.github.com)
every time a commit is pushed to the *master* branch.
See files `.travis.yml` and `.update-website.sh`.
Inspired by
[Sleepy Coders](http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html)
and
[Mathieu Leplatre](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html).

[![TravisCI status](http://img.shields.io/travis/leouieda/website.svg?style=flat)](https://travis-ci.org/leouieda/website)

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
