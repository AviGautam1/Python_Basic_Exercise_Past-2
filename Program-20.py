'''
Write a Python function to convert a given string to all uppercase if it
contains at least 2 uppercase characters in the first 4 characters.
'''


str = input("Enter the String : ")

num_upper = 0
for letter in str[:4]:
	if letter.upper() == letter:
		num_upper += 1
if num_upper >= 2:
	print(str.upper())

print(str)


'''
output = 
Enter the String : coMPuter
COMPUTER
coMPuter
'''