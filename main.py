import dash
from dash import html, dcc, callback, Output, Input, State

app = dash.Dash(__name__)

# Assume you have a users dictionary for simplicity. In a real app, you'd use a database.
users = {'admin': 'admin'}

# Register the login page
app.config.suppress_callback_exceptions = True
app.title = 'My Dash App'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

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
    html.H2('Welcome to My Dash App!'),
    # Add your main app content here
])

main_layout = html.Div([
    html.H1('work in progress')
])


# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return login_layout
    elif pathname == '/main':
        return main_layout
    elif pathname == '/register':
        return register_layout
    else:
        return front_layout


# Callback to handle the login logic
@app.callback(Output('login-output', 'children'),
              [Input('login-button', 'n_clicks')],
              [State('username-input', 'value'),
               State('password-input', 'value')])
def login(n_clicks, username, password):
    if n_clicks is not None:
        if username in users and users[username] == password:
            # Successful login, redirect to the main page
            return dcc.Location(pathname='/main', id='redirect-home', refresh=True)
        else:
            return html.Div('Invalid username or password. Please try again.')



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
