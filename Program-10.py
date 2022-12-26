'''
Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends
with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
'''

def change_str(str):
    length = len(str)

    if length > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'
    return str


print(change_str("ab"))
print(change_str("abc"))
print(change_str('string'))


'''
output = 
ab
abcing
stringly
'''