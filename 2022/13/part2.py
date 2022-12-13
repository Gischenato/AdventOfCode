import json

def compare(val1, val2):
    if isinstance(val1, list) and isinstance(val2, list):
        for v1, v2 in zip(val1, val2):
            result = compare(v1, v2)
            if result == 0 or result == 1: return result
        size1 = len(val1)
        size2 = len(val2)
        if   size1 > size2: return 0
        elif size1 < size2: return 1
        return 2
    elif isinstance(val1, int) and isinstance(val2, int):
        if   val1 == val2: return 2
        elif val1 <  val2: return 1
        else: return 0
    else:
        if isinstance(val1, list): return compare(val1, [val2])
        if isinstance(val2, list): return compare([val1], val2)
    pass


#*# compare(val1, val2) Returns 0 if val1 >  val2
#*#                     Returns 1 if val2 >= val1
def partition(packets, start, end):
    pivot = packets[start]
    low = start+1
    high = end

    while True:
        while low <= high:
            ans = compare(pivot, packets[high])
            if ans == 1: break
            high -= 1

        while low <= high:
            ans = compare(pivot, packets[low])
            if ans == 0: break
            low += 1

        if low < high: packets[low], packets[high] = packets[high], packets[low]
        else: break
    packets[start], packets[high] = packets[high], packets[start]
    return high

def quickPacketsSort(packets, start, end, last_p=-1):
    if start >= end: return
    p = partition(packets, start, end)
    if p < 0 or p == 1: return
    quickPacketsSort(packets, start, p-1)
    quickPacketsSort(packets, p-1, end, last_p=p)

pacotes = []

for line in open('in'):
    if line == '\n': continue
    pacotes.append(json.loads(line))
pacotes.append([[2]])
pacotes.append([[6]])

for p in pacotes:
    print(p)
print('==================')
quickPacketsSort(pacotes, 0, len(pacotes)-1)


pos1, pos2 = 0,0
pacotes.reverse()
for i in range(len(pacotes)):
    p = pacotes[i]
    if p == [[2]]: pos1 = i+1
    elif p == [[6]]: pos2 = i+1
    print(p)

print(pos1,pos2)
print(pos1*pos2)