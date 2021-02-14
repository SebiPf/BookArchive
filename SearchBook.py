import json
from Book import Book
from AdminAuth import Authentification
def run_Search_Book():
    inputBook = input('what Book are you searching for?: ')
    with open('BooksList.json') as json_file:
    
        data = json.load(json_file)
    for p in data['book']:
        book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
        title = book.gettitle()
        isbn = book.getisbn()
        check = False
        if inputBook in title or inputBook in isbn:
            print('Title: ' + book.gettitle())
            print('Release: ' , book.getyear())
            print('Autor: ' , book.getautor())
            print('Publisher: ' , book.getpublisher())
            print('ISBN-13: ' , book.getisbn())
            print('Category: ' , book.getbooktype())
            print('Pages: ' , book.getpages())
            print('')

            loginauthentification = False
            auth = Authentification(loginauthentification)
            auth = auth.getauthentification()

            with open('UserData.json') as json_file: 
                data = json.load(json_file)
             
            if auth == True:
                for p in data['Admin']:
                    p['NumberViewed'] = p['NumberViewed'] + 1
            else:
                for p in data['User']:
                    p['NumberViewed'] = p['NumberViewed'] + 1
    
            with open('UserData.json'  , 'w') as file:
                json.dump(data, file, indent=2)
            check = True
    if check == False :
        print('No Book with this Title available')

    
