string_for_coding = input()
coded_string = ""
for character in range(len(string_for_coding)):
    coded_string += chr(ord(string_for_coding[character]) + 3)

print(coded_string)

# test inputs:

# Programming is cool!

# One year has 365 days.
