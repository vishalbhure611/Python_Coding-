# Q18. Find the top three most frequent words in a paragraph using Counter.
from collections import Counter
def top_three(para):
    words = para.lower().split(" ")
    print(words)

    freq = Counter(words).most_common(3)
    return freq

para = "python is easy python is powerful"
print(top_three(para))