# Q9. Given two lists, find the common elements without duplicates.
list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 3, 4, 5]

# Method 1: Using set intersection operator (&)
common_elements = list(set(list1) & set(list2))
print(common_elements)

# Method 2: Using the .intersection() method
common_elements_alt = list(set(list1).intersection(list2))
print(common_elements_alt) 

#Method3: using List
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = []
for item in list1:
    if item in list2:
        common_elements.append(item)

print("Common elements using lists:", common_elements)