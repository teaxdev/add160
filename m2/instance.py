"""  
    Instance methods are unique to each student
    Class methods are set to the class and sets an attribute for all students
    Static methods dont need any input from the class or instances
"""

class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def announce(self): # Instance Method: prints the selected students name
        return f"This students name is: {self.name}"
    
    @classmethod #Class Method: Gives every student a gpa and sets it to 2
    def set_gpa(cls, gpa):
        cls.gpa = gpa
    
    @staticmethod # Static Method: Adds a bell, and it would ring after every class period
    def bell():
        return 'The bell rings, class is over'
    
stu1 = Student('Billy', '12')
stu2 = Student('Bobby', '11')
stu3 = Student('Kiley', '12')

print(stu1.announce())
print(stu2.announce())
print(stu3.announce())

Student.set_gpa('2')
print(Student.gpa)

print(Student.bell())