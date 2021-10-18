
# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

sumV = ''
prevNo = 0

for i in range (0,10):
    sumV = prevNo + i
    print(f"Current number:  {i} Previous number:  {prevNo} Sum:  {sumV}") 
    i = i + 1
    prevNo = i-1



# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


#Solution:

inputVar = input("single word here: ")

lenVar = len(inputVar)

for i in range(lenVar):
      
    if i % 2 == 0: 
        print(inputVar[i])



# Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting from zero up to n and return a new string.

# For example:

# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string.


# Solution:


strInput = input("Your text here: ")
n = len(strInput)
newStr = ""

for i in range(0,n):
    if i > 1:
        newStr = newStr + strInput[i]

print(newStr)


# Having a bit of fun now:

qStr = int(input("How many first letters to take away: "))
wordStr = input("Your text here please: ")
wordLen = len(wordStr)
newWord = ""

for i in range(0,wordLen):
    if i > qStr - 1 :
        newWord = newWord + wordStr[i]

print(newWord)
print("")


# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

print("GAME(Place 5): compare 1st and last number to see if are the same")


num1,num2,num3,num4,num5 = input("Your numbers here ").split(",")
listInput = [num1, num2, num3, num4,num5]
lastPos = len(listInput)-1
print(listInput)

if listInput[0] == listInput[lastPos]:
    print("True: First and last number are the same")
else:
    print("Not the same numbers")


list1 = [10,20,30,40,10]
n = len(list1)-1

if list1[0] == list1[n]:
    print("True")
else:
    print("Not equal")


