# Simple RECURSIVE FACTORIAL PROGRAM
# COLIN KELLEHER

def factorial(n):
    if n == 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result

print(factorial(5))