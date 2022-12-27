# Write a Python function to reverse a string if it's length is a multiple of 4.

str = input("Enter Any String Which Multply By Four : ")

def reverse_str(str):
    if len(str) % 4 ==0:
        print(' '.join(reversed(str)))

    else:
        print("Try Again...")


reverse_str(str)



'''
output = 
Case-1
Enter Any String Which Multply By Four : avin
n i v a

Case-2
Enter Any String Which Multply By Four : avinesh
Try Again...
'''


