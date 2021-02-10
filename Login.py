import json
from AdminAuth import Authentification

def run_Login():
   
    with open('Admins.json') as json_file:
            data = json.load(json_file)
            auth = False
            while auth == False:
                testusername = input('enter your username')
                testpassword = input('enter your password')
            
                for p in data['Admin']:
                    if testusername == p['Name'] and testpassword == p['Password']:
                        p['Auth'] = True
                        auth = True
                        break
                    else:
                        print('please try again')
                        print('if you want to cancel type end as username')

                if testusername == 'end':
                    break

            with open('ADMINS.json'  , 'w') as file:
                json.dump(data, file, indent=2)