import os
import sys
import sphinx_rtd_theme

# Add project root to the system path
sys.path.insert(0, os.path.abspath('..'))

# Project Information
project = 'Senegal LCLUC'
author = 'Jordan Alexis Caraballo-Vega, etc.'
release = '0.0.2'

# General Configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML Output
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

# Intersphinx Mapping
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# Language Settings
language = 'en'
