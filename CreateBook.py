import json
from CheckCategory import CheckCategories
from GetCategories import run_categoreis

def run_create_book():

    Inputtitle = input('title')
    Inputyear = input('year')
    Inputautor = input('Autor')
    Inputpublisher = input('Publisher')
    Inputisbn13 = input('ISBN-13')
    print('please choose one of the following Categories')
    run_categoreis()
    Inputtype = input('Category: ')
    Check = CheckCategories(Inputtype)
    Inputtype = Check.getCategory()
    Inputlength = input('How many Pages')

    def write_json(data, filename='Bookslist.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 
      
      
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