from mysql.connector import connect


def create_connection():
    connection = connect(
        user="root"
    )
    return connection


def create_database(connection, database_name):
    cursor = connection.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cursor.execute(f"CREATE DATABASE {database_name}")
    print(f"Database '{database_name}' created successfully.")


def create_tables(connection):
    cursor = connection.cursor()

    # Create Users table
    create_users_table = """
    CREATE TABLE IF NOT EXISTS Users (
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL
    );
    """
    cursor.execute(create_users_table)

    # Create Titles table
    create_titles_table = """
        CREATE TABLE IF NOT EXISTS Titles (
            title_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            rating FLOAT,
            n_ratings INT,
            release_year INT,
            genre VARCHAR(255)
        );
        """
    cursor.execute(create_titles_table)

    # Create Movies table
    create_movies_table = """
    CREATE TABLE IF NOT EXISTS Movies (
        title_id INT PRIMARY KEY,
        playtime INT,
        FOREIGN KEY (title_id) REFERENCES Titles(title_id) ON DELETE CASCADE
    );
    """
    cursor.execute(create_movies_table)

    # Create Series table
    create_series_table = """
    CREATE TABLE IF NOT EXISTS Series (
        title_id INT PRIMARY KEY,
        n_seasons INT,
        n_episodes INT,
        FOREIGN KEY (title_id) REFERENCES Titles(title_id) ON DELETE CASCADE
    );
    """
    cursor.execute(create_series_table)

    # Create Ratings table
    create_ratings_table = """
    CREATE TABLE IF NOT EXISTS Ratings (
        username VARCHAR(255),
        title_id INT,
        rating FLOAT,
        FOREIGN KEY (username) REFERENCES Users(username),
        FOREIGN KEY (title_id) REFERENCES Titles(title_id),
        PRIMARY KEY (username, title_id)
    );
    """
    cursor.execute(create_ratings_table)

    # Create Actors table
    create_actors_table = """
    CREATE TABLE IF NOT EXISTS Actors (
        actor_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        date_of_birth DATE,
        nationality VARCHAR(255)
    );
    """
    cursor.execute(create_actors_table)

    # Create Featured table
    create_featured_table = """
    CREATE TABLE IF NOT EXISTS Featured (
        title_id INT,
        actor_id INT,
        FOREIGN KEY (title_id) REFERENCES Titles (title_id) ON DELETE CASCADE,
        FOREIGN KEY (actor_id) REFERENCES Actors (actor_id) ON DELETE CASCADE,
        PRIMARY KEY (title_id, actor_id)
    );
    """
    cursor.execute(create_featured_table)

    print("Tables created successfully.")


def create_db_with_tables():

    # Create a connection to the MySQL server
    connection = create_connection()

    if connection:
        # Create the database if it doesn't exist
        create_database(connection, "imdb")

        # Connect to the 'imdb' database
        connection = connect(
            user="root",
            host="localhost",
            database="imdb"
        )

        if connection:
            # Create tables
            create_tables(connection)

            # Close the connection
            connection.close()
    else:
        print("Unable to establish a connection to the MySQL server.")
