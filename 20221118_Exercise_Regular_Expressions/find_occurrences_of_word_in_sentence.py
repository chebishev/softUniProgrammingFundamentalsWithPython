import re

sentence = input()
word = input()
pattern = rf'\b{word}\b'
result = re.findall(pattern, sentence, re.IGNORECASE)
print(len(result))

# The waterfall was so high, that the child couldn't see its peak.
# the

# How do you plan on achieving that? How? How can you even think of that?
# how

# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there
