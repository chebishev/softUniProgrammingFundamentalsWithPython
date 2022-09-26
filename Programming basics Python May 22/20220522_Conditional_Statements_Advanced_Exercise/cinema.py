ticket_type = input()
rows = int(input())
columns = int(input())
cinema_capacity = rows * columns
income = 0

if ticket_type == "Premiere":
    income = cinema_capacity * 12.00
elif ticket_type == "Normal":
    income = cinema_capacity * 7.50
else:
    income = cinema_capacity * 5.00

print(f'{income:.2f}')

# test input Premiere 10 12
# test input Normal 21 13
# test input Discount 12 30
