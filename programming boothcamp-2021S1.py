# BY : Maximillian Purnomo
# This is a code for sorting an array of numbers
# The code works by going through the each items inside the array and use an index as a bench mark
# Then compare it to the rest of the items inside the array, it will swap the position when it found a smaller number 
# than the current benchmark's number.
# So when it finished going through the array of numbers, it will be sorted already
# as it will always try to put smaller number to the front 




# The sorting function
def sortingCode(aList):
    length=len(aList)
    for index in range(0,length):
        for index2 in range(index+1,length):
            if aList[index2]<aList[index]:
                temp=aList[index]
                aList[index]=aList[index2]
                aList[index2]=temp
    return aList


# The testing code
list1=[5,4,3,2,5.5]
list1=sortingCode(list1)
print(list1)
