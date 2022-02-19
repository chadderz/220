"""
Name: Margaux Walz
hw5.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    first, last = [], []
    name = input("enter a name (first last)")
    splitname = name.split()
    for i in splitname:
        first.append(i[0])
        last.append(i[1])
        print(last, first)


def company_name():
    domain = input("enter a domain: ")
    domain.split('.')
    for name in domain:
        print(name[2])


def initials():
    count = 0
    num_names = eval(input("how many students are in the class? "))
    for i in range(num_names):
        count = count + 1
        name_student = input("what is the name of student {}?".format(count))
        list1 = name_student.split(" ")
        ini = " "
        for name in list1:
            ini += name[0]
        print(ini)


def names():
    name_list = input("enter a list of names: ")
    name_split = name_list.split(" ")
    ini = " "
    for name in name_split:
        ini += name[0]
    print(ini, end=" ")


def thirds():
    count = 0
    terms = (eval(input("enter the number of sentences:")))
    printed = []
    for i in range(terms):
        count = count + 1
        sentence = input("enter sentence {}:".format(count))
        for m in range(0, len(sentence), 3):
            third = sentence[m]
            printed.append(third)
    print(' '.join(printed))


def word_average():
    sum_letters = 0
    sentence = input("enter a sentence:")
    spaces = sentence.count(" ")
    num_words = spaces + 1
    splitsentence = sentence.split(" ")
    length = len(splitsentence)
    for i in range(num_words+1):
        sum_letters += length
    average = sum_letters / num_words
    print(average)


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")
    split_sentence = sentence.split(" ")
    for i in split_sentence:
        i1 = i[0]
        stripped = i.lstrip(i1)
        print(stripped + i1, end="ay ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
