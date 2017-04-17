'''Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
seq_number = input("Please enter a sequence of comma-sparated numbers :")
seq_list = seq_number.split(",")
seq_tuple = tuple(seq_list)
print(seq_list)
print(seq_tuple)
