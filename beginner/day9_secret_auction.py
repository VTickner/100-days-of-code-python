from secret_auction_art import logo

def find_highest_bidder(bids):
    max_bid = 0
    winner = ""

    for bidder, bid in bids.items():
        if bid > max_bid:
            max_bid = bid
            winner = bidder

    print(f"The winner is {winner} with a bid of ${max_bid:.2f}")

print(logo)
bids = {}
bidding = True

while bidding:
    user_name = input("What is your name?: ")

    while True: 
        try:
            user_bid = float(input("What is your bid?: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    bids[user_name] = user_bid

    while True:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()
        if other_bidders in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter either 'yes' or 'no'.")

    if other_bidders == "yes":
        print("\n" * 20)
    else:
        bidding = False

find_highest_bidder(bids)