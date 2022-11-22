import unittest
from unittest.mock import patch
from fetcher import main


class MyTestCase(unittest.TestCase):

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('fetcher.__name__', '__main__'):
            self.assertEqual(main(), 'alright, this is main')
        with patch('fetcher.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
