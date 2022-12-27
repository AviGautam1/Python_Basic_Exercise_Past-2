# Python Program to Count the Number of Vowels in a String.


string = input("Enter string: ")

vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels = vowels + 1
print("Number of vowels are: ")
print(vowels)


'''
output = 
Enter string: avinesh gautam
Number of vowels are: 
6
'''