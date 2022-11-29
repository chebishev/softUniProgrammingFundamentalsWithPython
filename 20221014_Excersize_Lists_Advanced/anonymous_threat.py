import textwrap

data = input().split()
while True:

    command = input()
    if command == "3:1":
        print(' '.join(data))
        break

    command = command.split()
    action = command[0]

    if action == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        temp_string = ""
        if start_index < 0:
            start_index = 0
        if end_index >= len(data):
            end_index = len(data) - 1
        for index in range(start_index, end_index + 1):
            temp_string += data[index]
        for index in range(end_index, start_index - 1, -1):
            data.pop(index)
        data.insert(start_index, temp_string)

    elif action == "divide":
        index = int(command[1])
        partitions = int(command[2])
        piece_to_divide = data.pop(index)
        if len(piece_to_divide) / partitions == len(piece_to_divide) // partitions:
            temp_list = textwrap.wrap(piece_to_divide, len(piece_to_divide) // partitions)
        else:
            temp_list = textwrap.wrap(piece_to_divide, len(piece_to_divide) // partitions)
            temp_list[-2] = temp_list[-2] + temp_list[-1]
            temp_list.pop()

        for piece in range(len(temp_list) - 1, -1, -1):
            data.insert(index, temp_list[piece])

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
