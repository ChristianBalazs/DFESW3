
nameVar1 = "Brian"
nameVar2 = "John"

listOfAnimals = ['sheep', 'cat', 'Austrian tree frog', 'Pacific river moul', 'pig', 'rat', 'dog']
varForADictionary = {'name':'Leon', 'size':'nearly big', 'age':'young'}


if 'sheep' in listOfAnimals:
    print('Sheep is in the list of values')
print('This line will always print')


if nameVar1 == "Brian":
    print('This is true, Brian is here')

if nameVar1 =="Brian" and nameVar2 == "John":
    print('Both Brian and John are here')

if nameVar1 =="Brian" or nameVar2 == "Danny":
    print('Either Brian or Danny are here')

if 'cat' in listOfAnimals:
    print('found a cat')


if 'cat' in listOfAnimals:
    print('found a cat again')
elif 'dog' in listOfAnimals:
    print('found a dog')


if 'cow' in listOfAnimals:
    print('found a cow here')
elif 'dog' in listOfAnimals:
    print('found a dog')


if 'cow' in listOfAnimals:
    print('found a cow here')
elif 'elephant' in listOfAnimals:
    print('found a elephant')
elif 'dinosaur' in listOfAnimals:
    print('found a dinosaur')
elif 'dog' in listOfAnimals:
    print('found a dog actually')

