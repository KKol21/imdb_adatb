from dash import *

app = Dash(__name__)

# Register the login page
app.config.suppress_callback_exceptions = True
app.title = 'My Dash App'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

from callbacks import *

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
