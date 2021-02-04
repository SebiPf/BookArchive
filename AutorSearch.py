import json
from Autor import AutorInfo
from book import Book

def run_Autor_Search():
    i = input('enter autor Name')

    with open('Autorlist.json') as json_file:
    
        data = json.load(json_file)
    for p in data['Autor']:
        autor = AutorInfo(p['Name'], p['LastName'], p['Birthdate'], p['Gender'], p['NumberofBooks'])
    if i in p['Name'] or i in p['LastName']:
        
        print('Name: ' , autor.getAutorName())
        print('LastName: ' , autor.getLastName()),
        print('Birthday: ' , autor.getBirthdate()),
        print('Gender: ' , autor.getGender()),
        print('NumberofBooks: ' , autor.getNumberofBooks())

        with open('Bookslist.json') as json_file:
    
            data = json.load(json_file)
            AutorArray = []
        for p in data['book']:
            book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
            title = book.gettitle()
            autor = p['Autor']
            release = p['Release']
            #print(title)
            if autor == autor:
                AutorArray.append(title)
                AutorArray.sort()

        print('Books: ' , AutorArray[0],AutorArray[1],AutorArray[2],)
        print('Release Year: ' , release)
    