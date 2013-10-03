#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

AUTHOR = u'Leonardo Uieda'
SITENAME = u'/home/leo'
SITETAGLINE = u'Geophysics, inverse problems, and software'
SITEURL = ''

TIMEZONE = 'Brazil'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
# This will be
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'theme'

MENUITEMS = (
    ('About', '/about.html'),
    ('Archives', '/archives.html'),
)
SOCIAL = (
    ('Github', '#'),
    ('Twitter', '#'),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']

COPYRIGHT_NOTICE = """
Contents &copy; {date} {author} -
Except where otherwise noted, all content is
avilable under a
<a href="http://creativecommons.org/licenses/by/3.0/legalcode">CC-BY
license</a>
<img class="CCBY" src="/static/images/cc-by.jpg" width="90px">
""".format(author=AUTHOR, date=time.gmtime().tm_year)
