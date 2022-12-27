'''
Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
'''

phrase = input("Input words: ")

phrase_list = phrase.split(",")
#phrase_list.sort()
print((', ').join(sorted(set(phrase_list))))


'''
output = 
Input words: hi, there, my, name, is, avi, and, i, am, coder
 am,  and,  avi,  coder,  i,  is,  my,  name,  there, hi
'''