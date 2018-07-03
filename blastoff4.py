starting_number = int(raw_input("Number under 21 to start counting from? "))
counter = 0
while starting_number > 20:
    starting_number = int(raw_input("Number under 21 to start counting from? "))
numbers = range(0, starting_number + 1)
while abs(counter) < len(numbers):
    print numbers[counter - 1]
    counter -= 1
    if numbers[counter - 1] == 0:
        print numbers[counter - 1]
        print "End of the line."
        counter -= 1