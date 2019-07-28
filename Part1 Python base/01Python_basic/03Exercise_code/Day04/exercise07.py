import random

score = 0
for i in range(3):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    results = int(input((str(num1) + " + " +
                         str(num2) + " = ")))
    if results == num1 + num2:
        score += 10
    else:
        score -= 5

print(score)
