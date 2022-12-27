# Write a Python program to remove a newline in Python.


mystring = '\nThis is my string. \n'
print("With newlines:" + mystring)

# strip() function removes any trailing character at the beginning and end of the string.
print("After deleting the newlines:",mystring.strip())


'''
output = 
With newlines:
This is my string. 

After deleting the newlines: This is my string.
'''