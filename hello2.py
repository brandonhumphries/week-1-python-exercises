name = raw_input('WHAT IS YOUR NAME? ')
length = len(name)
print "HELLO, " + name.upper() + "!"
print "YOUR NAME HAS " + str(length) + " LETTERS IN IT! AWESOME!"


name = raw_input('WHAT IS YOUR NAME? ')
upcased_name = name.upper()
length = len(name)
print "HELLO, %s!" % upcased_name
print "YOUR NAME HAS " + str(length) + " LETTERS IN IT! AWESOME!"
