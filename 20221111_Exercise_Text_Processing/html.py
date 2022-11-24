print(f"<h1>\n\t{input()}\n</h1>")
print(f"<article>\n\t{input()}\n</article>")
command = input()
while command != "end of comments":
    print(f"<div>\n\t{command}\n</div>")
    command = input()

# test input:

# SoftUni Article
# Some content of the SoftUni article
# some comment
# more comment
# last comment
# end of comments
