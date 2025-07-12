# Source code for leouieda.com

This is the source code for my personal site
[leouieda.com](http://www.leouieda.com).

## Dependencies

You'll need to install [Nēnē](https://nene.leouieda.com/) and all it's
dependencies to build the site. I have been using Python 3.9 for the build. See
`environment.yml` for the complete dependency list.

You can create a conda environment with all required dependencies by running
`conda env create` in the root of the repository. To activate the environment
so we can run the build use `source activate leouieda.com`.

## Compiling the site

To build the website:

```
nene
```

To serve the website to localhost for development:

```
nene -s
```

## The theme

The website theme custom made with pure CSS.
The font used is
[Atkinson Hyperlegible Next](https://brailleinstitute.org/freefont) as well as
its monospace variant.
Syntax highlighting theme is
[Pitaya Smoothie](https://github.com/trallard/pitaya_smoothie).

The Jinja2 templates and CSS are located in the `_templates` and `css` folders.
I really should make this theme more generic and provide it to the world.
But, you know, time and things.
You can still use it by copying the folders to your own project.
I can't guarantee that things will work without my specific folder structure.

## Automatic deploy with GitHub Actions

The site is automatically built and deployed to
[leouieda/leouieda.github.com](https://github.com/leouieda/leouieda.github.com)
every time a commit is pushed to the *main* branch.
See files `.github/workflows/build.yml`.

## License

Except were otherwise noted, this work is licensed under a
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
