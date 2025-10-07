# my code
class book:
    def __init__(self,book_id,title,author,quantity):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.quantity=quantity
    
    def view(self):
        print(f"book id={self.book_id} | book title={self.title} | author={self.author} | quantity={self.quantity}")



class library:
    def __init__(self):
        self.books={}

    def add_book(self):
        book_id=input("enter book id")
        title=input("enter book title")
        author=input("enter author name")
        try:
            quantity=int(input("enter quantity"))
        except ValueError:
            print("enter integer quantity")
            return
    
        if book_id in self.books:
            print("book is already there so try return option\n")
            return

        else:
            self.books[book_id]=book(book_id,title,author,quantity)
            print(f"book id-{book_id} added successfully \n")

    def borrow_book(self):
        book_id=input("\nenter book id to borrow\n")
        try:
            quantity=int(input("\nenter the quantity\n"))
        except ValueError:
            print("enter numbers only\n")
            return

        if book_id not in self.books: 
            print("\nbook not found\n")
            
        
        elif self.books[book_id].quantity<quantity:
            print(f"\n the quantity is high only {self.books[book_id].quantity} books available ")
            

        elif book_id in self.books:
            print("\nbook found\n")
            self.books[book_id].quantity-=quantity
            print("book borrowed successfully")
            
        

    def return_book(self):
        book_id=input("\nenter book id to return\n")
        try:
            quantity=int(input("\n enter quantity\n"))
        except ValueError:
            print("enter numbers only\n")
            return

        if book_id not in self.books:
            print("\nthis is a new book so try another option\n")
            return
        
        

        else:
            self.books[book_id].quantity+=quantity
            print("\nbook added successfully\n")
            

    def view_all_books(self):
        print("\n---available books---")
        for b in self.books.values():
            b.view() 

    def view_a_book(self):
        book_id=input("enter book id to view")

        if book_id not in self.books:
            print("\nno book found\n")
            return

        else:
            self.books[book_id].view()

    def save_book(self):
        with open("library.txt","w") as file:
            for i in self.books.values():
                file.write(f"{i.book_id},{i.title},{i.author},{i.quantity}\n")
        print("books saved successfully\n")   

    def load_books(self):
        try:
            with open("library.txt","r") as file:
                line=file.readlines()
                for m in line:
                    book_id,title,author,quantity=m.strip().split(",")
                    self.books[book_id]=book(book_id,title,author,int(quantity))
                print("books loaded succesfully\n") 
        except FileNotFoundError:
            print("no files found start fresh\n")

                      


def main():
    print("welcome to simple library system\n")
    a=library()
    a.load_books()
    while True:
        print("press 1 for view all books")
        print("press 2 for view a book")
        print("press 3 for add a new book")
        print("press 4 for borrow a book")
        print("press 5 for return a book")
        print("press 0 for exit")

        user_input=int(input("enter your choice\n"))
       
        if user_input==1:
            a.view_all_books()

        elif user_input==2:
            a.view_a_book()

        elif user_input==3:
            a.add_book()

        elif user_input==4:
            a.borrow_book()

        elif user_input==5:
            a.return_book()

        elif user_input==0:
            a.save_book()
            print("\nthank you\n")
            break

        else:
            print("invalid inputs.")

main()            