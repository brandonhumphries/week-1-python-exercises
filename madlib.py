print "Please fill in the blanks below:"
print "___(name)___ likes to play ___(sport)___"
name = raw_input("What is name? ")
sport = raw_input("What is sport? ")
print name + " likes to play " + sport + "."


print "Please fill in the blanks below:"
print "___(name)___ likes to play ___(sport)___"
name = raw_input("What is name? ")
sport = raw_input("What is sport? ")
template = "%s likes to play %s."
message = template % (name, sport)
print message