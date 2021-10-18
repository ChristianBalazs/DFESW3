
# Doesn't seem to work ?

# In the following example, assume we have a file called "filename_ex.txt" which has 10 lines in it.
# We only want to keep the even lines, so discard the odd ones.

# file = open("filename_ex.txt", "r")

# outfile = ""
# file.close()

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename_ex.txt", "w")
# file.write(outfile)
# file.close()

# The outfile is the variable in which we are storing the data we wish to keep.
# The readline in the else statement skips the lines which are odd.



# Exercise - SOLVED :

# Create a Python file which does the following:

# Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
# Reads and displays the names of the 1st and 4th team in the file.


# 1. Create a variable to hold the content of the file which is opened
fileVar = open("teams.txt", "r")

# 2. Close the file
fileVar.close()


# 3. Create another variable to contain the new new information to be introduced into the file
newFile = ['Chelsea', 'Real Madrid', 'Manchester United', 'AC Milan','Celtic Glasgow']

# 4. Open the file in WRITE mode
fileVar = open("teams.txt", "w")

# 4. Create the program for adding each item from "newFile" into the content of file
for n in newFile: # for  each element in "NewFile"
    newLine = f'{n} \n' # Create new variable to hold the info to be written into the file
    # This "newLine" variable will be asigned f string with {n} which is the element in "NewFile" and \n for creating a new line when loading the nex {n}
    fileVar.write(newLine) # Command to write "newLine" variable content to "fileVar)

# 6. Close the file
fileVar.close()


# 7. Open the file again
fileVar = open("teams.txt", "r")

# 8. Create a variable to hold/access each line of "fileVar"
listVar = fileVar.readlines()

# 9. Print the name of the 1st and 4th team
nameDisp = listVar[0] + listVar[3]
print(nameDisp)

# 10. Close the file
fileVar.close()





