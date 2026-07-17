# 1.Given a string, count the frequency of each character while ignoring spaces and letter case.

str = " vishal BHure"

#1st way->
ans = {}
for char in str:
    if char !=" ":
        char = char.lower()
        ans[char]=ans.get(char,0)+1
print(ans)


freq= {}
for i in str.lower():
    if i !=" ":
        if i in freq:
            freq[i]+=1
        else:
            freq[i] =1
print(freq)


# using Counter
from collections import Counter

str1= "HeLlo World"
s = str1.lower().replace(" ","")
print(Counter(s))

#using Count()
s = "Hello World".lower().replace(" ", "")

freq = {}

for ch in s:
    freq[ch] = s.count(ch)

print(freq)

#  .count() is a built-in method used to count a specific item one at a time, while Counter is a class from the collections module that counts all unique items at once.



