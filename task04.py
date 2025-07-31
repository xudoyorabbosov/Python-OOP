class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

m = Movie("Inception", "fantastika", 148, 8.8)
print(m.title, m.genre, m.duration, m.rating)
