# Weight on the moon = weight on earth / earths gravity * moons gravity

# input()
earth_weight = input("Specify weight on earth: ")
earth_weight = float(earth_weight)

earth_gravity = 9.807
moon_gravity = 1.622

moon_weight = earth_weight / earth_gravity * moon_gravity

print(f"Weight on the moon is {moon_weight} kg")
