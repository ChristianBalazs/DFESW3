
def max_num(checkNum1, checkNum2, checkNum3):
    if checkNum1 > checkNum2:
        if checkNum1 > checkNum3:
            return checkNum1
        else:
            return checkNum3            
    else:
        if checkNum2 > checkNum3:
            return checkNum2
        else:
            return checkNum3


def add_calc(number1, number2):
    answer = number1 + number2
    return answer


def countname(personname):
    return len(personname)


def checkFunc(theNum, theRange):
    answer = "Corect"
    if theNum in theRange:
        return answer
    else:
        answer = "Not in range"
        return answer



