# -- Project information --
project = "py3dm"
copyright = "2025, StudioWEngineers"
author = "StudioWEngineers"

# -- General configuration --
extensions = [
    "sphinx_copybutton",
    "sphinxcontrib.moderncmakedomain",
    "sphinx.ext.intersphinx",
    "autoapi.extension",
    "sphinx.ext.intersphinx"
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

source_suffix = {'.rst': 'restructuredtext'}

master_doc = "index"

html_theme = "furo"
html_title = f"{project} documentation"

highlight_language = "python"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

exclude_patterns = [".build", "release.rst"]

autoapi_dirs = ['../py3dm']
autoapi_type = 'python'
autoapi_ignore = ['**/__init__.py']
autoapi_keep_files = False
