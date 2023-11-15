from dash import html

from colors import *


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

