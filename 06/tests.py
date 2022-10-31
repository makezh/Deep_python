import json
import queue
import sys
import unittest
from unittest import mock
from unittest.mock import patch

from client import process_file, check_argv, IP, SIZE, SPLIT_CHAR, client_connect, client_request
from server import common_words, create_parser, server_connect


class MyTestCase(unittest.TestCase):
    mock_file_content = """https://appstorrent.ru/803-skate-city.html
    https://appstorrent.ru/1640-dirt-rally.html"""

    @unittest.mock.patch(
        'builtins.open',
        new=unittest.mock.mock_open(read_data=mock_file_content),
        create=True
    )
    def test_process_file_by_client(self):
        test_que = process_file('/dev/null')
        self.assertEqual(test_que.get().strip(SPLIT_CHAR),
                         'https://appstorrent.ru/803-skate-city.html')
        self.assertEqual(test_que.get().strip(SPLIT_CHAR),
                         'https://appstorrent.ru/1640-dirt-rally.html')
        self.assertEqual(test_que.get().strip(SPLIT_CHAR),
                         '>END')

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
        expected_dict = {test_url:
                             {"всего": 20,
                              "голосов": 20,
                              "просмотры": 20,
                              "добавить": 20,
                              "закладки": 20}
                         }
        expected_json = json.dumps(expected_dict, ensure_ascii=False)
        self.assertEqual(common_words(test_url, 5), expected_json)

        fake_url = 'https://its_fake.adf'
        expected_fake_dict = {fake_url: 'error'}
        expected_fake_json = json.dumps(expected_fake_dict, ensure_ascii=False)
        self.assertEqual(common_words(fake_url, 5), expected_fake_json)

    def test_parser_argv_by_server(self):
        with patch("sys.argv", ["server.py", '-w', '241', '-k', '34']):
            parser = create_parser()
            namespace = parser.parse_args(sys.argv[1:])
            workers, top_k = namespace.workers, namespace.top_k
            self.assertEqual(workers, 241)
            self.assertEqual(top_k, 34)

    def test_server_connect(self):
        with mock.patch('socket.socket') as mock_socket:
            mock_socket.return_value.recv.return_value = 'test server...'
            test_socket = server_connect((IP, 12345))
        self.assertEqual(test_socket.recv(SIZE), 'test server...')

    def test_client_connect(self):
        with mock.patch('socket.socket') as mock_socket:
            mock_socket.return_value.recv.return_value = 'test client...'
            test_socket = client_connect((IP, 12345))
        self.assertEqual(test_socket.recv(SIZE), 'test client...')


if __name__ == '__main__':
    unittest.main()
