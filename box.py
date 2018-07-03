width = int(raw_input("Width? "))
height = int(raw_input("Height? "))
counter = 0
print "*" * width
while counter < (height - 2):
    print "*" + (" " * (width - 2)) + "*"
    counter += 1
print "*" * width

