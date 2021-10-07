
openedFile = open('Readme-copy.txt')

# print(openedFile)

# print(openedFile.read())

listObject1 = openedFile.readlines()

# manipulate contents

print(listObject1)
print(listObject1[1])

singleLine = listObject1.pop(1)
singleLine = singleLine.replace(' this ', ' ONY this ')
listObject1.insert(1,singleLine)

print(listObject1)


# Open in write morem write and close

openedFile.close()
openedFile = open('Readme-copy.txt', 'w')

bigstr = ''
for i in listObject1:
    bigstr = bigstr + i

openedFile.write(bigstr)
openedFile.close()

