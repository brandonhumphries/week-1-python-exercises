x_numbers = range(1,11)
y_numbers = range(1,11)
current_number_x = 0
current_number_y = 0
while current_number_x < len(x_numbers):
    while current_number_y < len(y_numbers):
        z = x_numbers[current_number_x] * y_numbers[current_number_y]
        message = "%d x %d = %d" % (x_numbers[current_number_x], y_numbers[current_number_y], z)
        print message
        current_number_y += 1
    while current_number_y >= len(y_numbers):
        print "..."
        current_number_y = 0
        current_number_x += 1
            
