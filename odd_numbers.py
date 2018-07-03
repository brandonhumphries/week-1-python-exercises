numbers = range(1, 11)
current_number = 0
print numbers
while current_number < len(numbers):
    if (numbers[current_number] + 1) % 2 == 0:
        print numbers[current_number]
        current_number += 1
    else:    
        current_number += 1