# https://www.w3resource.com/python-exercises/python-functions-exercises.php

# Exercise 2 :

# Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

varList = [8,2,3,0,7]

totalNo = int(len(varList))

def calcFunc():
    for i in range(1, totalNo):
        sumVal = int(i+i)
    return sumVal

theSum = calcFunc()

print(theSum)

# Don't know


# Potential solution:

varList = [8,2,3,0,7]

def sumFunc():
    sumF = sum(varList)
    return sumF

print(sumFunc())


# Exercse 3. Write a Python function to multiply all the numbers in a list.

varNewList = [8,2,3,-1,7]

def multiFunc(theList):
    result = 1
    for i in theList:
        result = result * i
    return result

print(multiFunc(varNewList))




# Exercise 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

theString = "1234abcd"
expString = "dcba4321"

revTxt = theString[::-1]

print(revTxt)
if revTxt == expString:
    print("Corect")



# Another solution with Leon:
def revStr(stringVar):
    strLen = len(stringVar) -1
    newStr =""
    for i in range(strLen,-1,-1):
        newStr = newStr + stringVar[i]    
    return newStr

print(revStr(theString))



# Exercise 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

firstNum = int(input("Your number here: "))

def factorialFunc(numVar):
    theanswer = numVar
    while numVar > 1:
        theanswer = theanswer * (numVar -1)
        numVar = numVar -1
    return theanswer

print(factorialFunc(firstNum))



# Exercise 6.Write a Python function to check whether a number falls in a given range


varNum = int(input("Say a no : "))
rangeNum = range (1,10)

def checkFunc(theNum, theRange):
    answer = "Corect"
    if theNum in theRange:
        return answer
    else:
        answer = "Not in range"
        return answer

print(checkFunc(varNum, rangeNum))


