student = {
    "first name": "Ola",
    "last name": "Nordmann",
    "favorite course": "Programmering 1"
}
#1. Printer ut begge dictionary keyene.
print("1.")
print(f"Fornavn: {student['first name']}")
print(f"Etternavn: {student['last name']}\n")

#2. Oppdaterer dictionary keyen ved å endre valuen.
student["favorite course"] = "ITF10219 Programmering 1"
print("2.")
print(f"Studentens favorittkurs: {student['favorite course']}\n")


#3. Legger til en ny key med en value inn i dictionarien.
student["age"] = "25"
print("3.")
print(f"Alder: {student['age']}")