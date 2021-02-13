import json
from Autor import AutorInfo
from Book import Book

def run_Search_Autor():
    i = input('enter autor Name')

    with open('AutorList.json') as json_file:
        data = json.load(json_file)

    for p in data['Autor']:
        autor = AutorInfo(p['Name'], p['LastName'], p['Birthdate'], p['Gender'], p['NumberofBooks'])
    
        if i in p['Name'] or i in p['LastName']:
            print('Name: ' , autor.getautorname())
            print('LastName: ' , autor.getlastname()),
            print('Birthday: ' , autor.getbirthdate()),
            print('Gender: ' , autor.getgender()),
            print('NumberofBooks: ' , autor.getnumberofbooks())
            name = autor.getautorname()
            lastname = autor.getlastname()
            with open('BooksList.json') as json_file:
                data = json.load(json_file)
                autorarray = []

            for p in data['book']:
                book = Book(p['Title'], p['Release'], p['Autor'], p['Publisher'], p['ISBN'], p['Category'], p['Pages'])
                title = book.gettitle()
                autor = p['Autor']
                release = p['Release']
                if name == autor or lastname== autor:
                    autorarray.append(title)
                    autorarray.sort()

            if len(autorarray)>2:
                print('books: ' , autorarray[0], ' : ',autorarray[1], ' : ',autorarray[2])
            elif len(autorarray)==2:
                print('books: ' , autorarray[0], ' : ',autorarray[1])
            elif len(autorarray)==1:
                print('books: ' , autorarray[0])
            else:
                print('No Books for this autor yet')
            print(release)
        
    