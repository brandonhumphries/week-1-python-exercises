numbers = range(0,11)
counter = 0
while abs(counter) < len(numbers):
    print numbers[counter - 1]
    counter -= 1
    if numbers[counter - 1] == 0:
        print numbers[counter - 1]
        print "End of the line."
        counter -= 1