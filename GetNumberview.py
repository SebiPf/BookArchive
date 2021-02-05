import json





def run_Number_Viewed():
    with open('UserData.json') as json_file:
        data = json.load(json_file)
        for p in data['User']:
            print('You looked up: ' , p['NumberViewed'] , ' Book(s)')
            print('and lokked up: ' , p['NumberCategory'] , 'Categorie(s)')