'''Write a program that accepts a sentence and calculate the number of upper
case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
s = input("Please enter the string: ")
ucase = 0
lcase = 0
for x in s:
    if x.isupper():
        ucase += 1
    elif x.islower():
        lcase += 1
    else:
        pass
print("Upper Case {0} \nLower Case {1}".format(ucase, lcase))
