degrees = float(input())

if 35.00 >= degrees >= 26.00:
    print("Hot")
elif 25.9 >= degrees >= 20.1:
    print("Warm")
elif 20.00 >= degrees >= 15.00:
    print("Mild")
elif 14.9 >= degrees >= 12.00:
    print("Cool")
elif 11.9 >= degrees >= 5.00:
    print("Cold")
else:
    print("unknown")

# test input 16.5
# test input 8
# test input 22.4
