
# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.



print("GAME(Up to 5): compare 1st and last number to see if both are the same")


num1,num2,num3,num4,num5 = input("Your numbers here ").split(",")

listInput = [num1, num2, num3, num4,num5]

lastPos = len(listInput)-1

print(listInput)

if listInput[0] == listInput[lastPos]:
    print("True: First and last number are the same")
else:
    print("Not the same numbers")

