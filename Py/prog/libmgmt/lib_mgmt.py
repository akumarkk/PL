class Book:
    def __init__(self, title, author, isbn):
        self.title =  title
        self.author = author
        self.isbn= isbn
    
    def display(self):
        print("{0} {1} {2}".format(self.isbn, self.title, self.author))

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display(self):
        for b in self.books:
            b.display()


l = Library()
bal=Book('C', 'Balaguruswamy', '1234')
l.add_books(bal)
yash=Book('C', 'yashwanth', '12345')
l.add_books(yash)
l.display()

l.remove_book(yash)
l.display()
