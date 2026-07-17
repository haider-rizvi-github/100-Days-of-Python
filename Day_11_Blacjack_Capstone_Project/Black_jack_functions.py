import random

# create a function that will deal a random card from the deck


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    # random.choice() helps to randomly select a card from the list of cards
    return card


""" 
Create a function that will calculate the score of the cards
Use a list as an argument to calculate the score of the cards in the list
"""


def calculate_score(cards):

    # check for a blackjack (a hand with only 2 cards: ace(11) + 10)
    # if not return the sum of the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # removes the ace card from the list of cards
        cards.append(1)  # adds the ace card as 1 to the list of cards

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has a Blackjack! You lose!"
    elif user_score == 0:
        return "You have a Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21! You lose!"
    elif computer_score > 21:
        return "Computer went over 21! You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
