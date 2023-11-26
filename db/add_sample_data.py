import random
from dao import movieDAO, seriesDAO, actorDAO
from faker import Faker
from db.db_connector import conn


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
        "Infinite Illusion",
        "Quantum Echoes",
        "Midnight Serenade",
        "Nebula Odyssey",
        "Enigma's Embrace",
        "Whispering Shadows",
        "Ephemeral Eternity",
        "Chromatic Chronicles",
        "Labyrinth of Illusions",
        "Stellar Reverie",
        "Velvet Mirage",
        "Celestial Catalyst",
        "Solitude Symphony",
        "Sirens of Synchrony",
        "Aether Alchemy",
        "Echoes of Epochs",
        "Penumbral Paradox",
        "Serendipity Solstice",
        "Ethereal Escapade",
        "Kaleidoscope Dreams",
        "Paradigm Flux",
        "Phantasmal Odyssey",
        "Astral Ascendance",
        "Nebulous Nocturne",
        "Zephyr's Zephyros",
        "Luminescent Labyrinth",
        "Ethereal Enchantment",
        "Cynosure Chronicles",
        "Enigmatic Epoch",
        "Lucid Lullabies",
        "Quasar Quest",
        "Vortex Vignettes",
        "Cascade Constellations",
        "Juxtaposed Journeys",
        "Oracle of Oceans",
        "Velvet Vortex",
        "Enchanted Echo",
        "Celestial Cipher",
        "Quantum Quiescence",
        "Pondering Paradox",
        "Harmonic Hues",
        "Spectrum Sonata",
        "Kingdom's Whisper",
        "Parisian Echoes",
        "Gotham Grief",
        "Culinary Crossroads",
        "Street Symphony",
        "Chivalrous Betrayal",
        "Renaissance Rendezvous",
        "Café Noir Chronicles",
        "Steel Serenade",
        "Two Wheels Tango",
        "The Searing Forge",
        "Les Misérables Redux",
        "Shadows of Bourbon Street",
        "Noir Nostalgia",
        "Culinary Vendetta",
        "Gearhead's Lament",
        "Knights of the Round Tableau",
        "American Tragedy",
        "Boulangerie Brawl",
        "Thunder on Two Wheels",
        "Dynasty Discord",
        "Bastille Reckoning",
        "Vengeance on Vichy",
        "Gear Shift Confessions",
        "Medieval Melancholy",
        "Éclair Elegy",
        "Sons of Steel",
        "Culinary Conspiracies",
        "Road Rash Redemption",
        "Mafia Masquerade"
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
        "The Astral Almanac",
        "Midnight Mosaic",
        "Aegis of Arcadia",
        "Celestial Cipher",
        "Timeless Twilight",
        "Arcane Aria",
        "Velvet Vanguard",
        "Enigmatic Equinox",
        "Cosmic Caravan",
        "Ethereal Echoes"
    ]

    genres = ["Sci-Fi", "Fantasy", "Mystery", "Adventure", "Drama", "Thriller", "Romance"]

    entries = []

    # Generate creative entries for movies
    for i in range(len(movie_titles)):
        title = random.choice(movie_titles)
        movie_titles.remove(title)
        rating = round(random.uniform(3, 10), 2)
        if rating == int(rating):
            rating = int(rating)
        genre = random.choice(genres)
        release_year = random.randint(1980, 2023)
        n_ratings = random.randint(50, 2000)
        playtime = random.randint(90, 180)
        entries.append(
            {"title": title, "rating": rating, "genre": genre, "release_year": release_year, "n_ratings": n_ratings,
             "playtime": playtime})

    # Generate creative entries for series
    for i in range(len(series_titles)):
        title = random.choice(series_titles)
        series_titles.remove(title)
        rating = round(random.uniform(3, 10), 2)
        genre = random.choice(genres)
        release_year = random.randint(2010, 2023)
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


def fillDatabase():
    cursor = conn.cursor()

    do_titles = False
    do_actors = True
    do_features = True

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
