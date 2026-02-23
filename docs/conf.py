import os
import re


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

VERSION_REGEX = re.compile(
    r"^\s*#\s*define\s+PY3DM_VERSION_([A-Z]+)\s+(.*)$", re.MULTILINE)

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
version_file = os.path.join(repo_root, "src", "bindings", "bindings.h")

with open(version_file) as f:
    matches = dict(VERSION_REGEX.findall(f.read()))
    version = "{MAJOR}.{MINOR}.{PATCH}".format(**matches)

html_theme = "furo"
html_title = f"{project} v{version} documentation"

highlight_language = "python"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

exclude_patterns = [".build", "release.rst"]

autoapi_dirs = ['../py3dm']
autoapi_type = 'python'
autoapi_ignore = ['**/__init__.py']
autoapi_keep_files = False
