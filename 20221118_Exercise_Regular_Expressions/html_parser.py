import re

html_code = input()
title_pattern = r"<title>(.*)<\/title>"
body_pattern = r"<body>(.+)<\/body>"
title = re.findall(title_pattern, html_code)
print(f"Title: {title[0]}")
body_search = re.findall(body_pattern, html_code)
body = ""
tag_found = False
new_line = False
for char in body_search[0]:
    if tag_found:
        if char == ">":
            tag_found = False
            continue
        continue
    else:
        if char == "<":
            tag_found = True
            continue
        elif char == "\\":
            new_line = True
            continue
        if char == "n":
            if new_line:
                new_line = False
                continue
        body += char

print(f"Content: {body}")
