
#TUTORIAL:

devs_money = 100
dev_can_play_smash = False


if devs_money > 10 and dev_can_play_smash:
    print("Dev enters the smash tournament!")
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")




# EXERCISE: 

# Create a new Python file and write a program that does the following:

# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"
# Try to do this both with and without elif statements.


# SOLUTION with elif statement :

varMark = int(input("Your mark here: "))

if varMark > 85:
    print("Distinction")
elif varMark > 65 and varMark < 85:
    print("Pass")
else:
    print("Fail")



# SOLUTION without elif statement but with errors because will run line 50 as well:

varMark = int(input("Your mark here again : "))

if varMark > 85:
    print("Distinction")
if varMark > 65 and varMark < 85:
    print("Pass")
else:
    print("Fail")


# SOLUTION without else statement:

varMark = int(input("Your mark here once more : "))

if varMark > 85:
    print("Distinction")
if varMark > 65 and varMark <85:
    print("Pass")
if varMark < 65:
    print("Fail")




# SOLUTION from David - nested if statements:

mark = int(input("Your mark: "))

if mark >= 65:
    if mark > 85:
        print("Distinction")
    else:
         print("Pass") 
else:
    print("Fail")