def check(opponent, case):
    winers = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }
    values = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    if case == 'X': # Lose
        return values[winers[opponent]]
    if case == 'Y': # Draw
        return values[opponent] + 3
    if case == 'Z': # Win
        return values[winers[winers[opponent]]] + 6

def main():
    total = 0
    for line in open('in'):
        line = line.split()
        total += check(line[0], line[1])
    print(total)

main()