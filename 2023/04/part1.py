tot = 0

for line in open('in'):
    card, numbers = line.strip().split(':')
    winner, my_card = numbers.split('|')
    winner = set(winner.strip().replace('  ', ' ').split(' '))
    my_card = set(my_card.strip().replace('  ', ' ').split(' '))
    qnt_winner = len(winner.intersection(my_card))
    if qnt_winner > 0:
        tot += 2**(qnt_winner-1)

print(tot)