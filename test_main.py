import unittest
import io
import main
from unittest.mock import Mock
from unittest.mock import patch
from main import (welcome_game,
                  game,
                  end_game,
                  play_again,
                  user_shift,
                  computer_says
                  )

class testing(unittest.TestCase):

    #1 testing the game is executed // testing a call
    def test_welcome_game(self):
        with patch('main.game') as mock:
            welcome_game()
            mock.assert_called_once()
    
    # 2 testing the loop is stopped when the secret number is discovered
    # testing a value is compared and passed to the call
    def test_game(self):
        with patch('builtins.input', return_value="10"):
            with patch('main.random_number', return_value=10):
                with patch('main.end_game') as mock:
                    game()
                    mock.assert_called_with(10, 1, ['Your guess on shift #1: 10'], "user")

    #3 testing the scores are correctly printed when game is over
    # testing a print is executed with the correct value
    def test_end_game(self):
        with patch('main.play_again'):
            with patch('builtins.print') as mock_print:
                scores = ['Your guess on shift #1: 10']
                end_game(10, 1, scores, "user")
                for item in scores:
                    mock_print.assert_called_with(item)

    #4 testing the game is stoped when user decides printing goodbye message
    # testing an input value triger an action
    def test_play_again(self):
        with patch('builtins.input', return_value="N"):
            with patch('main.cow_says') as mock:
                    play_again()
                    mock.assert_called_with("See you later!!")

    #5 testing a value returned to be equal from a user input
    # testing an input value is returned
    def test_user_shift(self):
        with patch('builtins.input', return_value="20"):
            self.assertEqual("20", user_shift(1))

    #6 testing a string returned to be equal passing a message as argument
    # testing a return passing an argument
    def test_computer_says(self):
        self.assertEqual(" ___\n|[_]|\n|+ ;|  System: \033[47m Hi \033[0m\n`---'\n", computer_says("Hi"))
    
if __name__ == "__main__":
    unittest.main()