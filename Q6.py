# Q6. Given a list of integers, remove duplicate elements while preserving the original order.

 #using list only
def remove_dupints(lst):
    ans =[]
    for i in lst:
        if i not in ans:
            ans.append(i)
    return ans

numbers = [1,2,1,4,3,3,4]
print(remove_dupints(numbers))

# like Q5 we can also use set+list- O(n)
def remove_dup(n):
    seen = set()
    lst = []

    for i in n:
        if i not in seen:
            seen.add(i)
            lst.append(i)
    return lst

print(remove_dup(numbers))

#using fromkeys() -O(n)
def remove_duplicatenum(lst):
    result = dict.fromkeys(lst)
    return list(result)

lst = [1,1,2,2,3,4,4,3,5]
print(remove_duplicatenum(lst))