number_of_electrons = int(input())
index = 1
shell = []
while True:
    current_free_shell = 2 * (index * index)
    if current_free_shell < number_of_electrons:
        shell.append(current_free_shell)
        number_of_electrons -= current_free_shell
    else:
        shell.append(number_of_electrons)
        break
    index += 1

print(shell)

# test inputs:

# 10

# 44
