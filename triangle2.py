height = int(raw_input("Height? "))
counter = 0
width = (2 * height) - 1
while counter < height:
    spaces = " " * (((width +1) / 2) - (counter + 1))
    asterisks = ("*" * (width - (2 * (height - (counter + 1)))))
    triangle_line = spaces + asterisks + spaces
    print triangle_line
    counter += 1


#wide = (2 * row) - 1
#width = 2 * (height - 1) + 1