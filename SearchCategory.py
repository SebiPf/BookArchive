import json
from Book import Book
from GetCategories import run_Categories
from SearchBook import run_Search_Book
from AdminAuth import Authentification

def run_Search_Category():
    check = False
    while check == False:
        inputCategory = input('What Category would you like to search?: ')
        with open('BooksList.json') as json_file:
    
            data = json.load(json_file)
        for p in data['book']:
            book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
            cattype = book.getbooktype()
            if inputCategory == cattype:
                print('Title: ' + book.gettitle())

                
                check = True
        if check == False:
            print('either there are no Books in that Category or you spelled it wrong')
            print('Those are your Options')
            run_Categories()

        answer = input('would you like to get transferred to Book search so you can get the details of one of those Books? (yes/no): ')
        if answer == ('yes'):
            run_Search_Book()
        else:
            print('you will get returned to the main menu!')
            check = True

        loginauthentification = False
        auth = Authentification(loginauthentification)
        auth = auth.getauthentification()

        with open('UserData.json') as json_file: 
            data = json.load(json_file)
        
        if auth == True:
            for p in data['Admin']:
                p['NumberCategory'] = p['NumberCategory'] + 1

        else:
            for p in data['User']:
                p['NumberCategory'] = p['NumberCategory'] + 1 
    
        with open('UserData.json'  , 'w') as file:
            json.dump(data, file, indent=2)
            