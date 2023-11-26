from dash import html, dash_table

from colors import yellow, black
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


def get_most_famous_actor():
    cursor.execute("""SELECT name FROM actors WHERE actor_id =
                    (
                      SELECT f.actor_id
                      FROM featured f
                      JOIN movies m ON m.title_id = f.title_id
                      GROUP BY actor_id
                      ORDER BY COUNT(*) DESC
                      LIMIT 1)"""
                   )
    return cursor.fetchone()[0]


def get_series_from_most_famous_actor():
    cursor.execute("""SELECT t.title
                      FROM titles t
                      JOIN series s ON t.title_id = s.title_id
                      JOIN featured f ON f.title_id = s.title_id
                      WHERE f.actor_id = (
                          SELECT f.actor_id
                          FROM featured f
                          JOIN movies m ON m.title_id = f.title_id
                          GROUP BY actor_id
                          ORDER BY COUNT(*) DESC
                          LIMIT 1)
                        """)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    # Convert the result to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]
    return data


def get_top_movie_for_actors():
    cursor.execute("""
    SELECT
        a.name AS actor_name,
        t.title AS title,
        t.rating AS rating
    FROM
        actors a
    JOIN
        featured f ON a.actor_id = f.actor_id
    JOIN
        movies m ON f.title_id = m.title_id
    JOIN
        titles t ON m.title_id = t.title_id
    WHERE
        (f.actor_id, t.rating) IN (
            SELECT
                f.actor_id,
                MAX(t.rating) AS max_rating
            FROM
                featured f
            JOIN
                movies m ON f.title_id = m.title_id
            JOIN 
                titles t ON t.title_id = m.title_id
            GROUP BY
                f.actor_id
    )
                    """)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    # Convert the result to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]
    return data


def get_main_layout():
    return html.Div(
        children=[html.Div([
            html.Div([
                "Top series since 2019",
                dash_table.DataTable(
                    id="top-series",
                    columns=[{'name': 'Title', 'id': 'title', 'editable': False},
                             {'name': 'Release year', 'id': 'release_year', 'editable': False},
                             {'name': 'Rating', 'id': 'rating', 'editable': False}],
                    data=get_top_series(),
                    style_header={'backgroundColor': yellow,
                                  'fontWeight': 'bold',
                                  'border': f'2px solid {black}',
                                  'textAlign': 'center'},
                    style_cell={'border': f'2px solid {yellow}'},
                    style_data={'backgroundColor': black,
                                'color': 'white',
                                'textAlign': 'center'},
                )], className='dashboard'),
            html.Div([
                "Number of movie releases after 2000",
                dash_table.DataTable(
                    id="movie-releases",
                    columns=[{'name': 'Year', 'id': 'release_year', 'editable': False},
                             {'name': 'Number of movies', 'id': 'n_movies', 'editable': False}],
                    data=get_n_movie_releases(),
                    style_header={'backgroundColor': yellow,
                                  'fontWeight': 'bold',
                                  'border': f'2px solid {black}',
                                  'textAlign': 'center'},
                    style_cell={'border': f'2px solid {yellow}'},
                    style_data={'backgroundColor': black,
                                'color': 'white',
                                'textAlign': 'center'},
                )
            ], className='dashboard', style={'fontWeight': 'bold'}),
            html.Div([
                f"Series from the most famous actor: {get_most_famous_actor()}",
                dash_table.DataTable(
                    id="movie-releases",
                    columns=[{'name': 'Title', 'id': 'title', 'editable': False}],
                    data=get_series_from_most_famous_actor(),
                    style_header={'backgroundColor': yellow,
                                  'fontWeight': 'bold',
                                  'border': f'2px solid {black}',
                                  'textAlign': 'center'},
                    style_cell={'border': f'2px solid {yellow}'},
                    style_data={'backgroundColor': black,
                                'color': 'white',
                                'textAlign': 'center'},
                )
            ], className='dashboard', style={'fontWeight': 'bold'})
        ]),
            html.Div([
                "Top movies for each actor",
                dash_table.DataTable(
                    id="top-movies-for-actors",
                    columns=[{'name': 'Actor', 'id': 'actor_name', 'editable': False},
                             {'name': 'Title', 'id': 'title', 'editable': False},
                             {'name': 'Rating', 'id': 'rating', 'editable': False}],
                    data=get_top_movie_for_actors(),
                    style_header={'backgroundColor': yellow,
                                  'fontWeight': 'bold',
                                  'border': f'2px solid {black}',
                                  'textAlign': 'center'},
                    style_cell={'border': f'2px solid {yellow}'},
                    style_data={'backgroundColor': black,
                                'color': 'white',
                                'textAlign': 'center'},
                )], className='dashboard')
        ], style={"display": "flex", 'justify-content': 'space-evenly'})
