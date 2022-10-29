import json
import sys
import unittest
from unittest.mock import patch

from client import process_file, check_argv
from server import common_words, create_parser


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

    def test_common_words_by_server(self):
        test_url = 'https://habr.com/ru/company/vk/blog/'
        expected_dict = {"https://habr.com/ru/company/vk/blog/":
                             {"всего": 20,
                              "голосов": 20,
                              "просмотры": 20,
                              "добавить": 20,
                              "закладки": 20}
                         }
        expected_json = json.dumps(expected_dict, ensure_ascii=False)
        self.assertEqual(common_words(test_url, 5), expected_json)

    def test_parser_argv_by_server(self):
        with patch("sys.argv", ["server.py", '-w', '241', '-k', '34']):
            parser = create_parser()
            namespace = parser.parse_args(sys.argv[1:])
            workers, top_k = namespace.workers, namespace.top_k
            self.assertEqual(workers, 241)
            self.assertEqual(top_k, 34)


if __name__ == '__main__':
    unittest.main()
