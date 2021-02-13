
class AutorInfo():
    def __init__(self, Name, LastName, Birthdate, Gender, NumberofBooks):

        self.name = Name
        self.lastname =LastName
        self.birthdate = Birthdate
        self.gender = Gender
        self.numberofbooks = NumberofBooks

    def getautorname(self):
        return self.name
    
    def getlastname(self):
        return self.lastname
    
    def getbirthdate(self):
        return self.birthdate
    
    def getgender(self):
        return self.gender
    
    def getnumberofbooks(self):
        return self.numberofbooks
    