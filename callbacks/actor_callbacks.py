from dash import Input, Output, State

from dao.actorDAO import ActorDAO
from time import sleep

actorDAO = ActorDAO()


def add_actor_callbacks(app):
    data_out = Output('actor-table', 'data', allow_duplicate=True)

    @app.callback(
        data_out,
        Input('add-row-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def add_row(n_clicks):
        if n_clicks:
            # Add a new row to the table with default or empty values
            actorDAO.create_actor("", "", "")

            # Retrieve updated data for the table
            return actorDAO.get_actors()

    # Dash callback to save changes and delete empty rows
    @app.callback(
        data_out,
        Input('save-button', 'n_clicks'),
        State('actor-table', 'data'),
        prevent_initial_call=True
    )
    def save_changes(n_clicks, data):
        if n_clicks:
            # Delete rows with empty values
            empty_rows = [idx for idx, row in enumerate(data)
                          if all(value == '' or value is None for value in list(row.values())[1:])]
            data = [row for idx, row in enumerate(data) if idx not in empty_rows]

            # Remake the table with the current data
            actorDAO.delete_actors()
            for row in data:
                row = dict(list(row.items())[1:])
                actorDAO.create_actor(**row)
            sleep(0.2)

            # Retrieve updated data for the table
            return actorDAO.get_actors()
