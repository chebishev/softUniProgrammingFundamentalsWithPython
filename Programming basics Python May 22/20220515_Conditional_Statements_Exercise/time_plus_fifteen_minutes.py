hours = int(input())
minutes = int(input()) + 15

if minutes >= 60:
    hours += 1
    minutes -= 60

if hours > 23:
    hours -= 24

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')

# test input 1 46
# test input 0 01
# test input 11 08
# test input 12 49
# test input 23 59
