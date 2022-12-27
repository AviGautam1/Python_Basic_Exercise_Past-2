# Write a Python program to display formatted text (width=50) as output.

import textwrap
para = """
Python is an interpreted, object-oriented, high-level programming language that can be used for a wide variety of applications. Python is a powerful general-purpose programming language. First developed in the late 1980s by Guido van Rossum. Python is open source programming language. Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
"""

'''
Module (textwrap.wrap(text, width = 70, **kwargs)) − This method wraps the input paragraph.

Module (textwrap.fill(text, width = 70, **kwargs)) − The fill() method is similar to the wrap method, 
but it does not generate a list.
'''
print(textwrap.fill(para, width=35))
print("\n\n",textwrap.fill(para, width=70))


'''
output = 
 Python is an interpreted, object-
oriented, high-level programming
language that can be used for a
wide variety of applications.
Python is a powerful general-
purpose programming language. First
developed in the late 1980s by
Guido van Rossum. Python is open
source programming language. Guido
van Rossum named it after the BBC
Comedy TV series Monty Python’s
Flying Circus


  Python is an interpreted, object-oriented, high-level programming
language that can be used for a wide variety of applications. Python
is a powerful general-purpose programming language. First developed in
the late 1980s by Guido van Rossum. Python is open source programming
language. Guido van Rossum named it after the BBC Comedy TV series
Monty Python’s Flying Circus
'''

