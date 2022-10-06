
print("5.1")
# Lager en liste med dictionaries med filmene oppgitt.
movies = [{"name": "Inception", "year": 2010, "rating": 8.7},
        {"name": "Inside Out", "year": 2015, "rating": 8.1},
        {"name": "Con Air", "year": 1997, "rating": 6.9}]

# Lager en funksjon som legger til filmnavn, år og rating som 5.0 default.
def addMovie(log, name, year, rating=5.0):
    log.append({"name": name, "year": year, "rating": rating})
# Legger til 3 filmer med og en uten rating med funksjonen.
addMovie(movies, "The Lord of the Rings: The Return of the King", 2003, 8.9)
addMovie(movies, "American Psycho", 2000, 7.6)
addMovie(movies, "Spirited Away", 2001, 8.5)
addMovie(movies, "Cats", 2019)
print(movies)

print("\n5.2")
# Definerer en funksjon som printer ut alle dictionaries i listen ved gitt filmutskrift.
def print_movie(movies):
    for log in movies:
        print(f"{log['name']} - {log['year']} has a rating of {log['rating']}")

print_movie(movies)
print()

# Definerer en funksjon som tar summen av alle ratings på filmene i gitt liste,
# og deler på antall distionaries i listen.
def average_rating(log):
    print(f"Gjennomsnittsrating: Sum av alle ratings / antall filmer i listen = "
          f"{float(sum(rating['rating'] for rating in log)) / len(log)}")
# Tester med filmliste tildligere brukt.
average_rating(movies)


print("\n5.3")