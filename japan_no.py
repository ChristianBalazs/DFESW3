# inspiration from Amelia Sommer exercise

arabNo = [1,     2,    3,    4,    5,   6,    7,    8,    9,   10,  100,  1000]
japanNo = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "百", "千" ]

numberInput = int(input("Number here (up to 9999): "))

# How japan numbers work:
#
#     2456 
#  二  千    四   百    五    十   六
#  2  1000   4   100    5   10     6

# numberLen = len(numberInput)

# print(numberLen)



#multiIndex = numberInput

charLen = len(str(numberInput))

numberStr = str(numberInput)


answerNo = 0 

if charLen == 1:
    arabIndex = arabNo.index(numberInput)+1
    print(arabIndex)
    x = arabIndex - 1
    answerNo = japanNo[x]
    print(answerNo)

# Example : 55 = 5 10 5



if charLen == 2:
    a = 0
    for numberStr[a] in numberStr:
        print(numberStr)
        answerNo2 = japanNo[i-1] + japanNo[9] + japanNo[i-1]
    print(answerNo2)

# for i in numberInput:
#     if numberLen == 1:
#         answerNo = japanNo[i]







# to continue to work on