
# 1. Run a Python program in the Python IDLE that returns "Hello World"

print("Hello World")


# 2. Create a python file that will input your first name, last name and outputs "Hello [firstname] [lastname]"

firstName = input("Your first name here: ")
lastName = input("Your last name here: ")

print("Hello " +  firstName + lastName)



# 3. What does this program do?

number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))
answer = number1 + number2

print(number1, "+", number2, "=", answer)

# Answer : will prompt to request a first number, then a second number, then display the sum of those numbers as a float )
# Correct answer: ...then display the entire operation (a+b+=c)  not just the sum.

# Attention: ny using float() turns the input number from string (text) type to integer.
