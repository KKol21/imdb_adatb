from dash import html, dcc

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
                                  style={'marginBottom': '10px'})
                    ]
                ),
                html.Div([
                    html.Label('Password: ', style={'fontSize': '18px'}),
                    dcc.Input(id='password-input',
                              type='password',
                              style={'marginBottom': '20px'})
                ]),
                html.Div(
                    html.Button('Login', id='login-button',
                                style={'fontSize': '16px',
                                       'padding': '10px 20px',
                                       'width': '100px',
                                       'align': 'center'})),
                html.Div(id='login-output',
                         style={'marginTop': '20px'})
            ]
        ),
        dcc.Link("/register", href='register',
                 style={'fontSize': '16px'}),
        html.H2('IMDB Data Analytic Thing! WOOHOO!',
                style={'marginTop': '40px',
                       'color': '#333'})
    ]
)

register_layout = html.Div(
    style={'backgroundColor': '#f2f2f2',
           'padding': '20px',
           'textAlign': 'center'},
    children=[
        html.Div([
            html.Label('Username: ', style={'fontSize': '18px'}),
            dcc.Input(id='username-input',
                      type='text',
                      style={'marginBottom': '10px'})
        ]),
        html.Div([
            html.Label('Password: ', style={'fontSize': '18px'}),
            dcc.Input(id='password-input',
                      type='password',
                      style={'marginBottom': '10px'})
        ]),
        html.Div([
            html.Label('Password_2: ', style={'fontSize': '18px'}),
            dcc.Input(id='password_2-input',
                      type='password',
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
