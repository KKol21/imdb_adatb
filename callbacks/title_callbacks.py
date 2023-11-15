import dash
from dash import Output, Input, State

from dao.movieDAO import MoviesDAO
from db.db_connector import conn

MoviesDAO = MoviesDAO(db_conn=conn)


def add_title_callbacks(app):
    @app.callback(
        Output("add-movies-output", "children"),
        [Input("add-movies-button", "n_clicks")],
        [State(f"movies-{col}-input", "value") for col in
         ["title", "rating", "n_ratings", "release_year", "genre", "playtime"]]
    )
    def add_movie(n_clicks, title, rating, n_ratings, release_year, genre, playtime):
        if n_clicks is not None:
            if None in [title, rating, n_ratings, release_year, genre, playtime]:
                return "Each field must be filled out!"
            movies = MoviesDAO.get_movies()
            if (title, rating, release_year) in zip(movies[0:2], movies[4]):
                return "This movie already exists!"
            else:
                MoviesDAO.create_movie(title, rating, genre, release_year, n_ratings, playtime)
                return "Movie has been created!"
