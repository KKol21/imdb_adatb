import db.db_connector
from app import app
from callbacks.auth_callbacks import add_auth_callbacks
from callbacks.main_callbacks import add_main_callbacks
from callbacks.redirect_callbacks import add_redirect_callbacks
from callbacks.title_callbacks import add_title_callbacks
from callbacks.actor_callbacks import add_actor_callbacks

from db import create_tables, add_sample_data
# Run the app
if __name__ == '__main__':
    # create_tables.create_db_with_tables()
    # add_sample_data.fillDatabase()

    add_redirect_callbacks(app)
    add_auth_callbacks(app)
    add_title_callbacks(app)
    add_actor_callbacks(app)
    add_main_callbacks(app)

    app.run_server(debug=True)
