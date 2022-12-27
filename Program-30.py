# Write a Python program to print the following integers with '*' on the right of specified width.


x = 3
y = 123

print("Original Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x));
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y));
print()


'''
output = 
Original Number:  3
Formatted Number(right padding, width 2):  3*
Original Number:  123
Formatted Number(right padding, width 6):  123***
'''
