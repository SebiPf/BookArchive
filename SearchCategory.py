import json
from book import Book
from GetCategories import run_categories
from SearchBook import run_search_book

def run_search_Category():
    check = False
    while check == False:
        inputCategory = input('What Category would you like to search?')
        with open('Bookslist.json') as json_file:
    
            data = json.load(json_file)
        for p in data['book']:
            book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
            cattype = book.getbooktype()
            if inputCategory == cattype:
                print('Title: ' + book.gettitle())

                answer = input('would you like to get trasfered to Book search so you can get the details of one of those Books? (yes/no): ')
                if answer == ('yes'):
                    run_search_book()
                else:
                    print('you will get returned to the main Menue!')
                check = True
        if check == False:
            print('please check your spelling')
            print('Those are your Options')
            run_categories()

        with open('UserData.json') as json_file: 
            data = json.load(json_file)

        for p in data['User']:
            p['NumberCategory'] = p['NumberCategory'] + 1 
    
        with open('UserData.json'  , 'w') as file:
            json.dump(data, file, indent=2)
            