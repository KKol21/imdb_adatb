from dash import *

# Layout for the login page
login_layout = html.Div([
    html.H2('Login Page'),
    html.Div([
        html.Label('Username'),
        dcc.Input(id='username-input', type='text', placeholder='Enter your username'),
        html.Label('Password'),
        dcc.Input(id='password-input', type='password', placeholder='Enter your password'),
        html.Button('Login', id='login-button'),
        html.Div(id='login-output')
    ])
])

register_layout = html.Div(
    [
        html.Label('Username'),
        dcc.Input(id='username-input', type='text', placeholder='Enter your username'),
        html.Label('Password'),
        dcc.Input(id='password-input', type='password', placeholder='Enter your password'),
        html.Label('Name'),
        dcc.Input(id='name-input', type='text', placeholder="Enter your name"),
        html.Button('Register', id='register-button'),
        html.Div(id='register-output')
    ]
)

# Layout for the main page (you can replace this with your actual app layout)
front_layout = html.Div([
    dcc.Link("/login", href='login'),
    dcc.Link("/register", href='register'),
    html.H2('IMDB Data Analytic Thing! WOOHOO!'),
    # Add your main app content here
])

main_layout = html.Div([
    html.Button('Logout', id='logout-button'),
    html.Button('Movies', id='movies-button'),
    html.Button('Series', id='series-button'),
    html.Button('Add movie', id='add-movie-button'),
    html.Button('Edit movie', id='edit-movie-button'),
    html.Button('Add series', id='add-series-button'),
    html.Button('Edit series', id='edit-series-button'),
    html.Div(id='logout-output'),
    html.H1('work in progress')
])
