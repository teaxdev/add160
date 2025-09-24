# OOP 2.9 Built in Inheritance

class VowelString(str):
    # def __init__(self): init breaks my code so I commented it out
    #     super().__init__()

    def count_vowels(self):
        count = 0
        for v in self.lower():
            if v == "a" or v == "e" or v == "i" or v == "o" or v == "u":
                count += 1
        return count
        
test = VowelString("Hello World!")
print(test.count_vowels())
