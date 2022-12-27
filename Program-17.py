'''
Write a Python function to get a string made of its first three
characters of a specified string. If the length of the string is
less than 3 then return the original string.
'''


def first_three_char(str):

    return str[:3] if len(str) > 3 else str

            # Or

#    if len(str) > 3:
#        print(str[:3])
#   else:
#        return str



print(first_three_char("avinesh"))
print(first_three_char("OM"))


'''
Output = 
avi
OM
'''