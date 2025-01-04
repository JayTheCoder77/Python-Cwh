# magic methods / dunder methods double underscore

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}" # this will return the string representation of the object
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author
    def __lt__(self,other):
        return self.pages < other.pages
    def __add__(self,other):
        return self.pages + other.pages
    def __contains__(self,item):
        return item in self.title or item in self.author
    def __getitem__(self,key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages
        else:
            return None

book1 = Book("Harry Potter" , "JK Rowling" , 500)
book2 = Book("Rich Dad Poor Dad" , "Robert Kiyosaki" , 300)
book3 = Book("Atomic HABITS" , "James Clear" , 280)
book4 = Book("Atomic HABITS" , "James Clear" , 280)

print(book1)
print(book2)
print(book3)

print(book3 == book2)
print(book3 < book2)
print(book3 + book2)

print("Robert" in book1)

print(book1['autho'])
