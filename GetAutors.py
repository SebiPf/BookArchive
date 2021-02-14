import json
from Book import Book
def run_Autors():
    
    with open('AutorList.json') as json_file:
        data = json.load(json_file)
        for p in data['Autor']:
            print(p['Name'])
            print(p['LastName'])
            print('Autor id', p['AutorNumber'])
            autorid = p['AutorNumber']

            with open('BooksList.json') as json_file:
    
                data = json.load(json_file)
            autorarray = []
            for p in data['book']:
                book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
                title = book.gettitle()
                autor = p['Autor']
                #print(title)
                if autorid == autor:
                    autorarray.append(title)
                    autorarray.sort()

            if len(autorarray)>2:
                print('books: ' , autorarray[0],autorarray[1],autorarray[2])
            elif len(autorarray)==2:
                print('books: ' , autorarray[0],autorarray[1])
            elif len(autorarray)==1:
                print('books: ' , autorarray[0])
            else:
                print('No Books for this autor yet')
            print('-------------------------------------------')

    
