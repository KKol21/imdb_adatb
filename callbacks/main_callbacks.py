from dash import Input, Output, State
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

    # Callback function
    @app.callback(
        Output("modal-titles", "is_open"),
        [Input("add-movies-button", "n_clicks"),
         Input("close-modal", "n_clicks")],
        State("modal-titles", "is_open")
    )
    def add_movie_modal(n_1, n_2, is_open):
        if n_1 or n_2:
            return not is_open
        return is_open


    @app.callback(
        Output("add-movies-confirm", "children"),
        [Input("add-movies-button-modal", "n_clicks")],
        [State(f"movies-{col}", "value") for col in
         ["title", "rating", "n_ratings", "release_year", "genre", "playtime"]]
    )
    def add_movie(n_clicks, title, rating, n_ratings, release_year, genre, playtime):
        if n_clicks is not None:
            if None in [title, rating, n_ratings, release_year, genre, playtime]:
                return "Each field must be filled out!"
            movies = movie_dao.get_movies()
            if (title, rating, release_year) in zip(movies[0:2], movies[4]):
                return "This movie already exists!"
            else:
                movie_dao.create_movie(title, rating, genre, release_year, n_ratings, playtime)
                return "Movie has been created!"


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
