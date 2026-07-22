# Q5. Given a string, remove duplicate characters while preserving their first occurrence.

#using set -O(n) but order is not preserved
def remove_duplicates(s):
    ans = set(s)  #it will not preserve the order
    return ans

s = "aabbccd"
print(remove_duplicates(s))

#using list ,without set - O(n^2) 
def remove_dup(s):
    ans1 =[]
    for i in s:                      # ->O(n)
        if i not in ans1:            # ->O(n)
            ans1.append(i)
    return ans1

print(remove_dup(s))

# set+list - to maintain order and O(n)
def remove_dup2(s):
    seen = set()            #here we can use any other ds but set uses hashing to search ele
    result =[]

    for i in s:
        if i not in seen:   #set uses hashing so it will only take O(1) tc to search the ele
            seen.add(i)
            result.append(i)

    return ''.join(result)  # this means->  '' + 'a' + 'b' + 'c' + 'd'

s1= "aaabbabbccee"
print(remove_dup2(s1))

#using fromkeys() method of dict - O(n)
def removedup(s):
   
    result = ''.join(dict.fromkeys(s2))
    return result

s2= "aabbccdd"
print(removedup(s2))