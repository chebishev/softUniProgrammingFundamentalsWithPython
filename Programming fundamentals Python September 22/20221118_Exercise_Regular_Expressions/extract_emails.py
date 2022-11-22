import re

sentence = input()
pattern = r"\s([a-z0-9]+[a-z0-9\.\-\_]*@([a-z-]+)+(\.[a-z]+)+)\b"
emails = re.findall(pattern, sentence)
for email in emails:
    print(email[0])

# test inputs:

# Please contact us at: support@github.com.

# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.

# Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –-
# steve.parker@softuni.de.
