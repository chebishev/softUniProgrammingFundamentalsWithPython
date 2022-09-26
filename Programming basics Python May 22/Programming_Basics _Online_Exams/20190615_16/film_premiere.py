movie = input()
menu_option = input()
tickets_count = int(input())
price_for_menu_option = 0
if movie == "John Wick":
    if menu_option == "Drink":
        price_for_menu_option = 12
    elif menu_option == "Popcorn":
        price_for_menu_option = 15
    else:
        price_for_menu_option = 19
elif movie == "Star Wars":
    if menu_option == "Drink":
        price_for_menu_option = 18
    elif menu_option == "Popcorn":
        price_for_menu_option = 25
    else:
        price_for_menu_option = 30
else:
    if menu_option == "Drink":
        price_for_menu_option = 9
    elif menu_option == "Popcorn":
        price_for_menu_option = 11
    else:
        price_for_menu_option = 14

total = tickets_count * price_for_menu_option
if movie == "Star Wars" and tickets_count >= 4:
    total *= 0.70

if tickets_count == 2 and movie == "Jumanji":
    total *= 0.85

print(f"Your bill is {total:.2f} leva.")

# test input John Wick Drink 6
# test input Star Wars Popcorn 4
# test input Jumanji Menu 2
