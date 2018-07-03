width = int(raw_input("Width? "))
height = int(raw_input("Height? "))
counter = 0
while counter <= height:
    if counter == 0 or counter == height:
        print "*" * width
        counter += 1
    else:
        print "*" + (" " * (width - 2)) + "*"
        counter += 1



