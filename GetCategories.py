import json
def run_categories():
    
    with open('Categorylist.json') as json_file:
        data = json.load(json_file)
        for p in data['Categories']:
            print(p['Category'])

    


