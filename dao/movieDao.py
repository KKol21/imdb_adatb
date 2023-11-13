from dao.titlesDao import TitlesDAO


class MoviesDAO(TitlesDAO):
    def __init__(self, db_conn):
        super().__init__(db_conn)

    def get_movie_details(self, title, release_year, rating):
        title_id = self.get_title_id(title, release_year, rating)
        # Retrieve all attributes of a given movie
        query = "SELECT t.*, m.playtime FROM titles t JOIN movies m ON t.title_id = m.title_id WHERE t.title_id = %s"
        values = (title_id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def get_movies(self):
        query = "SELECT t.*, m.playtime FROM titles t JOIN movies m ON t.title_id = m.title_id"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_movie(self, title, rating, genre, release_year, n_ratings, playtime):
        # Create or update the title entry
        self.create_title(title, rating, genre, release_year, n_ratings)

        title_id = self.get_title_id(title, release_year, rating)

        # Create or update the movie entry
        query = "INSERT INTO movies (title_id, playtime) VALUES (%s, %s) ON DUPLICATE KEY UPDATE playtime = %s"
        values = (title_id, playtime, playtime)
        self.cursor.execute(query, values)
        self.db_conn.commit()

    def update_movie(self, title, rating, genre, release_year, n_ratings, playtime):
        # Update the title entry
        title_id = self.get_title_id(title, release_year, rating)
        self.update_title(title_id, rating, genre, release_year, n_ratings)
        # Update the movie entry
        query = "UPDATE movies SET playtime = %s WHERE title_id = %s"
        values = (playtime, title_id)
        self.cursor.execute(query, values)
        self.db_conn.commit()
