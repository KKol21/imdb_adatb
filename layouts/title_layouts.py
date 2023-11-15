from dash import html, dcc
import dash_bootstrap_components as dbc
from colors import light_red, white


def get_titles_layout(titles_data, name):
    return html.Div(
        id='titles_layout',
        children=
        [html.Div(name.capitalize(),
                  style={'color': light_red,
                         'textAlign': 'center',
                         'fontSize': '100px'}),
         html.Button(f"Add {name}", id=f"add-{name}-button"),
         dbc.Modal(
             id="modal",
             children=[
                 dbc.ModalTitle(f"Add {name}"),
                 dbc.ModalBody([
                     add_movie_layout,
                     html.Div(id=f"add-{name}-output")
                 ], style={"height": "30vh"}),
                 dbc.ModalFooter([html.Button(f"Add {name}", id=f"add-{name}-button-modal"),
                                 html.Button(f"Close", id="close-modal")])
             ],
             is_open=False
         ),
         html.Div(
             [html.Div(
                 dcc.Link(f"{title[1]}({title[4]})",
                          href=f'/titles/{title[0]}'),
                 style={'backgroundColor': white,
                        'margin': '10px 50px',
                        'borderRadius': '10px'})
                 for title in titles_data],
             style={'display': 'flex',
                    'flexDirection': 'column',
                    'height': '150px',
                    'fontSize': '50px'}
         )
         ]
    )


add_movie_layout = html.Div(
    style={'display': 'flex', 'flexDirection': 'column'},
    children=
    [html.Div(
        children=[
            html.Label(col, style={'fontSize': '18px'}),
            dcc.Input(id=f'movies-{col}',
                      type='text',
                      style={'marginBottom': '10px'})
        ]
    ) for col in ["title", "rating", "n_ratings", "release_year", "genre", "playtime"]]
)


def get_single_title_layout(title_data, name):
    if name == "movie":
        return get_movie_layout(title_data)
    return get_series_layout(title_data)


def get_movie_layout(title_data):
    title, rating, n_ratings, release_year, genre, playtime = title_data[1:]

    return html.Div([
        html.Div(
            style={"display": "flex",
                   "flexDirection": "column",
                   "fontSize": "20px"},
            children=[
                html.Div([f"{title} ({release_year})"],
                         style={"fontSize": "50px"}),
                html.Div([f"Genre: {genre}"]),
                html.Div([f"Rating: {rating}/5 ({n_ratings} ratings)"]),
                html.Div([f"Playtime: {playtime} minutes"])
            ]
        ),
        html.Button('Edit title details', id=f'Edit-title')
    ])


def get_series_layout(series_data):
    title, rating, n_ratings, release_year, genre, n_seasons, n_episodes = series_data[1:]

    return html.Div([
        html.Div(
            style={"display": "flex",
                   "flexDirection": "column",
                   "fontSize": "20px"},
            children=[
                html.Div([
                    html.Div(f"{title} ({release_year})",
                             style={"fontSize": "50px"}),
                    html.Div(f"Genre: {genre}"),
                    html.Div(f"Rating: {rating}/5 ({n_ratings} ratings)"),
                    html.Div(f"{n_seasons} seasons, {n_episodes} episodes")
                ])
            ]
        ),
        html.Button('Edit title details', id=f'edit-title-button')
    ])
