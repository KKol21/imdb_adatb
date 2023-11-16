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
                       id="open-modal-button"),
            dbc.Modal(
                id="add-title-modal",
                scrollable=True,
                size="lg",
                is_open=False,
                children=[
                    dbc.ModalTitle(f"Add {name if name == 'series' else 'movie'}"),
                    dbc.ModalBody([
                        add_movie_layout if name == "movies" else add_series_layout,
                        html.Div(id=f"submit-title-output")
                    ], style={"height": "80vh"}),
                    dbc.ModalFooter([html.Button(f"Submit", id=f"submit-{name}-button"),
                                     html.Button(f"Close", id="close-modal-button")]),
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


add_movie_layout = html.Div([html.Label("Title: "),
                             dcc.Input(id="movies-title-input",
                                       type='text'),
                             html.Label("Rating: ", style={'fontSize': '18px'}),
                             dcc.Input(id=f'movies-rating-input',
                                       type='number',
                                       style={'margin': '10px 10px'}),
                             html.Label("Number of ratings: ", style={'fontSize': '18px'}),
                             dcc.Input(id=f'movies-n_ratings-input',
                                       type='number',
                                       style={'margin': '10px 10px'}),
                             html.Label("Release year: ", style={'fontSize': '18px'}),
                             dcc.Input(id=f'movies-release_year-input',
                                       type='number',
                                       style={'margin': '10px 10px'}),
                             html.Label("Genre: ", style={'fontSize': '18px'}),
                             dcc.Input(id=f'movies-genre-input',
                                       type='text',
                                       style={'margin': '10px 10px'}),
                             html.Label("Playtime (min): ", style={'fontSize': '18px'}),
                             dcc.Input(id=f'movies-playtime-input',
                                       type='number',
                                       style={'margin': '10px 10px'})],
                            style={'margin': '10px 10px',
                                   "display": "flex",
                                   "flexDirection": "column"})

add_series_layout = None


def get_single_title_layout(title_data, name):
    if name == "movie":
        return get_movie_layout(title_data)
    return get_series_layout(title_data)


def get_movie_layout(title_data):
    title, rating, n_ratings, release_year, genre, playtime = title_data[1:]

    return html.Div([
        html.Div(
            className='title-details',
            children=[
                html.Div([f"{title} ({release_year})"],
                         style={"fontSize": "50px"}),
                html.Div([
                    html.Div([f"Genre: {genre}"]),
                    html.Div([f"Rating: {rating}/5 ({n_ratings} ratings)"]),
                    html.Div([f"Playtime: {playtime} minutes"])
                ], style={'margin': '20px 0'}),
                html.Button('Edit title details', id=f'Edit-title', className='button',
                            style={'width': '100px', 'right': '10px', 'bottom': '10px', 'position': 'absolute'})
            ]
        )
    ])


def get_series_layout(series_data):
    title, rating, n_ratings, release_year, genre, n_seasons, n_episodes = series_data[1:]

    return html.Div([
        html.Div(
            className='title-details',
            children=[
                html.Div(f"{title} ({release_year})",
                         style={"fontSize": "50px"}),
                html.Div([
                    html.Div(f"Genre: {genre}"),
                    html.Div(f"Rating: {rating}/5 ({n_ratings} ratings)"),
                    html.Div(f"{n_seasons} seasons, {n_episodes} episodes")
                ], style={'margin': '20px 0'}),
                html.Button('Edit title details', id=f'Edit-title',
                            className='button',
                            style={'width': '100px', 'right': '10px', 'bottom': '10px', 'position': 'absolute'})
            ]
        ),
    ])
