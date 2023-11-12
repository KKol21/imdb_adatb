class TitlesDAO:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def get_titles(self):
        query = "SELECT * FROM titles"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_title(self, title, rating, genre):
        query = "INSERT INTO titles (title, rating, genre) VALUES (%s, %s, %s)"
        values = (title, rating, genre)
        self.cursor.execute(query, values)
        self.db_conn.commit()