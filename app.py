from dash_xinet.server import create_app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = create_app(__name__,
                 title='Sanstyle Dash',
                 external_stylesheets=external_stylesheets)
