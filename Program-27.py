# Write a Python program to add a prefix text to all of the lines in a string.

import textwrap
para = """
	Python is an interpreted, object-oriented programming languages. 
	high-level programming language that can be used for a wide variety of applications. 
	Python is a powerful general-purpose programming language.
	First developed in the late 1980s by Guido van Rossum. 
	Python is open source programming language.
	Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
"""

'''
dedent(text): This function is used to remove any 
common leading whitespace from every line in the input text.
'''
without_Indent = textwrap.dedent(para)
txt = textwrap.fill(without_Indent, width=70)

'''
The indent method adds the specified prefix to the 
beginning of the chosen text lines.

Syntax - textwrap.indent(text, prefix, predicate=None)
'''
res = textwrap.indent(txt, ' > ')

print(without_Indent)
print(txt)
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
high-level programming language that can be used for a wide variety of
applications.  Python is a powerful general-purpose programming
language. First developed in the late 1980s by Guido van Rossum.
Python is open source programming language. Guido van Rossum named it
after the BBC Comedy TV series Monty Python’s Flying Circus
 >  Python is an interpreted, object-oriented programming languages.
 > high-level programming language that can be used for a wide variety of
 > applications.  Python is a powerful general-purpose programming
 > language. First developed in the late 1980s by Guido van Rossum.
 > Python is open source programming language. Guido van Rossum named it
 > after the BBC Comedy TV series Monty Python’s Flying Circus
'''

