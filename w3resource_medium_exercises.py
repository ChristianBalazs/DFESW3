

# Python class, Basic application [12 exercises with solution]

# Exercise 1. Write a Python class to convert an integer to a roman numeral.

# Solution , using code from Google search

class Convert():
    def romanConv(self,x):

        arabicNo = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romanNo = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12

        while x:
            div = x // arabicNo[i]
            x = x % arabicNo[i]

            while div:
                print(romanNo[i], end = "")
                div = div - 1
            i = i - 1

theNum = Convert()

theNum.romanConv(21)

print('')


# Exercise 2. Write a Python class to convert a roman numeral to an integer

# Potential Solution  NOT FINISHED:

# take example romanNum = "MDCLXIV" = 1664

# create a list of each type of romanNum and another list of arabicNo to corespond at same index postion

# find a way to compare each item from "MDCLXIV" string to coresponding arabicNo

# class intConvert():
    
#     def arabicConv(self, rNum):
#         romanNo = ["I", "IV", "V", "IX", "X", "XL",
#         "L", "XC", "C", "CD", "D", "CM", "M"]
#         arabicNo = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#         indexP = 12
#         for i in rNum:




# Exercise 3. Budget App from towardsdatascience.com

# Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories”

# Potential solution here - NOT working:

# class budgetApp():

#     def __init__(self, category, depositSum, withdrawSum = 0):
#         self.category = category
#         self.depositSum = depositSum
#         self.withdrawSum = withdrawSum
#         print(int(self.depositSum))

#     def currentFunds(self):
#         self.currentFunds = self.depositSum - self.withdrawSum
#         self.currentFunds = self.currentFunds - self.withdraw
#         print(int(self.currentFunds))

#     def withdraw(self, withdraw):
#         self.withdraw = withdraw
        
    

# orangeVar = budgetApp('food', 100)

# orangeVar.currentFunds()

# orangeVar.withdraw(15)

# print(orangeVar.currentFunds())



# Another solution here - Works a bit:


class budgetApp():

    def __init__(self, category ):
        self.category = category
          
    def withdraw(self, withdraw):
        self.withdraw = withdraw

    def deposit(self, deposit):
        self.deposit = deposit

    def currentFunds(self):
        self.currentFunds = self.deposit - self.withdraw
        print(int(self.currentFunds))
    

orangeVar = budgetApp('food')

orangeVar.deposit(150)
orangeVar.withdraw(20)

orangeVar.currentFunds()

# orangeVar.withdraw(15)

# print(orangeVar.currentFunds())