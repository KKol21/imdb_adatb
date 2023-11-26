from datetime import timedelta

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from flask_session import Session


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# Flask-Session setup
app.server.config['SESSION_TYPE'] = 'filesystem'
app.server.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
Session(app.server)

app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    children=[dcc.Location(id='url', refresh=False),
              html.Div(id='page-content')],
    style={'color': '#000000'}
)
