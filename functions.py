# code reusing

"""
def "function name()":
    statements
    return (expr)
function_call()


def addfunc(a,b):
    #print("Hello")
    #print("World")
    #print(a + b)
    c = a * b
    return c

result = addfunc(2,"Krishnan ")
print(result)



def add(x, y):
    return x + y

def square(z):
    return z*z

result = square(add(2,3))
print(result)


def python():
    print("python")
    python()

python()


import sys

sys.setrecursionlimit(2001)

n = 0

def python():
    global n
    n = n + 1
    print("python", n)
    python()

python()


FACTORIAL
0! = 1
1! = 1 * 0! = 1 * 1 = 1
2! = 2 * 1! = 2 * 1 = 2
3! = 3 * 2! = 3 * 2 = 6
4! = 4 * 3! = 4 * 6 = 24
5! = 5 * 4! = 5 * 24 = 120
"""

def findfactorial(n):
    if n<2:
        return 1
    else:
        return n * findfactorial(n-1)

result = findfactorial(5)
print(result)