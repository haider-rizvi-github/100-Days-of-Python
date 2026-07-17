import Black_jack_functions as bjf
import art

# Initializing the variables

user_cards = []
computer_cards = []
user_score = 0
computer_score = 0


# Will deal two random cards to the user and the computer
for randomcards in range(2):
    user_cards.append(bjf.deal_card())
    computer_cards.append(bjf.deal_card())

print(art.black_jack)
print("Let's play a game of Blackjack!")

user_score = bjf.calculate_score(user_cards)
computer_score = bjf.calculate_score(computer_cards)

print("Your cards:", user_cards, "Current score:", user_score)
print("Computer's cards:", computer_cards, "Current score:", computer_score)

if user_score == 0 or computer_score == 0 or user_score > 21:
    if user_score == 0:
        print("You have a Blackjack! You win!")
    elif computer_score == 0:
        print("Computer has a Blackjack! You lose!")
    elif user_score > 21:
        print("You went over 21! You lose!")

"""
The Game will continue if the user and computer scores are less than or equal to 21
The user will be prompted to either get another card or pass
"""

if user_score <= 21 and computer_score <= 21:
    while user_score < 21:
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        print("\n" * 5)
        if user_choice == "y":
            user_cards.append(bjf.deal_card())
            user_score = bjf.calculate_score(user_cards)
            print("Your cards:", user_cards, "Current score:", user_score)
        else:
            break

    while computer_score < 17:
        computer_cards.append(bjf.deal_card())
        computer_score = bjf.calculate_score(computer_cards)

    print("Your final hand:", user_cards, "Final score:", user_score)
    print("Computer's final hand:", computer_cards, "Final score:", computer_score)

print(bjf.compare(user_score, computer_score))
