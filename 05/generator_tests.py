import unittest
from unittest.mock import patch
from generator import main, file_gen


class MyTestCase(unittest.TestCase):
    def test_without_mistakes(self):
        file_name = 'test_txt.txt'
        words = ['строчка']
        f_generator = file_gen(file_name, words)
        self.assertEqual(next(f_generator), 'первая строчка')
        self.assertEqual(next(f_generator), 'третья строчка')
        self.assertEqual(next(f_generator), 'какая-то строчка')
        with self.assertRaises(StopIteration):
            next(f_generator)

    def test_with_wrong_filename(self):
        file_name = 'test.txt'
        f_generator = file_gen(file_name)
        with self.assertRaises(FileNotFoundError):
            next(f_generator)

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('generator.__name__', '__main__'):
            self.assertEqual(main(), 'end of main')
        with patch('generator.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
