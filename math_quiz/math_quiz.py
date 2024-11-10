import random


def randomInteger(min, max):
    #returns a random integer between min and max
    return random.randint(min, max)


def randomOperation():
    #returns a random math operation
    return random.choice(['+', '-', '*'])


def mathProblem(number1, number2, operator):
    #returns the math problem and the correct answer

    calculation = f"{number1} {operator} {number2}"
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    else:
        raise ValueError("Invalid operator")
    return calculation, result

def math_quiz():
    score = 0
    questionAmount = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(questionAmount):
        number1 = randomInteger(1, 10); number2 = randomInteger(1, 5); operator = randomOperation()

        PROBLEM, ANSWER = mathProblem(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{questionAmount}")

if __name__ == "__main__":
    math_quiz()