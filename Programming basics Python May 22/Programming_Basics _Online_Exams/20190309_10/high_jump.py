final_goal = int(input())
current_goal = final_goal - 30
unsuccessful = 0
failed = False
jump_count = 0

while True:
    jump = int(input())
    jump_count += 1
    if jump > current_goal:

        if current_goal >= final_goal:
            break
        current_goal += 5
        unsuccessful = 0
    else:
        unsuccessful += 1

    if unsuccessful == 3:
        failed = True
        break

if not failed:
    print(f"Tihomir succeeded, he jumped over {current_goal}cm after {jump_count} jumps.")
else:
    print(f"Tihomir failed at {current_goal}cm after {jump_count} jumps.")

# test input 231 205 212 213 228 229 230 235
# test input 250 225 224 225 228 231 235 234 235
