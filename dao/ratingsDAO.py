class RatingsDAO:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()
