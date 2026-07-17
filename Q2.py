# # Q2. Given a string, find the first non-repeating character.

# #by finding the frequency
str = "aabbcddeef"
freq = {}

for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
# print(freq)
for i in freq:
    if freq[i]==1:
        print(i)
        break

#without finding the freq
def nonRep(s):
    n = len(s)
    for i in range(n):
        found = False
        for j in range(n):
            if i != j and s[i] == s[j]:
                found = True
                break
        if not found:
            return s[i]
    return '$'


s = "racecar"
print(nonRep(s))

# using fun->
freq = {}
def non(str):
    for i in str:
        freq[i]= freq.get(i,0)+1
    #print(freq)
    for i in freq:
        if freq[i]==1:
            return i
            
print(non("aabbcddeef"))