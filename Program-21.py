# Write a Python program to sort a string lexicographically.

s = input("Enter the String : ")

print(sorted(sorted(s), key=str.upper))     # sorted(iterable, key=key, reverse=reverse)


'''
output = 
Enter the String : avinesh gautam
[' ', 'a', 'a', 'a', 'e', 'g', 'h', 'i', 'm', 'n', 's', 't', 'u', 'v']
'''

