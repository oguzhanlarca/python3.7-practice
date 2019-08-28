# Using recursion to implement power and factorial functions

# recursive funcs need to have a breaking condition
# otherwise the code will get into an infinite loop
# and eventually crash the program
# eacg time the func is called, the old arg args are saved
# this is called the "call stack"


def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
