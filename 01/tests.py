import unittest.mock
import unittest
import io
from main import TicTacGame


class MyTestCase(unittest.TestCase):
    game = TicTacGame()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_board(self, expected_output, mock_stdout):
        self.game.show_board()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_show_board(self):
        expected = "-------------" + \
                   "\n| 1 | 2 | 3 |\n" +\
                   "-------------" \
                   "\n| 4 | 5 | 6 |\n" +\
                   "-------------" +\
                   "\n| 7 | 8 | 9 |\n" +\
                   "-------------\n"
        self.assert_stdout_board(expected)

    def run_validate_input(self, given_answer, expected_out):
        with unittest.mock.patch(
                'builtins.input',
                return_value=given_answer
        ), \
                unittest.mock.patch(
                    'sys.stdout',
                    new=io.StringIO()
                ) as fake_out:
            self.game.validate_input("X")
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def test_validate_input(self):
        incorrect = "Incorrect input. Enter a number from 1 to 9"
        engaged = "The field is already occupied :("
        self.run_validate_input(5, "")
        self.run_validate_input("sas", incorrect)
        self.run_validate_input(5, engaged)
        self.run_validate_input(123, incorrect)

    def test_winner_123(self):
        game_test = TicTacGame()
        game_test.board[0] = "X"
        game_test.board[1] = "X"
        game_test.board[2] = "X"
        self.assertEqual(game_test.check_winner(), "X")

    def test_winner_456(self):
        game_test = TicTacGame()
        game_test.board[3] = "X"
        game_test.board[4] = "X"
        game_test.board[5] = "X"
        self.assertEqual(game_test.check_winner(), "X")

    def test_winner_789(self):
        game_test = TicTacGame()
        game_test.board[6] = "X"
        game_test.board[7] = "X"
        game_test.board[8] = "X"
        self.assertEqual(game_test.check_winner(), "X")

    def test_winner_147(self):
        game_test = TicTacGame()
        game_test.board[0] = "O"
        game_test.board[3] = "O"
        game_test.board[6] = "O"
        self.assertEqual(game_test.check_winner(), "O")

    def test_winner_258(self):
        game_test = TicTacGame()
        game_test.board[1] = "X"
        game_test.board[4] = "X"
        game_test.board[7] = "X"
        self.assertEqual(game_test.check_winner(), "X")

    def test_winner_369(self):
        game_test = TicTacGame()
        game_test.board[2] = "O"
        game_test.board[5] = "O"
        game_test.board[8] = "O"
        self.assertEqual(game_test.check_winner(), "O")

    def test_winner_159(self):
        game_test = TicTacGame()
        game_test.board[0] = "X"
        game_test.board[4] = "X"
        game_test.board[8] = "X"
        self.assertEqual(game_test.check_winner(), "X")

    def test_winner_357(self):
        game_test = TicTacGame()
        game_test.board[2] = "O"
        game_test.board[4] = "O"
        game_test.board[6] = "O"
        self.assertEqual(game_test.check_winner(), "O")

    def test_winner_false(self):
        game_test = TicTacGame()
        game_test.board[2] = "X"
        game_test.board[4] = "O"
        game_test.board[6] = "X"
        self.assertEqual(game_test.check_winner(), False)

    def run_process(self, given_answer, expected_out):
        with unittest.mock.patch(
                'builtins.input',
                return_value=given_answer
        ), \
                unittest.mock.patch(
                    'sys.stdout',
                    new=io.StringIO()
                ) as fake_out:
            self.game.process()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)


if __name__ == '__main__':
    unittest.main()
