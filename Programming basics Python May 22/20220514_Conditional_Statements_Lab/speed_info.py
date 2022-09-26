speed = float(input())

if speed <= 10:
    print('slow')
elif speed <= 50:
        print('average')
elif speed <= 150:
    print('fast')
elif speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')

# test input 8
# test input 49.5
# test input 126
# test input 160
# test input 3500
