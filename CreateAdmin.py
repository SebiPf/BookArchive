import json
from AdminAuth import Authentification


def run_Create_Admin():
    LoginAuthentification = False
    auth = Authentification(LoginAuthentification)
    auth = auth.getauthentification()
    print(auth)
    if auth == True:
        inputname = input('Enter Username: ')
        inputpassword = input('Enter Password: ')

        with open('Admins.json') as json_file:
            data = json.load(json_file)
        for p in data['Admin']:
            anzahl = p['AdminNumber']
        anzahl = anzahl + '1'


        def write_json(data, filename='Admins.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
      
      
        with open('Admins.json') as json_file: 
            data = json.load(json_file) 
            temp = data['Admin'] 
            y = {"Name": inputname, 
                 "Password": inputpassword,
                 "AdminNumber": anzahl,
                 "Auth": False
                }  
            temp.append(y) 
  
        write_json(data) 
    else:
        print('Please log in')