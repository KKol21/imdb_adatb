from dao.titlesDAO import TitlesDAO


class SeriesDAO(TitlesDAO):
    def __init__(self):
        super().__init__()

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

    def update_series(self, title_id, new_data: dict):
        self.update_title(title_id, new_data)
        n_s = new_data["n_seasons"]
        n_ep = new_data["n_episodes"]
        val_str = None
        if n_s and n_ep:
            val_str = f"n_seasons = {n_s}, n_episodes = {n_ep}"
        elif n_s:
            val_str = f"n_seasons = {n_s}"
        elif n_ep:
            val_str = f"n_episodes = {n_ep}"
        if val_str is not None:
            query = f"UPDATE series SET" + val_str + f"WHERE title_id = {title_id}"
            self.cursor.execute(query)
            self.db_conn.commit()

    def delete_series(self, title_id):
        self.cursor.execute(f"DELETE FROM SERIES WHERE title_id = {title_id}")
