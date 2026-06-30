with open("write.txt", mode="wt") as file:
    file.write("This is a test file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is the last line.\n")

with open("write.txt", mode="r") as file:
    content = file.read()
    print(content)