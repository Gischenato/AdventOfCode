def meio(total, qnt):
     return int(round(total/qnt))

def soma(d):
     return (d*d + d)/2


X = [int(x) for x in open("input.txt").read().strip().split(',')]
X.sort()

best = 1e9
for med in range(max(X)):
     score = 0
     for x in X:
          d = abs(x-med)
          score += soma(d)
     if score < best:
          best = score

print(best)