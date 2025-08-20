# Book Object Oriented Programming Assignment

print("test")

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Percy Jackson, The Lightning Thief", "Rick Riordan", "377")
book2 = Book("Percy Jackson, The Sea Of Monsters", "Rick Riordan", "279")
book3 = Book("Percy Jackson, The Titan's Curse", "Rick Riordan", "213")

def display_details():
    for i in Book:
        print(f"")
        i += 1
    print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.pages}")
    print(book2.title, book2.author, book2.pages)
    print(book3.title, book3.author, book3.pages)
    
display_details()

def is_long_book():
    if int(book1.pages) >= 100:
        print("True")
    else:
        print("False")

is_long_book()

