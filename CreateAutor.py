import json
import re
from AdminAuth import Authentification
from Login import run_Login
from CheckDate import run_check_Structure

def run_Create_Autor():
    
    auth = run_Login()

    if auth == True:
        print('nice')
        InputName = input('Name: ')
        InputLastName = input('Last Name: ')
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
        print('You need to be logged in to Create a Autor')