planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_gravity = [3.7, 8.87, 9.803, 3.721, 24.79, 19.44, 8.87, 11.15]

your_weight = input("Specify your weight on Earth: ")
your_weight = float(your_weight)

if your_weight <= 0:
    print("Weight must be a positive number.")
    exit()

print("\n====Planets====")
print(f"1- {planets[0]}")
print(f"2 - {planets[0]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")

planet_number = input("\nPlease specify which planet you want to convert your weight to: ")
planet_number = int(planet_number)

if planet_number < 1 or planet_number> 8:
    print("Please specify one of the eight planets listed above")
    exit()

planet_index = planet_number-1

planet_weight = your_weight / planets_gravity[2] * planets_gravity[planet_index]

print(f"Your weight is {planet_weight}")