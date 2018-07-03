number = int(raw_input("Number? "))
numbers = range(1, number + 1)
counter = 0
factors = []
while counter < number:
    if (number % numbers[counter]) == 0:
        factors.append(numbers[counter])
        counter += 1
    else:
        counter += 1
print "The factors for %d are: %s" % (number, factors)