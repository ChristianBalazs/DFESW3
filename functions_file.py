
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



