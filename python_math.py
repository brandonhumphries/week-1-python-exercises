tip_input = raw_input('Be honest, how much did you tip? ')
tip = float(tip_input)

bill_input = raw_input('How much was the bill? ')
bill = float(bill_input)

tip_ratio = tip / bill

#tip_ratio less than 0.10:
#  say "stingy!"
if tip_ratio < 0.10:
    print "stingy!"
#tip_ratio greater than 0.20:
#  say "generous!"
elif tip_ratio > 0.20:
    print "generous!"
#otherwise:
#  say "average."
else:
    print "average."