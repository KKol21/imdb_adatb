from dash import Input, Output, State, no_update, callback
from dash import html, dcc
from flask import session

from dao import userDao
from db.db_connector import db_conn

userDao = userDao.UserDAO(db_conn=db_conn)


# Callback to handle the login logic
@callback(Output('login-output', 'children'),
          [Input('login-button', 'n_clicks')],
          [State('username-input', 'value'),
           State('password-input', 'value')])
def login(n_clicks, username, password):
    if n_clicks is not None:
        users = userDao.get_users()
        valid_user = any(
            username == user[0] and password == user[1]
            for user in users
        )
        if valid_user:
            # Successful login, redirect to the main page
            session['logged_in_user'] = username
            return dcc.Location(pathname='/main', id='login-to-main', refresh=True)
        else:
            return html.Div('Invalid username or password. Please try again.')


@callback(Output('register-output', 'children'),
          [Input('register-button', 'n_clicks')],
          [State('name-input', 'value'),
           State('username-input', 'value'),
           State('password-input', 'value'),
           State('password_2-input', 'value')])
def register(n_clicks, name, username, password, password_2):
    if n_clicks is not None:
        if None in [name, username, password, password_2]:
            return html.Div('Fill out the empty fields!')
        users = userDao.get_users()
        if users and username in users[0]:
            return html.Div('Username taken!')
        if password != password_2:
            return html.Div('The passwords do not match!')
        userDao.create_user(username=username, password=password, name=name)
        session['logged_in_user'] = username
        return [
            html.Div('Registration successful! Redirecting...'),
            dcc.Interval(id='redirect-to-main', interval=1000, n_intervals=0),
        ]


# Callback to handle logout
@callback(Output("logout-output", "children"),
          [Input("logout-button", "n_clicks")])
def logout(n_clicks):
    if n_clicks:
        session.pop('logged_in_user', None)
        # Redirect to the front page after logout
        return dcc.Location(pathname='/', id='redirect-to-login', refresh=True)
    return None


url_output = Output('url', 'pathname', allow_duplicate=True)


# Callback to redirect to the home page after logout
@callback(Output('url', 'pathname', allow_duplicate=True),
          [Input('redirect-to-login', 'n_intervals')],
          prevent_initial_call=True)
def redirect_to_login(n_intervals_to_front):
    if n_intervals_to_front > 0:
        return '/login'
    else:
        return no_update


@callback(Output('url', 'pathname', allow_duplicate=True),
          [Input('redirect-to-main', 'n_intervals')],
          prevent_initial_call=True)
def redirect_to_main(n_intervals_to_main):
    if n_intervals_to_main > 0:
        return '/main'
    else:
        return no_update
