import sys

number = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
odd_count = 0
even_count = 0

if number == 0:
    odd_min = 0
    odd_max = 0
    even_min = 0
    even_max = 0
else:
    for numbers in range(1, number + 1):
        temp_number = float(input())
        if numbers % 2 == 0:
            even_sum += temp_number
            even_count += 1
            if temp_number > even_max:
                even_max = temp_number
            if temp_number < even_min:
                even_min = temp_number
        else:
            odd_sum += temp_number
            odd_count += 1
            if temp_number > odd_max:
                odd_max = temp_number
            if temp_number < odd_min:
                odd_min = temp_number

print(f"OddSum={odd_sum:.2f},")
if odd_min == 0:
    print('OddMin=No,')
elif odd_count == 1:
    print(f"OddMin={odd_sum:.2f},")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == 0:
    print('OddMax=No,')
elif odd_count == 1:
    print(f'OddMax={odd_sum:.2f},')
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == 0:
    print('EvenMin=No,')
elif even_count == 0:
    print('EvenMin=No,')
elif even_count == 1:
    print(f'EvenMin={even_sum:.2f},')
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == 0:
    print('EvenMax=No')
elif even_count == 0:
    print('EvenMax=No')
elif even_count == 1:
    print(f'EvenMax={even_sum:.2f}')
else:
    print(f"EvenMax={even_max:.2f}")

# test input 6 2 3 5 4 2 1
# test input 2 1.5 -2.5
# test input 1 1
# test input 0
# test input 5 3 -2 8 11 -3
# test input 4 1.5 1.75 1.5 1.75
# test input 1 -5
# test input 3 -1 -2 -3
