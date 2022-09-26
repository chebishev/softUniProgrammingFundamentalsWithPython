serial_name = input()
seasons = int(input())
episodes = int(input())
duration = float(input())
special_episodes = seasons * 10
total = (seasons * episodes * duration) * 1.20 + special_episodes

print(f"Total time needed to watch the {serial_name} series is {int(total)} minutes.")

# test input Lucifer 3 18 55
# test input Game of Thrones 7 10 50
# test input Riverdale 3 21 45
