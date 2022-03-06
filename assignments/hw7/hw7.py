"""
Name: Margaux Walz
hw7.py

Problem: Open, read, and write in files

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    wordnum = 0
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    text_in = in_file
    for line in in_file:
        for word in line.split():
            wordnum = wordnum + 1
            out_file.write(wordnum)
            out_file.write(word)
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    for line in in_file:
        for word in line.split():
            print(word)



def calc_check_sum(isbn):
    pass


def send_message(file_name, friend_name):
    f = open(file_name, "r")
    f1 = open(friend_name, "w")
    for line in f:
        f1.write(line)
    f.close()
    f1.close()

def encode():
    message = "hi"
    key = 0
    encrypt = ""
    for char in message:
        num = ord(char) + key
        encrypt += chr(num % 128)
    return encrypt



def send_safe_message(file_name, friend_name, key):
    from encryption import encode
    message = ""
    key = 0
    in_file = open(file_name, "r")
    out_file = open(friend_name, "w")
    text_1 = in_file.read()
    text_2 = text_1.split('\n')
    for line in text_2:
        message = line.rstrip()
        encrypted = encode(message, key)
        print(encrypted, file=out_file)
    in_file.close()
    out_file.close()



def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
