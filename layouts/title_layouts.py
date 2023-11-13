from dash import html, dcc

from colors import light_red, white


def get_titles_layout(titles_data):
    name = "movies" if len(titles_data[0]) == 7 else "series"
    return html.Div(
        [html.Div(name.capitalize(),
                  style={'color': light_red,
                         'textAlign': 'center',
                         'fontSize': '100px'})] +
        [html.Div(
            [html.Div(
                dcc.Link(f"{title[1]}({title[4]})",
                         href=f'/titles/{title[0]}'),
                style={'backgroundColor': white, 'margin': '10px 50px', 'borderRadius': '10px'})
                for title in titles_data], style={'display': 'flex',
                                                  'flexDirection': 'column',
                                                  'height': '150px',
                                                  'fontSize': '50px'}, )
        ]
    )


def get_single_title_layout(title_data):
    title_id = title_data[0]
    title = title_data[1]
    html.Div(
        [html.Div(title,
                  style={'color': light_red,
                         'textAlign': 'center',
                         'fontSize': '100px'})]
        )


