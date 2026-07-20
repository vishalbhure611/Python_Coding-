# Q11. Given a paragraph, count the frequency of every word using a dictionary.
import string
def WordsFrequency(para):
    
    freq = {}

    for char in string.punctuation:   #replae Punctuations
        para = para.replace(char, "")

    words = para.lower().split()
    
    for i in words:
        freq[i] = freq.get(i,0)+1

    return freq

paragraph = "this is Python Practice , Python Practice makes you perfect."
print(WordsFrequency(paragraph))