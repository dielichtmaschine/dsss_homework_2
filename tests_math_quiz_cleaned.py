import unittest
from math_quiz_cleaned import GetRandomNumberInRange, ChooseRandomOperator, CalculatePlusMinusMultiply


class TestMathGame(unittest.TestCase):

    def test_GetRandomNumberInRange(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10

        #Check if GetRandomNumberInRange() works
        try:
            TestGetRandomNumber = GetRandomNumberInRange(min_val, max_val)
        except:
            print("GetRandomNumberInRange() doesn't work")

        for _ in range(1000):  # Test a large number of random values
            rand_num = GetRandomNumberInRange(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_ChooseRandomOperator(self):
        ChooseOperatorOperatorCounter = [0, 0, 0]
        ChooseOperatorOperatorList = ['+', '-', '*']

        # Check if ChooseRandomOperator() works
        try:
            TestOperator = ChooseRandomOperator()
        except:
            self.assertTrue(0 == 1, "ChooseRandomOperator() doesn't work")



        # Try ChooseRandomOperator() 1000 times
        for i in range(1000):
            TestOperator = ChooseRandomOperator()
            self.assertTrue(TestOperator in ChooseOperatorOperatorList)
            ChooseOperatorOperatorCounter[ChooseOperatorOperatorList.index(TestOperator)] += 1

        self.assertTrue(min(ChooseOperatorOperatorCounter) > 20)

        pass

    def test_CalculatePlusMinusMultiply(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 5, '*', '7 * 5', 35),
                (6, 9, '-', '6 - 9', -3),
                (1, 3, '+', '1 + 3', 4),
                (4, 4, '*', '4 * 4', 16),
                (2, 8, '-', '2 - 8', - 6),
                (10, 3, '+', '10 + 3', 13),
                (8, 2, '*', '8 * 2', 16),
                (15, 7, '-', '15 - 7', 8),
                (3, 6, '+', '3 + 6', 9),
                (9, 9, '*', '9 * 9', 81)
            ]

            # Check if CalculatePlusMinusMultiply() works
            try:
                TestOperator = CalculatePlusMinusMultiply(test_cases[0][0], test_cases[0][1], test_cases[0][2])
            except:
                self.assertTrue(0 == 1, "CalculatePlusMinusMultiply() doesn't work")



            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                self.assertTrue(CalculatePlusMinusMultiply(num1, num2, operator) == (expected_problem, expected_answer))

            pass

if __name__ == "__main__":
    unittest.main()
