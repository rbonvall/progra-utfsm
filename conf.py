# -*- coding: utf-8 -*-

import sys
from glob import glob
from os.path import abspath

sys.path.insert(0, abspath('.'))
sys.path.insert(0, abspath('_modules'))

#templates_path = ['_templates']
exclude_patterns = ['_build']

extensions = [
    'sphinx.ext.mathjax',
    'testcase',
    'testcase_directive',
]

source_suffix = '.rst'
master_doc = 'index'
highlight_language = 'python'
default_role = 'math'

project = u'Programación 1-2011'
copyright = u'2011, Roberto Bonvallet'
version = ''
release = ''
language = 'es'

pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

html_static_path = ['_static']
html_theme_path = ['_theme']

html_theme = 'progra'
html_theme_options = {
    'nosidebar': True,
}
html_title = u'Programación'
html_short_title = u'Programación'
#html_logo = None
#html_favicon = None

#html_sidebars = {}
#html_additional_pages = {}

html_use_modindex = False
html_use_index = True
#html_show_sourcelink = True

#html_use_opensearch = ''

htmlhelp_basename = 'progra-utfsm'

# -- Options for LaTeX output --------------------------------------------------

latex_paper_size = 'letter'
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'progra.tex', u'Programación', u'Roberto Bonvallet', 'manual'),
]

latex_elements = {
    'fontpkg': '\\usepackage{mathpazo}',
    'pointsize': '12pt',
    #'preamble': '\\usepackage[spanish]{babel} \selectlanguage{spanish}',
}

#latex_logo = None
#latex_use_parts = False
#latex_preamble = ''
#latex_appendices = []

latex_use_modindex = False

