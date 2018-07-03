bill = float(raw_input("Total bill amount? "))
level_of_service = raw_input("Level of service? ")
split = float(raw_input("Split how many ways? "))

if level_of_service.lower() == "good":
    tip = bill * 0.20
elif level_of_service.lower() == "fair":
    tip = bill * 0.15
elif level_of_service.lower() == "bad":
    tip = bill * 0.10
    
total = bill + tip
amount_per_person = total / split
print "Tip amount: $%.2f" % tip
print "Total amount: $%.2f" % total
print "Amount per person: $%.2f" % amount_per_person
