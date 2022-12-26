'''
Write a Python function that takes a sequence of numbers
and determines whether all the numbers are different from each other.
'''

def seq_number(numbers):
    if len(numbers) == len(set(numbers)):       # len(set(x)) tells you the size of the set of unique elements of x .
        return True
    else:
        return False


print(seq_number([1, 2, 3, 4]))
print(seq_number([1, 1, 2, 3, 3]))

"""
output = 
True
False
"""

