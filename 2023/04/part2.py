tot = 0

cards = {}

test = 10
for line in open('in'):
    if test < 0: break
    card, numbers = line.strip().split(':')
    _, card = card.replace('  ',' ').replace('  ', ' ').split(' ')
    card = int(card)
    qnt = cards.get(card, 0) + 1

    winner, my_card = numbers.split('|')
    winner = set(winner.strip().replace('  ', ' ').split(' '))
    my_card = set(my_card.strip().replace('  ', ' ').split(' '))
    qnt_winner = len(winner.intersection(my_card))

    cards[card] = qnt
    if qnt_winner > 0:
        for i in range(qnt_winner):
            card += 1
            cards[card] = cards.get(card, 0) + qnt

print(sum(cards.values()))