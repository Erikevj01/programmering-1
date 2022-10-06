import random
# Importerer random for å benytte random.randrange.

# Benytter random.randrange inni funksjonen for å få et tall mellom 0 og 100.
def print_random_number():
    print(f"*********\n***{random.randrange(1, 100)}***\n*********\n")

print("Random Numbers!\n")
print_random_number()
print_random_number()
print_random_number()

