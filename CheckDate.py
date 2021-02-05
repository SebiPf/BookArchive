import re


def run_check_Structure():
    check = False
    while check == False:
        Date = input('Birthdate: XX/XX/XXXX')
        #valid = False
        pattern = re.compile("^\d{1[0-3],2[0-9]}\/\d{1[0-1],2[0-9]}\/\d{4}$")
        if pattern.match(Date):
            check = True
        else:
            print('Date struckture should be: XX/XX/XXXX')

    return Date




