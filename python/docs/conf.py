import sys
from pathlib import Path

sys.path.append(str(Path(__file__, "../../src").resolve()))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "portone-server-sdk"
copyright = "2024, PortOne"
author = "portone <tech.support@portone.io>"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.napoleon", "sphinx.ext.autodoc", "sphinx.ext.autosummary"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
napoleon_preprocess_types = True
autodoc_mock_imports = ["httpx"]
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "imported-members": True,
    "inherited-members": True,
    "no-value": True,
}
autosummary_generate = True
autosummary_ignore_module_all = False


def hide_class_signature(app, what, name, obj, options, signature, return_annotation):
    if not name.endswith("PortOneClient") and (what == "class" or what == "exception"):
        return ("", return_annotation)


def setup(app):
    app.connect("autodoc-process-signature", hide_class_signature)
