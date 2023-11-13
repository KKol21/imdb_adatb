from dao.titlesDAO import TitlesDAO


class SeriesDAO(TitlesDAO):
    def __init__(self, db_conn):
        super().__init__(db_conn)

    def get_series(self):
        query = "SELECT t.*, s.n_seasons, s.n_episodes FROM titles t JOIN series s ON t.title_id = s.title_id"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_series(self, title, rating, genre, release_year, n_ratings, n_seasons, n_episodes):
        # Create or update the title entry
        self.create_title(title, rating, genre, release_year, n_ratings)
        title_id = self.get_title_id(title, release_year, rating)
        # Create or update the series entry
        query = "INSERT INTO series (title_id, n_seasons, n_episodes) VALUES (%s, %s, %s)"
        values = (title_id, n_seasons, n_episodes)
        self.cursor.execute(query, values)
        self.db_conn.commit()

    def update_series(self, title_id, n_seasons, n_episodes):
        query = "UPDATE series SET n_seasons = %s, n_episodes = %s WHERE title_id = %s"
        values = (n_seasons, n_episodes, title_id)
        self.cursor.execute(query, values)
        self.db_conn.commit()