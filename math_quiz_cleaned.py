import random


def GetRandomNumberInRange(min, max):
    '''
    Returns a random Number (int) in range of min an max

    Parameters
    ----------
    min: int
        Minimum value for the random number

    max: int
        Maximum value for the random number

    Returns
    -------
    CalculatedNum: int
        Random number in range (min, max) calculated by randint()
    '''
    CalculatedNum = random.randint(min, max)
    return CalculatedNum


def ChooseRandomOperator():
    '''
        Returns a random Operator: +, - or *

        Returns
        -------
        Operator: int
            Random operator chosen by random.choice()
    '''
    Operator = random.choice(['+', '-', '*'])
    return Operator

def CalculatePlusMinusMultiply(num1, num2, operator):
    '''
        Calculates two numbers with the help of an operator

        Parameters
        ----------
        num1: int
            First number used for calculation

        num2: int
            Second number used for calculation

        operator: str
            Operator used for calculation

        Returns
        -------
        problem: str
            resembles the task as a message

        answer:
            gives the solution of the calculation

        '''

    # Illustrate the problem as a string
    problem = f"{num1} {operator} {num2}"

    # Calculate num1 and num2 based on the chosen operator
    if operator == '+': answer = num1 + num2
    elif operator == '-': answer = num1 - num2
    else: answer = num1 * num2

    return problem, answer

def math_quiz():
    score = 0
    NumberOfTasks = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(NumberOfTasks):
        n1 = GetRandomNumberInRange(1, 10)
        n2 = GetRandomNumberInRange(1, 10)
        o = ChooseRandomOperator()

        UserTask, UserInput = CalculatePlusMinusMultiply(n1, n2, o)
        print(f"\nQuestion: {UserTask}")
        useranswer = int(input("Your answer: "))

        if useranswer == UserInput:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {UserInput}.")

    print(f"\nGame over! Your score is: {score}/{NumberOfTasks}")

if __name__ == "__main__":
    #Execute the math quiz
    math_quiz()
