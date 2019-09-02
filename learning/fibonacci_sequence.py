# Fibonacci Sequence Generator

def fibonacci_gen():
    trailing, lead = 0,1
    while True:
    	yield lead
    	trailing, lead = lead, trailing+lead

>>> fib=fibonacci_gen()
>>> fib.next()
1
>>> for _ in range(10):
...     fib.next()