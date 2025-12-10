from z3 import *

data = [x.split() for x in open('in').read().strip().split('\n')]

tot = 0

for line in data:
    entry, switches, outcome = list(line[0][1:-1]), line[1:-1], line[-1][1:-1]
    switches = [list(map(int,(l[1:-1].split(',')))) for l in switches]
    outcome = list(int(x) for x in outcome.split(','))
    start = [0 for _ in range(len(entry))]


    n = len(switches)
    m = len(outcome)
    
    x = [Int(f'x_{i}') for i in range(n)]
    s = Optimize()
    
    for xi in x:
        s.add(xi >= 0)
    
    for j in range(m):
        contributors = [If( BoolVal(True) , x[i], 0) for i in range(n) if j in switches[i]]
        if len(contributors) == 0:
            s.add(0 >= outcome[j] + 1)
        else:
            s.add(Sum(contributors) == outcome[j])

    total = Sum(x)
    s.minimize(total)

    if s.check() == sat:
        model = s.model()
        counts = [model[xi].as_long() for xi in x]
        print(counts, sum(counts))
        tot += sum(counts)
    else:
        print('Errado')


print(tot)
