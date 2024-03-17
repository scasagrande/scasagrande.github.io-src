AUTHOR = 'Steven Casagrande'
SITENAME = 'Steven Casagrande'
SITETITLE = "Steven Casagrande"
SITESUBTITLE = "Lead build systems developer for IBM Quantum"
SITEDESCRIPTION = ""
# SITEURL = "https://steven.casagrande.io"

PATH = "content"
ARTICLE_PATHS = ["blog"]
ARTICLE_SAVE_AS = "articles/{slug}.html"
ARTICLE_URL = "articles/{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
DISABLE_URL_HASH = True
# USE_GOOGLE_FONTS = False
COPYRIGHT_YEAR = 2024

THEME = "theme/Flex"
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


THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
THEME_COLOR = "light"
PYGMENTS_STYLE = "sas"
# PYGMENTS_STYLE = "catppuccin.LatteStyle"
# PYGMENTS_STYLE_DARK = "catppuccin.FrappeStyle"
# PYGMENTS_STYLE_DARK = "catppuccin.MacchiatoStyle"
PYGMENTS_STYLE_DARK = "catppuccin.MochaStyle"

# Blogroll
# LINKS = (
#     ('InstrumentKit', 'https://www.github.com/instrumentkit/InstrumentKit'),
#     ('Galvant Industries', 'http://galvant.ca/'),
# )

# Social widget
SOCIAL = (
    ('github', 'https://github.com/scasagrande'),
    ('linkedin', 'https://www.linkedin.com/in/steven-casagrande-633ba533'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
ABOUT_ME = "Lead build systems developer for IBM Quantum"
SITELOGO = "https://steven.casagrande.io/images/me.jpg"

# CNAME
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites"]
