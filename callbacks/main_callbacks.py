from dash import Input, Output
from flask import session

from dao import actorDAO, movieDAO, seriesDAO, ratingsDAO, titlesDAO
from db.db_connector import db_conn
from layouts.auth_layout import register_layout, login_layout
from layouts.layouts import main_layout, get_header_layout
from layouts.title_layouts import get_titles_layout, get_single_title_layout

actor_dao = actorDAO.ActorDAO(db_conn=db_conn)
movie_dao = movieDAO.MoviesDAO(db_conn=db_conn)
series_dao = seriesDAO.SeriesDAO(db_conn=db_conn)
ratings_dao = ratingsDAO.RatingsDAO(db_conn=db_conn)
titles_dao = titlesDAO.TitlesDAO(db_conn=db_conn)


def add_main_callbacks(app):
    # Callback to update the page content based on the URL
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if 'logged_in_user' not in session:
            if pathname == '/register':
                return register_layout
            return login_layout
        layout = main_layout
        if pathname in ['/movies', '/series']:
            layout = get_titles_layout_from_path(pathname)
        if '/title' in pathname:
            layout = get_title_layout_from_path(pathname)
        return get_header_layout(session['logged_in_user']), layout


def get_titles_layout_from_path(pathname):
    titles_data = movie_dao.get_movies() if pathname == '/movies' else series_dao.get_series()
    layout = get_titles_layout(titles_data=titles_data,
                               name=pathname.split('/')[1])
    return layout


def get_title_layout_from_path(pathname):
    title_id = pathname.split('/')[2]
    title_data = titles_dao.get_title_by_id_full(title_id)
    name = "movie" if len(title_data) == 7 else "series"
    layout = get_single_title_layout(title_data, name)
    return layout
