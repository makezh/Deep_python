import unittest
from unittest.mock import patch
from lru import main, LRUCache


class MyTestCase(unittest.TestCase):
    def test_lru(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('lru.__name__', '__main__'):
            self.assertEqual(main(), 'alright, this is main')
        with patch('lru.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
