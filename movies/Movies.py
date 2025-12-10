class movie:
    def __init__(self, movieId: int, title: str, genre: str):
        self.movieId = movieId
        self.title = title
        self.genre = genre


class links:
    def __init__(self, movieId: int, imdbId: int, tmdbId: int):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class ratings:
    def __init__(self, userId: int, movieId: int, rating: float, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class tags:
    def __init__(self, userId: int, movieId: int, tag: list, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp
