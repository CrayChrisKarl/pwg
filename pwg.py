#       -- PASSWORD GENERATOR PROJECT --

#   CLI frendly with flags given by the argparse module. By defualt it will give you a randomly generated password with a length of 10 charachters.
#   If you want a longer (or shorter for any reason) you can specify a custom length as an argument.
#   This will contain both upper and lower case letters. To add complexity you will have to add flags from the list below.


#       -- FLAGS --

#   -h, --Help          Will display a MAN-like page. (Basically this intro part after some finishing touches. 
#   -n, --Numbers       Will add numbers to the password.
#   -s, --symbols    Will add symbols to the password.

import os
import random
import string
import math
import argparse


DEFAULT_LENGTH = 10
OPTIONAL_PERCENTAGE = 0.2


def main():
    args = get_comp()
    comp = calc_comp(args)
    unshuffled_pass = make_comp(comp)
    password = make_pass(unshuffled_pass)
    print(password)
    #os.system(f'echo "{password}" | pbcopy')
    

def get_comp():

    parser = argparse.ArgumentParser(prog="pwg", prefix_chars="-")
    length = parser.add_argument("Length", type=int, nargs="?", help="Length of your password")
    parser.add_argument("-n", "--numbers", action="store_true", help="Adds numbers to your password")
    parser.add_argument("-s", "--symbols", action="store_true", help="Adds special symbols to your password")
    args = parser.parse_args()

    password_args = []
    
    if args.Length == None:
        length = DEFAULT_LENGTH
        password_args.append(length)

    else:
        length = args.Length
        password_args.append(length)

    if args.numbers:
        password_args.append("num")

    if args.symbols:
        password_args.append("sym")

    return password_args

def calc_comp(args):

    length = args[0]
    comp = {}

    if "num" in args:
        numbers = length * OPTIONAL_PERCENTAGE

    else:
        numbers = 0

    if "sym" in args:
        symbols = length * OPTIONAL_PERCENTAGE

    else:
        symbols = 0

    letters = length - math.floor(numbers) - math.floor(symbols)

    comp.update({"letters" : letters})
    comp.update({"numbers" : numbers})
    comp.update({"symbols" : symbols})

    return comp

def make_comp(dictionary):

    unshuffled_password = ""

    letters = dictionary.get("letters")
    letters = get_letter(letters)
    unshuffled_password += letters

    if "numbers" in dictionary:

        numbers = dictionary.get("numbers")
        numbers = get_number(numbers)
        unshuffled_password += numbers

    if "symbols" in dictionary:

        symbols = dictionary.get("symbols")
        symbols = get_sym(symbols)
        unshuffled_password += symbols

    return unshuffled_password

def get_letter(length):
    
    letters = ""
    for _ in range(0, length):
        _ = random.choice(string.ascii_letters)
        letters += _

    return letters

def get_number(n):

    numbers = ""
    for _ in range(0, int(n)):
        _ = random.randint(0, 9)
        numbers += str(_)

    return numbers

def get_sym(n):

    symbols = ""
    for _ in range(0, int(n)):
        _ = random.choice(string.punctuation)
        symbols += _

    return symbols

def make_pass(password):

    shuffled_password = "".join(random.sample(password, len(password)))
    
    return shuffled_password

main()
