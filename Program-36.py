# Write a Python program to strip a set of characters from a string.

str = "Am A Python Developer"
ch = "aeiouAEIOU"

print("Original String : ", str)
print("After stripping aeiou AEIOU :"," ".join(c for c in str if c not in ch))


'''
output = 
Original String :  Am A Python Developer
After stripping aeiou AEIOU : m     P y t h n   D v l p r
'''