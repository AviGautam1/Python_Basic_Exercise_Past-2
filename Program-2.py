'''
Write a Python program to create all possible strings by using
'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
'''

# The import random loads the random module, which contains a number of random number generation-related functions.
import random
alpha_list = ['a','e','i','o','u']

random.shuffle(alpha_list)   # random.shuffle(sequence) The shuffle() method takes a sequence, like a list, and reorganize the order of the items.

print(' '.join(alpha_list))

'''
Note - every time you run the code the string will be different
'''

'''
output =
u i a e o
a o e i u
e u a i o
i e o u a

Etc...
'''
