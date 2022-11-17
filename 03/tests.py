import functools
import unittest
from unittest.mock import patch

from CustomList import CustomList, main


def list_comparison(list_1, list_2) -> bool:
    return functools.reduce(lambda x, y: x and y,
                            map(lambda p, q: p == q, list_1, list_2), True)


class MyTestCase(unittest.TestCase):

    def test_print(self):
        list_1 = CustomList([1, 2, 3])
        list_2 = CustomList([])
        list_3 = CustomList()
        self.assertEqual(str(list_1), 'CustomList([1, 2, 3]) sum = 6;')
        self.assertEqual(str(list_2), 'CustomList([]) sum = 0;')
        self.assertEqual(str(list_3), 'CustomList([]) sum = 0;')
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

    def test_add_customs(self):
        init_list_1 = [5, 1, 3, 7]
        init_list_2 = [1, 2, 7]
        list_1 = CustomList(init_list_1)
        list_2 = CustomList(init_list_2)

        # сложение
        self.assertTrue(list_comparison(list_1 + list_2,
                                        CustomList([6, 3, 10, 7])))
        self.assertTrue(list_comparison(list_2 + list_1,
                                        CustomList([6, 3, 10, 7])))

        # вычитание
        self.assertTrue(list_comparison(list_1 - list_2,
                                        CustomList([4, -1, -4, 7])))
        self.assertTrue(list_comparison(list_2 - list_1,
                                        CustomList([-4, 1, 4, -7])))

        # проверка на неизменяемость
        self.assertTrue(list_comparison(list_1,
                                        CustomList(init_list_1)))
        self.assertTrue(list_comparison(list_2,
                                        CustomList(init_list_2)))

    def test_add_simple_and_custom(self):
        init_list = [6, 2, 4, 3]
        custom_list = CustomList(init_list)
        simple_list = [5, 1, 18]

        # сложение
        self.assertTrue(list_comparison(custom_list + simple_list,
                                        CustomList([11, 3, 22, 3])))
        self.assertTrue(list_comparison(simple_list + custom_list,
                                        CustomList([11, 3, 22, 3])))

        # вычитание
        self.assertTrue(list_comparison(custom_list - simple_list,
                                        CustomList([1, 1, -14, 3])))
        self.assertTrue(list_comparison(simple_list - custom_list,
                                        CustomList([-1, -1, 14, -3])))

        # проверка на неизменяемость
        self.assertTrue(list_comparison(custom_list, init_list))
        self.assertTrue(list_comparison(simple_list, [5, 1, 18]))

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('CustomList.__name__', '__main__'):
            self.assertEqual(main(), 'end of main')
        with patch('CustomList.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
