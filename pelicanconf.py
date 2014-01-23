#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

AUTHOR = u'Leonardo Uieda'
SITESUBTITLE = u'Geophysics, inverse problems, science, and software'
SITENAME = u'Leonardo Uieda'
#SITEURL = 'http://www.leouieda.com'
SITEURL = ''
DEFAULT_LANG = u'en'
TIMEZONE = u'America/Sao_Paulo'
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

FEED_ALL_RSS = 'rss.xml'
FEED_RSS = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

THEME = 'theme/pelican-bootstrap3'

SOCIAL = (
    ('github', 'https://github.com/leouieda'),
    ('twitter', 'https://twitter.com/leouieda'),
    ('google-plus', 'https://plus.google.com/+LeonardoUieda'),
    ('linkedin', 'http://www.linkedin.com/in/uieda'),
    ('rss', '/rss.xml'),
    ('figshare', 'http://figshare.com/authors/Leonardo%20Uieda/97471'),
    ('orcid', 'http://orcid.org/0000-0001-6123-9515'),
)

