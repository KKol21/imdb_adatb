from dao.titlesDAO import TitlesDAO


class MoviesDAO(TitlesDAO):
    def __init__(self, db_conn):
        super().__init__(db_conn)

    def get_movie_ids(self):
        query = "SELECT title_id FROM movies"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_movies(self):
        query = "SELECT t.*, m.playtime FROM titles t JOIN movies m ON t.title_id = m.title_id"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_movie(self, title, rating, genre, release_year, n_ratings, playtime):
        # Create or update the title entry
        self.create_title(title, rating, genre, release_year, n_ratings)
        title_id = self.get_title_id(title, release_year, rating)

        # Create or update the movie entry
        query = "INSERT INTO movies (title_id, playtime) VALUES (%s, %s)"
        values = (title_id, playtime)
        self.cursor.execute(query, values)
        self.db_conn.commit()

    def update_movie(self, title_id, new_data):
        self.update_title(title_id, new_data)
        if new_data["playtime"] is not None:
            query = f"UPDATE movies SET playtime = {new_data['playtime']} WHERE title_id = {title_id}"
            self.cursor.execute(query)
            self.db_conn.commit()

    def delete_movie(self, title_id):
        self.cursor.execute(f"DELETE FROM movies WHERE title_id = {title_id}")
