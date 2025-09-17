# -*- coding: utf-8 -*-
import os
import sys
import sphinx_rtd_theme
import platform

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))

# -- Project information -----------------------------------------------------

project = u'Java BLOG'
copyright = u'2018, 郑攀'
version = '1.0'
release = '1.0.0'
language = 'zh_CN'


simplepdf_vars = {
  'primary': '#333333',
  'links': '#FF3333',
}

extensions = [
            'sphinx.ext.viewcode', # 允许在文档中显示源代码
            "sphinx.ext.autosummary", # 用于生成 autodoc 的摘要文档。它会基于 docstring 自动生成类、方法、函数等的简短概要，提供一个概述。
            'chinese_search', 
            'myst_parser', 
            'sphinx_markdown_tables',
            'sphinx_copybutton',
            'sphinx.ext.todo',
            'sphinx.ext.autodoc',
            'sphinx.ext.napoleon',
            'sphinx.ext.autosectionlabel',
            # 'sphinxcontrib.inkscapeconverter',  # 用于 SVG 转换
            #   'sphinx_simplepdf'
            ]

autosectionlabel_prefix_document = True
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

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

latex_documents = [
    ('index', 'jblogs.tex', u'《Java笔记》',
     u'郑攀', 'manual',),
]



# 根据操作系统选择字体
if platform.system() == 'Windows':
    cjk_font = 'SimSun'
elif platform.system() == 'Darwin':  # macOS
    cjk_font = 'Songti SC'
else:  # Linux
    cjk_font = 'Noto Sans CJK SC'
# LaTeX配置
latex_engine = 'xelatex'  # 或者 'pdflatex'，根据你的需求选择
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '16pt',
    # 'figure_align': 'htbp', # 允许放在 here/top/bottom/page
    'figure_align': 'H',  # 强制当前位置
    'classoptions': ',oneside',
    'preamble': r'''
    # \usepackage{float}  % 提供 H 选项
    # \floatplacement{figure}{H} % 全局禁止跨页
    \usepackage{xeCJK}
    \setCJKmainfont{''' + cjk_font + r'''}
    '''
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


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# 配置默认的语法高亮语言
highlight_language = "python,go,javascript,html,java"

numfig = True
numfig_secnum_depth = 2

numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码 %s',
    'section': '节 %s',
}


