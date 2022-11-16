import random
import string

import pyperclip

let_low_case = list(string.ascii_lowercase)
let_up_case = list(string.ascii_uppercase)
mark_case = [".", ",", ";", "?", "!", "+", "&"]


def crepw():
    maxes = menu()
    spechar = 0
    if len(maxes) == 6:
        spechar = 5
    pw = []
    number_total = 0  # total numbers used in this password.
    letter_total = 0  # total letters used in this password.
    mark_total = 0  # total special characters used in this password
    for i in range(maxes[0]):
        lonom = random.randint(0, 7)  # what will this step be.

        if lonom == 0 or lonom == 4 or lonom == 7:  # this step will be number if total haven't reached its maximum
            if number_total >= maxes[1]:
                continue
            else:
                this_step = str(random.randint(0, 9))
                if spechar == 5:
                    if this_step in maxes[4]:
                        continue
                pw.append(this_step)
                number_total += 1

        elif lonom == 1 or lonom == 5:  # this step will be uppercase letter if total haven't reached its maximum
            if letter_total >= maxes[2]:
                continue
            else:
                this_step = let_up_case[random.randint(0, 25)]
                if spechar == 5:
                    if this_step in maxes[4]:
                        continue
                pw.append(this_step)
                letter_total += 1

        elif lonom == 2:  # this step will be mark if total haven't reached its maximum
            if mark_total >= maxes[3]:
                continue
            else:
                this_step = mark_case[random.randint(0, 6)]
                if spechar == 5:
                    if this_step in maxes[4]:
                        continue
                pw.append(this_step)
                mark_total += 1
        elif lonom == 3 or lonom == 6:
            if letter_total >= maxes[2]:
                continue
            else:
                this_step = let_low_case[random.randint(0, 25)]
                if spechar == 5:
                    if this_step in maxes[4]:
                        continue
                pw.append(this_step)
                letter_total += 1

    new_pw = ' '.join([str(i) for i in pw])
    new_pw = new_pw.replace(" ", "")

    return new_pw


def menu():
    while True:
        try:
            while True:
                pw_length = int(input("Length of Password:"))
                if pw_length <= 1:
                    print("Password length can't be shorter than 1.")
                else:
                    break
            break
        except:
            print("only use NUMBERS.")

    while True:
        try:
            while True:
                max_num = int(input("Maximum numbers preferred:"))
                if max_num < 0:
                    print("Only use natural numbers")
                else:
                    break
            break
        except:
            print("only use NUMBERS.")

    while True:
        try:
            while True:
                max_let = int(input("Maximum letters preferred:"))
                if max_let < 0:
                    print("Only use natural numbers")
                else:
                    break
            break
        except:
            print("only use NUMBERS")

    while True:
        try:
            while True:
                max_mark = int(input("Maximum special characters preferred:"))
                if max_mark < 0:
                    print("Only use natural numbers")
                else:
                    break
            break
        except:
            print("only use NUMBERS")

    if max_num + max_mark + max_let > pw_length:
        print(
            "WARNING! Maximum preferred choices are longer than your password length.This may result as not you wished.")
    elif max_num + max_mark + max_let < pw_length:
        print(
            "WARNING! Maximum preferred choices are shorter than your password length.We shortened your length to avoid problems.")
        pw_length = max_num + max_mark + max_let
    want_include = str(input("Enter 'y' if you want your password to doesn't contain selected characters."))
    if want_include == 'y':
        no_include = str(input(
            "Add any letter,number that you don't want your password to contain.Seperate with commas. /CASE SENSITIVE/:"))
        noinc_list = list(no_include.split(","))
        return [pw_length, max_num, max_let, max_mark, noinc_list, 5]  # 5means True for selected characters.
    return [pw_length, max_num, max_let, max_mark]


def securepw():
    password = crepw()
    while True:
        for i in range(0, 9):
            if password.count(str(i)) == len(password) - 1 or password.count(str(i)) == len(password):
                password = crepw()
        break
    return password


while True:
    password = securepw()
    with open("passwords.txt", "a") as file:
        file.write(password)
        file.write("\n")
    wnc = str(input("Would you like to copy your password to clipboard?(y or n):"))  # WaNt to Copy?
    if wnc.lower() == 'y':
        pyperclip.copy(password)
    print(password)
    kepu = str(input(
        "type 'n' to quit.Type ANYTHING to create another password:"))  # KEeP Up the app - if n, app won't create another.
    if kepu.lower() == 'n':
        break
