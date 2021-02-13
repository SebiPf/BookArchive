import json

class Authentification:
    
    def __init__(self, loginAuthentification):

        with open('Admins.json') as json_file:
            data = json.load(json_file)
            loginAuthentification = False

            for p in data['Admin']:
                if p['Auth'] == True:
                    self.loginAuthentification = True
                    break
                    
                else:
                    #print('please log in')
                    self.loginAuthentification = False

    def getauthentification(self):
    
        return self.loginAuthentification



            