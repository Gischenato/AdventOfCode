import re
tot = 0

n = "one two three four five six seven eight nine".split()
pattern = '(?=(' + '|'.join(n) + '|\\d))'

wordToNum = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
             'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

for line in open('in'):
    line = line.strip()
    
    print(line)
    numbers = re.findall(pattern, line)
    # print(numbers)
    n1 = numbers[0]
    n2 = numbers[-1]
    if n1 in wordToNum:
        n1 = wordToNum[n1]
    if n2 in wordToNum:
        n2 = wordToNum[n2]
    value = n1 + n2
    print(value)
    tot += int(value)

print(tot)