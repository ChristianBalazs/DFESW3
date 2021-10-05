
def leon_procedure(inputDataVar):
    print(inputDataVar)
    if inputDataVar < 5:
        exit()



x = 1000
y = 2000
z = x * y

print(z)
if z < 5:
    exit()
z = y-x 
print(z)
if z < 5:
    exit()
z = y * (x/2)
print(z)
if z < 5:
    exit()
z = x * x
print(z)
if z < 5:
    exit()
z = y *y 
print(z)
if z < 5:
    exit()

# transfer the top code to this:

leon_procedure(z)
z = y-x 
leon_procedure(z)
z = y * (x/2)
leon_procedure(z)
z = x * x
leon_procedure(z)
z = y *y 
leon_procedure(z)


