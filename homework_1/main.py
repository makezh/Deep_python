"""1st homework for deep python in Techopark"""


class TicTacGame:
    """
    Implementation of the TIC-TAC-TOE console game
    """

    def __init__(self):
        self.board = list(range(1, 10))

    def show_board(self):
        """
        Game board output
        :return:
        -------------
        | 1 | 2 | 3 |
        -------------
        | 4 | 5 | 6 |
        -------------
        | 7 | 8 | 9 |
        -------------
        """
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0 + i * 3],
                  "|", self.board[1 + i * 3],
                  "|", self.board[2 + i * 3],
                  "|")
            print("-" * 13)

    def validate_input(self, player_sign):
        """
        Check user input
        :param player_sign: int
        """
        player_answer = input("Choose the place for \""
                              + player_sign +
                              "\": ")

        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Incorrect input. Enter a number from 1 to 9")
            return False

        if 1 <= player_answer <= 9:
            if str(self.board[player_answer - 1]) not in "XO":
                self.board[player_answer - 1] = player_sign
                return True

            print("The field is already occupied :(")
            return False

        print("Incorrect input. Enter a number from 1 to 9")
        return False

    def process(self):
        """
        Process of game
        :return: bool
        """
        counter = 0
        win = False
        while not win:
            self.show_board()
            if counter % 2 == 0:
                valid = False
                while not valid:
                    valid = self.validate_input("X")
            else:
                valid = False
                while not valid:
                    valid = self.validate_input("O")
            counter += 1
            if counter > 4:
                tmp = self.check_winner()
                if tmp:
                    print(tmp, "Wins!")
                    win = True
                    return win
            if counter == 9:
                print("Draw!")
                return False
        self.show_board()

    def start_game(self):
        """
        Just start of game
        """
        print("|TIC-TAC-TOE|")
        self.process()

    def check_winner(self):
        """
        Checking for winnings
        :return: bool
        """
        wins = ((0, 1, 2), (3, 4, 5),
                (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))
        for each in wins:
            field_1 = self.board[each[0]]
            field_2 = self.board[each[1]]
            field_3 = self.board[each[2]]
            if field_1 == field_2 == field_3:
                return field_1
        return False


if __name__ == "__main__":
    TicTacGame().start_game()
