"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

try:
    file = open('sample.txt', 'r')
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
finally:
    file = open('sample.txt', 'w')
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines.")
    file.close()

file = open('sample.txt', 'r+')
print("Line 1: ", file.readline())
print("Line 2: ", file.readline())
file.close()