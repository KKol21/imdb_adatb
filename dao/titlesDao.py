class TitlesDAO:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def get_title_id(self, title, release_year, rating):
        query = "SELECT title_id FROM titles WHERE title LIKE %s AND release_year = %s AND rating LIKE %s"
        values = (title, release_year, rating)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result[0]

    def get_titles(self):
        query = "SELECT * FROM titles"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_title(self, title, rating, genre, release_year, n_ratings):
        query = "INSERT INTO titles (title, rating, genre, release_year, n_ratings) VALUES (%s, %s, %s, %s, %s)"
        values = (title, rating, genre, release_year, n_ratings)
        self.cursor.execute(query, values)
        self.db_conn.commit()

    def update_title(self, title_id, rating, genre, release_year, n_ratings):
        query = "UPDATE titles SET rating = %s, genre = %s, release_year = %s, n_ratings = %s WHERE title_id = %s"
        values = (rating, genre, release_year, n_ratings, title_id)
        self.cursor.execute(query, values)
        self.db_conn.commit()
