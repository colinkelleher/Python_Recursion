'''
1. Palindrome(n)
Write a recursive function that iteratively calculates whether a sequence is a palindrome
(the same forwards as backwards). You need to explicitly highlight the base case
and recursive case in your comments (marks will be heavily weighted towards this).
'''

import math #importing the math function

n = (input('Please enter a word/number to check if it is a palindrome or not :')) #here i am asking the user to input a word or numbers to check if it is a
#palindrome - the input is in the form of a string data type and is places in the variable 'n'

def recursive_palindrome(n): 
    if len(n) < 1: #if the length of the string is less than 1... complete the following: #here is the base case
        return "This is a palindrome"
    else:
        if n[0] == n[-1]: #if the first letter is equal to the last letter - complete the following: #here is the recursive case
            return recursive_palindrome(n[1:-1]) 
        else:
            return "This is not a palindrome" 
print(recursive_palindrome(n)) #envoking the function while also printing the output