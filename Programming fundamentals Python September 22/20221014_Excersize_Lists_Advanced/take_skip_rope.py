initial_string = input()
numbers_list = []
non_numbers_list = []
take_list = []
skip_list = []
taken_string = ""
skipped_string = ""
for symbol in initial_string:
    if symbol.isdigit():
        numbers_list.append(int(symbol))
    else:
        non_numbers_list.append(symbol)

for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])

for index in range(len(take_list)):
    for taking in range(take_list[index]):
        taken_string += non_numbers_list.pop(0)
    for skipping in range(skip_list[index]):
        skipped_string += non_numbers_list.pop(0)
print(taken_string)

# test inputs:

# T2exs15ti23ng1_3cT1h3e0_Roppe

# O{1ne1T2021wf312o13Th111xreve!!@!

# this forbidden mess of an age rating 0127504740
