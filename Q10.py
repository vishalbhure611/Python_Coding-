# Q10. Given two sorted lists, merge them into a single sorted list without using built-in sorting functions.

#using two-pointers-
def merge_sorted(list1, list2):
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):

        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Remaining elements of list1
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # Remaining elements of list2
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


list1 = [1,3,5,7]
list2 = [2,4,6,8]

print(merge_sorted(list1, list2))