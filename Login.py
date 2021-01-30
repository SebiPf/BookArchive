import json




class LoginT:
    #testusername = input('enter your username')
    #testpassword = input('enter your password')
    

    #LoginAuthentification = False
    def __init__(self, testpassword, testusername, LoginAuthentification):
        with open('Admins.json') as json_file:
            data = json.load(json_file)
            self.LoginAuthentification = False
            for p in data['Admin']:
                if testusername == p['Name'] and testpassword == p['Password']:
                    self.LoginAuthentification = True

                else:
                    print('please try again')


    def getLoginAuthentification(self):
        return self.LoginAuthentification



            