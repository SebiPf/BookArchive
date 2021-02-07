import re


def run_check_Name():
    check = False
    while check == False:
        name = input('Enter Name')
        pattern = re.compile("^[a-zA-Z]+$")
        if pattern.match(name):
            check = True
        else:
            print('Your input should only contain Letters')
    return name