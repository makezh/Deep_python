import unittest
import mock
from faker import Factory
from main import change_str, parse_json


class MyTestCase(unittest.TestCase):
    def test_change_str(self):
        self.assertEqual(change_str("qwerty"), "ytrewq")
        self.assertEqual(change_str("123"), "321")

    def test_parse_json_none(self):
        string = '{"key_1": "words", "key_2": "word2 word1"}'
        self.assertEqual(parse_json(string), None)
        self.assertEqual(parse_json(string, []), None)
        self.assertEqual(parse_json(string, [], []), None)
        self.assertEqual(parse_json(string, [], [], change_str), None)

    def test_parse_json(self):
        string = '{"key_1": "words", "key_2": "word2 word1"}'
        self.assertEqual(parse_json(string, ["key_1"], ["words"], change_str),
                         ['sdrow'])
        self.assertEqual(parse_json(string, ["key_2"], ["word1"], change_str),
                         ['1drow'])

    @mock.patch('main.change_str')
    def test_parse_json_count(self, changing):
        string = '{"key_1": "words word3", ' \
                 '"key_2": "word3 word2 word1", ' \
                 '"key_3": "word1 word2 word3 word4 word3"}'
        keys = ["key_1", "key_2", "key_3"]
        values = ["word3"]
        changing.return_value = "test"
        parse_json(string, keys, values, changing)
        self.assertEqual(changing.call_count, 4)

    def test_faker(self):
        fake = Factory().create()
        string = fake.json(num_rows=1,
                           data_columns={'key_1': 'catch_phrase',
                                         'key_2': 'name',
                                         'key_3': 'currency_name',
                                         'key_4': 'http_method'})
        keys = ['key_1', 'key_3']
        values = [fake.word(), fake.word(), fake.word()]
        self.assertEqual(parse_json(string, keys, values, change_str), None)


if __name__ == '__main__':
    unittest.main()
