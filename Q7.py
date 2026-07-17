# Q7. Given an array of integers, move all zeroes to the end while maintaining the order of the remaining elements.

def moveZeroes(lst):
    count =0
    ans =[]
    for i in lst:
        if i!=0:
            ans.append(i)
        else:
            count+=1
    # for i in range(count):
    #     ans.append(0)
    ans =ans+[0]*count
    return ans

num =[1,0,2,3,0,0,5,6]
print(moveZeroes(num))

#using Two-Pointers-O(n) best
def moveZeroesToEnd(arr):
    pos =0

    for i in range(len(arr)):
        if arr[i] !=0:
            arr[i],arr[pos]=arr[pos],arr[i]  #swap
            pos+=1
    return arr

arr= [1,2,0,4,5,0,6]
print(moveZeroes(arr))
