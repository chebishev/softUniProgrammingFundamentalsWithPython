number_of_cars = int(input())
car_dictionary = {}
for index in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    car_dictionary[car] = {}
    car_dictionary[car]["mileage"] = int(mileage)
    car_dictionary[car]["fuel"] = int(fuel)

while True:

    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    action = command[0]
    car = command[1]

    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > car_dictionary[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            car_dictionary[car]["fuel"] -= fuel
            car_dictionary[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car_dictionary[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            car_dictionary.pop(car)

    elif action == "Refuel":
        fuel = int(command[2])
        if car_dictionary[car]["fuel"] + fuel > 75:
            print(f"{car} refueled with {75 - car_dictionary[car]['fuel']} liters")
            car_dictionary[car]["fuel"] = 75
        else:
            car_dictionary[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        kilometers = int(command[2])
        car_dictionary[car]["mileage"] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
        if car_dictionary[car]["mileage"] < 10000:
            car_dictionary[car]["mileage"] = 10000

for car, stats in car_dictionary.items():
    current_fuel = 0
    for mileage, fuel in stats.items():
        current_fuel = fuel
    print(f"{car} -> Mileage: {car_dictionary[car]['mileage']} kms, Fuel in the tank: {current_fuel} lt.")

# test inputs:

# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop

# 4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop
