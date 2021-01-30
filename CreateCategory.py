import json


def run_create_Category():

    InputCategory = input('Category')
    

    def write_json(data, filename='Categorylist.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 
      
      
    with open('Categorylist.json') as json_file: 
        data = json.load(json_file) 
        temp = data['Categories'] 
        y = {"Category": InputCategory
            }  
        temp.append(y) 
      
    write_json(data) 



