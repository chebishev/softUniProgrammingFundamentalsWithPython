import re

phone_numbers = input()
match_result = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
result = re.findall(match_result, phone_numbers)
print(', '.join(result))

# test inputs:

# +359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222

# +359 2 222 2222, +359-2-222-2222
