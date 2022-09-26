season = input()
group_type = input()
students = int(input())
nights = int(input())
sport = ''
price = 0

if season == "Summer":
    if group_type == "boys":
        sport = "Football"
    elif group_type == "girls":
        sport = "Volleyball"
    else:
        sport = "Swimming"
    if group_type != "mixed":
        price = nights * students * 15
    else:
        price = nights * students * 20
elif season == "Winter":
    if group_type == "boys":
        sport = "Judo"
    elif group_type == "girls":
        sport = "Gymnastics"
    else:
        sport = "Ski"
    if group_type != "mixed":
        price = nights * students * 9.60
    else:
        price = nights * students * 10
else:
    if group_type == "boys":
        sport = "Tennis"
    elif group_type == "girls":
        sport = "Athletics"
    else:
        sport = "Cycling"
    if group_type != "mixed":
        price = nights * students * 7.20
    else:
        price = nights * students * 9.50

if students >= 50:
    price *= 0.50
elif 20 <= students < 50:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

print(f'{sport} {price:.2f} lv.')

# test input Spring girls 20 7
# test input Winter mixed 9 15
# test input Summer boys 60 7
# test input Spring mixed 17 14
