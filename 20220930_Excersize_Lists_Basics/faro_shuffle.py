cards_list = input().split()
shuffles_count = int(input())
last_shuffle = []
half_list = len(cards_list) // 2
for shuffle in range(shuffles_count):
    for i in range(0, half_list):
        first_card, second_card = cards_list[i], cards_list[half_list+i]
        last_shuffle.append(first_card)
        last_shuffle.append(second_card)
    if shuffle < shuffles_count - 1:
        cards_list = last_shuffle
        last_shuffle = []
print(last_shuffle)

# test inputs:

# a b c d e f g h
# 5

# one two three four
# 3
