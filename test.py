import unittest
from algo import Solution

solution_1 = Solution()
solution_1.read_file('input_data/career1.in')
solution_2 = Solution()
solution_2.read_file('input_data/career2.in')

max_experience_1 = solution_1.find_maximum_experience()
max_experience_2 = solution_2.find_maximum_experience()


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_experience_1, 12)

    def test_2(self):
        self.assertEqual(max_experience_2, 3)
