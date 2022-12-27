# Write a Python program to print the index of the character in a string.


str1 = "PYTHON"

'''
enumerate() allows us to iterate through a sequence but it keeps track of both the index and the element. 
The enumerate() function takes in an iterable as an argument, such as a list, string, tuple, or dictionary.18
'''

for index, char in enumerate(str1):
    print(char, "position at", index)


'''
output = 
P position at 0
Y position at 1
T position at 2
H position at 3
O position at 4
N position at 5
'''