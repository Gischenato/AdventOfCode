def is_ok(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != 0:
            return False
    return True

tot = 0
for line in open('in'):
    all_sequences = []
    sequence = list(map(int, line.strip().split(' ')))
    all_sequences.append(sequence)
    
    new_sequence = []

    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        new_sequence.append(diff)

    all_sequences.append(new_sequence)

    while not is_ok(all_sequences[-1]):
        sequence = new_sequence
        new_sequence = []
        for i in range(len(sequence) - 1):
            diff = sequence[i + 1] - sequence[i]
            new_sequence.append(diff)
        all_sequences.append(new_sequence)



    start = True
    for i in range(len(all_sequences)-1, -1, -1):
        if start:
            start = False
            all_sequences[i].append(all_sequences[i][0])
            continue
        all_sequences[i].append(all_sequences[i][0] - all_sequences[i+1][-1])
        # print(f'{i}: {all_sequences[i]}')

    # print('---------------------------------')
    # for sequence in all_sequences:
    #     print(f'{sequence} => ', end='')
    # print()

    tot += all_sequences[0][-1]

print(tot)

