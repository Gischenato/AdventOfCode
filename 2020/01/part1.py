numbers = sorted([int(line.strip()) for line in open('in')])

SUM = 2020

number1 = 0
number2 = 0

for i in range(len(numbers)):
    current = numbers[i]
    if current * 2 > SUM:
        break
    
    for j in range(i + 1, len(numbers)):
        other = numbers[j]
        if current + other > SUM: break
        if current + other == SUM:
            number1 = current
            number2 = other
            break



print(numbers)
print(number1, number2)
print(number1 * number2)