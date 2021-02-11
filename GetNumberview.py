import json
from AdminAuth import Authentification

def run_Number_Viewed():
    LoginAuthentification = False
    auth = Authentification(LoginAuthentification)
    auth = auth.getAuthentification()

    with open('UserData.json') as json_file:
        data = json.load(json_file)
        if auth == True:
            for p in data['Admin']:
                print('You looked up: ' , p['NumberViewed'] , ' Book(s)')
                print('and lokked up: ' , p['NumberCategory'] , 'Categorie(s)')
        else:
            for p in data['User']:
                print('You looked up: ' , p['NumberViewed'] , ' Book(s)')
                print('and lokked up: ' , p['NumberCategory'] , 'Categorie(s)')