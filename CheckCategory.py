import json



class CheckCategories:
    
    def __init__(self, Inputtype):
        
        with open('CategoryList.json') as json_file:
            data = json.load(json_file)

            checksum = False
            while checksum == False:
                for p in data['Categories']:
                    if Inputtype in p['Category']:
                        print('Category is valid')
                        self.Category = Inputtype
                        checksum = True

                        

                

                if checksum == False:
                    print('Please try again')
                    Inputtype = input()
                    self.Category = Inputtype
                    
                
                


                

    def getCategory(self):
        return self.Category