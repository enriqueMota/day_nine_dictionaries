from os import system
from art import logo

system('clear')
print(logo)
auction_participants = {}
continue_auction = True


def get_bidders(participants):
    current_participant = input("What is your name?: ")
    participant_price = int(input("What is your bid?: $"))
    participants[current_participant] = participant_price


def find_winner(participants):
    highest_bidder = {
        "name": "",
        "bid": 0
    }

    for participant in participants:
        if participants[participant] >= highest_bidder["bid"]:
            highest_bidder["bid"] = participants[participant]
            highest_bidder["name"] = participant

    return highest_bidder


while continue_auction:
    get_bidders(auction_participants)
    more_bidders = input(
        "Is there anyone else wanting to bid? Yes or No ").lower()
    if more_bidders == 'yes':
        system("cls")
    else:
        winner = find_winner(auction_participants)
        print(f"The winner is {winner['name']} and their bid was {winner['bid']}")
        continue_auction = False
