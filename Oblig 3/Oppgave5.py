
print("5.1")
# Lager en liste med dictionaries med filmene oppgitt
movies = [{"name": "Inception", "year": 2010, "rating": 8.7},
        {"name": "Inside Out", "year": 2015, "rating": 8.1},
        {"name": "Con Air", "year": 1997, "rating": 6.9}]

# Lager en funksjon som legger til filmnavn, år og rating som 5.0 default.
def addMovie(log, name, year, rating=5.0):
    log.append({"name": name, "year": year, "rating": rating})
addMovie(movies, "The Lord of the Rings: The Return of the King", 2003, 8.9)
addMovie(movies, "American Psycho", 2000, 7.6)
addMovie(movies, "Spirited Away", 2001, 8.5)
addMovie(movies, "Cats", 2019)
print(movies)

print("\n5.2")
def print_movie(movies):
    for log in movies:
        print(f"{log['name']} - {log['year']} has a rating of {log['rating']}")

print_movie(movies)

print("\n5.3")