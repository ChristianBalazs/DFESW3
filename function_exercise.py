
# Tutorial:

def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number + 20)

# Exercise:

# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.

# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.

# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)



# Solution:
# aparently do not use print inside functions

# def scoreFunc():
#     while hScore > 25:
#           print("Try again with values 0 to 25")
#           hScore = int(input("Homework score (/25): ")) 
#     while aScore > 50:
#           print("Try again with values 0 to 50")
#           aScore = int(input("Homework score (/50): "))
#     while fScore > 50:
#           print("Try again with values 0 to 100")
#           fScore = int(input("Homework score (/100): "))


# Final solution:

def calcuFunc():
    totalPoints = (hScore / 25) + (aScore / 50) + (fScore / 100)
    ICTgrade = int(totalPoints * 100 / 3)
    return ICTgrade

def calcuGrade():
    if theScore >= 90 and theScore <100:
        theGrade = "A"
    elif theScore >= 70 and theScore < 90:
        theGrade = "B"
    elif theScore >= 50 and theScore < 70:
        theGrade = "C"
    else:
        theGrade = "Fail"
    return theGrade



studentName = input("Your name here: ")

hScore = int(input("Homework score (/25): "))

while hScore > 25:
    print("Try again with values 0 to 25")
    hScore = int(input("Homework score (/25): ")) 

aScore = int(input("Assesment score (/50): ")) 

while aScore > 50:
    print("Try again with values 0 to 50")
    aScore = int(input("Assesment score (/50): "))  

fScore = int(input("Final exam score (/100): "))

while fScore > 100:
    print("Try again with values 0 to 100")
    fScore = int(input("Final exam score (/100): "))

theScore = calcuFunc()

finalGrade = calcuGrade()


print(f"{studentName} has and ICT grade of {theScore} % which is grade {finalGrade}.")




# totalPoints = (hScore / 25) + (aScore / 50) + (fScore / 100)
# ICTgrade = int(totalPoints * 100 / 3)












# def scoreInputFunc():
#     hScore = int(input("Homework score (/25): "))
#     while hScore > 25:
#         print("Try again with values 0 to 25")
#         hScore = int(input("Homework score (/25): "))
    
#     aScore = int(input("Assesment score (/50): "))
#     fScore = int(input("Final exam score (/100): "))
#     totalPoints = (hScore / 25) + (aScore / 50) + (fScore / 100)
#     ICTgrade = int(totalPoints * 100 / 3)
#     return ICTgrade


