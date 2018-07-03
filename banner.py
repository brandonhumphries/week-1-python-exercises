text = raw_input("Text? ")
text_length = len(text)
banner_length = text_length + 4
counter = 0
while counter < 3:
    if counter == 0:
        print "*" * banner_length
        counter += 1
    elif 0 < counter < 2:
        print "* " + text + " *"
        counter += 1
    else:
        print "*" * banner_length
        counter += 1