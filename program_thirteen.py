'''Write a program that accepts a sentence and calculate the number of letters
and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
letters = 0
digits = 0
inputstring = input("Please enter any text: ")
for c in inputstring:
    if c.isdigit():
        digits += 1
    elif c.isalpha():
        letters += 1
    else:
        pass
print("LETTERS {0} and DIGITS {1}".format(letters, digits))
