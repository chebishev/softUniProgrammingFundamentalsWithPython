count_numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range(count_numbers):
    value = int(input())
    if value < 200:
        p1 += 1
    elif value < 400:
        p2 += 1
    elif value < 600:
        p3 += 1
    elif value < 800:
        p4 += 1
    else:
        p5 += 1

p1_percent = (p1 / count_numbers) * 100
p2_percent = (p2 / count_numbers) * 100
p3_percent = (p3 / count_numbers) * 100
p4_percent = (p4 / count_numbers) * 100
p5_percent = (p5 / count_numbers) * 100


print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')


# test input 3 1 2 999
# test input 4 53 7 56 999
# test input 7 800 801 250 199 399 599 799
# test input 9 367 99 200 799 999 333 555 111 9
# test input 14 53 7 56 180 450 920 12 7 150 250 680 2 600 200
