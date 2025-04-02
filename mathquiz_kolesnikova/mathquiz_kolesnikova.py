# Предложить пользователю выбрать сложность заданий.
# Например:
# easy 1, medium 2, hard 3
# количество действий(+,-,/,*,**)
# величину случайно генерируемых чисел.

# В программе случайным образом задаются примеры, с учетом сложности провряемых знаний.
# После введенного пользователем ответа, проверяется его правильностью.

# Придумать условие выхода из цикла.(можно сначала указать количество примеров)

# В конце работы программы, надо сообщить тестируемому оценку.
# <60% - result 2
# 60-75% - result 3
# 75-90% - result 4
# >90% - result 5




import random

def generate_question(difficulty):
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])
    elif difficulty == 'medium':
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
    elif difficulty == 'hard':
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(['+', '-', '*', '/'])
   
    if operation == '/':
        while num2 == 0:
            num2 = random.randint(1, 20)
        answer = num1 / num2
    elif operation == '**':
        answer = num1 ** num2
    else:
        answer = eval(f"{num1} {operation} {num2}")
   
    return f"{num1} {operation} {num2}", answer

def evaluate_score(correct_answers, total_questions):
    percentage = (correct_answers / total_questions) * 100
    if percentage < 60:
        return 2
    elif percentage < 75:
        return 3
    elif percentage < 90:
        return 4
    else:
        return 5

def math_test():
    print("Math test")

    difficulty = input("Choose difficulty: easy - 1, medium - 2, hard - 3: ").strip().lower()
    if difficulty == '1':
        difficulty = 'easy'
    elif difficulty == '2':
        difficulty = 'medium'
    elif difficulty == '3':
        difficulty = 'hard'
    else:
        print("Wrong data. Medium difficulty has been chosen for you instead..")
        difficulty = 'medium'

    num_questions = int(input("Amount of quetions: "))
   
    correct_answers = 0
   

    for i in range(num_questions):
        question, correct_answer = generate_question(difficulty)
        print(f"Solve {i+1}: {question} = ?")
        try:
            user_answer = float(input("Answer: "))
            if user_answer == correct_answer:
                print("Correct")
                correct_answers += 1
            else:
                print(f"Incorrect. Right answer is: {correct_answer}")
        except ValueError:
            print("Wrong data. Try again.")
   
    
    print(f"\nYou got {correct_answers} correct answers out of {num_questions}.")
    percentage = (correct_answers / num_questions) * 100
    print(f"Percentage of correct answers is: {percentage:.2f}%")

if __name__ == "__main__":
   math_test()



