# Написать программу для проверки знаний по математике.
# Предложить пользователю выбрать сложность заданий.
# Например:
#     Tase 1, Tase 2, Tase 3
#     количество действий(+,-,/,*,**)
#     величину случайно генерируемых чисел.
# В программе случайным образом "задаются" примеры, с учетом сложности провряемых знаний.
# После введенного пользователем ответа, проверяется его правильностью.
# Придумать условие выхода из цикла.(можно сначала указать количество примеров)
# В конце работы программы, надо сообщить тестируемому оценку.
# <60% - Hinne 2
# 60-75% - Hinne 3
# 75-90% - Hinne 4
# >90% - Hinne 5
# import random

import random
import operator

def generate_question(difficulty):
    if difficulty == 1:
        min_value, max_value = 1, 10
        operations = ['+', '-']
    elif difficulty == 2:
        min_value, max_value = 1, 50
        operations = ['+', '-', '*']
    elif difficulty == 3:
        min_value, max_value = 1, 100
        operations = ['+', '-', '*', '/']
    else:
        print("Wrong difficulty")
        return None

    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    operation = random.choice(operations)

    if operation == '/':
        while num2 == 0 or num1 % num2 != 0:
            num2 = random.randint(min_value, max_value)

    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    
    return question, correct_answer

def get_grade(percentage):
    if percentage < 60:
        return 2
    elif percentage < 75:
        return 3
    elif percentage < 90:
        return 4
    else:
        return 5

def math_test():
    print("Difficulty: 1 - easy, 2 - medium, 3 - hard")
    difficulty = int(input())

    print("Number of questions:")
    num_questions = int(input())

    correct_answers = 0

    for _ in range(num_questions):
        question, correct_answer = generate_question(difficulty)
        print(f"Answer: {question}")
        user_answer = float(input("Your answer: "))

        if user_answer == correct_answer:
            correct_answers += 1

    percentage = (correct_answers / num_questions) * 100
    print(f"You answered correctly {correct_answers} times out of {num_questions} questions.")
    print(f"Your grade: {get_grade(percentage)} (Percentage of correct answers: {percentage:.2f}%)")

if __name__ == "__main__":
    math_test()

