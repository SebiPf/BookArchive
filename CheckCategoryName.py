import re


def run_Check_Category_Name():
    check = False
    while check == False:
        categoryname = input('Enter Category: ')
        pattern = re.compile("^[a-zA-Z]+$")
        if pattern.match(categoryname):
            check = True
        else:
            print('Your input should only contain Letters')
    return categoryname