import json
from AdminAuth import Authentification
from CheckName import run_Check_Name
from CheckCategoryName import run_Check_Category_Name

def run_Create_Category():
    loginauthentification = False
    auth = Authentification(loginauthentification)
    auth = auth.getauthentification()
    if auth == True:

        inputCategory = run_Check_Category_Name()

        with open('CategoryList.json') as json_file:
            data = json.load(json_file)
        for p in data['Categories']:
            anzahl = p['CategoryNumber']
        anzahl = anzahl + '1'

        def write_json(data, filename='CategoryList.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
        
        
        with open('CategoryList.json') as json_file: 
            data = json.load(json_file) 
            temp = data['Categories'] 
            y = {"Category": inputCategory,
                "CategoryNumber": anzahl
                }  
            temp.append(y) 
        
        write_json(data) 

    else:
        print('please log in')



