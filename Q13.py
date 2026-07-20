# Q13. Given two dictionaries, merge them. If a key exists in both dictionaries, add their values.

from collections import Counter
def merge_dict(dict1,dict2):
    result = Counter(dict1) + Counter(dict2)  
    return dict(result)

dict1 = {"a":2,"b":3,"c":4}
dict2 = {"a":2,"d":3,"e":4}
print(merge_dict(dict1,dict2))

#When you add two Counter objects together using the + operator, Python automatically combines the keys and sums their corresponding values.

# This MERGES but does NOT sum the values, instead  it overrides the common key value from 1st dict by 2nd one.
# result = dict1 | dict2 

#using get() -best
def merge_dict_using_get(d1,d2):
    result = d1.copy()

    for key,value in d2.items():
        result[key] = result.get(key,0)+value
    
    return result

d1 = {"a": 10, "b": 20, "c": 30}

d2 = {"b": 5,"c": 15,"d": 40}

print(merge_dict_using_get(d1,d2))                          
