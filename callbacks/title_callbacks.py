from dash import Output, Input, State

from dao.movieDAO import MoviesDAO
from dao.seriesDAO import SeriesDAO
from dao.titlesDAO import TitlesDAO
from db.db_connector import conn

MoviesDAO = MoviesDAO()
SeriesDAO = SeriesDAO()
TitlesDAO = TitlesDAO()

cursor = conn.cursor()

def add_title_callbacks(app):
    @app.callback(
        Output("add-title-output", "children"),
        [Input("submit-movies-button", "n_clicks")],
        [State(f"movies-{col}-input", "value") for col in
         ["title", "rating", "genre", "release_year", "n_ratings", "playtime"]],
        prevent_initial_call=True)
    def add_movie(n_clicks, title, rating, genre, release_year, n_ratings, playtime):
        if n_clicks is not None:
            if None in [title, rating, genre, release_year, n_ratings, playtime]:
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
         ["title", "rating", "genre", "release_year", "n_ratings", "n_seasons", "n_episodes"]],
        prevent_initial_call=True)
    def add_series(n_clicks, title, rating, genre, release_year, n_ratings, n_seasons, n_episodes):
        if n_clicks is not None:
            if None in [title, rating, genre, release_year, n_ratings, n_seasons, n_episodes]:
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
        [Input('open-add-modal-button', 'n_clicks'),
         Input('close-add-modal-button', 'n_clicks')],
        State("add-title-modal", "is_open"))
    def trigger_add_title_modal(n_s, n_c, is_open):
        if n_s or n_c:
            return not is_open
        return is_open

    @app.callback(
        Output("edit-title-output", "children"),
        [Input('submit-edit-movie-button', "n_clicks")],
        [State(f"movies-{col}-input", "value") for col in
         ["title", "rating", "genre", "release_year", "n_ratings", "playtime"]]
        + [State("url", "pathname")],
        prevent_initial_call=True)
    def edit_movie(n_clicks, title, rating, genre, release_year, n_ratings, playtime, url):
        if n_clicks:
            if all(field is None for field in [title, rating, genre, release_year, n_ratings, playtime]):
                return "Provide data in order to update movie!"
            title_id = url.split('/')[2]
            new_data = {field: value for (field, value) in zip(
                ["title", "rating", "genre", "release_year", "n_ratings", "playtime"],
                [title, rating, genre, release_year, n_ratings, playtime]
            )}
            MoviesDAO.update_movie(title_id, new_data)
            return "Movie data has been edited!"

    @app.callback(
        Output("edit-title-output", "children", allow_duplicate=True),
        [Input("submit-edit-series-button", "n_clicks")],
        [State(f"series-{col}-input", "value") for col in
         ["title", "rating", "genre", "release_year", "n_ratings", "n_seasons", "n_episodes"]]
        + [State("url", "pathname")],
        prevent_initial_call=True)
    def edit_series(n_clicks, title, rating, genre, release_year, n_ratings, n_seasons, n_episodes, url):
        if n_clicks:
            if all(field is None for field in [title, rating, genre, release_year, n_ratings, n_seasons, n_episodes]):
                return "Provide data in order to update series!"
            title_id = url.split('/')[2]
            new_data = {field: value for (field, value) in zip(
                ["title", "rating", "genre", "release_year", "n_ratings", "n_seasons", "n_episodes"],
                [title, rating, genre, release_year, n_ratings, n_seasons, n_episodes]
            )}
            SeriesDAO.update_series(title_id, new_data)
            return "Series data has been edited!"

    @app.callback(
        Output("edit-title-modal", "is_open"),
        [Input('open-edit-modal-button', 'n_clicks'),
         Input('close-edit-modal-button', 'n_clicks')],
        State("edit-title-modal", "is_open"))
    def trigger_edit_title_modal(n_s, n_c, is_open):
        if n_s or n_c:
            return not is_open
        return is_open

    @app.callback(Output("confirm-delete", "displayed"),
                  [Input("delete-title-button", "n_clicks")])
    def confirm_delete(n_clicks):
        if n_clicks is not None:
            return True
        return False

    @app.callback(Output("url", "pathname", allow_duplicate=True),
                  [Input("confirm-delete", "submit_n_clicks")],
                  State("url", "pathname"),
                  prevent_initial_call=True)
    def delete_title(n_clicks, url):
        if n_clicks:
            title_id = url.split('/')[2]
            title_type = TitlesDAO.get_title_type_by_id(title_id=title_id)
            if title_type == "movie":
                MoviesDAO.delete_movie(title_id)
            else:
                SeriesDAO.delete_series(title_id)
            return '/movies' if title_type == "movie" else "/series"

    @app.callback(Output("rating-output", "children"),
                  [Input("rate-title-button", "n_clicks")],
                  [State("rating-radio", "value"),
                  State("url", "pathname")])
    def rate_title(n_clicks, rating, pathname):
        from flask import session
        if n_clicks:
            username = session["logged_in_user"]
            title_id = pathname.split('/')[2]
            cursor.execute(f"SELECT rating FROM ratings WHERE username = '{username}' AND title_id = {title_id}")
            user_prev_rating = cursor.fetchone()
            if user_prev_rating is not None:
                is_replace = True
            else:
                is_replace = False
            cursor.execute(f'INSERT INTO ratings (username, title_id, rating)'
                           f' VALUES (\'{username}\', {title_id}, {rating}) ON DUPLICATE KEY UPDATE rating = {rating}')

            conn.commit()

            title_data = TitlesDAO.get_title_by_id(title_id)
            n_ratings = title_data[3]
            prev_rating = title_data[2]
            if is_replace:
                new_rating = (prev_rating * n_ratings - user_prev_rating[0] + rating) / n_ratings
                new_rating = round(new_rating, 3)
                TitlesDAO.update_title(title_id=title_id,
                                       new_data={"n_ratings": n_ratings,
                                                 "rating": new_rating})
            else:
                new_rating = (prev_rating * n_ratings + rating) / (n_ratings + 1)
                new_rating = round(new_rating, 3)
                TitlesDAO.update_title(title_id=title_id,
                                       new_data={"n_ratings": n_ratings + 1,
                                                 "rating": new_rating})
            return "Title rated"
