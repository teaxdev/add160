# OOP 2.9 Built in Inheritance

class VowelString(str):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def count_vowels(self):
        vowel = "aeiou"
        count = 0
        for v in str:
            count += 1
            return count
        
test = VowelString("Hello World!")
print(test.count_vowels())
