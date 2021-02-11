import json
from Book import Book
from AdminAuth import Authentification
def run_search_book():
    inputBook = input('what Bokk are you searching for?')
    #BookArray =[]
    with open('Bookslist.json') as json_file:
    
        data = json.load(json_file)
    for p in data['book']:
        book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
        title = book.gettitle()
        isbn = book.getisbn()
        if inputBook == title or inputBook == isbn:
            #BookArray.append(title)
            #BookArray.sort()

            #print(BookArray)
            print('Title: ' + book.gettitle())
            print('Release: ' , book.getyear())
            print('Autor: ' , book.getautor())
            print('Publisher: ' , book.getpublisher())
            print('ISBN-13: ' , book.getisbn())
            print('Category: ' , book.getbooktype())
            print('Pages: ' , book.getpages())
            print('')

            LoginAuthentification = False
            auth = Authentification(LoginAuthentification)
            auth = auth.getAuthentification()

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

    
