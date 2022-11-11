packing_list = []
command = ['legg til', 'slett', 'skriv ut']

print("Pakkeliste kommandoer:")
print(f"{command[0]}")
print(f"{command[1]}")
print(f"{command[2]}")
# Oppretter pakke liste og lager en liste over mulige kommandoer.

while True:
    input_command = str(input("\nHvilken kommando vil du benytte?\n"))
# Benytter en while løkke for at man skal kunne legge til
# og slette gjenstander fra pakkelista så mange ganger man vil

    if input_command == command[0]:
        lt = str(input("\nHva vil du legge til?\n"))
        packing_list.append(lt)
        print(f"{lt} ble lagt til")
        print("\nPakkeliste:")
        for list_item in packing_list:
            print(f"{list_item}")
        continue
# Definerer if for å legge til gjenstander på pakkelista.
# Tar input for hva som skal legges til og legger det til lista.
# Hviser da hva som er på lista og fortsetter koden.

    elif input_command == command[1]:
        print(packing_list)
        sl = str(input("\nHva vil du slette?\n"))
        packing_list.remove(sl)
        print(f"{sl} ble slettet")
        print("\nPakkeliste:")
        for list_item in packing_list:
            print(f"{list_item}")
        continue
# Definerer elif for å slette gjenstander fra pakkelista.
# Den er nesten helt lik legg til kommandoen men remover
# isteden for å appende den oppgitte gjennstanden fra pakkelista.

    elif input_command == command[2]:
        print("\nUtskrift av pakkeliste:")
        for list_item in packing_list:
            print(f"{list_item}")
        break
# Definerer elif for å skrive ut pakkelista.
# Printer da ut alle verdier på pakkelista og avslutter koden.

    else:
        print("Vennligst velg en av kommandonene 'legg til', 'slett' eller 'skriv ut'")
        continue

# Definerer else for når en ugyldig kommando benyttes. Fortsetter koden.