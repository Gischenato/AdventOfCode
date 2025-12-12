devices = {}

for line in open('in'):
    key, d = line.split(':')
    d = d.strip().split()
    devices[key] = set(d)
devices['out'] = set()

paths = {k: 0 for k in devices}

paths['svr'] = 1

print(paths)

def run(_paths, exclude = set()):
    add = True
    first_round = True
    while add:
        add = False
        new_paths = {k: 0 for k in devices}
        for k in paths:
            mult = _paths[k]
            if (k == 'out' or k in exclude) and not first_round:
                new_paths[k] += mult
                continue 
            if mult == 0: continue
            add = True
            for d in devices[k]:
                new_paths[d] += mult
        first_round = False
        _paths = new_paths.copy()
    return _paths

for i in range(3):
    paths = run(paths, exclude={'dac', 'fft'})
    if i == 2: break
    total_fft = paths['fft']
    total_dac = paths['dac']
    
    paths = {k: 0 for k in devices}
    paths['dac'] = total_dac
    paths['fft'] = total_fft

print(paths['out'])