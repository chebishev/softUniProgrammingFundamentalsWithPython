holidays = int(input())

working_days = 365 - holidays

play_norm = (working_days * 63) + (holidays * 127)
diff = abs(play_norm - 30000)
hours = diff // 60
minutes = diff % 60

if play_norm > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

# test input 20
# test input 113
