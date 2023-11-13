from dash import html

from colors import *


def get_header_layout(username=None):
    if username is not None:
        return get_logged_header(username)
    return None


def get_logged_header(username):
    return html.Div([
        html.Div('IMDB',
                 style={'backgroundColor': light_red,
                        'fontSize': '50px',
                        'margin': '4px',
                        'borderRadius': '5px'}
                 ),
        html.Div([
            html.Div(f'Logged in as {username}',
                     style={'fontSize': '20px'}),
            html.Button('Logout', id='logout-button',
                        style={'width': '100px',
                               'height': '30px',
                               'backgroundColor': light_red,
                               'border': 'none',
                               'borderRadius': '10px'}
                        )],
                 style={'display': 'flex',
                        'flexDirection': 'column'})
        ],
        style={'backgroundColor': purple,
               "height": "60px",
               'display': 'flex',
               'justify-content': 'space-between'}
    )


def get_basic_header():
    pass


# Layout for the login page

temp = html.Div([
    html.Button('Add movie', id='add-movie-button'),
    html.Button('Edit movie', id='edit-movie-button'),
    html.Button('Add series', id='add-series-button'),
    html.Button('Edit series', id='edit-series-button')
])

buttonStyle = {
    'fontSize': '50px',
    'padding': '10px 20px',
    'backgroundColor': white,
    'border': 'none',
    'borderRadius': '20px',
    'cursor': 'pointer',
    'transition': 'background-color 0.3s',
    'height': '70px',
    'width': '250px',
    'textAlign': 'center'
}

main_layout = html.Div([
    html.Div(
        style={'display': 'flex', 'justify-content': 'space-between', 'margin': '30px 250px 0'},
        children=[
            html.Button('Movies', id='movies-button', style=buttonStyle),
            html.Button('Series', id='series-button', style=buttonStyle),
            html.Button('Actors', id='actor-button', style=buttonStyle)
        ]),
    html.Div(id='logout-output'),
    html.H1('work in progress')
])
