# Write a Python program to get the last part of a string before a specified character.


x = 'http://test.com/lalala-avi'

print(x.rsplit('/', 1)[0])          # rsplit() split string from right side
print(x.rsplit('-', 1)[0])


'''
output = 
http://test.com
http://test.com/lalala
'''