import unittest
import calculator

class test_calculator(unittest.TestCase):
    def setUp(self):
        print('setup method execution...')

    def tearDown(self):
        print('tearDown method execution...')

    def test_add(self):
        self.assertEqual(calculator.add(4, 2), 6)
        with self.assertRaises(TypeError):
            calculator.add('a', 2)

    def test_sub(self):
            self.assertEqual(calculator.sub(4, 2), 2)
            with self.assertRaises(TypeError):
                calculator.sub('a', 2)

    def test_mul(self):
            self.assertEqual(calculator.mul(4, 2), 8)
            with self.assertRaises(TypeError):
                calculator.mul('a', b)

    def test_div(self):
            self.assertEqual(calculator.div(4, 2), 2)

            with self.assertRaises(ValueError):
                calculator.div(4, 0)

            with self.assertRaises(TypeError):
                calculator.div('a', 2)


if __name__ == '__main__':
    unittest.main()

