from collections import Counter

FIVE_KIND = 'five_kind'
FOUR_KIND = 'four_kind'
FULL_HOUSE = 'full_house'
THREE_KIND = 'three_kind'
TWO_PAIR = 'two_pair'
ONE_PAIR = 'one_pair'
HIGH_CARD = 'high_card'

COMBINATIONS_VALUES = {
    FIVE_KIND: 10,
    FOUR_KIND: 9,
    FULL_HOUSE: 8,
    THREE_KIND: 7,
    TWO_PAIR: 6,
    ONE_PAIR: 5,
    HIGH_CARD: 4
}

CARD_VALUES = {
    'J': 1,
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    'T': 10, 
    'Q': 11, 
    'K': 12, 
    'A': 13
}

INPUT = 'in'

lines = [(cards,int(bid)) for cards, bid in[line.strip().split(' ') for line in open(INPUT)]]

def order_hand(hands):
    return sorted(hands, key=lambda x: (
        COMBINATIONS_VALUES[check_hand(x[0])], 
        CARD_VALUES[x[0][0]],
        CARD_VALUES[x[0][1]],
        CARD_VALUES[x[0][2]],
        CARD_VALUES[x[0][3]],
        CARD_VALUES[x[0][4]]
        )
    )

def check_hand(hand):
    counter = Counter(hand)
    
    most_common = list(counter.most_common())

    qnt_of_jokers = hand.count('J')

    if most_common[0][1] == 5:
        return FIVE_KIND
    elif most_common[0][1] == 4:
        if qnt_of_jokers in [1, 4]:
            return FIVE_KIND
        return FOUR_KIND
    elif most_common[0][1] == 3 and most_common[1][1] == 2:
        if qnt_of_jokers == 1:
            return FOUR_KIND
        if qnt_of_jokers in [2, 3]:
            return FIVE_KIND
        return FULL_HOUSE
    elif most_common[0][1] == 3:
        if qnt_of_jokers in [1, 3]:
            return FOUR_KIND
        if qnt_of_jokers == 2:
            return FIVE_KIND
        return THREE_KIND
    elif most_common[0][1] == 2 and most_common[1][1] == 2:
        if qnt_of_jokers == 1:
            return FULL_HOUSE
        if qnt_of_jokers == 2:
            return FOUR_KIND
        return TWO_PAIR
    elif most_common[0][1] == 2:
        if qnt_of_jokers in [1, 2]:
            return THREE_KIND
        return ONE_PAIR
    else:
        if qnt_of_jokers == 1:
            return ONE_PAIR
        return HIGH_CARD


lines = order_hand(lines)

rank = 1
tot = 0
for x,y in lines:
    # print(f'{x}: ', end='')
    # print(f'{check_hand(x)}, {y} * {rank} = {y * rank}')
    # print('----')
    tot += y * rank
    rank += 1
print(tot)