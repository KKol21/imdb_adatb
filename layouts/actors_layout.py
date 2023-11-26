from dash import html, dash_table
import dash_bootstrap_components as dbc

from colors import light_red, yellow, black
from dao.actorDAO import ActorDAO

actorDAO = ActorDAO()

actors_layout = html.Div([
    html.Div("Actors",
             style={'color': light_red,
                    'textAlign': 'center',
                    'fontSize': '100px'}),
    html.Div(
        dash_table.DataTable(
            id='actor-table',
            page_size=50,
            columns=[
                {'name': 'Name', 'id': 'name', 'editable': True},
                {'name': 'Nationality', 'id': 'nationality', 'editable': True},
                {'name': 'Date of Birth', 'id': 'date_of_birth', 'editable': True},
            ],
            row_deletable=True,
            editable=True,
            style_table={'overflowX': 'auto'},
            style_header={'backgroundColor': yellow,
                          'fontWeight': 'bold',
                          'border': f'2px solid {black}'},
            style_cell={'border': f'2px solid {yellow}'},
            style_data={'backgroundColor': black,
                        'color': 'white',
                        'textAlign': 'center'},
            data=actorDAO.get_actors_dict()
        ),
        style={'margin': '0 400px'}
    ),

    html.Div(
        children=[dbc.Button('Add Row', id='add-row-button'),
                  dbc.Button('Save Changes', id='save-button')],
        style={'display': 'flex', 'justify-content': 'space-evenly'}
    )
])
