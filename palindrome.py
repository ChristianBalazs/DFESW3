
#Exercise 

# A palindrome reads the same forwards and backwards e.g. otto or racecar.
	
# ask a user to type in a string
	
# get then length of the string
	
# reverse the string by reading letter by letter
	
# check the reversed string against the original string
	
# if they are the same it is a palindrome



#SOLUTION with Leon :

theInput = input("Word here: ")

numChars = len(theInput) - 1

varInvert =""

while numChars >= 0:
    varInvert =  varInvert + theInput[numChars]
    numChars = numChars - 1

if varInvert == theInput:
    print("Pallindrome")
else:
    print("No")



