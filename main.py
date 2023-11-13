from app import app

from callbacks.main_callbacks import add_main_callbacks
from callbacks.redirect_callbacks import add_redirect_callbacks
from callbacks.auth_callbacks import add_auth_callbacks

# Run the app
if __name__ == '__main__':
    add_redirect_callbacks(app)
    add_auth_callbacks(app)
    add_main_callbacks(app)
    app.run_server(debug=True)