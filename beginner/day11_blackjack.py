import random
from blackjack_art import logo


# --------- INITIALISE ----------#

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# --------- INPUT HANDLER ----------#

def get_choice(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice
        print("Invalid input. Please enter either 'y' or 'n'.")


# --------- HELPER FUNCTION ----------#

def has_blackjack(hand):
    return sum(hand) == 21 and len(hand) == 2


# --------- BLACKJACK LOGIC ----------#

def deal_card():
    return random.choice(card_values)


def change_ace_score(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        

def deal_initial_cards():
    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]
    # convert one ace to avoid busting on [11, 11]
    change_ace_score(player)
    change_ace_score(dealer)

    return player, dealer


def show_final_cards(player, dealer):
    print(f"\nYour final hand: {player}, final score: {sum(player)}")
    print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")


def check_blackjack(player, dealer):
    player_blackjack = has_blackjack(player)
    dealer_blackjack = has_blackjack(dealer)

    if player_blackjack or dealer_blackjack:
        show_final_cards(player, dealer)
        if player_blackjack and dealer_blackjack:
            print("You both have blackjack. Draw")
        elif player_blackjack:
            print("You have blackjack. You win 😀")
        elif dealer_blackjack:
            print("Dealer has blackjack. You lose 😤")
        return True
    
    return False


def bust(who, player, dealer):
    show_final_cards(player, dealer)
    if who == "player":
        print("You went over. You lose 😤")
    else:
        print("Dealer went over. You win 😁")        


def player_turn(player, dealer):
    while True:
        change_ace_score(player)
        player_score = sum(player)

        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score >= 21:
            break

        if get_choice("Type 'y' to get another card, type 'n' to pass: ") == "y":
            player.append(deal_card())
        else:
            break
    
    return player_score, player_score > 21 # returns (score, is_bust)


def dealer_turn(dealer):
    dealer_score = sum(dealer)

    while dealer_score < 17:
        dealer.append(deal_card())
        change_ace_score(dealer)
        dealer_score = sum(dealer)
    
    return dealer_score, dealer_score > 21 # returns (score, is_bust)


def compare_scores(player_score, dealer_score): 
    if player_score == dealer_score:
        return "It's a draw!"
    elif player_score > dealer_score:
        return "You win 😀"
    else:
        return "You lose 😤"


def start_game():
    print("\n" + logo)
    player, dealer = deal_initial_cards()

    if check_blackjack(player, dealer):
        return
    
    player_score, player_bust = player_turn(player, dealer)
    if player_bust:
        bust("player", player, dealer)
        return

    print(f"Dealer's full hand: {dealer}, current score: {sum(dealer)}")

    dealer_score, dealer_bust = dealer_turn(dealer)
    if dealer_bust:
        bust("dealer", player, dealer)
        return

    show_final_cards(player, dealer)
    print(compare_scores(player_score, dealer_score))


def play_blackjack():
    while True:
        start_game()
        if get_choice("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
            break


# ---------- PLAY BLACKJACK ----------#

play_blackjack()