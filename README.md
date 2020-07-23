# Souce code for leouieda.com

[![build-html](https://github.com/leouieda/website/workflows/build-html/badge.svg?event=push)](https://github.com/leouieda/website/actions?query=workflow%3Abuild-html)
[![Powered by Urubu](https://img.shields.io/badge/powered_by-urubu-blue.svg?style=flat-square)](http://urubu.jandecaluwe.com/)

This is the source code for my personal site
[leouieda.com](http://www.leouieda.com).

## Dependencies

You'll need to install Urubu and all it's dependencies to build the site. I
have been using Python 3.5 for the build. See `environment.yml` for the
complete dependency list.

You can create a conda environment with all required dependencies by running
`conda env create` in the root of the repository. To activate the environment
and run the build use `source activate urubu`.

## Compiling the site

Use the `Makefile`:

    make
    make serve

The command `make serve` will start a simple server at the `_build` folder
where the built HTML files are.
Point your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000)
to view the site.
The server runs in the background so you can continue working on the site.

## The theme

The website theme is made using [bootstrap](http://getbootstrap.com/)
and tweaked from the Cosmo [Bootswatch](http://bootswatch.com/) theme.
Icons are provided by [FontAwesome](http://fontawesome.io/) and
[Academicons](http://jpswalsh.github.io/academicons/).

The Jinja2 templates and CSS are located in the `_layouts` and `css` folders.
I really should make this theme more generic and provide it to the world.
But, you know, time and things.
You can still use it by copying the folders to your own project.
I can't guarantee that things will work without my specific folder structure.

## Adding an article/talk/course/software

The papers, talks, courses and software entries are `.md` files in the
corresponding folders.
The site theme takes a lot of extra metadata in the post to make the "Info"
section of each entry.

To add a new entry, create the `.md` file in the corresponding folder.

## Metadata for entries

The template makes extensive use of metadata entries for pages. You can specify
things like the DOI, Github repository, etc and the template will include it in
the publication side bar. See the existing publications for examples.


## Automatic deploy with TravisCI

The site is automatically built and deployed to
[leouieda/leouieda.github.com](https://github.com/leouieda/leouieda.github.com)
every time a commit is pushed to the *master* branch.
See files `.github/workflows/build.yml`.

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
Except were otherwise noted, this work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).

All source code is distributed under the [BSD 3-clause
License](https://opensource.org/licenses/BSD-3-Clause).
