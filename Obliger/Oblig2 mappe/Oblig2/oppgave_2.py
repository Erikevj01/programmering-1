print("Alle oddetall fra og med 9 til 101. (For loop)")
for number in range(9, 102):
    if (number % 2) == 0:
        continue
    else:
        print(number)

# Her benytter jeg en for løkke og en if-test for å sjekke om tallene fra og med 9 til 101 er oddetall.

print("\nAlle oddetall fra og med 9 til 101. (While loop)")
number = 9
while number <= 101:
    print(number)
    number += 2

# Her benytter jeg en while løkke og printer annenhvert tall fra og med 9 til 101.
