import random

#print(random.randrange(1, 101))

guess = random.randrange(1, 101)

while guess != 69:
    print(f"The guess was: {guess}")
    guess = random.randrange(1, 101)

print("The guess was correct. The number is 69")
