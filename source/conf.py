# -*- coding: utf-8 -*-
import os
import sys

extensions = ['chinese_search', ]
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_encoding = 'utf-8'
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
    'preamble': r'''
    \usepackage{xeCJK}
    \usepackage{indentfirst}
    ''',
}

latex_documents = [
    ('index', 'mkdocs.tex', u'《Java笔记》',
     u'郑攀', 'howto',),
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


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

highlight_langeuage="java,javascript,python,html"
_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
