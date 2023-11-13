import random
from dao import movieDao, seriesDao
from db.db_connector import db_conn


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
        n_ratings = random.randint(50, 500)
        playtime = random.randint(90, 180)
        entries.append(
            {"title": title, "rating": rating, "genre": genre, "release_year": release_year, "n_ratings": n_ratings,
             "playtime": playtime})

    # Generate creative entries for series
    for i in range(20):
        title = random.choice(series_titles)
        series_titles.remove(title)
        rating = round(random.uniform(3, 5), 2)
        genre = random.choice(genres)
        release_year = random.randint(1990, 2023)
        n_ratings = random.randint(50, 500)
        n_seasons = random.randint(1, 8)
        n_episodes = random.randint(10, 20)
        entries.append(
            {"title": title, "rating": rating, "genre": genre, "release_year": release_year, "n_ratings": n_ratings,
             "n_seasons": n_seasons, "n_episodes": n_episodes})

    return entries


# Assuming you have an instance of your class called imdb_instance
movieDao = movieDao.MoviesDAO(db_conn=db_conn)
seriesDao = seriesDao.SeriesDAO(db_conn=db_conn)


# Generate and insert creative movie and series entries
def fillDatabase():
    creative_entries = generate_creative_entries()
    for data in creative_entries:
        if "playtime" in data:
            movieDao.create_movie(**data)
        elif "n_seasons" in data and "n_episodes" in data:
            seriesDao.create_series(**data)
