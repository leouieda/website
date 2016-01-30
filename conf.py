from __future__ import unicode_literals
import os
import subprocess
import datetime

AUTHOR = u'Leonardo Uieda'
SITETITLE = u"LEONARDO <b>UIEDA</b>"
SITENAME = u"Leonardo Uieda"
SITEKEYWORDS = u'geophysics, earth, earthscience, science, foss, scientific software'
SITEURL = ''
REPOURL = 'https://github.com/leouieda/website'
DESCRIPTION = """
<strong>Welcome!</strong> This website is about my academic life.
I'm interested in gravity and magnetic methods, inverse problems,
and free software.
I really enjoy teaching and believe that science should be open.
"""
BANNER = "images/torres-del-paine.jpg"
BUILD_TIME = datetime.date.today().strftime(format='%d-%b-%Y')

# Get the current git commit hash
COMMIT = ''
process = subprocess.Popen('git rev-parse HEAD'.split(), cwd='.',
                           stdout=subprocess.PIPE)
git_hash = process.communicate()[0].strip().decode('utf-8')
if git_hash:
    COMMIT = ' (<a href="{url}/commit/{commit}">{commit_link}</a>)'.format(
            url=REPOURL, commit=git_hash, commit_link=git_hash[:7])

# Language and time
DEFAULT_LANG = u'en'
TIMEZONE = u'America/Sao_Paulo'

# This goes at the footer of the site
FOOTER_LEFT = """
This work is licensed
<a rel="license"
 href="http://creativecommons.org/licenses/by/4.0/deed.en_US">CC-BY</a>.
<br/>
Powered by <a href="http://getpelican.com/">Pelican</a>,
<a href="http://python.org">Python</a>,
and <a href="http://getbootstrap.com/">Bootstrap</a>.
</br>
Icons by <a href="http://fontawesome.io/">Font Awesome</a>
and <a href="http://jpswalsh.github.io/academicons/">Academicons</a>.
"""
FOOTER_RIGHT = """
Built by <a href="https://travis-ci.org/">Travis CI</a>
and
hosted on <a href="https://pages.github.com/">Github Pages</a>.
</br>
Latest build on {date}{commit}.
</br>
Source code at
<a href="{repo}">{repo_name}</a>.
""".format(date=BUILD_TIME, commit=COMMIT, repo=REPOURL, repo_name=REPOURL[8:])

# Where to put generated files
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
USE_FOLDER_AS_CATEGORY = True
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = [
    'images',
    'notebooks',
    'pdf',
    'misc',
    'extra/CNAME',
    'extra/.nojekyll',
    'extra/favicon.ico',
    'extra/favicon.png',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/.nojekyll': {'path': '.nojekyll'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'},
}

READERS = {"html": None}

ARTICLES_FRONT_PAGE = 2
SUMMARY_MAX_LENGTH = 25
DEFAULT_PAGINATION = 0
DISPLAY_CATEGORIES_ON_MENU = False

# Feeds
FEED_ALL_RSS = 'rss.xml'
FEED_ALL_ATOM = False

THEME = 'theme'

# Top menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('About', '/about.html'),
    #('Research', '/research.html'),
    ('Papers', '/papers'),
    ('Talks', '/talks'),
    ('Teaching', '/teaching'),
    ('Software', '/software'),
    ('Contact', '/contact.html'),
    ('<i class="fa fa-github fa-lg" title="Github"></i>',
     'https://github.com/leouieda'),
    ('<i class="fa fa-twitter fa-lg" title="Twitter"></i>',
     'https://twitter.com/leouieda'),
    ('<i class="fa fa-rss fa-lg" title="RSS feed for papers and talks"></i>', '/rss.xml'),
]

CATEGORY_HEADERS = [
    ['teaching', """
    <p>
    These are some the classes I've taught or am teaching at the moment.
    Most have Github repositories and links to download and view all content.
    There is a mixture of semester long university courses
    (<i class="fa fa-graduation-cap"></i>) and short courses
    (<i class="fa fa-info-circle"></i>).
    </p>
    """],
    ['talks', """
    <p>
    A list of talks (<i class="fa fa-comments-o"></i>)
    and poster presentations (<i class="fa fa-picture-o"></i>)
    I have given over the years.
    All have links to download the poster/slides.
    Most include links to source-code and data used to produce the results
    (look for the <i class="fa fa-github-square"></i> icon).
    </p>
    """],
    ['software', """
    <p>
    Most of my research work involves writing software. These are some of the
    open-source packages I have developed.
    </p>
    """],
    ['papers', """
    <p>
    Publications marked with a
    <i class="fa fa-unlock-alt"></i> are
    <a href="https://en.wikipedia.org/wiki/Open_access">open-access (OA)</a>.
    I have made available links for you to download free PDFs from all non-OA
    publications.
    Many papers include links to accompanying source-code repositories on
    Github (<i class="fa fa-github-square"></i>) and supplementary material
    hosted on <a href="http://figshare.com/">figshare</a> or
    <a href="http://zenodo.org/">Zenodo</a>.
    </p>
    """],
]

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary',
           'render_math',
           'sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5},
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'}
}

RESPONSIVE_IMAGES = False
FIGURE_NUMBERS = True
