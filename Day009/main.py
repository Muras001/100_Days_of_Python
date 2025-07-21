import art
print(art.logo)

bidders_dic = {}

continue_bid = True


def find_highest_bidder(bidding_dictionary):
    winner = ""
    base_score = 0
    for bidder in bidders_dic:
        score = bidders_dic[bidder]
        if score > base_score:
            base_score = score
            winner = bidder

    print("\n" * 100)
    print(f"The winner is {winner} with a bid of ${base_score}.")
while continue_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'y' or 'n': ").lower()

    bidders_dic[name] = bid

    if other_bidders == 'n':
        continue_bid = False
        find_highest_bidder(bidders_dic)

    else:
        print("\n"*100)
        print(art.logo)
