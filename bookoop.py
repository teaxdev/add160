# Book Object Oriented Programming Assignment
class Book(): # Defining the book class
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Percy Jackson, The Lightning Thief", "Rick Riordan", "377")
book2 = Book("Percy Jackson, The Sea Of Monsters", "Rick Riordan", "279")
book3 = Book("Percy Jackson, The Titan's Curse", "Rick Riordan", "213")

def display_details(x): # Cycles through each book and prints its details
    if x == 1:
        print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.pages}")
    elif x == 2:
        print(f"Title: {book2.title}, Author: {book2.author}, Pages: {book2.pages}")
    else:
        print(f"Title: {book3.title}, Author: {book3.author}, Pages: {book3.pages}")

def is_long_book(x): # Prints whether each book is more than 100 pages
    if x == 1:
        if int(book1.pages) >= 100:
            print("True")
        else:
            print("False")
    if x == 2:
        if int(book2.pages) >= 100:
            print("True")
        else:
            print("False")
    elif x == 3:
        if int(book3.pages) >= 100:
            print("True")
        else:
            print("False")

def main(): # Loops through each function 3 times
    i = 1
    while i <= 3:
        display_details(x=i)
        is_long_book(x=i)
        i += 1

main()
