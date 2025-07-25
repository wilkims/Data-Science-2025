# -*- coding: utf-8 -*-
"""Assignment_15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EaEGMWyn6kVMBWJ9Fjubqiruo77zBWGN
"""

def recur_factorial(n):
    """
    n: int >= 0
    Returns the factorial of n using recursion.
    """
    if n == 0:
        return 1  # base case
    else:
        return n * recur_factorial(n - 1)  # recursive step

# 🧪 Test Cases
print(recur_factorial(0))  # Output: 1
print(recur_factorial(5))  # Output: 120
print(recur_factorial(7))  # Output: 5040

def is_palindrome_recur(s):
    """
    s: string
    Returns True if s is a palindrome using recursion, False otherwise.
    """
    # Base case: empty string or single character is always a palindrome
    if len(s) <= 1:
        return True
    # Recursive case
    if s[0] != s[-1]:
        return False
    return is_palindrome_recur(s[1:-1])

# 🧪 Test Cases
print(is_palindrome_recur("racecar"))  # Output: True
print(is_palindrome_recur("hello"))    # Output: False
print(is_palindrome_recur("madam"))    # Output: True

