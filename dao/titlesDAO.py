from db.db_connector import conn


class TitlesDAO:
    def __init__(self):
        self.db_conn = conn
        self.cursor = conn.cursor()

    def get_title_type_by_id(self, title_id):
        title_data = self.get_title_by_id_full(title_id)
        return "movie" if len(title_data) == 7 else "series"

    def get_title_details(self, title, rating, release_year):
        title_id = self.get_title_id(title, release_year, rating)
        return self.get_title_by_id_full(title_id)

    def get_title_id(self, title, release_year, rating):
        query = "SELECT title_id FROM titles WHERE title LIKE %s AND release_year = %s AND rating LIKE %s"
        values = (title, release_year, rating)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result[0]

    def get_title_by_id(self, title_id):
        query = "SELECT * FROM titles WHERE title_id = %s"
        self.cursor.execute(query, (title_id,))
        return self.cursor.fetchone[0]

    def get_title_by_id_full(self, title_id):
        query = f"""
            SELECT
                titles.*,
                CASE
                    WHEN movies.title_id IS NOT NULL THEN movies.playtime
                    WHEN series.title_id IS NOT NULL THEN series.n_seasons 
                END AS additional_col,
                CASE 
                    WHEN series.title_id IS NOT NULL THEN series.n_episodes
                END AS n_episodes
            FROM
                titles
            LEFT JOIN
                movies ON titles.title_id = movies.title_id
            LEFT JOIN
                series ON titles.title_id = series.title_id
            WHERE
                titles.title_id = %s
                """
        self.cursor.execute(query, (title_id,))
        result = self.cursor.fetchone()
        return [val for val in result if val is not None]

    def get_titles(self):
        query = "SELECT * FROM titles"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_title(self, title, rating, genre, release_year, n_ratings):
        query = """INSERT INTO titles (title, rating, genre, release_year, n_ratings)
                VALUES (%s, %s, %s, %s, %s)"""
        values = (title, rating, genre, release_year, n_ratings)
        self.cursor.execute(query, values)
        self.db_conn.commit()

    def update_title(self, title_id, new_data: dict):
        query = "UPDATE titles SET "
        for field, value in new_data.items():
            if value is not None:  # Only include non-None values
                if isinstance(value, str):
                    query += f"{field} = '{value}', "
                else:
                    query += f"{field} = {value}, "
        query = query.rstrip(", ")

        query += f" WHERE title_id = {title_id}"
        self.cursor.execute(query)
        self.db_conn.commit()
