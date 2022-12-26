# Python program to print all the possible combinations.

def comb(lst):

    for i in range(3):
        for j in range(3):
            for k in range(3):

                # check if the indexes are not same
                if (i != j and j != k and i != k):
                    print(lst[i], lst[j], lst[k])


comb([2, 4, 6])

'''
output = 
2 4 6
2 6 4
4 2 6
4 6 2
6 2 4
6 4 2
'''