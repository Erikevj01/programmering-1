#Oppgave 1.2
numbers = []

for x in range(5):
    numbers.append(x)

print(numbers)

numbers = []

for x in range(5):
    numbers.insert(x, 0)

print(numbers)
print()

#Oppgave 1.3
class Course:
    def __init__(self, name, number_of_students, study_points=10):
        self.name = name
        self.number_of_students = number_of_students
        self.study_points = study_points

    def get_description(self):
        return f"The course {self.name} has {self.number_of_students} students" \
               f" and {self.study_points} study points."


programmering_1 = Course("Programmering 1", 215)

print(programmering_1.get_description())
print()

#Oppgave 1.4
animals_in_zoo = {"honey badger": 2, "ape": 15, "zebra": 6, "giraffe": 4}

for animal in animals_in_zoo:
    if animals_in_zoo[animal] < 5:
        print(animal.title())
print()

#Oppgave 1.5
numbers = [5, 2, 3, 2, 4, 1]

sum_of_numbers = 0
for number in numbers:
    if number <= 2:
        sum_of_numbers += number
    else:
        sum_of_numbers += 1

print(sum_of_numbers)
print()

#Oppgave 1.6
animals = ["honey badger", "giraffe", "ape", "zebra"]

animals[1] = "elephant"

animals.sort()

animals = animals[:2]

for animal in animals:
    print(animal)
print()

#Oppgave 1.7
animals = ["Elephant", "Dog", "Cat", "Gorilla", "Dodo"]

animals = animals[1:3]

animals[0] = "Alligator"

animals.sort(reverse=True)

print(animals)
print()

#Oppgave 1.8
shopping_list = {}


def add_item(item_name, quantity=1):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity


add_item("Bread", 2)
add_item("Milk")
add_item("Milk", 2)
add_item("Bread", 2)
add_item("Eggs")
print(shopping_list)
print()

#Oppgave 1.9
x = 0

for i in range(0, 5, 2):
    x += i

print(x)

x = 0

for i in range(0, 5):
    x += i

print(x)
print()

#Oppgave 1.10
a = 5
b = 2
c = 0

c += a ** b
print(c)

c += a % b
print(c)

c += a - b * 2
print(c)

c //= b
print(c)
print()

#Oppgave 1.11
class Game:
    def __init__(self, name, genre, age_rating=18):
        self.name = name
        self.genre = genre
        self.age_rating = age_rating

    def description(self):
        return f"The game {self.name} if of the genre {self.genre} and has an age rating of {self.age_rating}"

game1 = Game("Hades", "Rouge-lite", 12)
game2 = Game("God of War", "Action")
print(game1.age_rating)
print(game2.description())
print()

#Oppgave 1.12
randomList = [1, 'a', 2, 'b', 3]
result = 0
for entry in randomList:
    try:
        result += int(entry)
    except ValueError:
        print("A ValueError occurred.")

print(f"The sum is: {result}")