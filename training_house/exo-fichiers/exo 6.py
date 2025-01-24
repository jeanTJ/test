class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def view(self):
        print(f"Titre du livre: {self.title} \nNom de l'auter : {self.author} \nPrix du livre : {self.price}")

myBook = Book("Python Crash Course" , "Eric Matthes" , "23 $")
myBook.view()
