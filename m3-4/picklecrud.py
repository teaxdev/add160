# OOP 4.2 Serialization with pickles

import pickle

book = {}

with open('book.pkl', 'wb') as f:
    pickle.dump(book, f)

def choice():
    print("Address Book Menu:\n \
1. Add New User\n \
2. Search for Existing User\n \
3. Change Existing User\n \
4. Delete Existing User\n \
5. Exit")
    x = input("input: ")
    if x == "1":
        print("goto 1")
        add()
    elif x == "2":
        print("goto 2")
        search()
    elif x == "3":
        print("goto 3")
        update()
    elif x == "4":
        print("goto 4")
        delete()
    else:
        print("exit")

def add():
    count = 1
    print("Please input First Name:")
    fname = input("Input: ")
    print("Please input Last Name:")
    lname = input("Input: ")
    print("Please input Phone Number:")
    num = input("Input: ")
    print("Please input Email:")
    ema = input("Input: ")
    book[f"book{count}"] = {f"First Name": fname, "Last Name": lname, "Number": num, "Email": ema}
    count += 1

    save()
    choice()

def search():
    inp1 = input("Please Input the first name: ")
    inp2 = input("Please Input the last name: ")
    for book_id, info in book.items():
        if info["First Name"].lower() == inp1.lower() and info["Last Name"].lower() == inp2.lower(): 
            print(f"Found Address: {book_id}")
            print(f"Address {info}")
            return book_id
    
    print("No Address found.")
    choice()
    
def update():
    book_id = search()
    print("What would you like to change")
    x = input("input: ")
    if x == "1":
        print("name")
        new_name = input("New Name: ")
        book[book_id]["First Name"] = new_name
    if x == "2":
        print("lname")
        new_lname = input("New Last Name: ")
        book[book_id]["Last Name"] = new_lname
    if x == "3":
        print("phone")
        new_phone = input("New Phone Number: ")
        book[book_id]["Number"] = new_phone
    if x == "4":
        print("email")
        new_email = input("New Email: ")
        book[book_id]["Email"] = new_email
    else:
        print("exit")

    save()

    choice()

def delete():
    book_id = search()
    inp1 = input(f"Are you sure you would like to delete {book_id}? (yes/no)")
    if inp1 == "yes":
        del book[book_id]
    elif inp1 == "no":
        choice()
    else:
        print("Please type yes or no!")
        delete()

    save()
    choice()

def save():
    with open('book.pkl', 'wb') as f:
        pickle.dump(book, f)
choice()