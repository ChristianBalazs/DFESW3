
# for loop

books = ['Winnie the Pooh', 'War and Peace', '1984', 'My family and other animals', 'Boy', 'The Art of War', 'Of Mice and Men', 'Peter and James']

for bookItem in books:
    print("I have read " + bookItem)


for bookItem in books:
    if bookItem == '1984':
        print(bookItem + " is the only book in the list that can be cast into a number")
    else:
        print(bookItem)



strVar = 'This is a string'
for charVar in strVar:
    if charVar == " ":
        print('space character')
    else:
        print('alphabet character')
print(charVar)



for numVar in range(0,20,2):
    print(numVar)




# While loop

inputNumVar = int(input('Shove a whole number in: '))
resultVar = 1

while inputNumVar > 0:
    resultVar = resultVar * inputNumVar
    inputNumVar = inputNumVar - 1

print(resultVar)

# for 4 for example resultvar = ((((1*4)*3)*2)*1) = 24



books = ['Winnie the Pooh', 'War and Peace', '1984', 'My family and other animals', 'Boy', 'The Art of War', 'Of Mice and Men', 'Peter and James']

# for bookItem in books:
#     if bookItem =='1984':
#         continue
#     print(bookItem)


# for bookItem in books:
#     if bookItem =='1984':
#         break
#     print(bookItem)



# To continue this :

varForADictionary = {'name':'Leon', 'size':'nearly big', 'age':'still young'}

for thingsVar in varForADictionary:
    print(varForADictionary[thingsVar]) 