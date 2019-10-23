def findOdd(lst):
    oddSum = []
    
    for firstNum in range(len(lst) - 1):
        for secondNum in range(firstNum + 1, len(lst)):
            num = lst[firstNum] + lst[secondNum]
            if num % 2 == 1 and num not in oddSum:
                oddSum.append(num)
    
    return sorted(oddSum)

def findEven(lst):
    evenProduct = []

    for firstNum in range(len(lst) - 1):
        for secondNum in range(firstNum + 1, len(lst)):
            num = lst[firstNum] * lst[secondNum]
            if num % 2 == 0 and num not in evenProduct:
                evenProduct.append(num)

    return sorted(evenProduct)

userInput = input("Please enter a number separated by comma: ")
numList = userInput.split(",")

for item in range(len(numList)):
    numList[item] = int(numList[item])

# Odd sum
print("List of odd sum:", findOdd(numList))

# Even sum
print("List of even product:", findEven(numList))
