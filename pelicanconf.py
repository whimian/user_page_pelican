#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# from __future__ import unicode_literals

AUTHOR = u'yuhao'
SITENAME = u'Yu Hao'
SITEURL = ''

PATH = 'articles'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('weibo', 'http://weibo.com/whimsicalyuhao'),
          ('github', 'http://github.com/whimian'),
          ('linkedin', 'https://www.linkedin.com/in/hao-yu-79ab2658'),
          ('Another social link', '#'),)

SHARE = (('twitter', 'http://twitter.com/share', '?text=', '&amp;url='),
         ('facebook', 'http://facebook.com/sharer.php', '?t=', '&amp;u='),
        )
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# THEME = '..\..\..\martin-pelican'
THEME = 'themes\martin-pelican'
# THEME = r'..\..\..\voidy-bootstrap'
# THEME = 'simple'
# SITESUBTILE = u'地球物理'
# SITETAG = u"于浩"



# Extra stylesheets, for bootstrap overrides or additional styling.
# STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button
# implementation.
# CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
# CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode
# without sidebar.
# SIDEBAR = "sidebar.html"

# SOCIAL = (
#     ('LinkedIn', 'https://www.linkedin.com/in/hao-yu-79ab2658',
#       'fa fa-linkedin-square fa-fw fa-lg'),
#     ('GitHub', 'http://github.com/whimian',
#      'fa fa-github-square fa-fw fa-lg')
# )

STATIC_PATHS = ['images',
                # 'html_file'
               ]
# make pelican not to process html_file folder
PAGE_EXCLUDES = ['html_file']
ARTICLE_EXCLUDES = ['html_file']

# Take advantage of the following defaults
# STATIC_SAVE_AS = '{path}'
# STATIC_URL = '{path}'
# put 404.html in the root folder
# EXTRA_PATH_METADATA = {
#     'html_file/404.html': {'path': '404.html'},
#     }
# Plugins
# PLUGIN_PATHS = [r'..\..\pelican-plugins']
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math',
           'better_figures_and_images',
           'cjk-auto-spacing']
# better_figures_and_images
RESPONSIVE_IMAGES = True
# cjk-auto-spacing
CJK_AUTO_SPACING_TITLE = True


DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('<i class="fa fa-user" aria-hidden="true"></i>HOME', '/'),
             ('<i class="fa fa-graduation-cap" aria-hidden="true"></i>Research', '/pages/research.html'),
             ('<i class="fa fa-code-fork" aria-hidden="true"></i>Code', '/pages/code.html'),
             ('<i class="fa fa-pencil" aria-hidden="true"></i>Posts', '/blog_index.html')]

WEIBO = True
WEIBO_KEY = "appproximate000001"

# READERS = {"html": None}
# NOT_RENDERING = ['404.html']
# PAGE_PATHS = ['None']

INDEX_SAVE_AS = 'blog_index.html'
