starting_number = int(raw_input('Start from: '))
ending_number = int(raw_input('End on: '))
current_number = 0

while starting_number > ending_number:
    print 'Please enter a number for "End on" that is less than the number for "Start from".'
    starting_number = int(raw_input('Start from: '))
    ending_number = int(raw_input("End on: "))

number_range = range(starting_number, (ending_number + 1))

while current_number < len(number_range):
    print number_range[current_number]
    current_number += 1