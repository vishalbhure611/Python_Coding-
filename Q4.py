# Q4. Given two strings, determine whether they are anagrams.(two strings are anagrams if they contain the      exact same characters in the same frequencies but in a different order) eg- silent and listen, heart and earth
def isAnagram(s1,s2):

    if len(s1) != len(s2):
        return False
   
    freq1={}
    freq2= {}

    for i in s1:
        freq1[i] = freq1.get(i,0)+1
    for i in s2:
        freq2[i]=freq2.get(i,0)+1

    print(freq1)
    print(freq2)
    if freq1==freq2:
        return True
    return False

s1 = "silent"
s2="listen"
print(isAnagram(s1,s2))

#
def isAnagram2(s1,s2):
    freq={}
    
    for i in s1:
        freq[i]= freq.get(i,0)+1

    for i in s2:
        if i not in freq:
            return False
        else:
            freq[i]-=1
    return True
s1 = "silent"
s2="listen"
print(isAnagram2(s1,s2))