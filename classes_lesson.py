



var1 = "Ten"   #string
var2 = 10      #int
var3 = 10.000  #float

print(type(var1))

# class names should always start with Capital letter
class Dog:
    breed = "Corgi"
    height = 16
    energy = "medium"

    def speak(self): 
        print("yap")
    #create method with parameter inside

    def whatami(self):
        print(self.breed)
    #create another method inside the same class


#create an object and assigne it to class
bilbo_waggins = Dog()

chewbarka = Dog()

# Test objects 
bilbo_waggins.speak()
chewbarka.speak()

print(chewbarka.breed)

# Assign another "breed" to one object and print to check
chewbarka.breed = "Spaniel"
print(chewbarka.breed)

# test whatami() method
bilbo_waggins.whatami() # will print "Corgi"




# Example with atributes inside methods not assigned to the class directly

# __init__ is a special method that will be called whenever we create an instance of the given class.

class Cat: 

    def __init__(self, breed, height, energy):
        self.breed = breed
        self.height = height
        self.energy = energy
        self.type = "mamal"
        
    def speaky(self): 
        print("miau")

    def whatamy(self):
        print(self.breed)


funny_cattty = Cat('egyptian', 8, 'low')

funny_cattty.whatamy()





# Tutorial 1:

# In a new Python file we will create a class of students.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Now we will add some objects to the class.

John = Student("John", "21")
Jane = Student("Jane", "22")

# We can get the name age of John.
print(getattr(John, "age"))
# will print 21




#Exercise 1:

# In a new Python file, create a class of students.

# It should contain the following attributes: name, age, and class with default value "student".

# It should also contain a method which takes in 3 test scores and prints the students average test score.


# Solution:

class Students:
    name = "student"
    age = "student"
    classVar = "student"

    def scores(self, score1, score2, score3):
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        avgScore = (score1 + score2 + score3)/3
        print(int(avgScore))

Johny = Students()
Johny.name = "Johny"
Johny.age = 14
Johny.classVar = 9

Johny.scores(7,2,3)
# Will print 6



#Another solution:

#create class
class Students:
    # create __init__ method to contain "name" and "age" atributes
    # and a "class" attribute with default value set to "student"
    def __init__(self, name, age, classVar = "student"):
        self.name = name
        self.age = age

    # create a new method to contain 3 atributes for each of those 3 scores    
    def scores(self, score1, score2, score3):
        # create variable to calculate the average of those 3 scores
        avgScore = (score1 + score2 + score3)/3
        # create print function to print the average score
        print(int(avgScore))

# Created object "Mary" , assigned to "Students" class
# When creating , assigned values for "name" and "age" veriables
Mary = Students('Mary-Anne', 18 )

# run the "scores()" method on that new object "Mary" and placed 3 scores "(5,15,10)" to calculate the average
Mary.scores(5,15,10)
# will print 10




#Robin exercises

class LetterGame:

    def __init__(self):
        self.vowels = "AEIOU"
        self.lettersNoEndPoint = "BPO"
        self.lettersWithCurvedLines = "COS"
        self.letterWithTwoEnclosed = "B"

    def checking(self, x):        
        response = True
        if x in self.vowels:
            print(response)
        else:
            response = False
            print(response)
    
    def leterGroup(self,x):
        if x in self.lettersNoEndPoint:
            print("Yes, is part of NoEndPoint Group")
        if x in self.lettersWithCurvedLines:
            print("Yes, is part of WithCurvedLines Group")
        if x in self.letterWithTwoEnclosed:
            print("Yes, is part of WithTwoEnclosed Group")
        if not x in self.lettersNoEndPoint and not x in self.lettersWithCurvedLines and not x in self.letterWithTwoEnclosed:
            print("Sorry, not in any group")

vowelVar = LetterGame()

vowelVar.checking('E')

vowelVar.leterGroup('O')




#Another different solution where new objects create a separate instance of the class (pseudo-variable that can be called by that object):

class gameLetter():
    def __init__(self,letterCheck):
        self.letterCheck = letterCheck
    
    def checkThing(self,x):
        return x in self.letterCheck

vowelVar = gameLetter('AEIOU')

letterswithneendpoint = gameLetter('P')

horizontalasymmetry = gameLetter('BCDEHIKOX')


for testIn in 'A':
    print(vowelVar.checkThing(testIn))
    print(letterswithneendpoint.checkThing(testIn))




# New exercise 1:
# Write a Python class to convert an integer to a roman numeral.

class Convert():
    # def __init__(self,numCheck):
    #     self.numCheck = numCheck


    def romanConv(self,x):

        arabicNo = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romanNo = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12

        while x:
            div = x // arabicNo[i]
            x = x % arabicNo[i]

            while div:
                print(romanNo[i], end = "")
                div = div - 1
            i = i - 1

theNum = Convert()

theNum.romanConv(44)







# From Leon explanantion


# class cloud_login():
#     username = "admin"
#     password = "pasword123"
#     auth_url = "https://thecloud.com"

#     def login(self, username, password, auth_url):
#         print("#some code here")

# prodcloud = cloud_login()
# prodcloud.username = "admin_leon"
# prodcloud.password = "leon_password123"

# testcloud = cloud_login()
# testcloud.username ="test_leon"
# testcloud.password = "test_pass123"

# prodcloud.login()
# testcloud.login()








