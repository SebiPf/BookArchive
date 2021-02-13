import re


def run_Check_Name():
    check = False
    while check == False:
        name = input('Enter Name: ')
        pattern = re.compile("^[A-Z][a-z]*(?:-[A-Z][a-z]*)?$")
        if pattern.match(name):
            check = True
        else:
            print('Your input should only contain Letters or be seperated by - and contain Capital letter (Marie-Luise would work but not marie-luise')
    return name