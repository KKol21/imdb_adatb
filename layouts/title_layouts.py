import dash_bootstrap_components as dbc
from dash import html, dcc

from colors import light_red


def get_titles_layout(titles_data, name):
    return html.Div(
        id='titles_layout',
        children=[
            html.Div(name.capitalize(),
                     style={'color': light_red,
                            'textAlign': 'center',
                            'fontSize': '100px'}),
            dbc.Button(f"Add title",
                       id="open-add-modal-button"),
            dbc.Modal(
                id="add-title-modal",
                scrollable=True,
                size="lg",
                children=[
                    dbc.ModalTitle(f"Add {name if name == 'series' else 'movie'}"),
                    dbc.ModalBody([
                        add_movie_layout if name == "movies" else add_series_layout,
                        html.Div(id=f"submit-title-output")
                    ], style={"height": "80vh"}),
                    dbc.ModalFooter([html.Button(f"Submit", id=f"submit-{name}-button", className='button'),
                                     html.Button(f"Close", id="close-add-modal-button", className='button')],
                                    style={'backgroundColor': '#5A5A5A'}),
                    html.Div(id=f"add-title-output")
                ]
            ),
            html.Div(id='titles-list',
                     children=[
                         html.Div(id='title',
                                  children=dcc.Link(f"{title[1]} ({title[4]})",
                                                    href=f'/titles/{title[0]}', className='link'),
                                  )
                         for title in titles_data]
                     )
        ]
    )


def get_add_titles_layout_base(name):
    return [html.Label("Title: ", style={'fontSize': '18px'}),
            dcc.Input(id=f"{name}-title-input",
                      type='text'),
            html.Label("Rating (1 - 10): ", style={'fontSize': '18px'}),
            dcc.Input(id=f'{name}-rating-input',
                      type='number',
                      min=1,
                      max=10,
                      style={'margin': '10px 10px'}),
            html.Label("Number of ratings: ", style={'fontSize': '18px'}),
            dcc.Input(id=f'{name}-n_ratings-input',
                      type='number',
                      min=1,
                      step=1,
                      style={'margin': '10px 10px'}),
            html.Label("Release year: ", style={'fontSize': '18px'}),
            dcc.Input(id=f'{name}-release_year-input',
                      type='number',
                      min=1896,
                      step=1,
                      max=2024,
                      style={'margin': '10px 10px'}),
            html.Label("Genre: ", style={'fontSize': '18px'}),
            dcc.Input(id=f'{name}-genre-input',
                      type='text',
                      style={'margin': '10px 10px'})]


add_movie_layout = html.Div(style={'margin': '10px 10px',
                                   "display": "flex",
                                   "flexDirection": "column"},
                            children=get_add_titles_layout_base("movies") + [
                                html.Label("Playtime (min): ", style={'fontSize': '18px'}),
                                dcc.Input(id=f'movies-playtime-input',
                                          type='number',
                                          min=1,
                                          step=1,
                                          style={'margin': '10px 10px'})],
                            )

add_series_layout = html.Div(style={'margin': '10px 10px',
                                    "display": "flex",
                                    "flexDirection": "column"},
                             children=get_add_titles_layout_base("series") + [
                                 html.Label("Number of seasons: ", style={'fontSize': '18px'}),
                                 dcc.Input(id=f'series-n_seasons-input',
                                           type='number',
                                           min=1,
                                           step=1,
                                           style={'margin': '10px 10px'}),
                                 html.Label("Number of episodes: ", style={'fontSize': '18px'}),
                                 dcc.Input(id='series-n_episodes-input',
                                           type='number',
                                           min=1,
                                           step=1,
                                           )
                             ])


def get_single_title_layout(title_data, name):
    del_confirm = dcc.ConfirmDialog(id="confirm-delete",
                                    message="Are you sure you want to delete this title?")
    if name == "movie":
        return html.Div([del_confirm, get_movie_layout(title_data)])
    return html.Div([del_confirm, get_series_layout(title_data)])


def get_movie_layout(title_data):
    title, rating, n_ratings, release_year, genre, playtime = title_data[1:]

    return html.Div(
        className='title-details',
        children=[
            html.Div([f"{title} ({release_year})"],
                     style={"fontSize": "50px"}),
            html.Div([
                html.Div([f"Genre: {genre}"]),
                html.Div([f"Rating: {rating}/10 ({n_ratings} ratings)"]),
                html.Div([f"Playtime: {playtime} minutes"])
            ], style={'margin': '20px 0'}),
            dbc.Modal(
                id="edit-title-modal",
                size="lg",
                children=[
                    dbc.ModalTitle("Edit movie data"),
                    dbc.ModalBody([add_movie_layout,
                                   html.Div(id="edit-title-output")]),
                    dbc.ModalFooter([
                        html.Button("Edit movie", id="submit-edit-movie-button", className='button'),
                        html.Button("Close", id="close-edit-modal-button", className='button')],
                        style={'backgroundColor': '#5A5A5A'}
                    )]
            ),
            html.Button('Edit movie data', id=f'open-edit-modal-button', className='button',
                        style={'width': '100px', 'right': '10px', 'bottom': '10px', 'position': 'absolute'}),
            html.Button('Delete movie data', id='delete-title-button', className='button',
                        style={'width': '100px', 'right': '130px', 'bottom': '10px', 'position': 'absolute'}),
        ]
    )


def get_series_layout(series_data):
    title, rating, n_ratings, release_year, genre, n_seasons, n_episodes = series_data[1:]

    return html.Div(
        className='title-details',
        children=[
            html.Div(f"{title} ({release_year})",
                     style={"fontSize": "50px"}),
            html.Div([
                html.Div(f"Genre: {genre}"),
                html.Div(f"Rating: {rating}/10 ({n_ratings} ratings)"),
                html.Div(f"{n_seasons} seasons, {n_episodes} episodes")
            ], style={'margin': '20px 0'}),
            dbc.Modal(
                id="edit-title-modal",
                size="lg",
                children=[
                    dbc.ModalTitle("Edit series data"),
                    dbc.ModalBody([add_series_layout,
                                   html.Div(id="edit-title-output")]),
                    dbc.ModalFooter([
                        html.Button("Edit series", id="submit-edit-series-button"),
                        html.Button("Close", id="close-edit-modal-button")],
                        style={'backgroundColor': '#5A5A5A'}
                    )]
            ),
            html.Button('Edit series data', id=f'open-edit-modal-button', className='button',
                        style={'width': '100px', 'right': '10px', 'bottom': '10px', 'position': 'absolute'}),
            html.Button('Delete series data', id='delete-title-button', className='button',
                        style={'width': '100px', 'right': '130px', 'bottom': '10px', 'position': 'absolute'}),
        ]
    )
