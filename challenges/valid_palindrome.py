"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

def is_valid_palindrome(s):
    clean_string = ''.join(char.lower() for char in s if char.isalnum())
    reversed_sring = clean_string[::-1]
    if clean_string == reversed_sring:
        return True
    return False


print(is_valid_palindrome("A man, a plan, a canal: Panama"))