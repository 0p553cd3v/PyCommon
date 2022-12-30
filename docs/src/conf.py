import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PyCommon'
copyright = '2022, 0p553cd3v'
author = '0p553cd3v'
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

numfig = True

extensions = ['myst_parser']

extensions.append('sphinx.ext.todo')
extensions.append('sphinx.ext.autodoc')
extensions.append('sphinx.ext.autosummary')
extensions.append('sphinx.ext.viewcode')
extensions.append('sphinx.ext.coverage')
extensions.append('sphinx.ext.doctest')
extensions.append('sphinx.ext.graphviz')
extensions.append('sphinx.ext.ifconfig')
extensions.append('sphinx.ext.napoleon')

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []
source_suffix = '.md'

pygments_style = 'sphinx'
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

