from db.db_connector import conn


class ActorDAO:
    def __init__(self):
        self.db_conn = conn
        self.cursor = conn.cursor()

    def delete_actors(self):
        self.cursor.execute("DELETE FROM actors")
        self.db_conn.commit()

    def get_actor_id(self, name, nat, date_of_birth):
        query = f"SELECT * FROM actors WHERE name = ? AND nationality = ? AND date_of_birth = ?"
        values = (name, nat, date_of_birth)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result[0]

    def get_actors(self):
        query = "SELECT * FROM actors"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        columns = [desc[0] for desc in self.cursor.description]

        # Convert the result to a list of dictionaries
        data = [dict(zip(columns, row)) for row in rows]
        return data

    def create_actor(self, name, nationality, date_of_birth):
        query = f"INSERT INTO actors (name, nationality, date_of_birth) VALUES (%s, %s, %s)"
        values = (name, nationality, date_of_birth)
        self.cursor.execute(query, values)
        self.db_conn.commit()

    def delete_actor(self, actor_id):
        query = f"DELETE FROM actors WHERE actor_id = {actor_id}"
        self.cursor.execute(query)
        self.db_conn.commit()
