# OOP 2.1 Core Syntax Assignment

class AddressBook():
    """
    A class that represents an Address Book

    Attributes:
    first_name: str -- the users first name
    last_name: str -- the users last name
    birthday: str -- the users date of birth
    email: str -- the users email address
    street_address: str -- the users street address
    city: str -- the city where the user lives
    state: str -- the state where the user lives
    zip: int -- the users zip code
    phone: int -- the users phone number

    Methods:
    __str__
    __repr__
    __eq__
    """
    def __init__(self, first_name, last_name, birthday, email,
                   street_address, city, state, zip, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone

    def __str__(self):
        print()

    def __repr__(self):
        print()

    def __eq__(self):
        print()