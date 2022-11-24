list_of_numbers = input().split()
final_list = []
index = 0
while len(final_list) != 2:
    for number in range(2):
        current_first_number = int(list_of_numbers[index])
        index += 1
        current_second_number = int(list_of_numbers[index])
        current_sum = current_first_number + current_second_number
        final_list.append(current_sum)
    if len(final_list) > 2:
        list_of_numbers = final_list
        index = 0
        continue
    if len(final_list) == 2:
        print(sum(final_list))
        break

# For this release IT WORKS ONLY WITH INPUT OF 3 NUMBERS
