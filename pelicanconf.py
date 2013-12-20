#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

AUTHOR = u'Leonardo Uieda'
SITESUBTITLE = u'Geophysics, inverse problems, science, and software'
SITENAME = u'&lt;insert witty geoscience title&gt; - {}'.format(SITESUBTITLE)
#SITEURL = 'http://leouieda.github.io'
SITEURL = ''
COPYRIGHT_NOTICE = """
Contents &copy; {date} {author} -
Except where otherwise noted, all content is
avilable under a
<a href="http://creativecommons.org/licenses/by/3.0/legalcode">CC-BY
license</a>
<img class="CCBY" src="/static/images/cc-by.jpg" width="90px">
""".format(author=AUTHOR, date=time.gmtime().tm_year)

ARTICLE_URL = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
STATIC_PATHS = ['images']
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = '../pelican-themes/pelican-bootstrap3'
GITHUB_USER = 'leouieda'
GITHUB_REPO_COUNT = 10

TWITTER_USERNAME = 'leouieda'
SOCIAL = (
    ('github', 'https://github.com/leouieda'),
    ('twitter', 'https://twitter.com/leouieda'),
    ('google-plus', 'https://plus.google.com/+LeonardoUieda'),
    ('linkedin', 'http://www.linkedin.com/in/uieda'),
    ('figshare', 'http://figshare.com/authors/Leonardo%20Uieda/97471'),
    ('orcid', 'http://orcid.org/0000-0001-6123-9515'),
    ('google-scholar',
        'http://scholar.google.com.br/citations?user=qfmPrUEAAAAJ'),
)

