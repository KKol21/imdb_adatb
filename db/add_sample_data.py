import random
from dao import movieDAO, seriesDAO, actorDAO
from faker import Faker
from db.db_connector import conn


# Assuming you have a class with the methods create_title, create_series, create_movie

# Function to generate creative entries for movies and series
def generate_creative_entries():
    movie_titles = [
        "The Quantum Paradox",
        "Eternal Moonlight",
        "Cipher of Dreams",
        "Starlight Serenade",
        "Chronicles of Nebula",
        "Whispers in the Wind",
        "Enigma of Eternity",
        "Midnight Mirage",
        "Surreal Symphony",
        "Galactic Odyssey",
        "Echoes of Tomorrow",
        "Mystic Masquerade",
        "Celestial Serendipity",
        "The Velvet Eclipse",
        "Voyage of the Cosmic Muse",
        "Crimson Nebula",
        "Spectral Sonata",
        "Stellar Enchantment",
        "Oracle's Overture",
        "Infinite Illusion"
    ]

    series_titles = [
        "Realm of Shadows",
        "Twilight Nexus",
        "Secrets of Atlantis",
        "Aetherial Chronicles",
        "Chrono Paradox",
        "Lunar Labyrinth",
        "Quantum Quest",
        "Serenity Spectrum",
        "Epic Epoch",
        "Galactic Genesis",
        "Cosmic Conundrum",
        "Nebula Nexus",
        "Astro Arcana",
        "Mystic Metropolis",
        "Stellar Symphony",
        "Ethereal Enigma",
        "Infinity Incognito",
        "Celestial Cipher",
        "Dreamscape Dynasty",
        "The Astral Almanac"
    ]

    genres = ["Sci-Fi", "Fantasy", "Mystery", "Adventure", "Drama", "Thriller", "Romance"]

    entries = []

    # Generate creative entries for movies
    for i in range(20):
        title = random.choice(movie_titles)
        movie_titles.remove(title)
        rating = round(random.uniform(3, 5), 2)
        genre = random.choice(genres)
        release_year = random.randint(1980, 2023)
        n_ratings = random.randint(50, 2000)
        playtime = random.randint(90, 180)
        entries.append(
            {"title": title, "rating": rating, "genre": genre, "release_year": release_year, "n_ratings": n_ratings,
             "playtime": playtime})

    # Generate creative entries for series
    for i in range(20):
        title = random.choice(series_titles)
        series_titles.remove(title)
        rating = round(random.uniform(3, 10), 2)
        genre = random.choice(genres)
        release_year = random.randint(1990, 2023)
        n_ratings = random.randint(50, 500)
        n_seasons = random.randint(1, 8)
        n_episodes = random.randint(10, 20)
        entries.append(
            {"title": title, "rating": rating, "genre": genre, "release_year": release_year, "n_ratings": n_ratings,
             "n_seasons": n_seasons, "n_episodes": n_episodes})

    return entries


def generate_actor_data():
    entries = []
    for _ in range(200):
        fake = Faker()
        nationalities = ['Martian', 'Atlantean', 'Time Traveler', 'Candy Kingdom', 'Middle-earth']
        name = fake.name()
        nationality = random.choice(nationalities)
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
        entries.append({"name": name, "nationality": nationality, "date_of_birth": date_of_birth})
    return entries


def generate_feature_data():
    cursor = conn.cursor()
    cursor.execute('SELECT actor_id FROM actors')
    actor_ids = cursor.fetchall()
    cursor.execute('SELECT title_id FROM movies')
    movie_ids = cursor.fetchall()
    cursor.execute('SELECT title_id FROM titles')
    title_ids = cursor.fetchall()

    most_movie_actor_id = actor_ids[0]
    featured = []
    for _ in range(10):
        row = (most_movie_actor_id[0], random.choice(movie_ids)[0])
        movie_ids.remove((row[1],))
        if row not in featured:
            featured.append(row)

    for actor_id in actor_ids:
        for _ in range(3):
            row = (actor_id[0], random.choice(title_ids)[0])
            if row not in featured:
                featured.append(row)
    """for title_id in title_ids:
        for _ in range(3):
            row = (random.choice(actor_ids)[0], title_id[0])
            if row not in featured:
                featured.append(row)"""
    return featured


movieDAO = movieDAO.MoviesDAO()
seriesDAO = seriesDAO.SeriesDAO()
actorDAO = actorDAO.ActorDAO()


# Generate and insert creative movie and series entries
def fillDatabase():
    cursor = conn.cursor()

    do_titles = False
    do_actors = False
    do_features = False

    if do_titles:
        cursor.execute("DELETE FROM titles")
        conn.commit()
        creative_entries = generate_creative_entries()
        for data in creative_entries:
            if "playtime" in data:
                movieDAO.create_movie(**data)
            elif "n_seasons" in data and "n_episodes" in data:
                seriesDAO.create_series(**data)
    if do_actors:
        actorDAO.delete_actors()
        for actor in generate_actor_data():
            actorDAO.create_actor(**actor)
    if do_features:
        cursor.execute("DELETE FROM featured")
        conn.commit()
        for feature in generate_feature_data():
            query = "INSERT INTO featured (actor_id, title_id) VALUES (%s, %s)"
            cursor.execute(query, feature)
            conn.commit()
