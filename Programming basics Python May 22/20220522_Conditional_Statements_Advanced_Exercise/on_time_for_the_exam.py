exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_all_min = (exam_hour * 60) + exam_minutes
arrival_all_min = (arrival_hour * 60) + arrival_minutes

diff = abs(arrival_all_min - exam_all_min)

if arrival_all_min > exam_all_min:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hour = diff // 60
        minute = diff % 60
        if minute < 10:
            print(f'{hour}:0{minute} hours after the start')
        else:
            print(f'{hour}:{minute} hours after the start')
elif arrival_all_min == exam_all_min or diff <= 30:
    print("On Time")
    if diff >= 1:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        hour = diff // 60
        minute = diff % 60
        if minute < 10:
            print(f"{hour}:0{minute} hours before the start")
        else:
            print(f"{hour}:{minute} hours before the start")

# test input 9 30 9 50
# test input 9 00 8 30
# test input 16 00 15 00
# test input 9 00 10 30
# test input 14 00 13 55
# test input 11 30 8 12
# test input 10 00 10 00
# test input 11 30 10 55
# test input 11 30 12 29
