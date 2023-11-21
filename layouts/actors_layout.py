from dash import html, dash_table

from dao.actorDAO import ActorDAO

actorDAO = ActorDAO()

actors_layout = html.Div([
    dash_table.DataTable(
        id='actor-table',
        page_size=50,
        columns=[
            {'name': 'actor_id', 'id': 'actor_id', 'editable': False},
            {'name': 'Name', 'id': 'name', 'editable': True},
            {'name': 'Nationality', 'id': 'nationality', 'editable': True},
            {'name': 'Date of Birth', 'id': 'date_of_birth', 'editable': True},
        ],
        hidden_columns=['actor_id'],
        row_deletable=True,
        editable=True,
        style_table={'overflowX': 'auto'},
        data=actorDAO.get_actors_dict()
    ),

    # Button to add a new row
    html.Button('Add Row', id='add-row-button'),

    # Button to save changes
    html.Button('Save Changes', id='save-button')
])
