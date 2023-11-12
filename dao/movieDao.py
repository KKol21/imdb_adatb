class MovieDAO:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def get_movies(self):
        query = "SELECT * FROM movies"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_movie(self, playtime, release_year, title_id):
        query = "INSERT INTO movies (playtime, release_year, title_id) VALUES (%s, %s, %s)"
        values = (playtime, release_year, title_id)
        self.cursor.execute(query, values)
        self.db_conn.commit()