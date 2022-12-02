def check(my, opponent):
    change = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z' 
    }
    
    values = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    
    opponent = change[opponent]
    if my == opponent: return values[my] + 3
    if my == 'X' and opponent == 'Z': return values[my] + 6
    if my == 'Y' and opponent == 'X': return values[my] + 6
    if my == 'Z' and opponent == 'Y': return values[my] + 6
    return values[my]


def main():
    total = 0
    for line in open('in'):
        line = line.split()
        total += check(line[1], line[0])
    print(total)

main()