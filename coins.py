coins = 0
message = 'You have %d coins.' % coins
print message
another = raw_input("Do you want another? ")
while another.lower() == "yes":
    coins += 1
    print 'You have %d coins.' % coins
    another = raw_input("Do you want another? ")
print "Bye"