from itertools import combinations
numbers = [int(line.strip()) for line in open('in')]

SUM = 2020

for conjunto in combinations(numbers, 3):
    if sum(conjunto) == SUM:
        number1, number2, number3 = conjunto
        break

print(numbers)
print(number1, number2, number3)
print(number1 * number2 * number3)