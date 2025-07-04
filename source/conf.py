# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PythonProjectNine'
copyright = '2025, Author'
author = 'Author'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- Meta Tags Injection: Bing & Canonical -----------------------------------

def add_custom_meta_tags(app, pagename, templatename, context, doctree):
    context['metatags'] = context.get('metatags', '') + (
        '<meta name="msvalidate.01" content="0CD364F244E1C3C66ED4002465FC0441" />\n'
        '<link rel="canonical" href="https://coinbasehelp.readthedocs.io" />\n'
    )

def setup(app):
    app.add_config_value('meta_tags', '', 'html')
    app.connect('html-page-context', add_custom_meta_tags)


