# Given a list of integers, find the second largest distinct element.

def findSecondLargest(lst):
    max=-1
    secondMax = -1

    for i in lst:
        if i>max:
            max= i

    for i in lst:
        if i>secondMax and i !=max:
            secondMax =i
    return secondMax

#
def findSecondLarg(lst):
    max_val = max(lst)

    secondMax = float('-inf')

    for i in lst:
        if i != max_val and i > secondMax:
            secondMax = i

    return secondMax


    
lst=[1,2,3,4,5]
print(findSecondLargest(lst))
print(findSecondLarg(lst))

#onePass approach-one for loop
def findSecondLargestnum(lst):

    largest = float('-inf')
    second = float('-inf')

    for num in lst:

        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    return second

lst = [1,2,3,4,5]
print(findSecondLargestnum(lst))