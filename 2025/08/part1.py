from colorama import Fore, Style

open_file = 'in'
iterations = 10 if open_file == 'ex' else 1000

data = [list(map(int, l.split(','))) for l in open(open_file).read().strip().split('\n')]

distances = []

for i, p1 in enumerate(data):
    for j, p2 in enumerate(data):
        if i > j:
            x1,y1,z1 = p1
            x2,y2,z2 = p2
            distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            distances.append((distance, i, j))

distances = sorted(distances)

groups = []

for n, p in enumerate(distances):
    if n == iterations:
        break
    distance, p1, p2 = p
    print(f'{Fore.CYAN}Connecting points {Fore.RED}{p1}{Style.RESET_ALL} -> {Fore.RED}{p2}{Style.RESET_ALL}: {Fore.YELLOW}{distance}{Style.RESET_ALL}')
    for i, group in enumerate(groups):
        if p1 in group or p2 in group:
            group.add(p1)
            group.add(p2)
            print(f' {Fore.BLUE} Added to existing group: {Fore.GREEN}{i}{Style.RESET_ALL}')
            # merge groups if necessary
            for j, other_group in enumerate(groups):
                if j != i and (p1 in other_group or p2 in other_group):
                    group.update(other_group)
                    print(f' {Fore.WHITE} Merged with group {Fore.GREEN}{j}{Style.RESET_ALL}')
                    groups.remove(other_group)
            break
    else:
        groups.append(set([p1, p2]))
        print(f' {Fore.MAGENTA} Created new group {Fore.GREEN}{len(groups)-1}{Style.RESET_ALL}')

groups.sort(key=lambda x: len(x), reverse=True)

print(f'{Fore.YELLOW}Total groups formed: {len(groups)}{Style.RESET_ALL}')
for i, group in enumerate(groups):
    print(f' Group {Fore.GREEN}{i}{Style.RESET_ALL}: Size {Fore.YELLOW}{len(group)}{Style.RESET_ALL}')
    
import math

total = math.prod([len(group) for group in groups[:3]])
print(f'{Fore.CYAN}Product of sizes of the three largest groups: {Fore.MAGENTA}{total}{Style.RESET_ALL}')