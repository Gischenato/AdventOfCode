tot = 0
for line in open('ex'):
    qnt = {
        'blue': 0,
        'red': 0,
        'green': 0,
    }
    line = line.strip()
    game, colors = line.split(':')
    _, game = game.split(' ')
    bags = colors.split(';')

    for bag in bags:
        bag = bag.strip()
        curr = bag.split(',')
        for opt in curr:
            opt = opt.strip()

            n, color = opt.split(' ')
            n = int(n)
            if n > qnt[color]:
                qnt[color] = n

    power = qnt['blue'] * qnt['red'] * qnt['green']
    tot += power

print(tot)