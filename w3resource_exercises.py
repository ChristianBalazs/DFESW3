
# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

#varNum = range(1500, 2700,)

# for num in range(1500, 2700,20):
#     print(num)

# Sorted :
# for num in range(1500, 2700,):
#     while num % 7 == 0 and num % 5 == 0:
#         print(num)
#         num = num +1



# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]


# varCTemp = int(input("Celsius Temp here: "))
# convToF = varCTemp *9/5 + 32
# print(convToF)


# varFTemp = int(input("Fahrenheit Temp here: "))
# convToC = (varFTemp - 32) /(9/5)
# print(convToC)



# 3. Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# actualNo = 6
# userNo = ''
# while userNo != actualNo:
#     userNo = int(input("Your number here betwen 1 and 9: "))
#     print("Try again")

# if userNo == actualNo:
#     print("Well guessed!")



#works but prints "Try again" as well as "Well guessed" as the last line


#Another SOLUTION from Lauren for Exercise 3:

# import random
# exitchoice = 'nothing'
# while exitchoice != 'EXIT':
#     number = int(input('Enter a number between 0-9: '))
#     if number == random.randint(1,10):
#         print('YOU WIN!')
#     else:
#         print("Sorry, you didn't enter correctly!")
#     print('TRY AGAIN!')
# exitchoice = input("Press return to play again, or type EXIT to leave.")




# 4. Write a Python program to construct the following pattern, using a nested for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


# With while loop

i = 1
while i <=5:
    print('* '*i)
    i = i+1

i = i-2
while i>=1:
    print('* '*i)
    i = i-1



# Solution from the website 

n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

# don't really understand this solution



# Another suggestion on comments:

n = 10
for i in range(10):
    if i <=5:
        print('* ' *i)
    elif i > 5:
        print('* ' * (n - i))
# would be good to research this solution a bit more



#Another solution from Luke

digit = 5

for i in range(digit):
    for x in range(i):
        print('* ', end="")
    print ('')

for i in range(digit,0,-1):
    for x in range(i):
        print('* ', end="")
    print ('')





