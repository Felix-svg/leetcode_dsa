'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
'''

def lengthOfLastWord(s):
    word = s.strip().split(" ")
    return word[-1]
    
print(lengthOfLastWord("hello world"))