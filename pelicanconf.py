AUTHOR = 'Steven Casagrande'
SITENAME = 'Steven Casagrande'
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ["blog"]
ARTICLE_SAVE_AS = "articles/{slug}.html"
ARTICLE_URL = "articles/{slug}.html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

THEME = "theme/pelican-bootstrap3"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PAGES_SORT_ATTRIBUTE = "sortorder"

TIMEZONE = "America/Toronto"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('InstrumentKit', 'https://www.github.com/Galvant/InstrumentKit'),
    ('Galvant Industries', 'http://galvant.ca/'),
)

# Social widget
SOCIAL = (
    ('github', 'http://github.com/scasagrande'),
    ('twitter', 'https://twitter.com/stevecasagrande'),
    ('linkedin', 'https://www.linkedin.com/in/steven-casagrande-633ba533'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
ABOUT_ME = "Python lover, hardware builder, powerlifter, and tester of all the things"
# AVATAR = "images/profile_picture.jpg"

# CNAME
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites"]
