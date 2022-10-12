import unittest
from Metaclass import CustomClass


class MyTestCase(unittest.TestCase):
    def test_integrated_attrs(self):
        inst = CustomClass()
        self.assertEqual(hasattr(inst, 'x'), False)
        self.assertEqual(hasattr(inst, 'val'), False)
        self.assertEqual(hasattr(inst, 'line'), False)

        self.assertEqual(hasattr(inst, 'custom_val'), True)
        self.assertEqual(inst.custom_val, 99)

        self.assertEqual(hasattr(inst, 'custom_x'), True)
        self.assertEqual(inst.custom_x, 50)

        self.assertEqual(hasattr(inst, 'custom_line'), True)
        self.assertEqual(inst.custom_line(), 'Line: Custom_by_metaclass')

        self.assertEqual(str(inst), 'Custom_by_metaclass')

    def test_new_attrs(self):
        inst = CustomClass()
        inst.test = 'testing...'
        self.assertEqual(hasattr(inst, 'test'), False)
        self.assertEqual(hasattr(inst, 'custom_test'), True)
        self.assertEqual(inst.custom_test, 'testing...')


if __name__ == '__main__':
    unittest.main()
