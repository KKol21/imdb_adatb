from dash import Dash
from flask_session import Session
from datetime import timedelta

app = Dash(__name__)
# Flask-Session setup
app.server.config['SESSION_TYPE'] = 'filesystem'
app.server.config['SECRET_KEY'] = 'your_secret_key'
app.server.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
Session(app.server)

from callbacks.auth_callbacks import *
from callbacks.main_callbacks import *
from layouts import purple


app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    children=[dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')],
    style={'color': '#000000'}
)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
