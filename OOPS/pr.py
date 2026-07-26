# original = [1, 2, 3]
# reference = original # No copy made!
# print(reference)
# reference.append(4)
# print(original) # Output: [1, 2, 3, 4]

# a=2
# x =10
# print(id(x))
# x =x+a
# print(id(x))

a=1000
b=1000
# b=1001
print(a is b)
print(a==b)
print(a,b)
print(id(a))
print(id(b))
