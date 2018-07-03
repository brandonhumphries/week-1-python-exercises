bill = float(raw_input("Total bill amount? "))
# may be better to start off with bill_input to indicate this is input
#next line, you would then create bill to convert to float()
level_of_service = raw_input("Level of service? ")

if level_of_service.lower() == "good":
    tip = bill * 0.20
elif level_of_service.lower() == "fair":
    tip = bill * 0.15
elif level_of_service.lower() == "bad":
    tip = bill * 0.10
    
total = bill + tip
print "Tip amount: $%.2f" % tip
print "Total amount: $%.2f" % total


#instructor's coding
#bill_input = raw_input("Total bill amount? ")
#bill = float(bill_input)
#service = raw_input("Level of service? ")

#tip_percent = 0

#if service == "good":
#    tip_percent = 0.2
#elif service == "fair":
#    tip_percent = 0.15
#elif service = "bad":
#    tip_percent = 0.10

#tip_amount = bill * tip_percent
#print tip_amount

#total = bill + tip_amount
#print total