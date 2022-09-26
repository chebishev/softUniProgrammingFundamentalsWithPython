from math import ceil

tv_series = input()
episode_duration = int(input())
resting_time = int(input())

lunch_time = resting_time / 8
free_time = resting_time / 4
time_for_watching = resting_time - lunch_time - free_time
diff = abs(time_for_watching - episode_duration)
if time_for_watching >= episode_duration:
    print(f'You have enough time to watch {tv_series} and left with {ceil(diff)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {tv_series}, you need {ceil(diff)} more minutes. ')

# test input Game of Thrones 60 96
# test input Teen Wolf 48 60
