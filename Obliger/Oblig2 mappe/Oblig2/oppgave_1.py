# Bruker en while løkke for å sjekke om svaret som tastes inn er 42.
while True:
    guess = int(input("Hva er meningen med livet? Hint: Det er et tall.\nTast inn her: "))

    if guess == 42:
        print("Det stemmer, meningen med livet er 42!")
        break
    elif 30 < guess < 50:
        print("Nærme, men feil.")
    else:
        print("FEIL!")

# Bruker if, elif, else for å definere de ulike betingelsene som er beskrevet i oppgaven.

print("Takk for at du gjettet.")