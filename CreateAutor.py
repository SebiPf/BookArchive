import json
import re
from AdminAuth import Authentification
from Login import run_Login
from CheckDate import run_Check_Structure
from CheckName import run_Check_Name

def run_Create_Autor():
    
    loginauthentification = False
    auth = Authentification(loginauthentification)
    auth = auth.getauthentification()

    if auth == True:
        inputName = run_Check_Name()
        inputLastName = run_Check_Name()
        #Date = input('Birthdate: ')
        inputBirthdate = run_Check_Structure()



        inputGender = input('Gender: ')

        with open('AutorList.json') as json_file:
            data = json.load(json_file)
        for p in data['Autor']:
            anzahl = p['AutorNumber']
        anzahl = anzahl + 1




        def write_json(data, filename='AutorList.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
      
      
        with open('AutorList.json') as json_file: 
            data = json.load(json_file) 
            temp = data['Autor'] 
            y = {"Name": inputName,
                "LastName": inputLastName,
                "Birthdate": inputBirthdate,
                "Gender": inputGender,
                "NumberofBooks": 0,
                "AutorNumber": anzahl
                }  
            temp.append(y) 
  
        write_json(data) 
    else:
        print('Please log in.')