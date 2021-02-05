import json
from CheckCategory import CheckCategories
from GetCategories import run_categories
from GetAutors import run_Autors

def run_create_book():

    Inputtitle = input('title')
    Inputyear = input('year')
    print('enter one of the following Autors')
    print('or enter newAutor to go to create Autor')
    run_Autors()
    Inputautor = input('Autor')
    if Inputautor == ('newAutor'):
        print('aaa')

    Inputpublisher = input('Publisher')
    Inputisbn13 = input('ISBN-13')
    print('please choose one of the following Categories')
    run_categories()
    Inputtype = input('Category: ')
    if Inputtype == ():
        Inputtype = ('No Category')
    Check = CheckCategories(Inputtype)
    Inputtype = Check.getCategory()
    Inputlength = input('How many Pages')

    def write_json(data, filename='Bookslist.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4, sort_keys=True) 
      
      
    with open('Bookslist.json') as json_file: 
        data = json.load(json_file) 
        temp = data['book'] 
        y = {"Title": Inputtitle, 
             "Release": Inputyear,
             "Autor": Inputautor,
             "Publisher": Inputpublisher,
             "ISBN": Inputisbn13,
             "Category": Inputtype,
             "Pages": Inputlength,
            }  
        temp.append(y) 
      
    write_json(data) 

    with open('Autorlist.json') as json_file: 
        data = json.load(json_file)

        for p in data['Autor']:
            if Inputautor == p['Name']:
                p['NumberofBooks'] = p['NumberofBooks'] + 1 
    
    with open('Autorlist.json'  , 'w') as file:
        json.dump(data, file, indent=2)
        