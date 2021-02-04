
class AutorInfo():
    def __init__(self, Name, LastName, Birthdate, Gender, NumberofBooks):

        self.Name = Name
        self.LastName =LastName
        self.Birthdate = Birthdate
        self.Gender = Gender
        self.NumberofBooks = NumberofBooks

    def getAutorName(self):
        return self.Name
    
    def getLastName(self):
        return self.LastName
    
    def getBirthdate(self):
        return self.Birthdate
    
    def getGender(self):
        return self.Gender
    
    def getNumberofBooks(self):
        return self.NumberofBooks
    