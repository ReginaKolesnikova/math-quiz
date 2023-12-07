choose dificulty (Tase 1, Tase 2, Tase 3)
how much actions (+,-,*,/,**)
???????? ???????? ???????????? ?????

random tasks, depending on dificulty
check the answer (right,wrong)

how to leave cycle (amount of task on each level)

Hind
<60% - Hinne 2
60-75% - Hinne 3
75-90% - Hinne 4
>90% - Hinne 5

#??
print("Math Knowledge Test")
print("Difficulty and amount of tasks: ")
print("[1] - Easy, 3 tasks")
print("[2] - Medium, 5 tasks")
print("[3] - Hard, 10 tasks")
level=int(input("Choose difficulty: "))
if level in [1,2,3]:
  if level==1:
    print("Level 1")

import random
total = 3
correct = 0
nums = range(1,10)
for _ in range(total):
    ops = random.choice("+-*/**")
    a,b = random.choices(nums,k=2)
    while ops == "/" and (a%b != 0 or a<=b):
        a,b = random.choices(nums,k=2)
    while ops == "-" and a<b:
        a,b = random.choices(nums,k=2)
    result = askNum("What is {} {} {} = ".format(a,ops,b))
    corr = calc(a,ops,b)
    if  result == corr:
        correct += 1
        print("Correct")
    else:
        print("Wrong. Correct solution is: {} {} {} = {}".format(a,ops,b,corr))

print("You have {} out of {} correct.".format(correct,total))








#working version

print("Math Knowledge Test")
print("Difficulty and amount of tasks: ")
print("[1] - Easy, 3 tasks")
print("[2] - Medium, 5 tasks")
print("[3] - Hard, 10 tasks")
level=int(input("Choose difficulty: "))
if level in [1,2,3]:
  if level==1:
    print("Level 1")
    import random
total = 3
correct = 0
nums = range(1,10)
for _ in range(total):
    ops = random.choice("+-*/**")
    a,b = random.choices(nums,k=2)
    while ops == "/" and (a%b != 0 or a<=b):
        a,b = random.choices(nums,k=2)
    while ops == "-" and a<b:
        a,b = random.choices(nums,k=2)
    result = input("What is {} {} {} = ".format(a,ops,b))





#?
level=int(input("Choose difficulty: "))

if level==1:
  print("")

  if level==2:
    print("")

  if level==3:
    print("")

else: 
    print("This level does not exist")