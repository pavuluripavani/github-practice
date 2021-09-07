import student
import unittest

s1 = student.student()


class test_student(unittest.TestCase):

    def setUp(self):
        print('setup method execution...')

    def tearDown(self):
        print('tearDown method execution...')

    def test_totalmarks(self):
        self.assertAlmostEqual(s1.total(5, 5, 5), 15)

        with self.assertRaises(TypeError):
            s1.total('a', 6, 4)

    def test_average(self):
        self.assertAlmostEqual(s1.average(5, 5, 5), 5)

        with self.assertRaises(TypeError):
            s1.average('a', 6, 4)


if __name__=='__main__':
    unittest.main()
