import json



class Book:
    def __init__(self, title, release, bookautor, publisher, isbn, booktype, pages):
        self.booktitle = title
        self.releaseyear = release
        self.bookautor = bookautor
        self.publisher = publisher
        self.isbn = isbn
        self.booktype = booktype
        self.pages = pages

        with open('AutorList.json') as json_file:
            data = json.load(json_file)
            for p in data['Autor']:
                if self.bookautor == p['AutorNumber']:
                    self.bookautor = p['Name']

    def gettitle(self):
        return self.booktitle

    def getyear(self):
        return self.releaseyear

    def getautor(self):
        return self.bookautor

    def getpublisher(self):
        return self.publisher

    def getisbn(self):
        return self.isbn

    def getbooktype(self):
        return self.booktype

    def getpages(self):
        return self.pages






