import datetime


def run_Check_Structure():
    check = False
    
    while check == False:
        date = input('Enter Date (DDMMYYYY): ')
        date = int(date)
        day = date / 1000000
        day = int(day)
        month = (date -day * 1000000) / 10000
        month = int(month)
        year = (date -day * 1000000) - month * 10000
        year = int(year)
        
        try:
            date = datetime.datetime(year,month,day)
            date = str(date)
            check = True
        except ValueError:
            check = False
        print(str(date))

    return date




