lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toy_counter = 0
saved_money = 0
brother_take = 0

for numbers in range(1, lily_age + 1):
    if numbers % 2 == 0:
        saved_money += numbers * 5
        brother_take += 1
    else:
        toy_counter += 1

toys_total = toy_price * toy_counter
total_money = saved_money - brother_take + toys_total

if total_money < washing_machine_price:
    print(f'No! {(washing_machine_price - total_money):.2f}')
else:
    print(f'Yes! {(total_money - washing_machine_price):.2f}')

# test input 10 170.00 6
# test input 21 1570.98 3
