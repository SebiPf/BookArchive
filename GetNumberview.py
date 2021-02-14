import json
from AdminAuth import Authentification

def run_Number_Viewed():
    loginauthentification = False
    auth = Authentification(loginauthentification)
    auth = auth.getauthentification()

    with open('UserData.json') as json_file:
        data = json.load(json_file)
        if auth == True:
            for p in data['Admin']:
                print('You looked up: ' , p['NumberViewed'] , ' Book(s)')
                print('and looked up: ' , p['NumberCategory'] , 'Categorie(s)')
        else:
            for p in data['User']:
                print('You looked up: ' , p['NumberViewed'] , ' Book(s)')
                print('and looked up: ' , p['NumberCategory'] , 'Categorie(s)')