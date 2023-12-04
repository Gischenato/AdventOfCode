tot = 0
for line in open('ex'):
    qnt = {
        'blue': 14,
        'red': 12,
        'green': 13,
    }
    ok = True

    line = line.strip()
    game, colors = line.split(':')
    _, game = game.split(' ')
    bags = colors.split(';')
    for bag in bags:
        if not ok:
            break
        bag = bag.strip()
        curr = bag.split(',')
        for opt in curr:
            opt = opt.strip()

            n, color = opt.split(' ')
            n = int(n)
            if n > qnt[color]:
                ok = False
                break
    if ok:
        tot += int(game)


print(tot)