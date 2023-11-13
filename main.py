from dash import Dash
from flask_session import Session
from datetime import timedelta

app = Dash(__name__)
# Flask-Session setup
app.server.config['SESSION_TYPE'] = 'filesystem'
app.server.config['SECRET_KEY'] = 'your_secret_key'
app.server.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
Session(app.server)

from create_tables import create_db
from auth_callbacks import *

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Run the app
if __name__ == '__main__':
    create_db()
    app.run_server(debug=True)
