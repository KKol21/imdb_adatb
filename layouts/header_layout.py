from dash import html, dcc

basic_header = None


def get_header_layout(username=None):
    if username is not None:
        return get_logged_header(username)
    return basic_header


def get_logged_header(username):
    return html.Div(className='header',
                    children=[
                        dcc.ConfirmDialog(id="confirm-logout",
                                          message="Are you sure you want to logout?"),
                        html.Button('IMDB', id="imdb-button"),
                        html.Button('Movies', id='movies-button', className='msa-button'),
                        html.Button('Series', id='series-button', className='msa-button'),
                        html.Button('Actors', id='actors-button', className='msa-button'),
                        html.Div(id='logout-corner',
                                 children=[
                                     html.Div(f'Logged in as {username}',
                                              style={'fontSize': '20px', 'color': '#FFFFFF'}),
                                     html.Button('Logout', id='logout-button', className='button')
                                 ]
                                 )
                    ]
                    )
