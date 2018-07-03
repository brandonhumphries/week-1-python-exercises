#Sum the numbers
def sum_the_numbers(list1):
    total = 0
    for number in list1:
        total += number
    return total


#Largest Number
def largest_number(list1):
    largest = list1[0]
    for i in range(len(list1)):
        if list1[i] > largest:
            largest = list1[i]
    return largest



#Smallest Number
def smallest_number(list1):
    smallest = list1[0]
    for i in range(len(list1)):
        if list1[i] < smallest:
            smallest = list1[i]
    return smallest



#Even Numbers
def even_numbers(list1):
    even_number_list = []
    for number in list1:
        if number % 2 == 0:
            even_number_list.append(number)
    return even_number_list



#Positive Numbers
def positive_numbers(list1):
    positive_number_list = []
    for number in list1:
        if number > 0:
            positive_number_list.append(number)
    return positive_number_list



#Multiply a list
def multiply_a_list(list1, factor):
    multiplied_list = []
    for number in list1:
        multiplied_list.append(number * factor)
    return multiplied_list



#Multiply Vectors
def multiply_vectors(list1, list2):
    product_vector = []
    for i in range(len(list1)):
        product_vector.append(list1[i] * list2[i])
    return product_vector


#Matrix Addition
def create_empty_matrix(width, height):
    result = []
    #Initialize the resulting matrix. Helps simplify code and reduce possible edge cases.
    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(0)
    return result


def add_matrices(m1, m2):
    height = len(m1)
    width = len(m1[0])
    matrix = create_empty_matrix(width, height)

    #Fill in the matrix
    for i in range(0, height):
        for j in range(0, width):
            cell1 = m1[i][j]
            cell2 = m2[i][j]

            matrix[i][j] = cell1 + cell2
    return matrix


#De-dup
def de_dup(list1):
    new_list = []
    for thing in list1:
        if thing not in new_list:
            new_list.append(thing)
    return new_list

#LeetSpeak
def leetspeak(sentence):
    ls1 = ["A", "E", "G", "I", "O", "S", "T"]
    ls2 = ["4", "3", "6", "1", "0", "5", "7"]
    leet_string = ""
    for char in sentence:
        if char.upper() in ls1:
            for j in range(len(ls1)):
                if char.upper() == ls1[j]:
                    leet_string += ls2[j]
        else:
            leet_string += char
    return leet_string

#Instructor LeetSpeak
def leet(paragraph):
    subs = {
        'A': '4',
        'E': '3',
        'G': '6',
        'I': '1',
        'O': '0',
        'S': '5',
        'T': '7'
    }
    new_paragraph = ''
    for letter in paragraph:
        upper = letter.upper()
        if upper in subs:
            letter = subs[letter]
        new_paragraph += letter
    
    return new_paragraph

sentence = 

#Word Breakdown
def sentence_breakdown(sentence):
    padded_sentence = sentence + ' '
    words = []
    curr_word = ''

    for char in padded_sentence:
        if char == ' ':
            words.append(curr_word)
            curr_word = ''
        else:
            curr_word += char
    return words

def word_count(sentence):
    word_count_dictionary = {}
    words_imported = sentence_breakdown(sentence)

    for word in words_imported:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else:
            word_count_dictionary[word] = 1

    return word_count_dictionary


#MadLib
def collect_madlib_responses():
    output_dictionary = {}
    output_dictionary[subject] = raw_input('What is your favorite subject? ')
    output_dictionary[hobby] = raw_input('What is your favorite hobby? ')
    return output_dictionary

def madlib(responses)

    return 'Your favorite subject is math!'

def do_the_things();
    responses = collect_madlib_responses()
    print madlib(responses)


listy = [1, 5, 2, 4, 1, 0, 2, 3]

listx = [1, 99, -3, 0, 3, -1003, 4, 7]

listz = ['apple', 'cheese', 'milk', 'cheese', 'bread', 'cheese']

largest_number(listx)

smallest_number(listx)

even_numbers(listx)

positive_numbers(listx)

multiply_a_list(listx, 2)

multiply_vectors(listx, listy)

de_dup(listz)

string = "Given A string, print the string uppercased."
print leetspeak(string)

sentence_example = 'to be or not to be'
print word_count(sentence_example)