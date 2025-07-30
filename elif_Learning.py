operand_1 = int(input("Enter operand1: "))
operand_2 = int(input("Enter operand2: "))
operator = input("Enter the operator (* + - /) : ")

"""
if (test expression): 
    statement
elif(test expression):
    statement
elif....

else: ... 
    statement
statement
"""

if operator == '+':
    print(operand_1 + operand_2)
elif operator == '-':
    print(operand_2 - operand_1)
elif operator == '*':
    print(operand_1 * operand_2)
elif operator == '/':
    print(operand_1 / operand_2)
else:
    print("Invalid operator")
print("This is simple calculator")