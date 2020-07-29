from random import randrange

game = {number: state for number in range(1, 10) for state in ["No"]}
game["turn"] = 0


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
    gets the players name, symbols to use and tells the user the rules of the game
    """
    name = input("please key in your name: ")
    while True:
        ans = input("will you be going first? ")
        if ans.lower() in ["y", "yes"]:
            game["human"] = {"player_x": "player_1", "name": name}
            game["computer"] = {"player_x": "player_2"}
            break
        elif ans.lower() in ["n", "no"]:
            game["computer"] = {"player_x": "player_1"}
            game["human"] = {"player_x": "player_2", "name": name}
            break
        else:
            print('please key in "y", "yes", "n" or "no"!')
            print()

    human_symbol = input(f"please key in the symbol for {game['human']['name']}: ")
    game["human"]["symbol"] = human_symbol
    computer_symbol = input("please key in the symbol for the computer: ")
    game["computer"]["symbol"] = computer_symbol
    print(
        f"""
    {game['human']['name']}'s move will be represented with {game['human']['symbol']} while
    the computer's name will be represented with {game['human']['symbol']}.
    Key in the number as shown in the figure below to input your move.
    """.replace(
            "    ", ""
        )
    )
    print(table)
    return


def check():
    """
    checks the dictionary to see if the condition to win has been fulfilled
    """
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
    for [i, j, k] in winning_positions:
        if game[i] == game[j] == game[k] != "No":
            if game[i] == game["computer"]["symbol"]:
                print("Sorry, you have lost")
            else:
                print("Congratulations on winning!")
            exit()
    # can use while loop/if dict does not contain "no" but it is slower
    if game["turn"] == 9:
        print("You have drawed")
        exit()


def computers_turn(table):
    """
    Automates the computers turn
    For this, I am going to make the difficulty level easy by making the computer do random moves
    """
    i = randrange(1, 10)
    while game[i] != "No":
        i = randrange(1, 10)
    table = table.replace(str(i), game["computer"]["symbol"])
    game[i] = game["computer"]["symbol"]

    game["turn"] += 1
    return table

    # for i in range(1, 10):
    #     temp_table = table
    #     if game[i] != "No":
    #         temp_table = table.replace(str(i), game['computer']['symbol'])
    #         check()


def humans_turn(table):
    """
    asks the human to key in a number and changes the state of the game as such.
    """
    while True:
        i = input("your turn: ")
        int_i = int(i)
        if int_i in range(1, 10) and game[int_i] == "No":
            break
        else:
            print("please input a number from 1-9 and try again!")

    table = table.replace(i, game["human"]["symbol"])
    game[int(i)] = game["human"]["symbol"]

    game["turn"] += 1
    return table


# I tried to shorten the code by making a 'computer/human algorithm', but unforunately,
# there was an unbound local variable.
instructions()
if game["computer"]["player_x"] == "player_1":
    while True:
        # computers turn
        table = computers_turn(table)
        print(table)
        print(game)
        check()

        # humans turn
        table = humans_turn(table)
        print(table)
        print(game)
        check()
else:
    while True:
        # humans turn
        table = humans_turn(table)
        print(table)
        print(game)
        check()

        # computers turn
        table = computers_turn(table)
        print(table)
        print(game)
        check()


# def check(state=0):
#     '''
#     checks the dictionary to see if the condition to win has been fulfilled
#     '''
#     winning_positions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
#     for [i,j,k] in winning_positions:
#         if game[i] == game[j] == game[k] != "No" or game["turn"] != 9:
#             if game[i] == "O":
#                 print("Sorry, you have lost")
#             else:
#                 print("Congratulations on winning!")
#             return 1
#     #can use while loop/if dit does not contain "no" but it is slower
#     if game["turn"] == 9:
#         print("You have drawed")
#         return 1


# t = {i: x for i in range(8) for x is 3}
# t.values = 'asdf'
# print(t)
