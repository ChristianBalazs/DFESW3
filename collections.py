
varForAString = 'I like Pies'
print(varForAString[3])

# 1. List

listOfShopping = [ 'meat', 'veg', 'cake', 'beer for the weekend']
print(listOfShopping[1])



emptyList =[]

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]



cool_animals = [cool_cows, cool_sheep, cool_pigs]


print(cool_animals[1])
# ['Baaaart', 'Baaaarnaby']

print(cool_animals[1][0])
# Baaaart

# How to select "Hamlet"
print(cool_animals[2][1])


# .append will add another item at the end of the list
cool_pigs.append("Babe")
print(cool_animals[2])




# 2. Tupple - is a READ ONLY list, can't change the data inside a tupple

tuppleOfShopping = ('meat', 'veg', 'cake', 'beer for the weekend', 'cake')






# 3. Dictionary

varForADictionary = { 'name':'Leon', 'size':'big', 'age':'34'}

print(varForADictionary['name'])

# unlike list where listOfShopping[1] - include a number to reach a particular item, 
# with varForADictionary[''key] -include a key 



# 4. Sets - similar to lists but very complex - do not use unless you absolutely have to 



#Tutorial exercise:

# Create a dictionary where they keys are books, and the values are their authors.

booksDictionary = {'Eat that Frog':'Brian Tracy', 'Happiness':'Matthieu Ricard', 'Start with Why':'Simon Sinek'}

# We can query the author of any book.
print(booksDictionary)

print(booksDictionary['Happiness'])


# However if we try to query what books have been written by an author, we get the following error.
# KeyError: 'Matthieu Ricard'

print(booksDictionary['Matthieu Ricard'])

#This is because "Matthieu Ricard" is a value not a key.
# Recall we cannot query a dictionary using a value.

