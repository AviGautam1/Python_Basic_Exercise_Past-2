# Write a Python program to reverse words in a string.

# initializing the string
string = "I am a python programmer"
# splitting the string on space
words = string.split()
# reversing the words using reversed() function
words = list(reversed(words))
# joining the words and printing
print(" ".join(words))

# output = programmer python a am I