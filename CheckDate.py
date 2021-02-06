import datetime


def run_check_Structure():
    check = False
    
    while check == False:
        Date = input('enter Date: DDMMYYYY')
        Date = int(Date)
        day = Date / 1000000
        day = int(day)
        month = (Date -day * 1000000) / 10000
        month = int(month)
        year = (Date -day * 1000000) - month * 10000
        year = int(year)
        
        try:
            Date = datetime.datetime(year,month,day)
            Date = str(Date)
            check = True
        except ValueError:
            check = False
        print(str(Date))

    return Date




