#Uppercase a string
string = "Given a string, print the string uppercased."
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
new_string = ""
for i in string:
    if i in lower_case:
        for k in range(len(lower_case)):
            if lower_case[k] == i:
                new_string += upper_case[k]
            # elif upper_case[k] == i:
            #     new_string += i
    else:
        new_string += i
print new_string

print ""
print ""

#Uppercase a string instructor answer
message = 'you shall NOT pass'
upcased = ''

lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for char in message:
    letter = char
    #Search through list of lowercase letters
    for i in range(len(lowercase)):
        lowerletter = [i]
        if lowerletter == char:
            letter = uppercase[i]
            break
    upcased = upcased + letter
print upcased
# one option
# for char in message:
#     letter = char
#     if char == 'a':
#         letter = 'A'
#     elif char = 'b':
#         letter = 'B'

#     upcased = upcased + char

print upcased

print ''
print ''

#Uppercase a string
# string = "Given a string, print the string uppercased."
# lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# new_string = ""
# for i in string:
#     if i in lower_case:
#     ##print i
#     ##print string[i]
# #    for j in string[i]:
#         for k in range(len(lower_case)):
#             ##for l in lower_case:
#             ##print k
#             if lower_case[k] == i:
#                 new_string += upper_case[k]
#             elif upper_case[k] == i:
#                 new_string += i
# #            elif i != lower_case[k]:
# #                new_string += i 
#             ##elif string[i] != lower_case[k] or string[i] != upper_case[i]:
#             ##    new_string += string[i]
#     else:
#         new_string += i
# print new_string
#     # #        if string[k] == lower_case[k]:
#     # #            new_string.append(lower_case[k])
#     # #print new_string
#     #     #print j
#     # #    if string[i] == lower_case[i]
#     # #print string[0]
#     # #    if string[i] != 
#     # #        append



#Capitalize a string
# string = "Given a string, print the string uppercased."
# capitalized = ""

# lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# for i in range(len(string)):
#     letter = string[i]
#     if string[i - 1] == " ":
#         for i in range(len(lowercase)):
#             lowerletter = lowercase[i]
#             if letter == lowerletter:
#                 letter == uppercase[i]
#                 break
#         capitalized = capitalized + letter
# print capitalized

statement = "Given a string, print the string uppercased."
new_string = ""
placeholder = ""

lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for j in range(len(statement)):
    for i in range(len(lowercase)):
        if j == statement[0]:
            if statement[j] == str(lowercase[i]):
                placeholder = lowercase[i]
                new_string += str(uppercase[i])
                break
        elif statement[j-1] == " ":
            if statement[j] == str(lowercase[i]):
                placeholder = lowercase[i]
                new_string += str(uppercase[i])
                break
        else:
            new_string += statement[j]
            break
        
print new_string
                

#Reverse a string
#for i in range(len(string)):
# string_reversed = ""
# counter = 0
# while abs(counter) < len(string):
#     counter -= 1
#     string_reversed += string[counter]
# print string_reversed

#string = "Given a string, print the string uppercased."
#print string[::-1]

print ''
print ''


#Leetspeak
# string = "Given A string, print the string uppercased."
# ls1 = ["A", "E", "G", "I", "O", "S", "T"]
# ls2 = ["4", "3", "6", "1", "0", "5", "7"]
# leet_string = ""
# for i in string:
#     if i in ls1:
#         for j in range(len(ls1)):
#             if i == ls1[j]:
#                 leet_string += ls2[j]
#     else:
#         leet_string += i
# print leet_string

string = "Given A string, print the string uppercased."
ls1 = ["A", "E", "G", "I", "O", "S", "T"]
ls2 = ["4", "3", "6", "1", "0", "5", "7"]
leet_string = ""
for char in string:
    letter = char
    for j in range(len(ls1)):
        if char.upper() == ls1[j]:
            letter = ls2[j]
            break
    leet_string += letter
print leet_string

string = "Given A string, print the string uppercased."
ls1 = ["A", "E", "G", "I", "O", "S", "T"]
ls2 = ["4", "3", "6", "1", "0", "5", "7"]
leet_string = ""
for char in string:
    if char.upper() in ls1:
        for j in range(len(ls1)):
            if char.upper() == ls1[j]:
                leet_string += ls2[j]
    else:
        leet_string += char
print leet_string

text = "Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements."
leet_text = ""
ls1 = ["A", "E", "G", "I", "O", "S", "T"]
ls2 = ["4", "3", "6", "1", "0", "5", "7"]

for char in text.upper():
    letter = char
    for i in range(len(ls1)):
        leetletter = ls1[i]
        if leetletter == char:
            letter = ls2[i]
            break
    leet_text = leet_text + letter
print leet_text

print ''
print ''

for char in message:
    letter = char
    #Search through list of lowercase letters
    for i in range(len(lowercase)):
        lowerletter = lowercase[i]
        if lowerletter == char:
            letter = uppercase[i]
            break
    upcased = upcased + letter
print upcased

print ""
print ""

#Long-long Vowels
# long_string = "Good"
# vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
# new_long_string = ""
# for i in range(len(long_string)):
#     for j in range(len(vowels)):
#         if long_string[i] == vowels[j]:
#             if long_string[i] == long_string[i-1]:
#                 new_long_string += (long_string[i]* 4)
#                 break
#         else:
#             new_long_string += long_string[i]
#             break
# print new_long_string


long_string = "Good"
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
new_long_string = ""
for i in range(len(long_string)):
    if long_string[i] in vowels:
        if long_string[i] == long_string[i-1]:
                new_long_string += (long_string[i]* 4)
        else:
            new_long_string += long_string[i]
    else:
        new_long_string += long_string[i]
print new_long_string

print ''
print ''


string = "Given a string, print the string uppercased."
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
new_string = ""
for i in string:
        for k in lower_case:
            #print string[i]
            if i == k:
                ind1 = lower_case.index(k)
                new_string += upper_case[ind1]
            #elif i == upper_case[k]:
            #    new_string += i
            else:
                new_string += i
print new_string


#Caesar Cipher
caesar_string = 'lbh zhfg hayrnea jung lbh unir yrnearq'
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ciphered_string = ''

for char in caesar_string:
    for i in range(len(lower_case)):
        letter = ''
        if lower_case[i] == char:
            i += 13
            if i > 25:
                i -= 26
            letter = lower_case[i]
            ciphered_string += letter
            break
        elif upper_case[i] == char:
            i += 13
            if i > 25:
                i -= 26
            letter = upper_case[i]
            ciphered_string += letter
            break
        elif char == ' ':
            letter = char
            ciphered_string += letter
            break
print ciphered_string