# syntax error
"""
a = 2
if a < 1:
    print("Hello")
else:
    print("Welcome")

# Indentation error

    print("Hello")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 11

a = 2
if a < 1:
#print("Hello")
    print("hello")
else:
    print("Welcome")

#3 zero division error
print(8/0)


#4 Module error
import mathematics
print(mathematics.pi)


#5 type error
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
a = 2
b = '5'
print(a + b)


#6 Logic error
# wrong logic / operator for example
a = 2
b = 5
print(a * b)
"""