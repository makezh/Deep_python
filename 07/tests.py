import unittest
from unittest.mock import patch

from main import create_matrix, chain_mul, main


class MyTestCase(unittest.TestCase):
    def test_create_matrix(self):
        matrix2x2 = create_matrix((2, 2))
        matrix3x3 = create_matrix((3, 3))
        matrix5x3 = create_matrix((5, 3))
        self.assertEqual(matrix2x2.shape, (2, 2))
        self.assertEqual(matrix3x3.shape, (3, 3))
        self.assertEqual(matrix5x3.shape, (5, 3))

    def test_chain_mul(self):
        with self.assertRaises(ValueError):
            chain_mul(-4, 214)

        res1 = chain_mul(3, 3)
        res2 = chain_mul(5, 4)
        res3 = chain_mul(10, 5)
        self.assertEqual(res1.shape, (3, 3))
        self.assertEqual(res2.shape, (4, 4))
        self.assertEqual(res3.shape, (5, 5))

    @patch('builtins.print')
    def test_main(self, mock_print):
        with patch('main.__name__', '__main__'):
            self.assertEqual(main(), 'end of main')
        with patch('main.__name__', '__not_main__'):
            self.assertEqual(main(), 'just end')


if __name__ == '__main__':
    unittest.main()
