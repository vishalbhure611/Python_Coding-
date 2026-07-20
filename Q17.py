# Q17. Count the frequency of characters using collections.Counter.

from collections import Counter
def count_frequency(str):
    
    return dict(Counter(x for x in str if x!=' '))

s = "Vishal Bhure"
print(count_frequency(s))
