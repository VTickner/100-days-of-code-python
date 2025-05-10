import random
from blackjack_art import logo


# --------- INITIALISE ----------#

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# --------- INPUT HANDLER ----------#

def get_choice(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice
        print("Invalid input. Please enter either 'y' or 'n'.")


# --------- BLACKJACK LOGIC ----------#

def draw_card():
    return random.choice(cards)


def change_ace_score(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1


def show_final_cards(player, player_score, dealer, dealer_score):
    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Computer's final hand: {dealer}, final score: {dealer_score}")


def bust(hand, player, player_score, dealer, dealer_score):
    if hand == "player":
        show_final_cards(player, player_score, dealer, dealer_score)
        print("You went over. You lose 😤")
    else:
        show_final_cards(player, player_score, dealer, dealer_score)
        print("Computer went over. You win 😁")        


def player_turn(player, dealer):
    while True:
        player_score = sum(player)

        # convert Ace from 11 to 1 if over 21 before printing hand and score
        if player_score > 21 and 11 in player:
            change_ace_score(player)
            player_score = sum(player)

        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score == 21:
            break
        elif player_score > 21:
            return player_score, True # True = bust

        another_card = get_choice("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            player.append(draw_card())
        else:
            break
    
    return player_score, False # False = not bust


def dealer_turn(player, player_score, dealer):
    dealer_score = sum(dealer)

    while dealer_score < 17:
        dealer.append(draw_card())
        dealer_score = sum(dealer)

        while dealer_score > 21 and 11 in dealer:
            change_ace_score(dealer)
            dealer_score = sum(dealer)
    
    if dealer_score > 21:
        bust("dealer", player, player_score, dealer, dealer_score)
        return
    else:
        return dealer_score


def compare_scores(player, player_score, dealer, dealer_score):
    if player_score == dealer_score == 21 and len(player) == 2 and len(dealer) == 2:
        return "You both have blackjack. Draw"
    elif player_score == 21 and len(player) == 2:
        return "You have blackjack. You win 😀"
    elif dealer_score == 21 and len(dealer) == 2:
        return "Computer has blackjack. You lose 😤"
    elif player_score == dealer_score:
        return "Draw"
    elif player_score > dealer_score:
        return "You win 😀"
    else:
        return "You lose 😤"


def start_game():
    print(logo)

    dealer = []
    player = []
    
    player.append(draw_card())
    player.append(draw_card())
    dealer.append(draw_card())
    dealer.append(draw_card())

    # convert one ace to avoid busting on [11, 11]
    change_ace_score(player)
    change_ace_score(dealer)

    player_score = sum(player)
    dealer_score = sum(dealer)

    # blackjack check
    if player_score == 21 and dealer_score == 21 and len(player) == 2 and len(dealer) == 2:
        show_final_cards(player, player_score, dealer, dealer_score)
        print("You both have blackjack. Draw")
        return
    elif player_score == 21 and len(player) == 2:
        show_final_cards(player, player_score, dealer, dealer_score)
        print("You have blackjack. You win 😀")
        return
    elif dealer_score == 21 and len(dealer) == 2:
        show_final_cards(player, player_score, dealer, dealer_score)
        print("Computer has blackjack. You lose 😤")
        return
    
    player_score, is_bust = player_turn(player, dealer)
    if is_bust:
        bust("player", player, player_score, dealer, dealer_score)
        return

    dealer_score = dealer_turn(player, player_score, dealer)
    if dealer_score is not None:  # ← Only run if dealer didn't bust
        show_final_cards(player, player_score, dealer, dealer_score)
        print(compare_scores(player, player_score, dealer, dealer_score))


def play_blackjack():
    while True:
        start_game()
        play_again = get_choice("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_again == 'n':
            break


# ---------- PLAY BLACKJACK ----------#

play_blackjack()