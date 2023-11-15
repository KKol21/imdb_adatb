from mysql import connector

conn = connector.connect(user="root", database="imdb", connect_timeout=10000)
