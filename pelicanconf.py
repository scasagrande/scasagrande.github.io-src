#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Steven Casagrande'
SITENAME = 'Steven Casagrande'
SITEURL = ''

PATH = 'content'

THEME = 'theme'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('InstrumentKit', 'https://www.github.com/Galvant/InstrumentKit'),
         ('Galvant Industries', 'http://galvant.ca/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/scasagrande'),
          ('twitter', 'https://twitter.com/stevecasagrande'),
          ('linkedin', 'https://www.linkedin.com/in/steven-casagrande-633ba533'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']
PROFILE_PICTURE = "profile_picture.png"

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('CV', '/pages/cv')]
