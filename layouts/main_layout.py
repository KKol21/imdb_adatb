from dash import html, dash_table

from db.db_connector import conn

cursor = conn.cursor()


def get_n_movie_releases():
    cursor.execute(
        """SELECT release_year, COUNT(*) as n_movies
           FROM titles t 
           JOIN movies m on t.title_id = m.title_id                      
           WHERE release_year > 2000
           GROUP BY release_year
           ORDER BY release_year DESC
            """)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    # Convert the result to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]
    return data


def get_top_series():
    cursor.execute("""SELECT t.title, t.release_year, t.rating
                      FROM Titles t
                      JOIN Series s ON t.title_id = s.title_id
                      WHERE t.release_year > 2019
                      ORDER BY t.rating DESC
                      LIMIT 5""")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    # Convert the result to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]
    return data


def get_series_from_most_famous_actor():
    pass


def best_movie_per_actor():
    pass


def get_main_layout():
    return html.Div([
        html.Div(id='logout-output'),
        html.Div([
            "Top series since 2019",
            dash_table.DataTable(
                id="top-series",
                columns=[{'name': 'Title', 'id': 'title', 'editable': False},
                         {'name': 'Release year', 'id': 'release_year', 'editable': False},
                         {'name': 'Rating', 'id': 'rating', 'editable': False}],
                data=get_top_series(),
            )
        ],
            style={'position': 'relative', 'top': 0, 'left': 0,
                   'width': '20%', 'height': '20%',
                   'display-style': 'flex', 'flexDirection': 'column'}),
        html.Div([
            "Number of movie releases after 2000",
            dash_table.DataTable(
                id="movie-releases",
                columns=[{'name': 'Year', 'id': 'release_year', 'editable': False},
                         {'name': 'Number of movies', 'id': 'n_movies', 'editable': False}],
                data=get_n_movie_releases(),
            )
        ],
            style={'position': 'absolute', 'top': 100, 'right': 10,
                   'width': '20%', 'height': '20%',
                   'display-style': 'flex', 'flexDirection': 'column'})

    ])
