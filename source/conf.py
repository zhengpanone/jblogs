# -*- coding: utf-8 -*-
import os
import sys
import sphinx_rtd_theme

# project information
project = u'Java BLOG'
copyright = u'2018, 郑攀'
version = '1.0'
release = '1.0.0'
language = 'zh_CN'
# gengral configuration

simplepdf_vars = {
    'primary': '#333333',
    'links': '#FF3333',
}

extensions = ['chinese_search', 
              'recommonmark', 
              'sphinx.ext.autodoc',
              'sphinx_copybutton',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              'sphinx_markdown_tables',
              'sphinx.ext.autosectionlabel',
              'sphinxcontrib.inkscapeconverter',
            #   'sphinx_simplepdf'
              ]

# LaTeX配置
latex_engine = 'xelatex'  # 或者 'pdflatex'，根据你的需求选择
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}


# 使用 cairosvg 作为 SVG 转 PDF 的转换器
svg2pdf_converter = ('cairosvg',)

from sphinx.builders.html import StandaloneHTMLBuilder

StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml', 'image/png', 'image/gif', 'image/jpeg'
]

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
html_css_files = [
       'css/custom.css',
]
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
    ('index', 'mkdocs.tex', u'《Java笔记》',
     u'郑攀', 'manual',),
]

man_pages = [
    ('index', 'pansblog', 'Pan\'s Blog Documentation',
     [u'郑攀'], 1)
]


texinfo_documents = [
    ('index', 'PansBlog', '《Java博客》',
     u'郑攀', 'PansBlog', '《Java博客》',
     'Miscellaneous'),
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# 配置默认的语法高亮语言
highlight_language = 'go,javascript,html'

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
