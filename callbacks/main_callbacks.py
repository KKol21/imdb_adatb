from dash import Input, Output, callback
from flask import session

from dao import actorDao, movieDao, seriesDao, ratingsDao, titlesDao
from db.db_connector import db_conn
from layouts.auth_layout import register_layout, login_layout
from layouts.layouts import main_layout, get_header_layout
from layouts.title_layouts import get_titles_layout, get_single_title_layout

actor_dao = actorDao.ActorDAO(db_conn=db_conn)
movie_dao = movieDao.MoviesDAO(db_conn=db_conn)
series_dao = seriesDao.SeriesDAO(db_conn=db_conn)
ratings_dao = ratingsDao.RatingsDAO(db_conn=db_conn)
titles_dao = titlesDao.TitlesDAO(db_conn=db_conn)


# Callback to update the page content based on the URL
@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if 'logged_in_user' not in session:
        if pathname == '/register':
            return register_layout
        return login_layout
    layout = main_layout
    if pathname in ['/movies', '/series']:
        title_data = movie_dao.get_movies() if pathname == '/movies' else series_dao.get_series()
        layout = get_titles_layout(title_data)
    if '/title' in pathname:
        title_id = pathname.split('/')[2]

        layout = get_single_title_layout(title_id)
    return get_header_layout(session['logged_in_user']), layout


@callback(Output('url', 'pathname', allow_duplicate=True),
          [Input('movies-button', 'n_clicks')],
          prevent_initial_call=True)
def display_movies(n_clicks):
    if n_clicks is not None:
        return '/movies'


@callback(Output('url', 'pathname', allow_duplicate=True),
          [Input('series-button', 'n_clicks')],
          prevent_initial_call=True)
def display_series(n_clicks):
    if n_clicks is not None:
        return '/series'
