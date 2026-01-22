class Movie:
    def __init__(self, title: str, genre: str, duration: int, rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration      
        self.rating = rating          



movie1 = Movie("Inception", "action", 148, 8.8)


print("Kino nomi:", movie1.title)
print("Janri:", movie1.genre)
print("Davomiyligi:", movie1.duration, "daqiqa")
print("IMDB reytingi:", movie1.rating)
