'''
Write a Python function to create the HTML string with tags around the word(s).
Sample function and result.
'''

def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)


print(add_tags('a', 'Avi'))
print(add_tags('b', 'Gautam'))


'''
output = 
<a>Avi</a>
<b>Gautam</b>
'''
