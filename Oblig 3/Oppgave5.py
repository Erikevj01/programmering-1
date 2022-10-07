
print("5.1 A-C")
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

print("\n5.2 A)")
# Definerer en funksjon som printer ut alle dictionaries i listen ved gitt filmutskrifts format.
def printMovie(movies):
    for log in movies:
        print(f"{log['name']} - {log['year']} has a rating of {log['rating']}")
printMovie(movies)

print("\n5.2 B)")
# Definerer en funksjon som tar summen av alle ratings på filmene i gitt liste,
# og deler på antall distionaries i listen.
def averageRating(movies):
    print(f"Gjennomsnittsrating: Sum av alle ratings / antall filmer i listen = "
          f"{float(sum(rating['rating'] for rating in movies)) / len(movies)}")
# Tester med filmliste tildligere brukt.
averageRating(movies)

print("\n5.2 C)")
# Definerer funksjon som legger til kun filmer fra 2010 og etter til en blank liste.
def moviesAfterYear(movies, year):
    blank_list = []
    for log in movies:
        if log["year"] >= year:
            blank_list.append(log)
    return blank_list
# Bruker printMovie fra tidligere for å kjøre funksjonen og få ut all info om hver film
printMovie(moviesAfterYear(movies, 2010))

print("\n5.3 A)")
print("Sjekk docs/movies.txt")
# Definerer en funksjon med movies og file som parameter
# Benytter "with open" til å skrive inn dictionaries fra lista inn på .txt filen
def addToFile(movies, file):
    file_list = []
    with open(file, 'w') as file:
        for log in movies:
            file.write(f"{log['name']} - {log['year']} has a rating of {log['rating']}\n")

addToFile(movies, "docs/movies.txt")

print("\n5.3 B)")
# Definerer en funksjon med movies og file som parameter
#
def readFile(file):
    file_list = []
    with open(file, 'r') as file:
        for log in file:
            movie = log
            file_list.append(movie)
    for info in file_list:
        print(info)

readFile("docs/movies.txt")