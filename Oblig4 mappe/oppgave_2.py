import random

import blackjack_module as bjm

shuffledDeck = bjm.get_new_shuffled_deck()

dealer_hand = []
player_hand = []


def deal_card(hand):
    card = random.choice(shuffledDeck)
    hand.append(card)
    shuffledDeck.remove(card)


deal_card(player_hand)
deal_card(dealer_hand)
deal_card(player_hand)
deal_card(dealer_hand)

print(f"The cards have been dealt. Your cards are: {player_hand}, "
      f"with a total value of {bjm.calculate_hand_value(player_hand)}.\n"
      f"The dealers visible card is a {dealer_hand[0]}, "
      f"with a value of {bjm.get_card_value(dealer_hand[0])}.\n")


def check_bj(hand):
    hand_value = bjm.calculate_hand_value(hand)
    if hand_value == 21:
        print(f"Blackjack! Player won...")
        play_again()


def check_dealer(dealer_hand_value):
    if dealer_hand_value < 17:
        card = random.choice(shuffledDeck)
        dealer_hand.append(card)


def print_result(dealer_hand_value, player_hand_value):
    while True:
        print(f"Would you like to hit or stand?\n"
              f"1 - Hit\n"
              f"2 - Stand\n")
        player_choice = input()

        if player_choice == "2":

            if dealer_hand_value < 17:
                card = random.choice(shuffledDeck)
                dealer_hand.append(card)

            if dealer_hand_value > 21:
                print(f"\nDealer's cards: {dealer_hand}\n"
                      f"Dealer's hand value: {bjm.calculate_hand_value(dealer_hand)}\n"
                      f"Player's cards: {player_hand}\n"
                      f"Player's hand value: {bjm.calculate_hand_value(player_hand)}\n")
                print(f"Dealer Busted. Player won...\n")

            elif player_hand_value > dealer_hand_value:
                print(f"\nDealer's cards: {dealer_hand}\n"
                      f"Dealer's hand value: {bjm.calculate_hand_value(dealer_hand)}\n"
                      f"Player's cards: {player_hand}\n"
                      f"Player's hand value: {bjm.calculate_hand_value(player_hand)}\n")
                print(f"Player has highest cards. Player won...\n")

            elif dealer_hand_value > player_hand_value:
                print(f"\nDealer's cards: {dealer_hand}\n"
                      f"Dealer's hand value: {bjm.calculate_hand_value(dealer_hand)}\n"
                      f"Player's cards: {player_hand}\n"
                      f"Player's hand value: {bjm.calculate_hand_value(player_hand)}\n")
                print(f"Dealer has highest cards. Player lost...\n")

            elif player_hand_value == dealer_hand_value:
                print(f"\nDealer's cards: {dealer_hand}\n"
                      f"Dealer's hand value: {bjm.calculate_hand_value(dealer_hand)}\n"
                      f"Player's cards: {player_hand}\n"
                      f"Player's hand value: {bjm.calculate_hand_value(player_hand)}\n")
                print(f"Tied. Player's chips are returned...\n")
            break

        elif player_choice == "1":
            deal_card(player_hand)
            check_bj(player_hand)
            player_hand_value = bjm.calculate_hand_value(player_hand)
            if player_hand_value > 21:
                print(f"Dealer's cards: {dealer_hand}\n"
                      f"Dealer's hand value: {bjm.calculate_hand_value(dealer_hand)}\n"
                      f"Player's cards: {player_hand}\n"
                      f"Player's hand value: {bjm.calculate_hand_value(player_hand)}\n")
                print(f"Player Busted. Player lost...")
                break
            else:
                print(f"You have chosen hit and received another card.\n"
                      f"You now have these cards {player_hand} "
                      f"with a total value of {bjm.calculate_hand_value(player_hand)}.\n")
                continue
        else:
            print("Invalid, Please choose either Hit or Stand")
            continue


def play_again():
    print(f"Would you like to play again?\n"
          f"1 - Yes\n"
          f"2 - No\n")
    player_choice = input()

    if player_choice == "1":
        player_hand.clear()
        dealer_hand.clear()
        print("Restaring game...")

        deal_card(player_hand)
        deal_card(dealer_hand)
        deal_card(player_hand)
        deal_card(dealer_hand)
        print(f"The cards have been dealt. Your cards are: {player_hand}, "
              f"with a total value of {bjm.calculate_hand_value(player_hand)}.\n"
              f"The dealers visible card is a {dealer_hand[0]}, "
              f"with a value of {bjm.get_card_value(dealer_hand[0])}.\n")
        check_bj(player_hand)

        print_result(bjm.calculate_hand_value(dealer_hand), bjm.calculate_hand_value(player_hand))
        play_again()

    elif player_choice == "2":
        return


check_bj(player_hand)
print_result(bjm.calculate_hand_value(dealer_hand), bjm.calculate_hand_value(player_hand))
play_again()
