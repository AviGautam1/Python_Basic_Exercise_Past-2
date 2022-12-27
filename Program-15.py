'''
Write a Python function to get a string made of 4 copies of the last two
characters of a specified string (length must be at least 2).
'''

def copy_end(str):
    a = str[-2:]
    return a * 4


print("Copies Of String", copy_end("Avinesh"))


# output = Copies Of String shshshsh