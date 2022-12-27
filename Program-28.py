# Write a Python program to print the following floating numbers upto 2 decimal places with a sign.

a = 84.752
b = 23.36778

print("Original Value A : ", a)
print("Formatted Value A : "+"{:+.2f}".format(a))
print("Original Value B : ", b)
print("Formatted Value B : "+"{:+.2f}".format(b))

'''
output = 
Original Value A :  84.752
Formatted Value A : +84.75
Original Value B :  23.36778
Formatted Value B : +23.37
'''

