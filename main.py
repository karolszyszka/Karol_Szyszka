import sqlite3
con = sqlite3.connect('test.db')
cursor =con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    movieId INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS links(
    movieId INTEGER PRIMARY KEY AUTOINCREMENT,
    imdbId INTEGER NOT NULL,
    tmdbId INTEGER NOT NULL,
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings(
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    movieId INTEGER NOT NULL,
    rating TEXT NOT NULL,
    timestamp INTEGER NOT NULL,
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tags(
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    movieId INTEGER NOT NULL,
    tag TEXT NOT NULL,
    timestamp INTEGER NOT NULL,
)
""")