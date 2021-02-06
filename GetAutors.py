import json
from book import Book
def run_Autors():
    
    with open('Autorlist.json') as json_file:
        data = json.load(json_file)
        for p in data['Autor']:
            print(p['Name'])
            autor=p['Name']
            print(p['LastName'])

            with open('Bookslist.json') as json_file:
    
                data = json.load(json_file)
            AutorArray = []
            for p in data['book']:
                book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
                title = book.gettitle()
                autor = p['Autor']
                #print(title)
                if autor == autor:
                    AutorArray.append(title)
                    AutorArray.sort()

            print('books: ' , AutorArray[0],AutorArray[1],AutorArray[2],)

    
