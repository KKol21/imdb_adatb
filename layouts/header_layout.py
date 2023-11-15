from dash import html, dcc

from colors import light_red, purple

basic_header = None


def get_header_layout(username=None):
    if username is not None:
        return get_logged_header(username)
    return basic_header


def get_logged_header(username):
    return html.Div([
        dcc.ConfirmDialog(id="confirm-logout",
                          message="Are you sure you want to logout?"),
        html.Button('IMDB',
                    style={'backgroundColor': light_red,
                           'fontSize': '50px',
                           'margin': '4px',
                           'borderRadius': '5px'},
                    id="imdb-button"
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
