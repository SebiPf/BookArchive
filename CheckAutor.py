import json
from GetAutors import run_Autors
from CreateAutor import run_Create_Autor

def run_Check_Autor():
    check = False
    while check == False:
        print('Enter one of the following Autors')
        print('or enter new Autor to go to create Autor')
        run_Autors()
        i = input('Autor: ')
        with open('AutorList.json') as json_file:
            data = json.load(json_file)

        for p in data['Autor']:
            name = p['Name']
            lastname = p['LastName']
            if i == name or i == lastname:
                inputautor = i
                check = True
        if i == 'new Autor':
            run_Create_Autor()
            with open('AutorList.json') as json_file:
                data = json.load(json_file)
            for p in data['Autor']:
                inputautor = p['Name']
            check = True

        if check == False:
            print('Check spelling or type new Autor as name to create a New Autor and use the new as Autor for the Book')

    return inputautor