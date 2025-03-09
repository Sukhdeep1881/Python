class Library:
    no_of_books = 0
    books = []

    def add_book(self,book):
        self.books.append(book)
        self.no_of_books += 1
        print(f"Added {book}")

    def check(self):
        if self.no_of_books == len(self.books):
            return True
        else:
            return False


a = Library()
a.add_book("English")
a.add_book("Math")
a.add_book("Hindi")
a.add_book("S.S.T")
print(a.books)
print(a.no_of_books)
print(a.check())