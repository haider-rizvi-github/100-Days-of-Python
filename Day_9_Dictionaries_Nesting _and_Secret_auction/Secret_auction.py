import art

# TODO-1: Ask the user for their name and welcome them to the secret auction.

print("Welcome to the secret auction!")

name = input("what is your name?")
bid = int(input("what is your bid? $"))

# TODO-2: Save data into dictionary. {name: bid}
auction_data = {}  # create an empty dictionary to store the auction data
auction_data[name] = bid  # adding the name and bid to the dictionary

# TODO-3: Ask the user if there are any other bidders. If yes, repeat step 1 and 2.
should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
while should_continue == "yes":
    name = input("what is your name?")
    bid = int(input("what is your bid? $"))
    auction_data[name] = bid  # adding the name and bid to the dictionary
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()

# TODO-4: Find the highest bidder in dictionary and print their name and bid amount.
highest_bid = max(auction_data.values())
for key in auction_data:
    if auction_data[key] == highest_bid:
        print(f"The winner is {key} with a bid of ${highest_bid}.")
