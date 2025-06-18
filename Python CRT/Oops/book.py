"""
write a python program to create a book class declare the states as 
BookName
AuthorName
PublisherName
PublishedDate
CategoryOfBook
1)Create 5 objects & initialize the values using constructor where out of five
    --Create 1st object using one parameterized constructor
    --Create 2nd object using two parameters constructor
    --Create 3rd object using zero parameterized constructor
    --Create 4th object using four parameters constructor
    --Create 5th object using five parameters constructor 
2)Access the values using Accessor methods
3)Update the values using Mutator method for name of the book
"""
class Book:
    def __init__(self, BookName=None, AuthorName=None, PublisherName=None, PublishedDate=None, CategoryOfBook=None):
        self.BookName=BookName
        self.AuthorName=AuthorName
        self.PublisherName=PublisherName
        self.PublishedDate=PublishedDate
        self.CategoryOfBook=CategoryOfBook
    def set_details(self, BookName, AuthorName, PublisherName, PublishedDate, CategoryOfBook):
        self.BookName=BookName
        self.AuthorName=AuthorName
        self.PublisherName=PublisherName
        self.PublishedDate=PublishedDate
        self.CategoryOfBook=CategoryOfBook                    
    def get_details(self):          
        print(f"Book Name: {self.BookName}")
        print(f"Author Name: {self.AuthorName}")
        print(f"Publisher Name: {self.PublisherName}")
        print(f"Published Date: {self.PublishedDate}")
        print(f"Category of Book: {self.CategoryOfBook}")
    def update_book_name(self, new_name):
        self.BookName = new_name
        print(f"Updated Book Name: {self.BookName}")
# Class definition remains the same
class Book:
    def __init__(self, BookName=None, AuthorName=None, PublisherName=None, PublishedDate=None, CategoryOfBook=None):
        self.BookName = BookName
        self.AuthorName = AuthorName
        self.PublisherName = PublisherName
        self.PublishedDate = PublishedDate
        self.CategoryOfBook = CategoryOfBook

    def set_details(self, BookName, AuthorName, PublisherName, PublishedDate, CategoryOfBook):
        self.BookName = BookName
        self.AuthorName = AuthorName
        self.PublisherName = PublisherName
        self.PublishedDate = PublishedDate
        self.CategoryOfBook = CategoryOfBook

    def get_details(self):
        print(f"Book Name: {self.BookName}")
        print(f"Author Name: {self.AuthorName}")
        print(f"Publisher Name: {self.PublisherName}")
        print(f"Published Date: {self.PublishedDate}")
        print(f"Category of Book: {self.CategoryOfBook}")
    def update_book_name(self, new_name):
        self.BookName = new_name
b1 = Book("Wings of fire")
b2 = Book("YOGA", "Navya")
b3 = Book()
b4 = Book("RAMAYAN", "Valmiki", "Gita press", "1950")
b5 = Book("Mahabharat", "Vyas", "Geeta", "1800", "mythology")
b1.get_details()
print("*******************************")
b2.get_details()
print("*******************************")
b3.get_details()
print("*******************************")
b4.get_details()
print("*******************************")
b5.get_details()
print("*******************************")
print("\n--- Updating Book Name for book2 ---")
b2.update_book_name("The Pilgrimage")
b2.get_details() 