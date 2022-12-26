'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
'''

str1 = input("Enter First String : ").lower()
str2 = input("Enter Second String : ").lower()

def swap_first_two_char(str1, str2):
    a = str2[:2] + str1[2:]
    b = str1[:2] + str2[2:]

    return a + ' ' + b

print(swap_first_two_char(str1, str2))


'''
output = 
Enter First String : avi
Enter Second String : gau
gai avu
'''

