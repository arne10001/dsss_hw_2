import unittest
from math_quiz import randomInteger, randomOperation, mathProblem


class TestMathGame(unittest.TestCase):

    def test_randomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randomOperation(self):
        # tests if the random operation is one of the specified operations (+,-,*)
        for _ in range(1000):
            operator = randomOperation()
            self.assertTrue(operator in ['+', '-', '*'])


    def test_mathProblem(self):
            test_cases = [(5, 2, '+', '5 + 2', 7)]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                expected_problem, expected_answer = mathProblem(num1, num2, operator)
                self.assertEqual(expected_problem, expected_problem)
                self.assertEqual(expected_answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
