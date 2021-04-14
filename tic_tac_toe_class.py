from random import randrange

WINNING_POSITIONS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


def main():
    game_1 = ttt("human", "X", "O", "hard")
    while True:
        if game_1.turn == "computer":
            game_1.hard()
            game_1.turn = "human"
        else:
            game_1.humans_turn()
            game_1.turn = "computer"
        print(game_1.table)
        if game_1.check_winning_condition() != -1:
            break


class ttt:
    game = {number: state for number in range(1, 10) for state in ["None"]}
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

    def __init__(self, turn, computer_symbol, human_symbol, difficulty):
        self.turn = turn
        self.computer_symbol = computer_symbol.upper()
        self.human_symbol = human_symbol.upper()
        self.difficulty = difficulty

    def move(self, a, player):
        self.a = a
        if self.turn == "computer":
            self.table = self.table.replace(str(a), self.computer_symbol)
            self.game[a] = self.computer_symbol
        elif self.turn == "human":
            self.table = self.table.replace(str(a), self.human_symbol)
            self.game[a] = self.human_symbol
        else:
            return None
        self.game["turn"] += 1

    def check_winning_condition(self):
        for [i, j, k] in WINNING_POSITIONS:
            if self.game[i] == self.game[j] == self.game[k] != "None":
                if self.game[i] == self.computer_symbol:
                    print("Sorry, you have lost.")
                    return 2
                print("Congratulations on winning!")
                return 1
        if self.game["turn"] == 9:
            print("You have drawed.")
            return 0
        return -1

    def easy(self):
        i = randrange(1, 10)
        while self.game[i] != "None":
            i = randrange(1, 10)
        self.move(i, "computer")

    def hard(self):
        # Makes a dict such that it only contains the numbers in game
        # The computer checks if it has a winning move in its next turn
        # It then checks if the human has a winning move in its next turn
        # If both conditions are false, it falls back to using RNG
        temp_dict = {
            number: state
            for (number, state) in self.game.items()
            if type(number) == int
        }
        if self.game["turn"] >= 4:
            for i in temp_dict:
                if temp_dict[i] == "None":
                    temp_dict[i] = self.computer_symbol
                    for [a, b, c] in WINNING_POSITIONS:
                        if (
                            temp_dict[a]
                            == temp_dict[b]
                            == temp_dict[c]
                            == self.computer_symbol
                        ):
                            self.move(i, "computer")
                            return
                    temp_dict[i] = "None"
            # alternatively can use combinations from itertools
        if self.game["turn"] >= 3:
            for [a, b, c] in WINNING_POSITIONS:
                if (
                    self.game[a] == self.game[b] == self.human_symbol
                    and self.game[c] == "None"
                ):
                    j = c
                    break
                elif (
                    self.game[b] == self.game[c] == self.human_symbol
                    and self.game[a] == "None"
                ):
                    j = a
                    break
                elif (
                    self.game[a] == self.game[c] == self.human_symbol
                    and self.game[b] == "None"
                ):
                    j = b
                    break
                else:
                    continue
            try:
                self.move(j, "computer")
                return
            except UnboundLocalError:
                pass

        self.easy()
        return

    def humans_turn(self):
        while True:
            i = input("Your turn: ")
            try:
                int_i = int(i)
            except ValueError:
                print("Please enter an integer!")
                continue
            if int_i in range(1, 10) and self.game[int_i] == "None":
                break
            elif int_i in range(1, 10):
                print(
                    f"spot {i} has already been taken\n"
                    "Please input a number from 1-9 and try again!"
                )
            else:
                print("Please input a number from 1-9 and try again!")
        self.move(int(i), "human")


if __name__ == "__main__":
    main()
