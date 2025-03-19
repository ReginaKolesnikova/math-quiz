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

# print("Math Knowledge Test")
# print("Difficulty and amount of tasks: ")
# print("[1] - Easy, 3 tasks")
# print("[2] - Medium, 5 tasks")
# print("[3] - Hard, 10 tasks")
# level=int(input("Choose difficulty: "))
# if level in [1,2,3]:
#   if level==1:
#     print("Level 1")
#     total = 3
#     correct = 0
#     nums = range(1,10)
#   for _ in range(total):
#     ops = random.choice("+-*/**")
#     a,b = random.choices(nums,k=2)
#     while ops == "/" and (a%b != 0 or a<=b):
#         a,b = random.choices(nums,k=2)
#     while ops == "-" and a<b:
#         a,b = random.choices(nums,k=2)
#     result = input("What is {} {} {} = ".format(a,ops,b))
#     corr = result.format(a,ops,b)
#     if  result == corr:
#         correct += 1
#         print("Correct")
#     else:
#         print("Wrong. Correct solution is: {} {} {} = {}".format(a,ops,b,corr))

# print("You have {} out of {} correct.".format(correct,total))




import random
import operator

def generate_question(difficulty):
    # Определим диапазон чисел и операторы в зависимости от сложности
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
        print("Неверная сложность!")
        return None

    # Генерация случайных чисел и операции
    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    operation = random.choice(operations)

    if operation == '/':
        # Для деления гарантируем, что делитель не равен 0 и результат будет целым числом
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
    print("Выберите сложность: 1 - Легкая, 2 - Средняя, 3 - Сложная")
    difficulty = int(input())

    print("Введите количество примеров:")
    num_questions = int(input())

    correct_answers = 0

    for _ in range(num_questions):
        question, correct_answer = generate_question(difficulty)
        print(f"Вопрос: {question}")
        user_answer = float(input("Ваш ответ: "))

        if user_answer == correct_answer:
            correct_answers += 1

    percentage = (correct_answers / num_questions) * 100
    print(f"Вы правильно ответили на {correct_answers} из {num_questions} вопросов.")
    print(f"Ваша оценка: {get_grade(percentage)} (Процент правильных ответов: {percentage:.2f}%)")

if __name__ == "__main__":
    math_test()

