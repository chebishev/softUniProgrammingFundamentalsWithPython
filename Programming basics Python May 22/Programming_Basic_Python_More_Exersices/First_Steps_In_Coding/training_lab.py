length_cm = float(input()) * 100
width_cm = (float(input()) * 100) - 100

desks_count = width_cm // 70
rows_count = length_cm // 120

sits_count = (desks_count * rows_count) - 3

print(int(sits_count))

# test input 15 8.9
# test input 8.4 5.2
