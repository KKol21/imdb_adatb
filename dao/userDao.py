class UserDAO:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def get_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_user(self, username, password, name):
        query = "INSERT INTO users (username, password, name) VALUES (%s, %s, %s)"
        values = (username, password, name)
        self.cursor.execute(query, values)
        self.db_conn.commit()
