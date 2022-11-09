data = input().split()
command = input().split()
while command[0] != "3:1":
    action = command[0]
    index = int(command[1])
    command_final = int(command[2])
    if action == "merge":
        data[index:command_final] = [''.join(data[index:command_final])]
    elif action == "divide":
        part_length = len(data[index]) // command_final
        current_string = data.pop(index)
        current_index = index
        splited_string = ""
        parts_counter = 1
        completed_parts = False
        for character in current_string:
            splited_string += character
            if completed_parts:
                splited_string += character
            if len(splited_string) == part_length:
                data.insert(current_index, splited_string)
                current_index += 1
                splited_string = ""
                parts_counter += 1
    command = input().split()
print(' '.join(data))

# 40/100

# test inputs:

# Ivo Johny Tony Bony Mony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1

# abcd efgh ijkl mnop qrst uvwx yz
# merge 4 10
# divide 4 5
# 3:1
