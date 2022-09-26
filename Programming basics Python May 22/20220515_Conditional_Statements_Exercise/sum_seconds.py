time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')

# test input 35 45 44
# test input 22 7 34
# test input 50 50 49
# test input 14 12 10
