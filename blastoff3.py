starting_number = int(raw_input("Number to start counting from? "))
numbers = range(0, starting_number + 1)
counter = 0
while abs(counter) < len(numbers):
    print numbers[counter - 1]
    counter -= 1
    if (numbers[counter - 1]) == 0:
        print numbers[counter - 1]
        print "End of the line."
        counter -= 1