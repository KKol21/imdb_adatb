from dash import *

purple = '#22092C'
dark_red = '#872341'
light_red = '#BE3144'
orange = '#F05941'
white = '#F8F8F4'


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
                        'borderRadius': '5px'}),
        html.Div([
            html.Div(f'Logged in as {username}',
                     style={'fontSize': '20px'}),
            html.Button('Logout', id='logout-button', style={'width': '100px',
                                                             'height': '30px',
                                                             'backgroundColor': light_red,
                                                             'border': 'none',
                                                             'borderRadius': '10px'})],
            style={'display': 'flex', 'flexDirection': 'column'}
            ),
    ],
        style={'backgroundColor': purple, "height": "60px", 'display': 'flex', 'justify-content': 'space-between'}
    )


def get_basic_header():
    pass


# Layout for the login page
login_layout = html.Div(
    style={'backgroundColor': '#f2f2f2', 'padding': '20px', 'textAlign': 'center'},
    children=[
        html.H2('Login Page', style={'color': '#333'}),
        html.Div(
            style={'display': 'flex', 'flexDirection': 'column'},
            children=[
                html.Div(
                    children=[
                        html.Label('Username: ', style={'fontSize': '18px'}),
                        dcc.Input(id='username-input',
                                  type='text',
                                  placeholder='Enter your username',
                                  style={'marginBottom': '10px'})
                    ]
                ),
                html.Div([
                    html.Label('Password: ', style={'fontSize': '18px'}),
                    dcc.Input(id='password-input',
                              type='password',
                              placeholder='Enter your password',
                              style={'marginBottom': '20px'})
                ]),
                html.Div(
                    html.Button('Login', id='login-button',
                                style={'fontSize': '16px',
                                       'padding': '10px 20px',
                                       'width': '100px',
                                       'align': 'center'})),
                html.Div(id='login-output', style={'marginTop': '20px'})
            ]
        ),
        dcc.Link("/register", href='register', style={'fontSize': '16px'}),
        html.H2('IMDB Data Analytic Thing! WOOHOO!', style={'marginTop': '40px', 'color': '#333'})
    ]
)

register_layout = html.Div(
    style={'backgroundColor': '#f2f2f2', 'padding': '20px', 'textAlign': 'center'},
    children=[
        html.Div([
            html.Label('Username: ', style={'fontSize': '18px'}),
            dcc.Input(id='username-input', type='text', placeholder='Enter your username',
                      style={'marginBottom': '10px'})
        ]),
        html.Div([
            html.Label('Password: ', style={'fontSize': '18px'}),
            dcc.Input(id='password-input', type='password', placeholder='Enter your password',
                      style={'marginBottom': '10px'})
        ]),
        html.Div([
            html.Label('Password_2: ', style={'fontSize': '18px'}),
            dcc.Input(id='password_2-input', type='password', placeholder='Enter your password again',
                      style={'marginBottom': '10px'})
        ]),
        html.Div([
            html.Label('Name: ', style={'fontSize': '18px'}),
            dcc.Input(id='name-input', type='text', placeholder="Enter your name", style={'marginBottom': '20px'})
        ]),
        html.Button('Register', id='register-button', style={'fontSize': '16px', 'padding': '10px 20px'}),
        html.Div(id='register-output', style={'marginTop': '20px'})
    ]
)

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


# title_data: title_id, title, rating, release_year
def titles_layout(titles_data, title_type):
    name = title_type[1:].capitalize()
    return html.Div(
        [html.Div(name, style={'color': light_red, 'textAlign': 'center', 'fontSize': '100px'})] +
        [html.Div(
            [html.Div(
                dcc.Link(f"{title[1]}({title[4]})",
                      href=f'/{title[0]}'),
                style={'backgroundColor': white, 'margin': '10px 50px', 'borderRadius': '10px'})
                for title in titles_data], style={'display': 'flex',
                                                  'flexDirection': 'column',
                                                  'height': '150px',
                                                  'fontSize': '50px'},)
        ]
    )
