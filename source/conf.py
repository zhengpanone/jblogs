# -*- coding: utf-8 -*-
import os
import sys
import sphinx_rtd_theme

# project information
project = u'Go BLOG'
copyright = u'2018, 郑攀'
version = '1.0'
release = '1.0.0'
language = 'zh_CN'
# gengral configuration

extensions = ['chinese_search', 'recommonmark', 'sphinx.ext.autodoc','sphinx_copybutton','sphinxcontrib.svg2pdfconverter']
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_encoding = 'utf-8'
master_doc = 'index'
language = 'zh_CN'
exclude_patterns = []

pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
htmlhelp_basename = 'Java Blogs'

formats = ["htmlzip", "pdf", "epub"]

# LaTeX 配置
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

latex_documents = [
    ('index', 'mkdocs.tex', u'《Golang笔记》',
     u'郑攀', 'manual',),
]

man_pages = [
    ('index', 'pansblog', 'Pan\'s Blog Documentation',
     [u'郑攀'], 1)
]


texinfo_documents = [
    ('index', 'PansBlog', '《Golang博客》',
     u'郑攀', 'PansBlog', '《Golang博客》',
     'Miscellaneous'),
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

highlight_langeuage="go,javascript,html"

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
