import unittest
from unittest.mock import patch
from lru import main, LRUCache


class MyTestCase(unittest.TestCase):
    def test_overflow(self):
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

    def test_set(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k2", "val21")

        self.assertEqual(cache.get("k2"), "val21")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k2", "val22")
        cache.set("k2", "val23")
        cache.set("k2", "val24")

        self.assertEqual(cache.get("k2"), "val24")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k1", "val11")
        cache.set("k1", "val12")
        cache.set("k1", "val13")

        self.assertEqual(cache.get("k2"), "val24")
        self.assertEqual(cache.get("k1"), "val13")

        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val13")

        cache.set("k1", "val14")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val14")

        cache.set("k4", "val4")
        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val14")

    def test_single_cache_size(self):
        cache = LRUCache(1)

        self.assertEqual(cache.get("something"), None)

        cache.set("new_one", "data")
        self.assertEqual(cache.get("new_one"), "data")

        cache.set("new_one", "new_data")
        self.assertEqual(cache.get("new_one"), "new_data")

        cache.set("newest_one", "final_data")
        self.assertEqual(cache.get("new_one"), None)
        self.assertEqual(cache.get("newest_one"), "final_data")

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('lru.__name__', '__main__'):
            self.assertEqual(main(), 'alright, this is main')
        with patch('lru.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
