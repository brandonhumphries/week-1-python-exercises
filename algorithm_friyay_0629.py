# total = 0
# for number in range(1000):
#     if (number % 3 == 0) or (number % 5 == 0):
#         total += number

# print total



# last_fib = 1
# current_fib = 2
# total = 2
# while current_fib < 4000000:
#     next_fib = last_fib + current_fib
#     if next_fib % 2 == 0:
#         total += next_fib
#     last_fib = current_fib
#     current_fib = next_fib
# print total


giant_number = 600851475143
potential = 1

while potential < giant_number:
    potential += 1
    while (giant_number % potential == 0): # and (giant_number != 1):
        giant_number = giant_number / potential
      
print potential

#Prime Number Instructor Answer
number = 600851475143

remainder = number
factor = 2

while remainder != 1:
    if remainder % factor == 0:
        remainder /= factor #this is a short way to say remainder = remainder / factor
    else:
        factor += 1

print factor
