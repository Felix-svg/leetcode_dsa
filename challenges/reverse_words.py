"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

def reverseWords(s):
    new_word = s.strip().split()
    start = 0
    end = len(new_word) - 1
    while start < end:
        new_word[start], new_word[end] = new_word[end], new_word[start]

        start += 1
        end -= 1

    return " ".join(new_word)
    #return new_word

print(reverseWords("the sky is blue"))
print(reverseWords(" hello world  "))
print(reverseWords("a good   example"))