from fastapi import FastAPI
import movies.Movies as mov

app = FastAPI()


@app.get("/movies")
def get_movies():
    results = []
    with open("movies/movies.csv", "r", encoding="utf-8") as file:
        for i in file:
            parts = i.strip().split(",")

            if len(parts) == 3:

                movie_object = mov.movie(parts[0], parts[1], parts[2])
                jason_movie = movie_object.__dict__
                results.append(jason_movie)
    return results


@app.get("/links")
def get_links():
    results = []
    with open("movies/links.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 3:

                link_obj = mov.links(parts[0], parts[1], parts[2])
                results.append(link_obj.__dict__)
    return results


@app.get("/ratings")
def get_ratings():
    results = []
    with open("movies/ratings.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                ratings_obj = mov.ratings(parts[0], parts[1], parts[2], parts[3])
                results.append(ratings_obj.__dict__)
    return results


@app.get("/tags")
def get_tags():
    results = []
    with open("movies/tags.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                tags_obj = mov.tags(parts[0], parts[1], parts[2], parts[3])
                results.append(tags_obj.__dict__)
    return results
