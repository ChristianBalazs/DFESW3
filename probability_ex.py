
#Exercise - prability calculator

# Goal: “Create a lottery ball, or Hat, 
# 
# that takes a variable number of arguments that specify the number of balls of each color that are in the hat. 

# Ex: input1 {red:6, blue:10, puce:3}
#     input2 {mahogany:5, teal:23, saddlebrown:40, mint_green:1}
# 

# Ex: create a variable that has the total of each
# Ex: input1 = [red red red red red red blue blue blue blue blue blue blue blue blue blue puce puce puce] 




#list = []
# for i in input.keys():
#     for j in range(input[i]):
#         list.append(i)



# Give the object the ability to pick a random number of balls from the hat, 
# 
# Ex: loop 
# for i in radint(x)


# which will then be used to compute the probability of picking a certain distribution of balls over a large number of experiments”



import random


class Hat():

    def __init__(self, **balls):
        self.ballsdict = balls

    
    for i in self.ballsdict.keys():
        for j in range(self.ballsdict[i]):
            list.append(i)

    list = []

    def grabballs(self):
        randBalls = random.randint(len(list))
        grabbedBalls = random.sample(list,randBalls)
        return grabbedBalls
    
    def compute_probability(self, experiNum):
        pass


daveThe = Hat({'red':6, 'blue':10, 'puce':3})
print(daveThe.graballs())






