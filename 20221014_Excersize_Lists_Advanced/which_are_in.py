string_list = input().split(", ")
list_for_check = input().split(", ")
final_list = []

for word in string_list:
    for item in list_for_check:
        if word in item:
            final_list.append(word)
            break

print(final_list)

# test inputs:

# arp, live, strong
# lively, alive, harp, sharp, armstrong

# tarp, mice, bull
# lively, alive, harp, sharp, armstrong
