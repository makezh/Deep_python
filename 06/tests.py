import sys
import unittest
from unittest.mock import patch

from client import process_file, check_argv


class MyTestCase(unittest.TestCase):
    def test_process_file_by_client(self):
        que = process_file('urls.txt')
        self.assertEqual(que.qsize(), 100 + 1)
        for i in range(que.qsize()):
            if i == 50:
                self.assertEqual(que.get(), 'https://appstorrent.ru/141-acdsee-photo-studio.html')
            elif i == 86:
                self.assertEqual(que.get(), 'https://appstorrent.ru/697-acorn.html')
            elif i == 100:
                self.assertEqual(que.get(), '>END')
            else:
                que.get()

    def test_argv_by_client(self):
        with self.assertRaises(AttributeError):
            check_argv()

        with patch("sys.argv", ["client.py", "aaa"]):
            with self.assertRaises(ValueError):
                check_argv()

        with patch("sys.argv", ["client.py", "10", "test.txt"]):
            with self.assertRaises(FileNotFoundError):
                check_argv()




if __name__ == '__main__':
    unittest.main()
