import json
from AdminAuth import Authentification


def run_Create_Admin():
    Authentification
    testusername = input('enter your username')
    testpassword = input('enter your password')
    

    LoginAuthentification = False



    auth = Authentification(testpassword, testusername, LoginAuthentification)
    #auth = Authentification.getLoginAuthentification
    auth = auth.getLoginAuthentification()
    if auth == True:
        print('nice')
        Inputname = input('enter Name: ')
        Inputpassword = input('enter Password: ')
        def write_json(data, filename='Admins.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
      
      
        with open('Admins.json') as json_file: 
            data = json.load(json_file) 
            temp = data['Admin'] 
            y = {"Name": Inputname, 
                 "Password": Inputpassword
                }  
            temp.append(y) 
  
        write_json(data) 
    else:
        print('not nice')