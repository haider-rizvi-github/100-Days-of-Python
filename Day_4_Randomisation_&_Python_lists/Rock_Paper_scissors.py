# Objective: Create a rock, paper and scissors game that will ask
# the user to input their choice and then randomly generate a choice for the computer.
# it should also display the result of the game in graphics ASCII.

import random
import Graphics  # custom module that contains the ASCII graphics for the game

# Creating a list
Game_choices = ["Rock", "Paper", "Scissors"]

#  generating a random choice for the computer
Computerchoice = random.randint(0, 2)
print(f"Computer chose: {Game_choices[Computerchoice]}")

print("Welcome to Rock, Paper, Scissors!")
User_input = input(
    "Enter your choice type the numbers(0[Rock], 1[Paper], 2[Scissors]): "
)
User_input = int(User_input)

if User_input == 0 and Computerchoice == 1:
    print("You lose! Computer chose Paper")
    print(Graphics.Paper)
elif User_input == 0 and Computerchoice == 2:
    print("You win! Computer chose Scissors")
    print(Graphics.Scissor)
elif User_input == 1 and Computerchoice == 0:
    print("You win! Computer chose Rock")
    print(Graphics.Rock)
elif User_input == 1 and Computerchoice == 2:
    print("You lose! Computer chose Scissors")
    print(Graphics.Scissor)
elif User_input == 2 and Computerchoice == 0:
    print("You lose! Computer chose Rock")
    print(Graphics.Rock)
elif User_input == 2 and Computerchoice == 1:
    print("You win! Computer chose Paper")
    print(Graphics.Paper)
else:
    print("It's a draw! Computer chose the same as you")
    print(Graphics.Draw)
