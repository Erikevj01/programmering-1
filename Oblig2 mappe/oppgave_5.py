import random

x = 1
number_of_players = int(input("Hvor mange spillere skal delta?: "))

# Definerer en input for hvor mange spillere som skall delta.

print("\nResultat:\n")
for throws in range(number_of_players):
    print(f"Spiller {x}:")
    score_range = random.sample(range(0, 61), 3)
    score_result = sum(score_range)
    print(f"{score_range} = {score_result}\n")
    x += 1

# Benytterfor løkke som lager en liste av scorer mellom 0 og 61 for alle de tre kastene.
# For løkken summerer da de tre kastene og gjør dette utifra hvor mange som deltar.