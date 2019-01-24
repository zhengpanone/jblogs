# -*- coding: utf-8 -*-

import os
import sys


extensions = ['chinese_search', ]


templates_path = ['_templates']

source_suffix = ['.rst', '.md']

master_doc = 'index'

project = u'PAN\'s BLOG'
copyright = u'2018, 郑攀'
version = '1.0'
release = '1.0.0'
language = 'zh_CN'

exclude_patterns = []


import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

htmlhelp_basename = 'PansBlogdoc'


latex_elements = {

    'papersize': 'a4paper',


    'pointsize': '15pt',
    'classoptions': ',oneside', 'babel': '',
    'inputenc': '',  # 必须
    'utf8extra': '',  # 必须
    # Additional stuff for the LaTeX preamble.
    'preamble': r'\usepackage{werkzeugstyle}',

}

latex_documents = [
    ('index', 'PansBlog.tex', 'Pan\'s Blog Documentation',
     'Pan', 'howto'),
]

man_pages = [
    ('index', 'pansblog', 'Pan\'s Blog Documentation',
     [u'郑攀'], 1)
]




texinfo_documents = [
    ('index', 'PansBlog', 'Pan\'s Blog Documentation',
     u'郑攀', 'PansBlog', 'One line description of project.',
     'Miscellaneous'),
]



epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
