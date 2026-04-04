# It is a word game where you have to find the treasure by making the right choices.

# variables
Answer = None
Game_over = "Your are Dead! Game Over."
PlayerName = input("What is your name? ")
OpenTreasure = r"""                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
"""

# Visuals
print(
    r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `"""
    "-"
    """"""
    """"""
    """"""
    """"""
    "-"
    """`
      """
)

PlayerWin = f"Congratulations! {PlayerName} You found the treasure and won the game."

print(
    f"Welcome {PlayerName} to Treasure Island.\n Your mission is to find the treasure."
)

# Story buildup
Answer = input(
    f" {PlayerName}, you are on a treasure island and there are two paths in front of you. Where do you want to go? Type 'L' for left or 'R' for right. "
)

if Answer == "L" or Answer == "l":
    print("Congratulations! You are on the right track.")

    Answer = input(
        f" {PlayerName}, you have come to a lake. There is an island in the middle of the lake. Type 'S' to swim across or 'W' to wait for a boat. "
    )
    if Answer == "W" or Answer == "w":
        print(f"Congratulations! {PlayerName} You are on the right track.")

        Answer = input(
            f" {PlayerName}, you have come to the island. There is a house with three doors. Which door do you want to choose? Type 'R' for red, 'B' for blue, or 'Y' for yellow. "
        )
        if Answer == "Y" or Answer == "y":
            print(OpenTreasure)

            print(PlayerWin)
        else:
            print(Game_over)
    else:
        print(Game_over)


else:
    print(Game_over)
