import json
import re
from AdminAuth import Authentification
from Login import run_Login
from CheckDate import run_check_Structure
from CheckName import run_check_Name

def run_Create_Autor():
    
    LoginAuthentification = False
    auth = Authentification(LoginAuthentification)
    auth = auth.getAuthentification()

    if auth == True:
        print('nice')
        InputName = run_check_Name()
        InputLastName = run_check_Name()
        #Date = input('Birthdate: ')
        InputBirthdate = run_check_Structure()



        InputGender = input('Gender: ')
        def write_json(data, filename='Autorlist.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
      
      
        with open('Autorlist.json') as json_file: 
            data = json.load(json_file) 
            temp = data['Autor'] 
            y = {"Name": InputName,
                "LastName": InputLastName,
                "Birthdate": InputBirthdate,
                "Gender": InputGender,
                "NumberofBooks": 0
                }  
            temp.append(y) 
  
        write_json(data) 
    else:
        print('please log in')