import re

line = input()
pattern = r"([w]{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+)"

while line:
    link = re.findall(pattern, line)
    if link:
        print(link[0][0])
        line = input()
    else:
        line = input()

# test inputs:

# Join WebStars now for free, at www.web-stars.com
# You can also support our partners:
# Internet - www.internet.com
# WebSpiders - www.webspiders101.com
# Sentinel - www.sentinel.-ko

# Need information about cheap hotels in London?
# You can check us at www.london-hotels.co.uk !
# We provide the best services in London.
# Here are some reviews in some blogs:
# London Hotels are awesome! - www.indigo.bloggers.com
# I am very satisfied with their services - ww.ivan.bg
# Best Hotel Services! - www.rebel21.sedecrem.moc
