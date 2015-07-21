from __future__ import unicode_literals
import os

AUTHOR = u'Leonardo Uieda'
SITETITLE = u"LEONARDO <b>UIEDA</b>"
SITENAME = u"Leonardo Uieda"
SITEKEYWORDS = u'geophysics, earth, earthscience, science, foss, scientific software'
SITEURL = ''

# Language and time
DEFAULT_LANG = u'en'
TIMEZONE = u'America/Sao_Paulo'

# This goes at the footer of the site
COPYRIGHT_NOTICE = """
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
>Creative Commons Attribution 4.0 International License</a>.
"""
EXTRA_FOOTER = """
Built by <a href="https://travis-ci.org/">Travis CI</a>
and
hosted on <a href="https://pages.github.com/">Github Pages</a>.
</br>
Icons by <a href="http://fontawesome.io/">Font Awesome</a>
and <a href="http://jpswalsh.github.io/academicons/">Academicons</a>.
</br>
Source code at <a href="https://github.com/leouieda/website">github.com/leouieda/website</a>.
"""

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
    'extra/favicon.ico',
    'extra/favicon.png',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'},
}

READERS = {"html": None}

ARTICLES_FRONT_PAGE = None
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
    ('About', '/index.html'),
    #('Research', '/research.html'),
    ('Papers', '/papers'),
    ('Talks', '/talks'),
    ('Teaching', '/teaching'),
    ('Software', '/software'),
    ('PINGA lab', 'http://www.pinga-lab.org'),
    ('<i class="fa fa-twitter fa-lg" title="Twitter"></i>',
     'https://twitter.com/leouieda'),
    ('<i class="ai ai-impactstory fa-lg" title="ImpactStory"></i>',
     'http://impactstory.org/leouieda'),
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
