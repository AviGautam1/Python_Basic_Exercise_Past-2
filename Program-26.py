# Write a Python program to print the following floating numbers upto 2 decimal places.


a = 83.1356
b = 23.36778

print("Original Value A : ", a)
print("Formatted Value A : "+"{:.2f}".format(a))        # 2f means to round up to two decimal places.
print("Original Value B : ", b)
print("Formatted Value B : "+"{:.2f}".format(b))


'''
output = 
Original Value A :  83.1356
Formatted Value A : 83.14
Original Value B :  23.36778
Formatted Value B : 23.37
'''