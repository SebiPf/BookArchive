import re


def run_check_Pages():
    check = False
    while check == False:
        page = input('Enter Pages')
        pattern = re.compile("^[0-9]*$")
        if pattern.match(page):
            check = True
        else:
            print('Your input should only contain numbers')
    return page