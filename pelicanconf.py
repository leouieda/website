from __future__ import unicode_literals
import os

AUTHOR = u'Leonardo Uieda'
SITETITLE = u"Leonardo <b>Uieda</b>"
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
EXTRA_FOOTER = 'Source code at <a href="https://github.com/leouieda/website">github.com/leouieda/website</a>.'

# Where to put generated files
ARTICLE_URL = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

STATIC_PATHS = ['images',
                'notebooks',
                'pdf',
                'extra/CNAME',
                'extra/favicon.ico',
                'extra/favicon.png',
                ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/favicon.png': {'path': 'favicon.png'},
                       }


# Blog articles display
ARTICLES_FRONT_PAGE = 3
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
    ('Research', '/research.html'),
    ('Publications', '/publications.html'),
    ('Talks', '/talks.html'),
    ('Teaching', '/teaching.html'),
    ('<i class="fa fa-twitter fa-lg" title="Twitter"></i>',
     'https://twitter.com/leouieda'),
    ('<i class="fa fa-github-square fa-lg" title="Github"></i>',
     'https://github.com/leouieda'),
    ('<i class="ai ai-impactstory fa-lg" title="ImpactStory"></i>',
     'http://impactstory.org/leouieda'),
    ('<i class="ai ai-google-scholar fa-lg" title="Google Scholar"></i>',
     'http://scholar.google.com.br/citations?user=qfmPrUEAAAAJ'),
    ('<i class="ai ai-researchgate-square fa-lg" title="ResearchGate"></i>',
     'https://www.researchgate.net/profile/Leonardo_Uieda'),
    ('<i class="ai ai-orcid fa-lg" title="ORCID"></i>',
     'http://orcid.org/0000-0001-6123-9515'),
    ('<i class="fa fa-rss fa-lg" title="RSS feed"></i>', '/rss.xml'),
]

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary',
           'better_figures_and_images',
           'html_rst_directive',
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
