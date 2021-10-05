
listVar = ['violin', 'viola', 'cello','traingle', 'harp', 'flute']

print('')
print(listVar[-3])
print('')
# to print item at position -3

listLen=len(listVar)
print(listVar[-listLen])
# to print item at position -lenght o the list = first on the list
print(' ')



# For loop

for tempVar in listVar:
    print(tempVar)


# While loop

inputNum = int(input("Type in whole num: "))
answerVar = 1


while inputNum > 0:
    answerVar = answerVar * inputNum
    inputNum = inputNum - 1
print(answerVar)

# Modulus 

print(7 // 4) #how many times 4 gets into 7 = 1
print(7 % 4) #whole no remainder after division = 3
print(7 / 4) #normal division with decimals = 1.75


