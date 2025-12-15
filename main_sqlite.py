import sqlite3
import csv

def create_connection(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            movieId INTEGER PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            genre TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS links(
            movieId INTEGER ,
            imdbId INTEGER NOT NULL,
            tmdbId INTEGER NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ratings(
            userId INTEGER NOT NULL,
            movieId INTEGER NOT NULL,
            rating REAL NOT NULL,
            timestamp INTEGER NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tags(
            userId INTEGER NOT NULL,
            movieId INTEGER NOT NULL,
            tag TEXT NOT NULL,
            timestamp INTEGER NOT NULL
        )
        """)


def load_data_from_csv(cursor, filename, table_name, columns_count):

    with open(filename, 'r', encoding='utf-8') as file:

        reader = csv.reader(file)
        next(reader) #pominiecie naglowka w celu unikniecia bledow
        placeholders = ', '.join(['?'] * columns_count)
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"

        try:
            cursor.executemany(query, reader)
            print(f"Załadowano dane do tabeli: {table_name} z pliku {filename}")
        except sqlite3.Error as e:
            print(f"Błąd przy ładowaniu {table_name}: {e}")
def main_setup():

    conn = sqlite3.connect("moviesBase.db")
    cursor = conn.cursor()

    # 1. Tworzenie tabel
    create_connection(cursor)

    # 2. Ładowanie danych
    # Kolejność argumentów: cursor, nazwa pliku, nazwa tabeli, liczba kolumn w CSV
    load_data_from_csv(cursor, 'movies/movies.csv', 'movies', 3)
    load_data_from_csv(cursor, 'movies/links.csv', 'links', 3)
    load_data_from_csv(cursor, 'movies/ratings.csv', 'ratings', 4)
    load_data_from_csv(cursor, 'movies/tags.csv', 'tags', 4)

    conn.commit()
    conn.close()
main_setup()