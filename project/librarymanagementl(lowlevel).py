class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
        self.id=id

    def addbook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
        # self.id=id

    def show(self):
        print(f"The number of books is {self.nobooks}")




        for book in self.books:
           print(book)

# Creating a Library instance
lib = Library()

# Adding a book
lib.addbook("The thousand miles")
lib.show()
lib.addbook("Harry potter")
lib.show()
lib.addbook("Cr ko chak")
lib.show()
lib.addbook("The thousand miles")
lib.show()
# Showing books

