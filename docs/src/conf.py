import os
import sys
import tomli
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,"src")))
print("path:" + os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,"src")))

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'pyproject.toml')), mode="rb") as fp:
   config = tomli.load(fp)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'PyCommon'
copyright = '2022, 0p553cd3v'
author = '0p553cd3v'
release = config["project"]["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

numfig = True

master_doc = "index"

extensions = [
    'myst_parser',
]

extensions.append('sphinx.ext.todo')
extensions.append('sphinx.ext.autodoc')
extensions.append('sphinx.ext.autosummary')
extensions.append('sphinx.ext.viewcode')
extensions.append('sphinx.ext.coverage')
extensions.append('sphinx.ext.doctest')
extensions.append('sphinx.ext.graphviz')
extensions.append('sphinx.ext.ifconfig')
extensions.append('sphinx.ext.githubpages')
extensions.append('sphinx.ext.napoleon')

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

pygments_style = 'sphinx'
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True