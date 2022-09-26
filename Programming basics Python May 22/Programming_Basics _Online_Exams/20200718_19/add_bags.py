luggage_over_twenty = float(input())
luggage_weight_in_kg = float(input())
days_to_trip = int(input())
luggage_count = int(input())
tax = 0

if luggage_weight_in_kg < 10:
    tax = luggage_over_twenty * 0.20
elif luggage_weight_in_kg <= 20:
    tax = luggage_over_twenty * 0.50
else:
    tax = luggage_over_twenty

if days_to_trip < 7:
    tax *= 1.40
elif days_to_trip <= 30:
    tax *= 1.15
else:
    tax *= 1.10

tax *= luggage_count

print(f"The total price of bags is: {tax:.2f} lv.")

# test input 30 18 15 2
# test input 25.50 5 36 6
# test input 63.80 23 3 1
