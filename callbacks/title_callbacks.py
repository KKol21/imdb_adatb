from dash import Output, Input, State

from dao.movieDAO import MoviesDAO
from db.db_connector import conn

MoviesDAO = MoviesDAO(db_conn=conn)


def add_title_callbacks(app):
    @app.callback(
        Output("add-title-output", "children"),
        [Input("submit-movies-button", "n_clicks")],
        [State(f"movies-{col}-input", "value") for col in
         ["title", "rating", "n_ratings", "release_year", "genre", "playtime"]])
    def add_movie(n_clicks, title, rating, n_ratings, release_year, genre, playtime):
        if n_clicks is not None:
            if None in [title, rating, n_ratings, release_year, genre, playtime]:
                return "Each field must be filled out!"
            movies = MoviesDAO.get_movies()
            #titles, ratings, release_years = [(movie[1], movie[2], movie[4]) for movie in movies]
            if (title, rating, release_year) in zip(movies[0:2], movies[4]):
                return "This movie already exists!"
            else:
                MoviesDAO.create_movie(title, rating, genre, release_year, n_ratings, playtime)
                return "Movie has been created!"

    @app.callback(
        Output("add-title-modal", "is_open"),
        [Input('open-modal-button', 'n_clicks'),
         Input('close-modal-button', 'n_clicks')],
        State("add-title-modal", "is_open"))
    def trigger_title_modal(n_s, n_c, is_open):
        if n_s or n_c:
            return not is_open
        return is_open
