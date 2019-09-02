#### one lin if condition ########################
import sys
condition = True
x = 1 if condition else 0
print(x)
#### large number formatting #####################
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')
#### we dont have to manually close file #########
with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
#### print array with index num ##################
names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names, start=1):
    print(index, name)
#### redirection stdout ##########################
sys.stdout = open('file', 'w')
print('test')
#### shell redirection when executing ############
$ python foo.py > file
#### how many times a word occurs in a file ######
with open('trash.txt') as f:
    for line in f:
        count += line.count("Bob")
##################################################