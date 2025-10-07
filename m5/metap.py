# OOP 5.1 Metaprogramming


# This creates a class named Dog dynamically
Dog = type("Dog", (), {"name": "Spot", "bark": "Woof!"}) 


# The instance, doggy, will inherit all methods defined in the dog class
doggy = Dog() 

# Calling doggy's attribute 'bark'
print(doggy.bark) 