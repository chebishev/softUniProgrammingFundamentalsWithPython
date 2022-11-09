numbers_count = int(input())

for _ in range(numbers_count):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")

# test inputs
# 2
# 12
# 286

# 5
# 2
# 9