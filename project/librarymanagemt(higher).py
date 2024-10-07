class library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lenddict={}

    def displaybooks(self):
        print(f"We have following books in {self.name}:")
        for book in self.bookslist:
         print(book)

    def lendbook(self,user):
        if  book  not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print(f"{book} has been lend to {user}")
        else:

            print("Sorry, the book is already in lent.")
    def addbook(self,book,writer):
        if book not in self.lenddict.keys():
            self.lenddict.update ({book:writer})
            self.bookslist.append(book)
            print(f"{book} has been upated in {self.name} by writer {writer}")
        else:
            print(f"The book is already in {self.name} can't append book")


    def returnbook(self,book,name):

            if book in self.lenddict.keys():
                self.lenddict.pop(book)
                print(f"{book} has been returned by {name}")
            else:
                print(f"The book '{book}' is not borrowed from {self.name}.")


def main():

 p1=library(["The 100 days","The shadow fight","Black hole theroy","You and I"],"Biratnagar library house")
 while True:
     print("\nLibrary Management System")
     print("1. Display Books")
     print("2. Lend a Book")
     print("3. Add a Book")
     print("4. Return a Book")
     choice = input("Enter the choice:")
     if choice not in ['1', '2', '3', '4']:
         print("Please enter a valid option")
         continue

     else:
         choice = int(choice)
     if choice==1:
         p1.displaybooks()
     if choice==2:
         book_name=input("Enter the book you want to lend:")
         user=input("Enter the name of the user:")
         p1.lendbook(book_name,user)
     if choice==3:
         book_name=input("Enter the book you want to add in library:")
         writer=input("Enter the writer: ")
         p1.addbook(book_name,writer)
     if choice==4:
         return_book=input("Enter the book you want to return:")
         name=input("Enter the returner name:")
         # user=input("Enter the name of the user:")
         p1.returnbook(return_book,name)

if __name__ == "__main__":
  main()

