"""
Task 1: Calculate Factorial Using a Function
0! = 1
1! = 1 * 0! = 1 * 1 = 1
2! = 2 * 1! = 2 * 1 = 2
3! = 3 * 2! = 3 * 2 = 6
4! = 4 * 3! = 4 * 6 = 24
5! = 5 * 4! = 5 * 24 = 120
"""

def calcfactorialfunc(number):
    if number < 2:
        return 1
    else:
        return number * calcfactorialfunc(number - 1)

value = int(input("Enter a number: "))
result = calcfactorialfunc(value)
print("Factorial of", value, "is:", result)