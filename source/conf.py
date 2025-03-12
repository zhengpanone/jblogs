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
              'sphinx_copybutton',
              'sphinx.ext.autodoc',
              'sphinx_markdown_tables',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode', # 允许在文档中显示源代码
              "sphinx.ext.autosummary", # 用于生成 autodoc 的摘要文档。它会基于 docstring 自动生成类、方法、函数等的简短概要，提供一个概述。
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.imgconverter',  # 用于图像转换 
              'sphinx.ext.imgmath',
              # 'sphinxcontrib.inkscapeconverter',  # 用于 SVG 转换
            #   'sphinx_simplepdf'
              ]

latex_documents = [
    ('index', 'mkdocs.tex', u'《Java笔记》',
     u'郑攀', 'manual',),
]

# LaTeX配置
latex_engine = 'xelatex'  # 或者 'pdflatex'，根据你的需求选择
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
    'classoptions': ',oneside',
    'fontpkg': '\\usepackage{fontspec}',
    'extraclassoptions': '\\XeTeXlinebreaklocale "zh" \\XeTeXlinebreakskip=0pt plus 1pt',
    
    'preamble': '''
        \\setmainfont{Noto Serif CJK SC}
        \\usepackage{graphicx}
        \\usepackage{svg}
         \\svgpath{{./images/}}  # 确保你有正确的 SVG 文件路径
    ''',
    
}


# 使用 magick convert 而不是 convert
image_converter = "magick"

# 使用 cairosvg 作为 SVG 转 PDF 的转换器
# svg2pdf_converter = ('cairosvg',)

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
html_static_path = ['_static']
html_css_files = [
       'css/custom.css',
]
htmlhelp_basename = 'Java Blogs'

formats = ["htmlzip", "pdf", "epub"]


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

# 配置默认的语法高亮语言
highlight_language = 'go,javascript,html'

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
