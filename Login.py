import json
import getpass

def run_Login():
   
    with open('Admins.json') as json_file:
            data = json.load(json_file)
            auth = False
            while auth == False:
                testusername = input('Enter your username: ')
                testpassword = getpass.getpass('Enter your password: ')
            
                for p in data['Admin']:
                    if testusername == p['Name'] and testpassword == p['Password']:
                        p['Auth'] = True
                        auth = True
                        print('You`re now logged in.')
                        break
                    else:
                        print('Please try again.')
                        print('If you want to cancel type "end" as username.')

                if testusername == 'end':
                    break

            with open('ADMINS.json'  , 'w') as file:
                json.dump(data, file, indent=2)