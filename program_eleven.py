'''Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
binary_divisable_five = []
inputString = input("Please enter multiple 4 digit binary numbers: ")
for bnum in inputString.split(","):
    if not (int(bnum, 2) % 5):
        binary_divisable_five.append(bnum)
print(binary_divisable_five)
