days_of_the_trip = int(input())
budget = float(input())
number_of_people = int(input())
price_fuel_kilometer = float(input())
food_expenses = float(input())
price_for_room = float(input())

current_expenses = 0

if number_of_people > 10:
    price_for_room *= 0.75

current_expenses += (price_for_room + food_expenses) * number_of_people * days_of_the_trip

for day in range(1, days_of_the_trip + 1):
    distance = float(input())

    expenses_for_traveled_kilometers = distance * price_fuel_kilometer
    current_expenses += expenses_for_traveled_kilometers

    if day % 3 == 0 or day % 5 == 0:
        current_expenses += current_expenses * 0.40

    if day % 7 == 0:
        current_expenses -= current_expenses / number_of_people

    if current_expenses > budget:
        print(f"Not enough money to continue the trip. You need {current_expenses - budget:.2f}$ more.")
        break

if budget >= current_expenses:
    print(f"You have reached the destination. You have {budget - current_expenses:.2f}$ budget left.")