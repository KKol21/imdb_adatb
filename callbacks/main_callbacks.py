from dash import Input, Output, State, no_update
from flask import session

from dao import actorDAO, movieDAO, seriesDAO, ratingsDAO, titlesDAO
from db.db_connector import conn

actor_dao = actorDAO.ActorDAO(db_conn=conn)
movie_dao = movieDAO.MoviesDAO(db_conn=conn)
series_dao = seriesDAO.SeriesDAO(db_conn=conn)
ratings_dao = ratingsDAO.RatingsDAO(db_conn=conn)
titles_dao = titlesDAO.TitlesDAO(db_conn=conn)


def no_update_or_path(curr_path, target_path):
    return no_update if curr_path == target_path else target_path


def add_main_callbacks(app):
    from layouts.auth_layout import register_layout, login_layout
    from layouts.main_layout import main_layout
    from layouts.header_layout import get_header_layout
    # Callback to update the page content based on the URL

    @app.callback([Output('page-content', 'children'),
                   Output('url', 'pathname')],
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if 'logged_in_user' not in session:
            if pathname == '/register':
                return register_layout, pathname
            return login_layout, '/login'
        header = get_header_layout(session['logged_in_user'])
        if pathname in ['/movies', '/series']:
            return [header, get_titles_layout_from_path(pathname)], pathname
        if '/title' in pathname:
            return [header, get_title_layout_from_path(pathname)], pathname
        return [header, main_layout], '/main'

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
