from dash import Input, Output, no_update
from flask import session

from dao import actorDAO, movieDAO, seriesDAO, ratingsDAO, titlesDAO
from db.db_connector import conn

actor_dao = actorDAO.ActorDAO()
movie_dao = movieDAO.MoviesDAO()
series_dao = seriesDAO.SeriesDAO()
ratings_dao = ratingsDAO.RatingsDAO(db_conn=conn)
titles_dao = titlesDAO.TitlesDAO()


def add_main_callbacks(app):
    from layouts.auth_layout import register_layout, login_layout
    from layouts.main_layout import main_layout
    from layouts.header_layout import get_header_layout
    from layouts.actors_layout import actors_layout

    @app.callback([Output('page-content', 'children'),
                   Output('url', 'pathname')],
                  [Input('url', 'pathname')])
    def display_page(pathname):
        # Check if the URL has changed
        if "prev_path" in session and session["prev_path"] == pathname:
            return no_update
        session["prev_path"] = pathname
        # Validate user
        if 'logged_in_user' not in session:
            if pathname == '/register':
                return register_layout, pathname
            return login_layout, '/login'
        # Display url or main
        header = get_header_layout(session['logged_in_user'])
        result = main_layout
        new_url = '/main'
        if pathname in ['/movies', '/series']:
            result, new_url = get_titles_layout_from_path(pathname), pathname
        if '/title' in pathname:
            result, new_url = get_title_layout_from_path(pathname), pathname
        if '/actors' == pathname:
            result, new_url = actors_layout, pathname
        return [header, result], new_url


def get_titles_layout_from_path(pathname):
    from layouts.title_layouts import get_titles_layout
    titles_data = movie_dao.get_movies() if pathname == '/movies' else series_dao.get_series()
    layout = get_titles_layout(titles_data=titles_data,
                               name=pathname.split('/')[1])
    return layout


def get_title_layout_from_path(pathname):
    from layouts.title_layouts import get_single_title_layout
    title_id = pathname.split('/')[2]
    title_data = titles_dao.get_title_by_id_full(title_id)
    name = "movie" if len(title_data) == 7 else "series"
    layout = get_single_title_layout(title_data, name)
    return layout
