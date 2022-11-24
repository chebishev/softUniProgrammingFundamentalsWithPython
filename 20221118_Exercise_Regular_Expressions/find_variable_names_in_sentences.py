import re

sentence = input()
variable_list = []
searched_match = r"\s_([a-zA-Z0-9]+)\b"
result = re.findall(searched_match, sentence)
for variable in result:
    variable_list.append(variable)
print(",".join(variable_list))

# test inputs:

# The _id and _age variables are both integers.

# Calculate the _area of the _perfectRectangle object.

# __invalidVariable _evenMoreInvalidVariable_ _validVariable
