import json

class Authentification:
    
    def __init__(self, LoginAuthentification):

        with open('Admins.json') as json_file:
            data = json.load(json_file)
            LoginAuthentification = False

            for p in data['Admin']:
                if p['Auth'] == True:
                    self.LoginAuthentification = True
                    break
                    
                else:
                    print('please log in')
                    self.LoginAuthentification = False

    def getAuthentification(self):
    
        return self.LoginAuthentification



            