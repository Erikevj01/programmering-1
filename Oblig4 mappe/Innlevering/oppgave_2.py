import random

full_deck = {"Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
             "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
             "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
             "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
             "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
             "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
             "Ace of diamonds": 11,
             "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
             "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
             "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
             "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
             "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
             "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
             }


def get_new_shuffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


shuffledDeck = get_new_shuffled_deck()


def deal(deck):
    hand = []
    for i in range(2):
        card = shuffledDeck.pop()
        hand.append(card)
    return hand


def card_value(card):
    card_value = 0
    if card == "Ace of clubs" or "Ace of diamonds" or "Ace of hearts" or "Ace of spades":
        if card_value >= 11:
            card_value += 1
        else:
            card_value += 11
    else:
        card == full_deck[card]
    return full_deck[card]


def hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += card_value(card)
    return hand_value


def hit(hand):
    card = random.choice(shuffledDeck)
    hand.append(card)
    shuffledDeck.remove(card)
    return hand


def print_dealer_results(hand):
    print(f"Dealer's cards: {hand}\n"
          f"Dealer's hand value: {hand_value(hand)}\n")


def print_player_results(hand):
    print(f"Player's cards: {hand}\n"
          f"Player's hand value: {hand_value(hand)}\n")


def play_again():
    while True:
        player_choice = input("Would you like to play again?\n"
                              "1 - Yes\n"
                              "2 - No\n").lower()
        if player_choice == "1":
            dealer_hand = []
            player_hand = []
            game()
        elif player_choice == "2":
            print("Quitting game..")
            exit()
        else:
            print("Invalid, Please choose either Hit or Stand")
            continue


def check(dealer_hand, player_hand):
    if hand_value(player_hand) == 21:
        print_dealer_results(dealer_hand)
        print_player_results(player_hand)
        print("Blackjack! Player won...\n")

    elif hand_value(dealer_hand) == 21:
        print_dealer_results(dealer_hand)
        print_player_results(player_hand)
        print("Dealer got a Blackjack. Player lost...\n")

    elif hand_value(player_hand) > 21:
        print_player_results(player_hand)
        print("Player Busted. Player lost...\n")

    elif hand_value(dealer_hand) > 21:
        print_dealer_results(dealer_hand)
        print_player_results(player_hand)
        print("Dealer Busted. Player won...\n")

    elif hand_value(player_hand) < hand_value(dealer_hand):
        print_dealer_results(dealer_hand)
        print_player_results(player_hand)
        print("Dealer has a higher score. Player lost...\n")

    elif hand_value(player_hand) > hand_value(dealer_hand):
        print_dealer_results(dealer_hand)
        print_player_results(player_hand)
        print("Player has a higher score. Player won...\n")


def blackjack(dealer_hand, player_hand):
    if hand_value(player_hand) == 21:
        print_player_results(player_hand)
        print("Blackjack! Player won...\n")
        play_again()
    elif hand_value(dealer_hand) == 21:
        print_dealer_results(dealer_hand)
        print_player_results(player_hand)
        print("Dealer got a Blackjack. Player lost...\n")
        play_again()


def game():
    player_choice = 0
    dealer_hand = deal(shuffledDeck)
    player_hand = deal(shuffledDeck)
    print(f"The cards have been dealt. Your cards are: {player_hand}, "
          f"with a total value of {hand_value(player_hand)}.\n"
          f"The dealers visible card is a {dealer_hand[0]}, "
          f"with a value of {card_value(dealer_hand[0])}.\n")
    while player_choice != "3":
        blackjack(dealer_hand, player_hand)
        player_choice = input(f"Would you like to do?\n"
                              f"1 - Hit\n"
                              f"2 - Stand\n"
                              f"3 - Stop playing\n").lower()
        if player_choice == "1":
            hit(player_hand)
            while hand_value(dealer_hand) < 17:
                hit(dealer_hand)
            check(dealer_hand, player_hand)
            play_again()
        elif player_choice == "2":
            while hand_value(dealer_hand) < 17:
                hit(dealer_hand)
            check(dealer_hand, player_hand)
            play_again()
        elif player_choice == "3":
            print("put chip stuff here")
            print("Stopping game...")
            exit()
        else:
            print("Invalid, Please choose either Hit, Stand or Stop playing")
            continue


game()
