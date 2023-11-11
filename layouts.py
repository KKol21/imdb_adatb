from dash import html, dcc, callback, Output, Input
from main import app  # Import the Dash app instance

# Layout for the login page
login_layout = html.Div([
    html.Div([
        html.Label('Username'),
        dcc.Input(id='username-input', type='text', placeholder='Enter your username'),
        html.Label('Password'),
        dcc.Input(id='password-input', type='password', placeholder='Enter your password'),
        html.Button('Login', id='login-button'),
        html.Div(id='login-output')
    ])
])

# Importing login_callback from the callbacks.py file
from callbacks import login_callback
