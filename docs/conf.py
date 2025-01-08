project = 'bio.tools documentation'

latex_engine = 'xelatex'  # allow us to build Unicode chars

autosectionlabel_prefix_document = True
hoverxref_auto_ref = True
hoverxref_roles = [
    'term',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

js_source_path = '../src/'
html_extra_path = ['_static']
html_context = {
    "comment": "This comment is injected manually as a test.",
}

