import json
from GetAutors import run_Autors
from CreateAutor import run_Create_Autor

def run_Check_Autor():
    check = False
    while check == False:
        print('Enter one of the following Authors IDs')
        print('or enter new Author to go to create Author')
        run_Autors()
        i = input('Author id: ')
        i = int(i)
        with open('AutorList.json') as json_file:
            data = json.load(json_file)

        for p in data['Autor']:
            autorid = p['AutorNumber']
            
            if i == autorid:
                inputautor = i
                check = True
        if i == 'new Author':
            run_Create_Autor()
            with open('AutorList.json') as json_file:
                data = json.load(json_file)
            for p in data['Autor']:
                inputautor = p['AutorNumber']
            check = True

        if check == False:
            print('Check spelling or type new Author as name to create a New Author and use the new as Autor for the Book')

    return inputautor