import dash
from dash import Output, Input, State

from dao.movieDAO import MoviesDAO
from dao.seriesDAO import SeriesDAO
from db.db_connector import conn

MoviesDAO = MoviesDAO(db_conn=conn)
SeriesDAO = SeriesDAO(db_conn=conn)


def add_title_callbacks(app):
    @app.callback(
        Output("add-title-output", "children"),
        [Input("submit-movies-button", "n_clicks")],
        [State(f"movies-{col}-input", "value") for col in
         ["title", "rating", "n_ratings", "release_year", "genre", "playtime"]],
        prevent_initial_call=True)
    def add_movie(n_clicks, title, rating, n_ratings, release_year, genre, playtime):
        if n_clicks is not None:
            if None in [title, rating, n_ratings, release_year, genre, playtime]:
                return "Fields cannot be empty or invalid!"
            movies = MoviesDAO.get_movies()
            key_data = [(movie[1], movie[2], movie[4]) for movie in movies]
            if (title, rating, release_year) in zip(*key_data):
                return "This movie already exists!"
            else:
                MoviesDAO.create_movie(title, rating, genre, release_year, n_ratings, playtime)
                return "Movie has been created!"

    @app.callback(
        Output("add-title-output", "children", allow_duplicate=True),
        [Input("submit-series-button", "n_clicks")],
        [State(f"series-{col}-input", "value") for col in
         ["title", "rating", "n_ratings", "release_year", "genre", "n_seasons", "n_episodes"]],
        prevent_initial_call=True)
    def add_series(n_clicks, title, rating, n_ratings, release_year, genre, n_seasons, n_episodes):
        if n_clicks is not None:
            if None in [title, rating, n_ratings, release_year, genre, n_seasons, n_episodes]:
                return "Fields cannot be empty or invalid!"
        all_series = SeriesDAO.get_series()
        key_data = [(series[1], series[2], series[4]) for series in all_series]
        if (title, rating, release_year) in zip(*key_data):
            return "This series already exists!"
        else:
            SeriesDAO.create_series(title, rating, genre, release_year, n_ratings, n_seasons, n_episodes)
            return "Series has been created!"

    @app.callback(
        Output("add-title-modal", "is_open"),
        [Input('open-modal-button', 'n_clicks'),
         Input('close-modal-button', 'n_clicks')],
        State("add-title-modal", "is_open"))
    def trigger_title_modal(n_s, n_c, is_open):
        if n_s or n_c:
            return not is_open
        return is_open

