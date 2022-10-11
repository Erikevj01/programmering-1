# Lager en input for brukeren som jeg konverterer fra string til float
number_1 = input("Type a number: ")
number_1 = float(number_1)

# Gjør det samme som jeg gjorde med det første tallet
number_2 = input("Type another number: ")
number_2 = float(number_2)

# Skriver ut tallene inn med følgende operatorer
print("Results")
print(f"Addition - {number_1 + number_2}")
print(f"Subtraction - {number_1 - number_2}")
print(f"Multiply - {number_1 * number_2}")
print(f"Division - {number_1 / number_2}")
print(f"Modulus - {number_1 % number_2}")
print(f"Exponentiation - {number_1 ** number_2}")
print(f"Floor division - {number_1 // number_2}")