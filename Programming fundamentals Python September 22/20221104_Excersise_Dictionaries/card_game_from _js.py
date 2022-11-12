def cards_values(power, color):
    card_deck = {"1": 10, "2": 2, "3": 3, "4": 4,
                 "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                 "J": 11, "Q": 12, "K": 13, "A": 14}
    multipliers = {"S": 4, "H": 3, "D": 2, "C": 1}
    return card_deck[power] * multipliers[color]


initial_List = input().split(", ")
card_dict = {}
current_key = ""
for element in initial_List:
    if ":" in element:
        name, card = element.split(": ")
        current_key = name
        if name not in card_dict.keys():
            card_dict[name] = {}
        card_dict[name][card] = {}
    else:
        card_dict[current_key][element] = {}
for key, value in card_dict.items():
    total = 0
    for card in value:   # S -> 4, H-> 3, D -> 2, C -> 1
        total += cards_values(card[0], card[-1])
    print(f"{key}: {total}")

# test inputs:

# Peter: 2C, 4H, 9H, AS, QS, Tomas: 3H, 10S, JC, KD, 5S, 10S, Andrea: QH, QC, QS, QD, Tomas: 6H, 7S, KC, KD, 5S, 10C, Andrea: QH, QC, JS, JD, JC, Peter: JD, JD, JD, JD, JD, JD

# John: 2C, 4H, 9H, AS, QS, Slav: 3H, 10S, JC, KD, 5S, 10S, Alex: 6H, 7S, KC, KD, 5S, 10C, Thomas: QH, QC, JS, JD, JC, Slav: 6H, 7S, KC, KD, 5S, 10C, Thomas: QH, QC, JS, JD, JC, Alex: 6H, 7S, KC, KD, 5S, 10C, Thomas: QH, QC, JS, JD, JC, John: JD, JD, JD, JD