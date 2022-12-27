# Write a Python program to swap comma and dot in a string.


amount = "12.345,678"

maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)

# output = 12,345.678