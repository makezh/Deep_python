import unittest
from unittest.mock import patch
from Descriptor import Data, main


class MyTestCase(unittest.TestCase):
    def test_without_mistakes(self):

        data = Data()
        self.assertEqual(str(data), '#1, name = base, price = 1$')
        data.name = 'new gift'
        data.num = 13
        data.price = 150
        self.assertEqual(str(data), '#13, name = new gift, price = 150$')

    def test_type_errors(self):
        data = Data()
        with self.assertRaises(TypeError):
            data.num = 1.1
        with self.assertRaises(TypeError):
            data.price = -12
        with self.assertRaises(TypeError):
            data.name = 31

    def test_attr_errors(self):
        data = Data()
        del data.price
        del data.num
        del data.name
        with self.assertRaises(AttributeError):
            del data.price
        with self.assertRaises(AttributeError):
            del data.num
        with self.assertRaises(AttributeError):
            del data.name

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('Descriptor.__name__', '__main__'):
            self.assertEqual(main(), 'end of main')
        with patch('Descriptor.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
