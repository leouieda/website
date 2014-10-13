# Souce code for leouieda.com

This is the source code for [leouieda.com](http://www.leouieda.com) (my personal site).
It's built using [Pelican](http://getpelican.com/) and hosted on 
[Github pages](https://github.com/leouieda/leouieda.github.com).

## Requires

* Pelican (3.4.0)
* markdown (2.4)
* pillow
* beautifulsoup4
* nodejs

To install the Python components:

    pip install pelican==3.4.0 markdown==2.4 pillow beautifulsoup4

To install nodejs on Ubuntu:

    sudo apt-get install nodejs

## Compiling the site

Use the `Makefile`:

    make
    make serve

The command `make serve` will start a simple server at the `output` dir
where the built HTML files are.
Point your browser to [http://127.0.0.1:8001](http://127.0.0.1:8001) 
to view the site.
Use `Ctrl+C` to kill the server.

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
