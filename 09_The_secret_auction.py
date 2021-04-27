all_bids = {}
stop = True


def winner_player(dictionary):
    highest_bid = 0
    winner = ""
    for player in dictionary:
        if dictionary[player] > highest_bid:
            highest_bid = dictionary[player]
            winner = player
    print(winner, dictionary[winner])


while stop:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    additional_player = input("Are there any other bidders? Type 'yes or 'no'. ")
    all_bids[name] = bid
    if additional_player == 'no':
        stop = False
        winner_player(all_bids)
