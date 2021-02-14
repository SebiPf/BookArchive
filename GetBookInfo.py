import json
from Book import Book

def run_Book_List():

    with open('BooksList.json') as json_file:
    
        data = json.load(json_file)
    for p in data['book']:
        book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
        print('Title: ' + book.gettitle())
        print('Release: ' , book.getyear())
        print('Autor: ' , book.getautor())
        print('Publisher: ' , book.getpublisher())
        print('ISBN-13: ' , book.getisbn())
        print('Category: ' , book.getbooktype())
        print('Pages: ' , book.getpages())
        print('------------------------------------------------')