"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of hay
"""

def index_of_first_occurence(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
        

print(index_of_first_occurence("sadbutsad", "sad"))
print(index_of_first_occurence("leetcode", "leeto"))