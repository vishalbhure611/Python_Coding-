# Q14. Given a dictionary, invert its keys and values.

#using loop
def invert_dict(dict):
    result ={}

    for k,v in dict.items():
        result[v] = k

    return result

dict = {"a":1,"b":2,"c":3}
print(invert_dict(dict))

#using Dictionary Comprehension
def invert_di(dict):
    result = {value:key for key,value in dict.items()}
                                 #For every key, value, create a new dictionary entry as  value: key.
    return result

dict2 = {"x":12,"y":12,"z":14}
print(invert_di(dict2)) 

#Above 2 ways cant handle if dict conatains duplicate values beacuase when inverting, values becomes keys but keys should be unique.(run 2nd func)
#to preserve duplicate values-
# Store the original keys in lists:
def invert_dict3(data):
    result = {}

    for key, value in data.items():
        if value not in result:
            result[value] = []

        result[value].append(key)

    return result


data = {
    "a": 1,
    "b": 2,
    "c": 1
}

print(invert_dict3(data))