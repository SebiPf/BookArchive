import json

def run_Exit():
    exitprogramm = True
    

    with open('UserData.json') as json_file: 
        data = json.load(json_file)

    for p in data['User']:
        p['NumberCategory'] = 0
        p['NumberViewed'] = 0 
    for p in data['Admin']:
        p['NumberCategory'] = 0
        p['NumberViewed'] = 0
    
    with open('UserData.json'  , 'w') as file:
        json.dump(data, file, indent=2)

    with open('Admins.json') as json_file:
        data = json.load(json_file)
        for p in data['Admin']:
            p['Auth'] = False
    with open('ADMINS.json'  , 'w') as file:
        json.dump(data, file, indent=2)

    return exitprogramm
