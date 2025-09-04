"""
Class to represent an address book entry.

Attributes:
   first_name
   last_name
   birthday
   email
   street_address
   city
   state
   zip
   phone

Methods:
   __str__
   __repr__
   __eq__
"""
class AddressBook(): # Defining the book class
    def __init__(self, first_name, last_name, birthday, email, street_address, city, state, zip, phone):
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
        return f"First Name: {self.first_name} \nLast Name: {self.last_name} \nBirthday: {self.birthday} \nEmail: {self.email} \nStreet Address: {self.street_address} \nCity: {self.city} \nState: {self.state} \nZip: {self.zip} \nPhone: {self.phone} \n"
    
    def __repr__(self):
        return f"first_name={self.first_name}, last_name={self.last_name}, birthday={self.birthday}, email={self.email}, street_address={self.street_address}, city={self.city}, state={self.state}, zip={self.zip}, phone={self.phone}"
    
    def __eq__(self, value):
        return (self.first_name == value.first_name and
                self.last_name == value.last_name and
                self.birthday == value.birthday and
                self.email == value.email and
                self.street_address == value.street_address and
                self.city == value.city and
                self.state == value.state and
                self.zip == value.zip and
                self.phone == value.phone)
    
person1 = AddressBook("John", "Doe", "01/01/1990", "john.doe@example.com", "123 Main St", "Anytown", 
                      "NY", 12345, "555-555-5555")
person2 = AddressBook("Jane", "Smith", "02/02/1985", "jane.smith@example.com", "456 Elm St", "Othertown", 
                      "CA", 67890, "555-555-1234")
person3 = AddressBook("Emily", "Johnson", "03/03/1975", "emily.johnson@example.com", "789 Oak St", "Sometown", 
                      "TX", 11111, "555-555-6789")
person4 = AddressBook("Michael", "Brown", "04/04/1965", "michael.brown@example.com", "101 Pine St", "Anycity", 
                      "FL", 22222, "555-555-2468")

print(str(person1))
print(str(person2))
print(str(person3))
print(str(person4))