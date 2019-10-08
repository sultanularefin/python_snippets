# 2. Anagrams
# This method can be used to check if two strings are anagrams.
# An anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.



from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


print("anagram(\"abcd3\", \"3acdb\"): ",anagram("abcd3", "3acdb"));

# please check the hashtable.cpp file to understand HashTabe