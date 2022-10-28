class Movies:
    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score

    def __str__(self):
        return (f"{self.name} was released in {self.year} and currently has a score of {self.score}"
                f"{self.name} was released in {self.year} and currently has a score of {self.score}"
                f"{self.name} was released in {self.year} and currently has a score of {self.score}")


movie_1 = Movies("Inception", 2010, 8.8)
movie_2 = Movies("The Martian", 2015, 8.0)
movie_3 = Movies("Joker", 2019, 8.4)

print("A) Filmer printet ut med format:")
print(f"{movie_1.name} was released in {movie_1.year} and currently has a score of {movie_1.score}")
print(f"{movie_2.name} was released in {movie_2.year} and currently has a score of {movie_2.score}")
print(f"{movie_3.name} was released in {movie_3.year} and currently has a score of {movie_3.score}")

print("\nB) Filmer printet ut med metode fra klasse:")
print(movie_1)
print(movie_2)
print(movie_3)