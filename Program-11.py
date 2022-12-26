'''
Write a Python function that takes a list of words and return
the longest word and the length of the longest one.
'''


def main():
    text = input("Please input a list of words to evaluate: ")

    longest = 0

    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words

    print("The longest word is", longest_word, "with length", len(longest_word))

main()

'''
output = 
oPlease input a list of words to evaluate: hi my name is avinesh gautam
The longest word is avinesh with length 7
'''