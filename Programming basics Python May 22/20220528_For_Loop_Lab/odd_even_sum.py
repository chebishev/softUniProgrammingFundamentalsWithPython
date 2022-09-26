count_numbers = int(input())
odd_sum = 0
even_sum = 0

for numbers in range(1, count_numbers+1):
    current_number = int(input())
    if numbers % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    diff = abs(odd_sum-even_sum)
    print("No")
    print(f"Diff = {diff}")

# test input 4 10 50 60 20
# test input 4 3 5 1 -2
# test input 3 5 8 1
