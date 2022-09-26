country = input()
tool = input()

total_points = 0
percent_difference = 0
hardness = 0
performance = 0

if country == "Russia":
    if tool == "ribbon":
        hardness = 9.100
        performance = 9.400
    elif tool == "hoop":
        hardness = 9.300
        performance = 9.800
    else:
        hardness = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        hardness = 9.600
        performance = 9.400
    elif tool == "hoop":
        hardness = 9.550
        performance = 9.750
    else:
        hardness = 9.500
        performance = 9.400
else:
    if tool == "ribbon":
        hardness = 9.200
        performance = 9.500
    elif tool == "hoop":
        hardness = 9.450
        performance = 9.350
    else:
        hardness = 9.700
        performance = 9.150

total_points = hardness + performance
percent_difference = ((20 - total_points) / 20) * 100

print(f"The team of {country} get {total_points:.3f} on {tool}.")
print(f"{percent_difference:.2f}%")

# test input Bulgaria ribbon
# test input Russia rope
# test input Italy hoop
