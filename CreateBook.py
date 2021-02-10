import json
from CheckCategory import CheckCategories
from GetCategories import run_categories
from GetAutors import run_Autors
from CheckPages import run_check_Pages
from AdminAuth import Authentification
from Login import run_Login
from DefaultCategory import Default

def run_create_book():

    LoginAuthentification = False
    auth = Authentification(LoginAuthentification)
    auth = auth.getAuthentification()
    if auth == True:

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
        print('please type one of the following Categories')
        run_categories()
        Inputtype = input('Category: ')
        if Inputtype == (''):
            Inputtype = None
        if Inputtype != None:
            Check = CheckCategories(Inputtype)
            Inputtype = Check.getCategory()
        else:
            Check = Default(Inputtype)
            Inputtype = Check.getDefault()

        
        Inputlength = run_check_Pages()

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
    else:
        print('please log in')
        
        