today_seats = [
    'Xavier',
    'Clinton',
    'Andrew',
    'Jimmy'
]

yesterday_seats = [
    'Xavier',
    'Andrew',
    'Clinton'
    'Jimmy'
]

#repeat a check:
#is the person in this seat different from yesterday?

current_row = 0


 while current_row < len(today_seats):
    if today_seats[current_row] == yesterday_seats[current_row]:
        print "Move to another seat, %s" % today_seats[current_row]
    current_row = current_row + 1


#generate lists
range()

for i in range(len(today_seats)):
    if today_seats[i] == yesterday_seats[i]:
        print "Move!"
