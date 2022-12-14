sequence = [int(x) for x in input().split()]
average = sum(sequence) / len(sequence)
sequence = sorted(sequence, reverse=True)
while sequence:
    number = sequence[-1]
    if number <= average:
        sequence.pop()
    else:
        break
if sequence:
    for index in range(len(sequence)):
        print(sequence[index], end=" ")
        if index == 4:
            break
else:
    print("No")

# test inputs:

# 10 20 30 40 50

# 5 2 3 4 -10 30 40 50 20 50 60 60 51

# 1

# -1 -2 -3 -4 -5 -6
