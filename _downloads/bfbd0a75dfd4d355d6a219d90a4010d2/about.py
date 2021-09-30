from dash import dcc, html
from utils.toml import load_option
from utils.nav import page_header
layout_options = load_option('options/about.toml')

header = page_header(title=layout_options.title)

layout = html.Article([header])
