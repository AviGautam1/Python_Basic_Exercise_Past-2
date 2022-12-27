# Write a Python program to remove existing indentation from all of the lines in a given text.

import textwrap
para = """
	Python is an interpreted, object-oriented programming languages. 
	high-level programming language that can be used for a wide variety of applications. 
	Python is a powerful general-purpose programming language.
	First developed in the late 1980s by Guido van Rossum. 
	Python is open source programming language.
	Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
"""
print(para)

'''
The dedent() is another function of the textwrap module. 
This function removes the common leading whitespaces from every line of your text.
'''
res = textwrap.dedent(para)
print(res)


'''
output = 
	Python is an interpreted, object-oriented programming languages. 
	high-level programming language that can be used for a wide variety of applications. 
	Python is a powerful general-purpose programming language.
	First developed in the late 1980s by Guido van Rossum. 
	Python is open source programming language.
	Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus


Python is an interpreted, object-oriented programming languages. 
high-level programming language that can be used for a wide variety of applications. 
Python is a powerful general-purpose programming language.
First developed in the late 1980s by Guido van Rossum. 
Python is open source programming language.
Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
'''