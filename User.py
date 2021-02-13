

class Userdata():
    def __init__(self,NumberCategory, NumberViewed):
        self.number = NumberViewed
        self.numbercat = NumberCategory

    def getnumberviewd(self):
        return self.number
    
    def getnumbercategory(self):
        return self.numbercat