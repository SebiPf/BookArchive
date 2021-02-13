import json
def run_Categories():
    
    with open('CategoryList.json') as json_file:
        data = json.load(json_file)
        for p in data['Categories']:
            print('- ', p['Category'])

    


