def findOddSum(lst):
    pairOfOddSum = []
    
    for firstNum in range(len(lst) - 1):
        for secondNum in range(firstNum + 1, len(lst)):
            num = lst[firstNum] + lst[secondNum]
            if num % 2 == 1 :
                pairOfOddSum.append([lst[firstNum],lst[secondNum]])
        
    
    return pairOfOddSum

def findEvenProduct(lst):
    pairOfEvenProduct = []

    for firstNum in range(len(lst) - 1):
        for secondNum in range(firstNum + 1, len(lst)):
            num = lst[firstNum] * lst[secondNum]
            if num % 2 == 0 :
                pairOfEvenProduct.append([lst[firstNum],lst[secondNum]])

    return pairOfEvenProduct

def printPretty(aTable):
    for i in range(len(aTable)):
        for j in range(len(aTable[i])):
            print(aTable[i][j],end=' ')
        print('')

userInput = input("Please enter a number separated by comma: ")
numList = userInput.split(",")

for item in range(len(numList)):
    numList[item] = int(numList[item])

# Odd sum
print("List of odd sum:")
printPretty(findOddSum(numList))

# Even product
print("List of even product:")
printPretty(findEvenProduct(numList))
