# OOP 3.1 Advanced Exceptions

class MissingStudentError(Exception):
    pass

class MissingItemError(Exception):
    pass

# def student_list():
#     try:
#         stu1 = "Michael"
#         stu2 = "Michelle"
#         stu3 = "Travis"
#         stu4 = "Ben"
#         print(stu1)
#         print(stu2)
#         print(stu3)
#         print(stu4)
#         print(stu5)
#     except NameError as e:
#         raise MissingStudentError("Missing students!")
    
def item_list():
    try:
        try:
            print(items[0])
            print(items[1])
            print(items[2])
            print(items[3])
            print(items[4])
        except IndexError as e:
            raise MissingItemError("Missing items!") from e
    except MissingItemError as e:
        print(f"MissingItemError: {e}")
        print(f"Cause: {e.__cause__}")
        print(f"Context: {e.__context__}")
    
items = ["pencil", "eraser", "dice", "can"]
# student_list()
item_list()