# Day 11 - project 1
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deck_print(deck_of_cards, player):
    '''Printing cards in deck with player they belong to'''
    print(f"{'Your' if player == 'player' else 'Dealer'} cards: {deck_of_cards}, value = {sum(deck_of_cards)}")


# Beginning of game
print(logo)
print("Welcom to Blackjack!")
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
another_game = True


# Game
while another_game:
    player_cards = [random.choice(deck), random.choice(deck)]
    dealer_cards = [random.choice(deck), random.choice(deck)]

    deck_print(player_cards, "player")
    print(f"Dealer first card: [{dealer_cards[0]}]\n")

    # Part when player picks cards, checking right away if it's more then 21
    drawing_round = 0
    while sum(player_cards) < 21:
        drawing_round += 1
        print(f"{drawing_round} DRAW")
        deck_print(player_cards, "player")
        another_card = input(
            "Do you want to draw another card? Type 'y' or 'n': ")
        if another_card == "y":
            player_cards.append(random.choice(deck))
            print("\n")
            if sum(player_cards) > 21:
                deck_print(player_cards, "player")
                print("You lost by exceeding 21 :(")
                another_game = False
        else:
            break

    # If it was more then 21, end game here
    if another_game == False:
        break

    # Final check with the dealer
    print("\n")
    print("Calculating results ...")
    if sum(player_cards) > sum(dealer_cards):
        deck_print(player_cards, "player")
        deck_print(dealer_cards, "dealer")
        print("You won!")
        break
    elif sum(player_cards) < sum(dealer_cards):
        deck_print(player_cards, "player")
        deck_print(dealer_cards, "dealer")
        print("You lost :(")
        break
    else:
        deck_print(player_cards, "player")
        deck_print(dealer_cards, "dealer")
        print("It's a draw!")
        break
print("Thanks for playing!")
