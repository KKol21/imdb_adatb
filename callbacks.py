from dash import *
from layouts import *
from main import app

import mysql.connector

db_conn = mysql.connector.connect(user="root")
cursor = db_conn.cursor()
# Assume you have a users dictionary for simplicity. In a real app, you'd use a database.
users = {'admin': 'admin'}

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return login_layout
    elif pathname == '/main':
        return main_layout
    elif pathname == '/register':
        return register_layout
    else:
        return front_layout


# Callback to handle the login logic
@app.callback(Output('login-output', 'children'),
              [Input('login-button', 'n_clicks')],
              [State('username-input', 'value'),
               State('password-input', 'value')])
def login(n_clicks, username, password):
    if n_clicks is not None:
        if username in users and users[username] == password:
            # Successful login, redirect to the main page
            return dcc.Location(pathname='/main', id='redirect-home', refresh=True)
        else:
            return html.Div('Invalid username or password. Please try again.')


@app.callback(Output('register-output', 'children'),
              [Input('register-button', 'n_clicks')],
              [State('name-input', 'value'),
               State('username-input', 'value'),
               State('password-input', 'value')])
def register(n_clicks, name, username, password):
    if n_clicks is not None:
        if username not in users:
            users.update({username: password})
            return [
                html.Div('Registration successful! Redirecting in 3 seconds...'),
                dcc.Interval(id='redirect-interval', interval=3000, n_intervals=0),
            ]
        else:
            return html.Div('Username taken!')


@app.callback(Output('url', 'pathname'),
              [Input('redirect-interval', 'n_intervals')])
def redirect_to_main(n_intervals):
    if n_intervals > 0:
        return '/main'
    else:
        return dash.no_update
