from random import randrange

game = {number: state for number in range(1, 10) for state in ["No"]}
# The game's turn is somewhat half a turn behind
game["turn"] = 0
winning_positions = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

table = """
         |        |        
    1    |   2    |    3   
---------------------------
         |        |        
    4    |   5    |    6   
---------------------------
         |        |        
    7    |   8    |    9   
"""


def instructions():
    """
    Gets the players symbol, and tells the user the rules of the game
    """
    while True:
        ans = input("Will you be going first? ")
        if ans.lower() in ["y", "yes"]:
            game["human"] = {"player_x": "player_1"}
            game["computer"] = {"player_x": "player_2"}
            break
        elif ans.lower() in ["n", "no"]:
            game["computer"] = {"player_x": "player_1"}
            game["human"] = {"player_x": "player_2"}
            break
        else:
            print('Please key in "y", "yes", "n" or "no"!')
            print()
    while True:
        human_symbol = input("Please key in the symbol for yourself: ")
        if len(human_symbol) == 1:
            break
    game["human"]["symbol"] = human_symbol.upper()
    while True:
        computer_symbol = input("Please key in the symbol for the computer: ")
        if len(computer_symbol) == 1:
            break
    game["computer"]["symbol"] = computer_symbol.upper()
    print(
        f"""
    Your move will be represented with {game['human']['symbol']},
    while the computer's name will be represented with {game['computer']['symbol']}.
    Key in the number as shown in the figure below to input your move.
    """.replace(
            "    ", ""
        )
    )
    print(table)
    return


def check():
    """
    Checks the dictionary to see if the condition to win has been fulfilled
    Returns 1 if the condition has been fulfilled
    """
    for [i, j, k] in winning_positions:
        if game[i] == game[j] == game[k] != "No":
            if game[i] == game["computer"]["symbol"]:
                print("Sorry, you have lost.")
            else:
                print("Congratulations on winning!")
            return 1
    # can use while loop/if dict does not contain "no" but it is slower
    if game["turn"] == 9:
        print("You have drawed")
        return 1 


def easy_computers_turn(table):
    """
    Makes the computer do random moves based on RNG
    """
    i = randrange(1, 10)
    while game[i] != "No":
        i = randrange(1, 10)
    table = table.replace(str(i), game["computer"]["symbol"])
    game[i] = game["computer"]["symbol"]

    game["turn"] += 1
    return table


def hard_computers_turn(table):
    """
    A simple AI that thinks 1 move ahead of its turn to see if causes it to lose/win
    """
    # Makes a dict such that it only contains the numbers in game
    # The computer checks if it has a winning move in its next turn
    # It then checks if the human has a winning move in its next turn
    # If both conditions are false, it falls back to using RNG
    temp_dict = {
        number: state for (number, state) in game.items() if type(number) == int
    }
    if game["turn"] >= 4:
        for i in temp_dict:
            if temp_dict[i] == "No":
                temp_dict[i] = game["computer"]["symbol"]
                for [a, b, c] in winning_positions:
                    if (
                        temp_dict[a]
                        == temp_dict[b]
                        == temp_dict[c]
                        == game["computer"]["symbol"]
                    ):
                        table = table.replace(str(i), game["computer"]["symbol"])
                        game[i] = game["computer"]["symbol"]
                        game["turn"] += 1
                        return table
                temp_dict[i] = "No"
        # alternatively can use combinations from itertools
    if game["turn"] >= 3:
        for [a, b, c] in winning_positions:
            if game[a] == game[b] == game["human"]["symbol"] and game[c] == "No":
                j = c
                break
            elif game[b] == game[c] == game["human"]["symbol"] and game[a] == "No":
                j = a
                break
            elif game[a] == game[c] == game["human"]["symbol"] and game[b] == "No":
                j = b
                break
            else:
                continue
        try:
            table = table.replace(str(j), game["computer"]["symbol"])
            game[j] = game["computer"]["symbol"]
            game["turn"] += 1
            return table
        except UnboundLocalError:
            pass

    table = easy_computers_turn(table)
    return table


def humans_turn(table):
    """
    Asks the human to key in a number and changes the state of the game as such.
    """
    while True:
        i = input("Your turn: ")
        try:
            int_i = int(i)
        except ValueError:
            print("Please enter an integer!")
            continue
        if int_i in range(1, 10) and game[int_i] == "No":
            break
        elif int_i in range(1, 10):
            print(f"Spot {i} has already been taken!\nPlease input a number into an available slot")
        else:
            print("Please input a number from 1-9 and try again!")

    table = table.replace(i, game["human"]["symbol"])
    game[int(i)] = game["human"]["symbol"]

    game["turn"] += 1
    return table


# if i is even--> computer's turn
# if i is odd--> human's turn
instructions()
i = 0
if game["human"]["player_x"] == "player_1":
    i = 1
while True:
    if i % 2 == 0:
        table = hard_computers_turn(table)
    else:
        table = humans_turn(table)
    print(table)
    print(game)
    if check() == 1:
        break
    i += 1

