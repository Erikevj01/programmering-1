# Lager en funksjon med lengde, bredde og høyde som bruker formelen.
def volume(lenght, width, height):
    print(f"\nVolum: lengde * bredde * høyde")
    print(f"{lenght} * {width} * {height} = {lenght * width * height}")

# Tar in input for lengde, bredde og høyde.
print("Tast inn lengde: ")
x = int(input())

print("Tast inn bredde: ")
y = int(input())

print("Tast inn høyde: ")
z = int(input())

# Kjører funksjonen
volume(x, y, z)

