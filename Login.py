import json
from AdminAuth import Authentification

def run_Login():
    
    
    testusername = input('enter your username')
    testpassword = input('enter your password')
    Authentification

    LoginAuthentification = False



    auth = Authentification(testpassword, testusername, LoginAuthentification)
    #auth = Authentification.getLoginAuthentification
    auth = auth.getLoginAuthentification()
    if auth == True:
        print('you`r now logged in')
        
        
    else:
        print('please try again')


    return auth