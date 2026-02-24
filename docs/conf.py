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
]

source_suffix = {'.rst': 'restructuredtext'}
master_doc = "index"

html_theme = "furo"
html_title = f"{project} documentation"

highlight_language = "python"

exclude_patterns = [
    ".build",
    "release.rst",
    "autoapi/index.rst"
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- AutoAPI --
autoapi_dirs = ["../py3dm"]
autoapi_type = "python"
autoapi_ignore = ["**/__init__.py"]
autoapi_keep_files = False

autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]

autoapi_own_page_level = "class"
templates_path = ["_templates"]

templates_path = ['_templates']
autoapi_template_dir = '_templates/autoapi'