import json
from CheckCategory import CheckCategories
from GetCategories import run_Categories
from GetAutors import run_Autors
from CheckPages import run_Check_Pages
from AdminAuth import Authentification
from Login import run_Login
from DefaultCategory import Default
from CreateAutor import run_Create_Autor
from CheckAutor import run_Check_Autor

def run_Create_Book():

    loginauthentification = False
    auth = Authentification(loginauthentification)
    auth = auth.getauthentification()
    if auth == True:

        inputtitle = input('Book Title: ')
        inputyear = input('Release Year: ')       
        inputautor = run_Check_Autor()
        inputpublisher = input('Publisher: ')
        inputisbn13 = input('ISBN-13: ')
        print('Please type one of the following categories: ')
        run_Categories()
        inputtype = input('Category: ')
        if inputtype == (''):
            inputtype = None
        if inputtype != None:
            check = CheckCategories(inputtype)
            inputtype = check.getCategory()
        else:
            check = Default(inputtype)
            inputtype = check.getDefault()

        
        inputlength = run_Check_Pages()

        def write_json(data, filename='BooksList.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4, sort_keys=True) 
            
            
        with open('BooksList.json') as json_file: 
            data = json.load(json_file) 
            temp = data['book'] 
            y = {"Title": inputtitle, 
                "Release": inputyear,
                "Autor": inputautor,
                "Publisher": inputpublisher,
                "ISBN": inputisbn13,
                "Category": inputtype,
                "Pages": inputlength,
                }  
            temp.append(y) 
            
        write_json(data) 

        with open('AutorList.json') as json_file: 
            data = json.load(json_file)

            for p in data['Autor']:
                if inputautor == p['AutorNumber']:
                    p['NumberofBooks'] = p['NumberofBooks'] + 1 
            
        with open('AutorList.json'  , 'w') as file:
            json.dump(data, file, indent=2)
    else:
        print('Please log in.')
        
        