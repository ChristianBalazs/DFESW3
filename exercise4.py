
# Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"

# Trying solution 1
# varAllNames = ' '
# varName = str(input("The name:"))
# inputTimes = 1

# while inputTimes <= 5:
#     varAllNames = str(varAllNames) , varName
#     print(varName + " is awesome!")
#     inputTimes = inputTimes +1
    
# print(varAllNames)



#Trying solution 2:
# Obsevartion - I needed to initialize an empty list and place the input (name) inside the loop to ask for input on each iteration

# varTheNames = []
# # changed varTheNames = () to =[]
# varEachName = input("The name of person: ")
# count = 1

# while count <= 5:
#     varTheNames.append(varEachName)
#     count = count +1

# print(varTheNames)



#Solution from Leon usig for loop:

# inputNamesList = []
# for i in range(5):
#     inputNameVar = input("Type name: ")
#     inputNamesList.append(inputNameVar)

# print(inputNamesList)





# AnNOTHER solution using while loop

# changed varTheNames = () to =[]
# moved varEachName = input("The name of person: ") inside the while loop


varTheNames = []
count = 1
while count <= 5:
    varEachName = input("The name of person: ")
    varTheNames.append(varEachName)
    count = count +1

print(varTheNames)
