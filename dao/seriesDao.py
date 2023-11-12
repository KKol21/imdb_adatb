class SeriesDAO:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def get_series(self):
        query = "SELECT * FROM series"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_series(self, n_seasons, n_episodes, title_id):
        query = "INSERT INTO series (n_seasons, n_episodes, title_id) VALUES (%s, %s, %s)"
        values = (n_seasons, n_episodes, title_id)
        self.cursor.execute(query, values)
        self.db_conn.commit()
