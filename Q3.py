# # Q3. Given a string, return the character that appears the maximum number of times.
str = "aaabbccdddde"
freq ={}
for i in str:
    # if i in freq:
    #     freq[i]+=1
    # else:
    #     freq[i]=1      or->
    freq[i]=freq.get(i,0)+1

max=0
max_char =''
for i in freq:
    if freq[i]>max:
        max =freq[i]
        max_char=i
print(max_char,":", max)


# # if freq[]

# result= max(dict.fromkeys(str))
# print(result)

