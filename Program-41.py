# Write a Python program to split a string on the last occurrence of the delimiter.

line1= "a,v,i,n,e,s,h"

print("Before Splitting:",line1)

'''
In rsplit() function 1 is passed with the argument so
 it breaks the string only taking one delimiter from last. 
 If the string has more than one delimiter and 2 is passed 
 in place of 1 the function split the string from second last 
 delimiter and last delimiter both.
'''
print(line1.rsplit(',',1))
print(line1.rsplit(',',2))
print(line1.rsplit(',',3))

'''
output = 
Before Splitting: a,v,i,n,e,s,h
['a,v,i,n,e,s', 'h']
['a,v,i,n,e', 's', 'h']
['a,v,i,n', 'e', 's', 'h']
'''