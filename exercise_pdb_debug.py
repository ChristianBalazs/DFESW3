
import pdb


# Example 1:

def tailRecursion(factorial, result = 1): #A function to find the factorial of a number using tail recursion
    if factorial == 1:
        return result
    else:
        return tailRecursion((factorial),(factorial + result))

# Example 2:
def dtailRecursion(factorial, result = 1):
    if factorial == 1:
        return result
    else:
        tempResult = factorial * result
        return dtailRecursion((factorial), tempResult)



# Exercise A - static analysis:


# user_funds = 10.31
# item_price = price["Burger"]

# if item_price < user_funds:
#     Print("You have enough money!")
# if item_price = user_funds:
#     print("You have the precise amount of money")
# if item_price < user_funds:
#     print(Sorry you don't have enough money)


# One solution here:

# user_funds = 10.31
# item_price = 10

# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price < user_funds:
#     print("Sorry you don't have enough money")


# Another ACURATE solution :

price = {'Chips':5,'Burger':10}
user_funds = 10.31
item_price = price["Burger"]

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you don't have enough money")


# Exercise B - static analysis:

# def product(n):
#     total == 1
#     for n in n:
#         total *= i
# return total

# print(product([4,4,5]))


# Solution here:
def product(n):
    total = 1
    for i in n:
        total *= i
    return total

print(product([4,4,5]))


# Exercise C - dynamic analysis:

# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n = 0:
#                 return False
#             return True

# Solution here :

pdb.set_trace()

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True

#just a static at n=0 to n==0

