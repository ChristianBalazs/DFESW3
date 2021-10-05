
# Find max of three numbers


num1 = int(input("Num1 here: "))
num2 = int(input("Num2 here: "))
num3 = int(input("Num3 here: "))

def max_num(checkNum1, checkNum2, checkNum3):
    if checkNum1 > checkNum2:
        if checkNum1 > checkNum3:
            return checkNum1
        else:
            return checkNum3            
    else:
        if checkNum2 > checkNum3:
            return checkNum2
        else:
            return checkNum3



# Another suggestion from Stewart - to be fixed
returnVar = max_num(num1, num2, num3)

print(returnVar)




