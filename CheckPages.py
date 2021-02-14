import re


def run_Check_Pages():
    check = False
    while check == False:
        page = input('How many pages does the Book have?: ')
        pattern = re.compile("^[0-9]*$")
        if pattern.match(page):
            check = True
        else:
            print('Your input should only contain numbers.')
    return page