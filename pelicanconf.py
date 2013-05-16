#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


SITENAME = u'Victoria Mo'
AUTHOR = u'Victoria Mo'
TAGLINE = u'Moving mountains, one stone at a time.'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%Y-%m-%d',
}
DEFAULT_PAGINATION = 10

THEME = 'themes/pelican-svbtle'


# display items
LOGO_URL = 'https://dl.dropboxusercontent.com/u/7030113/www/art-noveau-ornament.png'
MENUITEMS = (
    ('archives', '/archives.html'),
    ('feed', '/feeds/all.atom.xml'),
    ('github', 'https://github.com/vickimo/'),
)
DISPLAY_PAGES_ON_MENU = True
FOOTER_MESSAGE = u'This work is licensed under the <a href="http://creativecommons.org/licenses/by-sa/3.0/" rel="license">CC BY-SA</a>.'
TWITTER_USERNAME = u'mo_vicki'


#STATIC_PATHS = ()
FILES_TO_COPY = (
    ('extra/README', 'README'),
    ('extra/LICENSE', 'LICENSE'),
    ('extra/CNAME', 'CNAME'),
    ('extra/humans.txt', 'humans.txt'),
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/404.html', '404.html'),
    ('extra/snowy_peaks.jpg', 'snowy_peaks.jpg'),
)

# Plugins and their settings.
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ('sitemap', 'gist', )

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}
