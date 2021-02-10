from GetBookInfo import run_Book_list

class Userdata():
    def __init__(self,NumberCategory, NumberViewed):
        self.Number = NumberViewed
        self.NumberCat = NumberCategory

    def getNumberViewd(self):
        return self.Number
    
    def getNumberCategory(self):
        return self.NumberCat