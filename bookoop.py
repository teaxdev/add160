# Book Object Oriented Programming Assignment
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Percy Jackson, The Lightning Thief", "Rick Riordan", "377")
book2 = Book("Percy Jackson, The Sea Of Monsters", "Rick Riordan", "279")
book3 = Book("Percy Jackson, The Titan's Curse", "Rick Riordan", "213")

tup = (book1, book2, book3)
def display_details():
    count = 1
    if count == 1:
        print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.pages}")
        count += 1
        return count
    elif count == 2:
        print(f"Title: {book2.title}, Author: {book2.author}, Pages: {book2.pages}")
        count += 1
        return count
    else:
        print(f"Title: {book3.title}, Author: {book3.author}, Pages: {book3.pages}")
    
    
display = display_details()

def is_long_book():
    if int(book1.pages) >= 100:
        print("True")
    else:
        print("False")

def main():
    i = 1
    while i <= 3:
        display_details()
        is_long_book()
        i += 1

main()
