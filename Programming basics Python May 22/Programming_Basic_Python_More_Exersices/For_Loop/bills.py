billing_months = int(input())
electricity = 0

for numbers in range(billing_months):
    monthly_electricity = float(input())
    electricity += monthly_electricity

water_bill = 20 * billing_months
internet_bill = 15 * billing_months
others = (electricity + water_bill + internet_bill) * 1.20
average = (others + electricity + water_bill + internet_bill) / billing_months

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water_bill:.2f} lv')
print(f'Internet: {internet_bill:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')

# test input 5 68.63 89.25 132.53 93.53 63.22
# test input 8 123.54 231.54 140.23 100 122.4 430 178.52 64.2
