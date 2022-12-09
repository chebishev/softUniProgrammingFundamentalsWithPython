numbers_list = input().split()
step = int(input())
final_list = []
current_index = step - 1

while len(numbers_list) > 0:
    while current_index >= len(numbers_list):
        current_index -= len(numbers_list)
    replaced_index = numbers_list.pop(current_index)
    final_list.append(replaced_index)
    current_index += step - 1
print(f"[{','.join(final_list)}]")