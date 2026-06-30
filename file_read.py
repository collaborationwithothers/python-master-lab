file = open("README.md", "r")

with file:
    for line in file:
        print(line, end="")
        