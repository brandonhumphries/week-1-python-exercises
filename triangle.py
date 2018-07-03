#counter = 0
height = 4
width = 7
counter = 0
while counter < height:
    spaces = " " * (((width +1) / 2) - (counter + 1))
    asterisks = ("*" * (width - (2 * (height - (counter + 1)))))
    triangle_line = spaces + asterisks + spaces
    print triangle_line
    counter += 1


trih = 4
t = 1
c = 1

while c <= 4:
    print ((" " * trih) + "*" * (t))
    t += 2
    c += 1
    trih -= 1



height = raw_input("Please enter a height for the triangle:" )
width = 1 + (2 * height)

for i in range(1, height):
    spaces = " " * 