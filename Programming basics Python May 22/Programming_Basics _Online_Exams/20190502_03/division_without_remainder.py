numbers_count = int(input())
p1 = 0
p2 = 0
p3 = 0
for number in range(numbers_count):
    temp_number = int(input())
    if temp_number % 2 == 0:
        p1 += 1
    if temp_number % 3 == 0:
        p2 += 1
    if temp_number % 4 == 0:
        p3 += 1

p1_percent = p1 / numbers_count * 100
p2_percent = p2 / numbers_count * 100
p3_percent = p3 / numbers_count * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")

# test input 10 680 2 600 200 800 799 199 46 128 65
# test input 3 3 6 9
