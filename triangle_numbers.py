n_input = int(raw_input("How many triangles? "))
numbers = range(1, (n_input + 1))
counter = 0
while counter < len(numbers):
    formula = numbers[counter] * (numbers[counter] + 1) / 2
    print "Triangle %d: %d" % (numbers[counter], formula)
    counter += 1
