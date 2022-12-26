'''
Write a Python program to remove and print every third number
from a list of numbers until the list becomes empty.
'''

def remove_third_item(lst):
    pos = 3 - 1             # position
    index = 0
    len_list = len(lst)

    while len_list > 0:
        index = (pos + index) % len_list

        print(lst.pop(index))
        len_list = len_list - 1


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
remove_third_item(nums)


'''
output = 
30
60
90
40
80
50
20
70
10
'''
