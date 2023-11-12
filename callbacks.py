from dash import *
from layouts import *
from main import app
from mysql import connector
from dao import userDao, actorDao, movieDao, seriesDao, ratingsDao
from flask import session

db_conn = connector.connect(user="root", database="imdb")
userDao = userDao.UserDAO(db_conn=db_conn)
actor_dao = actorDao.ActorDAO(db_conn=db_conn)
movie_dao = movieDao.MovieDAO(db_conn=db_conn)
series_dao = seriesDao.SeriesDAO(db_conn=db_conn)
ratings_dao = ratingsDao.RatingsDAO(db_conn=db_conn)

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return login_layout
    elif pathname == '/main' and 'logged_in' in session and session['logged_in']:
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
        users = userDao.get_users()
        valid_user = any(
            username == user[0] and password == user[1]
            for user in users
        )
        if valid_user:
            # Successful login, redirect to the main page
            session['logged_in'] = True
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
        users = userDao.get_users()
        if users and username in users[0]:
            return html.Div('Username taken!')
        userDao.create_user(username=username, password=password, name=name)
        session['logged_in'] = True
        return [
            html.Div('Registration successful! Redirecting in 3 seconds...'),
            dcc.Interval(id='redirect-interval', interval=3000, n_intervals=0),
        ]


@app.callback(Output('url', 'pathname'),
              [Input('redirect-interval', 'n_intervals')])
def redirect_to_main(n_intervals):
    if n_intervals > 0:
        return '/main'
    else:
        return no_update
