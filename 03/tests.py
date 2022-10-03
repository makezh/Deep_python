import unittest
from unittest.mock import patch

from main import CustomList, main


class MyTestCase(unittest.TestCase):

    def test_print(self):
        list_1 = CustomList([1, 2, 3])
        list_2 = CustomList([])
        list_3 = CustomList()
        self.assertEqual(str(list_1), '[1, 2, 3] sum = 6;')
        self.assertEqual(str(list_2), '[] sum = 0;')
        self.assertEqual(str(list_3), '[] sum = 0;')
        self.assertEqual(repr(list_1), 'CustomList([1, 2, 3])')

    def test_len(self):
        self.assertEqual(len(CustomList([1, 2, 3])), 3)
        self.assertEqual(len(CustomList([])), 0)

    def test_diff(self):
        list_1 = CustomList([1, 2, 3])
        list_2 = CustomList([1, 1, 1, 1, 1])
        self.assertEqual(list_1 < list_2, False)
        self.assertEqual(list_1 <= list_2, False)
        self.assertEqual(list_1 > list_2, True)
        self.assertEqual(list_1 >= list_2, True)
        self.assertEqual(list_1 == list_2, False)
        self.assertEqual(list_1 != list_2, True)

    def test_adds(self):
        list_1 = CustomList([5, 1, 3, 7])
        list_2 = CustomList([1, 2, 7])
        simple_list = [1, 2, 3]
        self.assertEqual(list_1 + list_2, CustomList([6, 3, 10, 7]))
        self.assertEqual(list_1 - list_2, CustomList([4, -1, -4, 7]))
        self.assertEqual(list_1 - simple_list, CustomList([4, -1, 0, 7]))
        self.assertEqual(list_1 + simple_list, CustomList([6, 3, 6, 7]))
        self.assertEqual(simple_list - list_1, CustomList([-4, 1, 0, -7]))
        self.assertEqual(simple_list + list_1, CustomList([6, 3, 6, 7]))

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('main.__name__', '__main__'):
            self.assertEqual(main(), 'end of main')
        with patch('main.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
