# Write a Python program to count the number of characters (character frequency) in a string.

n = input("Enter the String: ").lower()
s = {}          # Create a empty dictionary.
for i in n:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
print(s)

'''
Enter the String: avinesh gautam
{'a': 3, 'v': 1, 'i': 1, 'n': 1, 'e': 1, 's': 1, 'h': 1, ' ': 1, 'g': 1, 'u': 1, 't': 1, 'm': 1}
'''