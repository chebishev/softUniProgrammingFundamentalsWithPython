import re

string = input()
regex = r'\b([A-Z][a-z]+ [A-Z][a-z]*)'
searched_content = re.findall(regex, string)
print(*searched_content)

# test input:

# Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett
