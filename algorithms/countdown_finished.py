# use recursion to implement a countdown counter

# recursive funcs need to have a breaking condition
# otherwise the code will get into an infinite loop
# and eventually crash the program
# eacg time the func is called, the old arg args are saved
# this is called the "call stack"

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)


countdown(5)
